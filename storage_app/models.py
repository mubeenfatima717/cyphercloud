from django.db import models
from django.contrib.auth.models import User
class Folder(models.Model):
    #field to store the folder name as text
    name = models.CharField(max_length=255)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name="sub_folder")
    owner=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name="folders")
    created_at=models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.name 
class File(models.Model): 
    file_name=models.CharField(max_length=255) #user sees like .pdf, .txt , etc

    owner=models.ForeignKey(User,related_name="files",on_delete=models.CASCADE)
    file_data=models.BinaryField()
    folder=models.ForeignKey(Folder,null=True,blank=True,related_name="files",on_delete=models.CASCADE)
    file_type=models.CharField(max_length=255) 
    file_size=models.BigIntegerField() 
    is_encrypted=models.BooleanField(default=True) 
    version=models.IntegerField(default=1)  
    uploaded_at=models.DateTimeField(auto_now_add=True) 
    def __str__(self): 
        return self.file_name 



