from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def logout_view(request):
    """Log the user out and redirect to the home page."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    """Handle user registration."""
    if request.method != 'POST':
        # No data submitted; create a blank registration form.
        form = UserCreationForm()
    else:
        # POST data submitted; process data
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to the home page.
            authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)