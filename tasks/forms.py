from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from tasks.models import TaskList

class SingupForm(UserCreationForm):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = User
        fields = [ 'username','email']


class ChangesPasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].help_text = None
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None

    class Meta:
        model = User
        fields = [ 'old_password','new_password1','new_password2']   
        
        
class TaskListForm(forms.ModelForm):
 
    class Meta:
        model = TaskList
        fields = ['title','images','price','categrory','description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }
