
import os
from .models import File
def get_available_name(file_name,user):
    name,ext=os.path.splitext(file_name)
    counter=1
    new_file=file_name
    while File.objects.filter(file_name=new_file, owner=user).exists():
        counter+=1
        new_file=f"{name}_v{counter}{ext}"
    return new_file 

