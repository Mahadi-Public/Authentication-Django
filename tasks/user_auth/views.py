from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash,get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from tasks.forms import SingupForm,ChangesPasswordForm

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.decorators import login_required

UserModel = get_user_model()


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request , data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, 'successfully login accounts')    
                return redirect('home_page_views')   
    else:
        form = AuthenticationForm()               
    return render(request, 'auth/login.html', {'form' : form})


def singup_page(request):
    if request.method == "POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save() #deactive accounts
            current_site = get_current_site(request)
            mail_subjects = 'Activate Your Accounts'
            message = render_to_string('auth/sendmail.html',{
                'user'   : user,
                'domain' : current_site.domain,
                'uid'    : urlsafe_base64_encode(force_bytes(user.pk)),
                'token'  : default_token_generator.make_token(user),
            })
            send_mail = form.cleaned_data.get('email')
            email = EmailMessage(mail_subjects,message, to=[send_mail])
            email.send()
            messages.info(request, 'Activate your account from the mail you provieded')
            return redirect ('login_page')
    else:
        form = SingupForm()
    return render(request, 'auth/singup.html', {'form' : form})    

@login_required
def activate_account(request,uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account is activate, now you can login')
        return redirect('login_page')
    else:
        messages.warning(request, 'activate link is invalid')
        return redirect ('singup_page')    


@login_required
def logout_page(request):
    logout(request)
    messages.success(request, 'Your account successfully logged out!')
    return redirect('login_page')

@login_required
def change_password(request):
    if request.method == "POST":
        form = ChangesPasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            return redirect('home_page_views')
    else:
        form = ChangesPasswordForm(user=request.user)
    return render(request, 'auth/passwordChange.html', {'form' : form})        




