from django.shortcuts import render

from django.shortcuts import redirect
from .models import File

#functions from other files 
from ai_classifier_app.classifier import analyze_file_type
from security_app.encryption import encrypt


def upload_view(request):
    # if not loged in
    if not request.user.is_authenticated:
        return redirect('login.html')
    
    #if file is uploaded
    if request.method == 'POST':
        f = request.FILES.get('user_file') # getting file

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
            return redirect('dashboard.html')

    return render(request, 'dashboard.html')



import os
from django.conf import settings
from django.http import HttpResponse
from .models import File
from security_app.encryption import decrypt 

def download_file(request, file_id):
    file_obj = File.objects.get(id=file_id)
    file_path = os.path.join(settings.MEDIA_ROOT, file_obj.encrypted_name)
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = decrypt(encrypted_data)
    response = HttpResponse(decrypted_data, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file_obj.file_name}"'
    return response
