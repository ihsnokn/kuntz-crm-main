from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from files.models import Lawyer
from .forms import LawyerModelForm

class LawyerListView(LoginRequiredMixin ,generic.ListView):
    template_name = "lawyers/lawyer_list.html"

    def get_queryset(self):
        return Lawyer.objects.all()

class LawyerCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "lawyers/lawyer_create.html"
    form_class = LawyerModelForm

    def get_success_url(self):
        return reverse("lawyers:lawyer-list")

    def form_valid(self, form):
        lawyer = form.save(commit=False)
        lawyer.organisation = self.request.user.userprofile
        lawyer.save()
        return super(LawyerCreateView, self).form_valid(form)

class LawyerDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "lawyers/lawyer_detail.html"
    context_object_name = "lawyer"

    def get_queryset(self):
        return Lawyer.objects.all()

class LawyerUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "lawyers/lawyer_update.html"
    form_class = LawyerModelForm

    def get_success_url(self):
        return reverse("lawyers:lawyer-list")

    def get_queryset(self):
        return Lawyer.objects.all()

class LawyerDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "lawyers/lawyer_delete.html"
    context_object_name = "lawyer"

    def get_success_url(self):
        return reverse("lawyers:lawyer-list")

    def get_queryset(self):
        return Lawyer.objects.all()
    