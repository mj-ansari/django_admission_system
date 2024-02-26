from django.shortcuts import redirect, render
from .forms import CustomSignupForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)

def user_signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully." )
            return redirect('login')
    else:
        form = CustomSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
