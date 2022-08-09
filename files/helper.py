import os
from .models import File,Image
from django.conf import settings

def classification_helper(name,files,form):
        #class_check=File.objects.filter(name=name).count()
        
        file = form.save(commit=False)
        file.save()
        file_name = File.objects.filter(dosya_no=file.dosya_no).first()
        for file in files:
            deneme= Image.objects.create(file_name=file_name, image=file)
            deneme.save()
            initial_path = deneme.image.path
            directory = str(name)
            parent_dir = settings.MEDIA_ROOT +"//class" ## windows için \\ 
            path = os.path.join(parent_dir, directory)
            x = str(deneme.image).split("/")
            if not os.path.exists(path):
                os.mkdir(path)
            new_path = settings.MEDIA_ROOT + "//" + x[0] + "//"  +  str(name)  + "//" + x[-1]  ## windows için \\ 
            print(x[0] + "//"  +  str(name)  + "//" + x[-1])  ## windows için \\ 
            link_path=x[0] + "//"  +  str(name)  + "//" + x[-1]  ## windows için \\ 
            os.replace(initial_path, new_path)
            deneme.image = link_path 
            deneme.save()
            