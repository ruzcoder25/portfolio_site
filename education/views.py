from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Education
from .forms import EducationForm
from django.contrib import messages

class EducationListView(LoginRequiredMixin, ListView):
    model = Education
    template_name = 'admin/educations/education_list.html'
    context_object_name = 'educations'



class EducationCreateView(LoginRequiredMixin, CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'admin/educations/education_form.html'
    success_url = reverse_lazy('education_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Yangi TA'LIM qo'shildi ✅")
        return super().form_valid(form)


class EducationUpdateView(LoginRequiredMixin, UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'admin/educations/education_form.html'
    success_url = reverse_lazy('education_list')


class EducationDeleteView(LoginRequiredMixin, DeleteView):
    model = Education
    template_name = 'admin/educations/education_confirm_delete.html'
    success_url = reverse_lazy('education_list')