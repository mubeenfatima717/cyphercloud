from django.shortcuts import render
from django.shortcuts import redirect
from .models import File
#functions from other files 
from ai_classifier_app.classifier import analyze_file_type
from security_app.encryption import encrypt


def upload_view(request):
    # if not loged in
    if not request.user.is_authenticated:
        return redirect('login')
    
    #if file is uploaded
    if request.method == 'POST':
        f = request.FILES.get('file_input') # getting file

        if f:
            #reading the file 
            data = f.read()
            ftype = analyze_file_type(f.name)#type of file
            locked_data = encrypt(data)#encrypting it

            #in data base
            File.objects.create(
                owner = request.user,
                file_name = f.name,
                file_data = locked_data,
                file_type = ftype,
                file_size = f.size
            )
            return redirect('dashboard')

    return render(request, 'storage/dashboard.html')
