from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Language

# Admin uchun test Mixin
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff  # faqat admin
    def handle_no_permission(self):
        return redirect('language_list')   # admin bo'lmasa ro'yxatga yo'naltirish

# 1️⃣ Har kim ko'ra oladigan ro'yxat
class LanguageListView(ListView):
    model = Language
    template_name = 'admin/language/list.html'
    context_object_name = 'languages'
    queryset = Language.objects.all()  # barcha foydalanuvchilar ko'rsin

# 3️⃣ Til qo'shish (faqat admin)
class LanguageCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Language
    fields = ['name', 'level']
    template_name = 'admin/language/form.html'
    success_url = reverse_lazy('language_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# 4️⃣ Til tahrirlash (faqat admin)
class LanguageUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Language
    fields = ['name', 'level']
    template_name = 'admin/language/form.html'
    success_url = reverse_lazy('language_list')

# 5️⃣ Til o'chirish (faqat admin)
class LanguageDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Language
    template_name = 'admin/language/delete.html'
    success_url = reverse_lazy('language_list')
