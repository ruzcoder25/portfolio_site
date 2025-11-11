from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Skill
from .forms import SkillForm  # SkillForm-ni avval forms.py-da yaratishingiz kerak

# Ro'yxat — barcha foydalanuvchilar ko‘rishi mumkin
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'admin/skill/skill_list.html', {'skills': skills})

# Batafsil — login talab qilinadi
@login_required
def skill_detail(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    return render(request, 'admin/skill/skill_detail.html', {'skill': skill})

# Yaratish — login talab qilinadi
@login_required
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ko‘nikma muvaffaqiyatli yaratildi.')
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'admin/skill/skill_form.html', {'form': form})

# Tahrirlash — login talab qilinadi
@login_required
def skill_update(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ko‘nikma muvaffaqiyatli yangilandi.')
            return redirect('skill_detail', pk=skill.pk)
    else:
        form = SkillForm(instance=skill)
    return render(request, 'admin/skill/skill_form.html', {'form': form, 'skill': skill})

# O‘chirish — login talab qilinadi
@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Ko‘nikma muvaffaqiyatli o‘chirildi.')
        return redirect('skill_list')
    return render(request, 'admin/skill/skill_delete.html', {'skill': skill})
