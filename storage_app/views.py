from django.shortcuts import render, redirect
from .models import File
from .models import Folder
# import os
# from django.conf import settings
from django.http import HttpResponse

# Functions from other files
from ai_classifier_app.classifier import analyze_file_type
from security_app.encryption import encrypt
from security_app.encryption import decrypt






#view for the dashboard and uploads
def upload_view(request, folder_id=None):
    if not request.user.is_authenticated:
        return redirect('login')

    #when file is uploaded
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file_input')
        parent_folder_id = request.POST.get('folder_id')

        parent_folder = None
        if parent_folder_id:
           
            parent_folder = Folder.objects.filter(owner=request.user, id=parent_folder_id).first()

        if uploaded_file:
            data = uploaded_file.read()
            ftype = analyze_file_type(uploaded_file.name)
            locked_data = encrypt(data)

            File.objects.create(
                owner=request.user,
                file_name=uploaded_file.name,
                file_data=locked_data,
                file_type=ftype,
                file_size=uploaded_file.size,
                folder=parent_folder 
            )

        # redirect the user back to the folder they were in
        if parent_folder:
            return redirect('dashboard_folder', folder_id=parent_folder.id)
        return redirect('dashboard')

    # get request of user
    current_folder = None
    if folder_id:
        # specific folder
        current_folder = Folder.objects.filter(owner=request.user, id=folder_id).first()

    if current_folder:
        #files that are inside the current folder
        files = File.objects.filter(owner=request.user, folder=current_folder)
    else:
        #files that are in the root not in any folder
        files = File.objects.filter(owner=request.user, folder__isnull=True)

    # all folders to display in the sidebar
    folders = Folder.objects.filter(owner=request.user)

    context = {
        'files': files,
        'folders': folders,
        'current_folder': current_folder,
    }
    return render(request, 'storage/dashboard.html', context)


def download_file(request, file_id):
    f = File.objects.get(id=file_id, owner=request.user)
    locked_data = f.file_data
    original_data = decrypt(locked_data)
    response = HttpResponse(original_data, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{f.file_name}"'
    return response


def delete_file(request, file_id):
    if not request.user.is_authenticated:
        return redirect('login')
    file_to_delete = File.objects.filter(id=file_id, owner=request.user).first()
    
    # Store the folder ID before deleting the file
    if file_to_delete and file_to_delete.folder:
        folder_id = file_to_delete.folder.id
        file_to_delete.delete()
        return redirect('dashboard_folder', folder_id=folder_id)
    elif file_to_delete:
        file_to_delete.delete()

    return redirect('dashboard')


def create_folder(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')
        if folder_name:
            Folder.objects.create(name=folder_name, owner=request.user)
        return redirect('dashboard')
    return render(request, 'storage/create_folder.html')