from django.urls import path
from .views import user_signup,profile_view
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm,CustomPasswordChangeForm,CustomPasswordResetForm,CustomSetPasswordForm

urlpatterns = [
    path("signup/", user_signup, name="signup"), 
    path("profile/", profile_view, name="profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html",form_class=CustomLoginForm),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change_form.html",form_class=CustomPasswordChangeForm
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset_form.html",form_class=CustomPasswordResetForm,
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",form_class=CustomSetPasswordForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
