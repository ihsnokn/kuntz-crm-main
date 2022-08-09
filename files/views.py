from distutils.log import Log
import os
from django.shortcuts import render, redirect, reverse,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect

from files.helper import classification_helper
from .models import File, Image, Lawyer
from .forms import FileForm, FileModelForm, CustomUserCreationForm, ImageForm
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib.auth import logout

# CRUD create retrieve update delete + list


class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


# LANDING PAGE VIEW
class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


def landing_page(request):
    return render(request, "landing.html")


# FILE LIST VIEW
class FileListView(LoginRequiredMixin, generic.ListView):
    template_name = "files/file_list.html"
    queryset = File.objects.all()
    context_object_name = "files"


def file_list(request):

    files = File.objects.all()

    context = {
        "files": files
    }

    return render(request, "files/file_list.html", context)

# FILE DETAIL VIEW


# class FileDetailView(LoginRequiredMixin, generic.DetailView):
#     template_name = "files/file_detail.html"
#     queryset = File.objects.all()
#     context_object_name = "file"


# def file_detail(request, pk):

#     file = File.objects.get(id=pk)
#     context = {
#         "file": file
#     }

#     return render(request, "files/file_detail.html", context)


def FileDetail(request,id):
    file = get_object_or_404(File,id = id)

    images = file.image_set.all()
    print(images)
    for i in images:

        print(i)
        #os.path.dirname(i)
    context = {
        "file": file,
        "images": images,
    }
    return render(request, "files/file_detail.html", context)



# FILE CREATE VIEW


# class FileCreateView(LoginRequiredMixin, generic.CreateView):
#     template_name = "files/file_create.html"
#     form_class = FileModelForm,ImageForm

#     def get_success_url(self):
#         return reverse("files:file-list")

#     def form_valid(self, form):
#         # TODO mail yolla

#         send_mail(
#             subject="Yeni dosya oluşturuldu",
#             message="Oluşturulan dosyayı görmek için sisteme girin",
#             from_email="test@test.com",
#             recipient_list=["test2@test.com"]
#         )

#         return super(FileCreateView, self).form_valid(form)


# def file_create(request):
#     #form = FileModelForm()
#     if request.method == "POST":
#         dosya_no = request.POST['dosya_no']
#         basvuran = request.POST['basvuran']
#         basvurulan = request.POST['basvurulan']
#         plaka = request.POST['plaka']
#         basvuru_konusu = request.POST['basvuru_konusu']
#         dava_tarihi = request.POST['dava_tarihi']
#         dosya_durumu = request.POST['dosya_durumu']
#         olusturan = request.POST['olusturan']
#        # dosya = request.FILE['dosya']
#         dosya = request.FILES.getlist("dosya")

#         a = File(dosya_no=dosya_no, basvuran=basvuran, basvurulan=basvurulan, plaka=plaka, basvuru_konusu=basvuru_konusu,
#                  dava_tarihi=dava_tarihi, dosya_durumu=dosya_durumu, olusturan=olusturan, dosya=dosya)
#         a.save()
#         return redirect("/files")
#     else:
#         return redirect("/files")


# def handle_uploaded_file(f):
#     with open(f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def FileCreateView(request):
    form=FileModelForm(request.POST or None)
    formimage=ImageForm(request.POST or None)
    if request.method == 'POST':
        files = request.FILES.getlist("image")
        name= form.data.get('dosya_no')
        if not (form.errors):
                classification_helper(name,files,form)
               # messages.success(request,"You are added product successfully.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,"files/file_create.html",{'form':form,'formimage':formimage})


def sign_out(request):
	logout(request)
	return redirect("login") 























# FILE UPDATE VIEW


class FileUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "files/file_update.html"
    queryset = File.objects.all()
    form_class = FileModelForm

    def get_success_url(self):
        return reverse("files:file-list")


