from django import forms
from matplotlib import widgets
from .models import File, Image
from django.forms import ClearableFileInput
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
import datetime
from django.utils.translation import gettext_lazy as _
User = get_user_model()


# class FileModelForm(forms.ModelForm):
#     class Meta:
#         model = File
#         fields = (
#             'dosya_no',
#             'basvuran',
#             'basvurulan',
#             'plaka',
#             'basvuru_konusu',
#             'dava_tarihi',
#             'dosya_durumu',
#             'olusturan',
#             'dosya',
#             'dosya_durumu',
#             'lawyer'
#         )
#         widgets = {'dosya': ClearableFileInput(attrs={'multiple': True}), }

# from .models import Lawyer # sonra bak

class FileModelForm(forms.ModelForm):
   # dosya = forms.FileField(
    # label="Dosya",
    #widget=forms.ClearableFileInput(attrs={"multiple": True}),
    # )
    class Meta:
        model = File
        fields = ('__all__')

        error_messages = {


        }


class FileForm(forms.Form):
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

    dosya_no = forms.IntegerField(min_value=0)
    basvuran = forms.CharField()
    basvurulan = forms.CharField()
    plaka = forms.CharField()
    basvuru_konusu = forms.CharField(widget=forms.Textarea)
    dava_tarihi = forms.DateTimeField(initial=datetime.date.today)

    dosya_durumu = forms.MultipleChoiceField(
        required=False, widget=forms.CheckboxSelectMultiple, choices=SOURCE_CHOICES,)
    olusturan = forms.CharField(max_length=30)

    # file upload#######################
    dosya = forms.FileField(
        required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    #lawyer = forms.CharField()
    # lawyer = forms.ForeignKey(Lawyer, on_delete=models.CAasaSCADE1) """


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class ImageForm(forms.ModelForm):
    image = forms.FileField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )

    class Meta:
        model = Image
        fields = ("image",)
        error_messages = {
            'image': {
                'null': _("Please input image."),
            },

        }
