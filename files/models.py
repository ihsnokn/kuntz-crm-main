from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django import forms


class User(AbstractUser):  # auth.models in prebuild user modeli
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# filefield 1.03


class Lawyer(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)  # auth için
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class File(models.Model):

    SOURCE_CHOICES = (
        # database name and display value respectively
        ('evrak_bekleyen', 'Evrak Bekleyen'),
        ('talep', 'Talep'),
        ('dava_acilacak', 'Dava Açılacak'),
        ('ara_karar', 'Ara Karar'),
        ('bilir_kisi_raporu', 'Bilir Kişi Raporu'),
        ('karar', 'Karar'),
        ('icra', 'İcra'),
        ('odeme_bekleyen', 'Ödeme Bekleyen'),
        ('kapanis', 'Kapanış'),
        ('ikinci_talep', '2. Talep'),
    )

    dosya_no = models.BigIntegerField(default=0)
    basvuran = models.CharField(max_length=30)
    basvurulan = models.CharField(max_length=30)
    plaka = models.CharField(max_length=10)
    basvuru_konusu = models.TextField(max_length=150)
    dava_tarihi = models.DateField(max_length=30, null=True, blank=True)
    dosya_durumu = models.CharField(
    default='', choices=SOURCE_CHOICES, max_length=100)
    olusturan = models.CharField(max_length=30)

    # File upload handle
    #dosya = models.FileField(upload_to='uploads/', blank=True, null=True)

    # avukat silinince dosya da silinecek
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.basvuran} {self.basvurulan}"
    @property
    def get_image(self):
        image = self.image_set.all()
        return image 

#------ Signals -----
def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)


class Image(models.Model):
    file_name = models.ForeignKey(File, on_delete=models.CASCADE)
    image = models.FileField(upload_to='class')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.image)
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