def file_update(request, pk):
    file = File.objects.get(id=pk)
    form = FileModelForm(instance=file)
    #
    if request.method == "POST":
        dosya_no = request.POST['dosya_no']
        basvuran = request.POST['basvuran']
        basvurulan = request.POST['basvurulan']
        plaka = request.POST['plaka']
        basvuru_konusu = request.POST['basvuru_konusu']
        dava_tarihi = request.POST['dava_tarihi']
        dosya_durumu = request.POST['dosya_durumu']
        olusturan = request.POST['olusturan']
        dosya = request.FILE['dosya']

        a = File(dosya_no=dosya_no, basvuran=basvuran, basvurulan=basvurulan, plaka=plaka, basvuru_konusu=basvuru_konusu,
                 dava_tarihi=dava_tarihi, dosya_durumu=dosya_durumu, olusturan=olusturan, dosya=dosya)
        a.save()
        return redirect("/files")
    else:
        return redirect("/files")


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    '''''
    if request.method == "POST":
        form = FileModelForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            return redirect("/files")
    context = {
        "form": form,
        "file": file
    }
    return render(request, "files/file_update.html", context)
'''
# FILE DELETE VIEW


class FileDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "files/file_delete.html"
    queryset = File.objects.all()

    def get_success_url(self):
        return reverse("files:file-list")


def file_delete(request, pk):
    file = File.objects.get(id=pk)
    file.delete()
    return redirect("/files")


"""def file_update(request, pk):
    file = File.objects.get(id=pk)
    form = FileForm()
    if request.method == "POST":
        print("receiving post req")
        form = FileForm(request.POST)
        if form.is_valid():
            print("Form is valid!")
            print(form.cleaned_data)
            dosya_no = form.cleaned_data['dosya_no']
            basvuran = form.cleaned_data['basvuran']
            basvurulan = form.cleaned_data['basvurulan']
            plaka = form.cleaned_data['plaka']
            basvuru_konusu = form.cleaned_data['basvuru_konusu']
            dava_tarihi = form.cleaned_data['dava_tarihi']
            dosya_durumu = form.cleaned_data['dosya_durumu']
            olusturan = form.cleaned_data['olusturan']
            dosya = form.cleaned_data['dosya'] #file upload

            file.dosya_no=dosya_no
            file.basvuran=basvuran
            file.basvurulan=basvurulan
            file.plaka=plaka
            file.basvuru_konusu=basvuru_konusu
            file.dava_tarihi=dava_tarihi
            file.dosya_durumu=dosya_durumu
            file.olusturan=olusturan
            file.dosya=dosya
            file.save()
            print("Dosya oluşturuldu")
            return redirect("/files")
    
    context = {
        "form": form,
        "file": file
    }
    return render(request, "files/file_update.html", context)"""


"""def file_create(request):
    form = FileForm()
    if request.method == "POST":
        print("receiving post req")
        form = FileForm(request.POST)
        if form.is_valid():
            print("Form is valid!")
            print(form.cleaned_data)
            dosya_no = form.cleaned_data['dosya_no']
            basvuran = form.cleaned_data['basvuran']
            basvurulan = form.cleaned_data['basvurulan']
            plaka = form.cleaned_data['plaka']
            basvuru_konusu = form.cleaned_data['basvuru_konusu']
            dava_tarihi = form.cleaned_data['dava_tarihi']
            dosya_durumu = form.cleaned_data['dosya_durumu']
            olusturan = form.cleaned_data['olusturan']
            dosya = form.cleaned_data['dosya'] #file upload
            lawyer = Lawyer.objects.first()
            File.objects.create(
                dosya_no=dosya_no,
                basvuran=basvuran,
                basvurulan=basvurulan,
                plaka=plaka,
                basvuru_konusu=basvuru_konusu,
                dava_tarihi=dava_tarihi,
                dosya_durumu=dosya_durumu,
                olusturan=olusturan,
                dosya=dosya,
                lawyer=lawyer
            )
            print("Dosya oluşturuldu")
            return redirect("/files")
    context = {
        "form": form
    }
    return render(request, "files/file_create.html", context)"""
