from tasks.views import home_page,create_tasks,tasks_list,tasks_list_details,tasks_list_update,tasks_list_delete
from tasks.user_auth.views import login_page,logout_page,singup_page,change_password,activate_account
from django.urls import path

#builtin use
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('home/' , home_page , name='home_page_views'),
    
    path('tasks-form/' , create_tasks , name='create_tasks'),
    path('tasks-list/' , tasks_list , name='tasks_list'),
    path('tasks-list-details/<int:id>/' , tasks_list_details , name='tasks_list_details'),
    path('tasks_list_update/<int:id>/' , tasks_list_update , name='tasks_list_update'),
    path('tasks_list_delete/<int:id>/' , tasks_list_delete , name='tasks_list_delete'),
    
    path('' , login_page , name='login_page'),
    path('logout/' , logout_page , name='logout_page'),
    path('signup/' , singup_page , name='singup_page'),
    path('password/' , change_password , name='change_password'),
    path('activate/<uidb64>/<token>/' , activate_account , name='activate_account'),


    path('reset-password/',PasswordResetView.as_view(template_name='auth/reset_password.html'), name='password_reset'),
    path('reset-password-done/',PasswordResetDoneView.as_view(template_name='auth/reset_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='auth/reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset-done/',PasswordResetCompleteView.as_view(template_name='auth/reset_password_complete.html'), name='password_reset_complete'),
]
