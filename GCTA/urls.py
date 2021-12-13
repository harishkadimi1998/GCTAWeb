from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('HomePage', views.HomePage , name='HomePage'),
    path('Login', views.Login , name='Login'),
    path('Logout', views.Logout , name='Logout'),
    path('Register', views.Register , name='Register'),
    path('RegisterPage', views.RegisterPage , name='RegisterPage'),
    path('Register_display', views.Register_display , name='Register_display'),
    path('Sendmail', views.Sendmail , name='Sendmail'),
    path('Submission', views.Submission , name='Submission'),
    path('Forgotpassword', views.Forgotpassword , name='Forgotpassword'),
    path('Pre_and_post', views.Pre_and_post , name='Pre_and_post'),
    path('Pre_and_post_insert', views.Pre_and_post_insert , name='Pre_and_post_insert'),
    path('Consentpage', views.Consentpage , name='Consentpage'),
    path('Consent', views.Consent , name='Consent'),
]

