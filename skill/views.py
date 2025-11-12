from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Skill
from .forms import SkillForm



@login_required
def skill_list(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'admin/skill/skill_list.html', {'skills': skills})


@login_required
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, 'Ko‘nikma muvaffaqiyatli yaratildi.')
            return redirect('skill_list')
        else:
            messages.error(request, 'Iltimos, formani to‘g‘ri to‘ldiring.')
    else:
        form = SkillForm()

    return render(request, 'admin/skill/skill_form.html', {'form': form})



@login_required
def skill_update(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ko‘nikma muvaffaqiyatli yangilandi.')
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)

    return render(request, 'admin/skill/skill_form.html', {'form': form, 'skill': skill})


@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    if request.method == 'POST':
        skill_name = skill.name
        skill.delete()
        messages.success(request, f'"{skill_name}" ko‘nikmasi muvaffaqiyatli o‘chirildi.')
        return redirect('skill_list')

    return render(request, 'admin/skill/skill_delete.html', {'skill': skill})


