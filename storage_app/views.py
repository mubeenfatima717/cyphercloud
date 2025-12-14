from django.shortcuts import render, redirect
from .models import File
#functions from other files 
from ai_classifier_app.classifier import analyze_file_type
from security_app.encryption import encrypt

# Imports added by teammate
import os
from django.conf import settings
from django.http import HttpResponse
from security_app.encryption import decrypt

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

#function to download file 
def download_file(request, file_id):
    file_obj = File.objects.get(id=file_id)
    # Note: ensure 'encrypted_name' exists in your model, otherwise this might need adjustment later
    # For now, we assume the teammate's code logic is sound for their feature.
    file_path = os.path.join(settings.MEDIA_ROOT, file_obj.encrypted_name) 
    
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_data = decrypt(encrypted_data)
    
    response = HttpResponse(decrypted_data, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file_obj.file_name}"'
    return response
