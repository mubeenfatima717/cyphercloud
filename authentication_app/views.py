from django.shortcuts import render

# Create your views here.

# View to render the Login Page (Task 2)
def login_view(request):
    # Renders the login.html template
    return render(request, 'authentication/login.html', {})

# View to render the Register Page (Task 3)
def register_view(request):
    # Renders the register.html template
    return render(request, 'authentication/register.html', {})