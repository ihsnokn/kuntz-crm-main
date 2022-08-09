from django.contrib import admin

from .models import Image, User, File, Lawyer, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(File)
admin.site.register(Lawyer)


admin.site.register(Image)
# Register your models here.
