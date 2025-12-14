from django.shortcuts import render, redirect

#to connect with table in sal and check the user 
from django.contrib.auth.models import User
# so that user is directly created in the database agter the signup button
from django.contrib.auth import login
#for authnenticate function
from django.contrib.auth import authenticate
#for logout
from django.contrib.auth import logout


# if registeration pageis opened
def register_view(request):
     
     #it checks if user press the registeration btn to register in website
     if request.method == 'POST':  # TODO: why capital
          
         #getting the user's info
         input_username = request.POST.get('username')
         input_email = request.POST.get('email')
         input_password = request.POST.get('password')

         #checking if user already exist in the database
         if User.objects.filter(username=input_username).exists():
            #  return HttpResponse("user already exists")
            return render(request, 'authentication_app/login.html', {'message': 'Account already exists. Please Log In.'})
         else:
             # TODO: all teh equvalent commands for the commands in sql
             new_user = User.objects.create_user(input_username , input_email , input_password)
             login(request, new_user)
             return redirect('dashboard') 
     # if user just seeing the page 
     else:
         return render(request, 'authentication_app/register.html')
      
     
def login_view(request):
    if request.method == "POST":
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')

        user = authenticate(username = input_username ,password = input_password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'authentication_app/login.html' , {'message' : 'wrong information or account does not exist'} ) 
     
    else:
        return render(request, 'authentication_app/login.html')
    

def logout_view(request):
    logout(request)
    return redirect('login')