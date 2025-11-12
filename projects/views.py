from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Project
from skill.models import Skill
from skill.forms import SkillForm  # Skill form ni import qilish


@login_required
def project_create(request):
    # Foydalanuvchining skill larini tekshirish
    skill_exists = Skill.objects.filter(user=request.user).exists()

    # Yangi skill form
    skill_form = SkillForm(user=request.user)

    if request.method == 'POST':
        # Agar yangi skill qo'shish so'ralgan bo'lsa
        if 'add_skill' in request.POST:
            skill_form = SkillForm(request.POST, user=request.user)
            if skill_form.is_valid():
                skill = skill_form.save(commit=False)
                skill.user = request.user
                skill.save()
                messages.success(request, 'Yangi ko\'nikma muvaffaqiyatli qo\'shildi!')
                # Sahifani qayta yuklash
                return redirect('project_create')

        # Agar loyiha yaratish so'ralgan bo'lsa
        else:
            form = ProjectForm(request.POST, user=request.user)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user
                project.save()
                form.save_m2m()
                messages.success(request, 'Loyiha muvaffaqiyatli yaratildi.')
                return redirect('project_list')
            else:
                messages.error(request, 'Iltimos, formani to\'g\'ri to\'ldiring.')
    else:
        form = ProjectForm(user=request.user)

    context = {
        'form': form,
        'skill_form': skill_form,
        'skill_exists': skill_exists,
        'object': None,
        'user_skills': Skill.objects.filter(user=request.user)  # Foydalanuvchi ko'nikmalari
    }
    return render(request, 'admin/project/project_create.html', context)


# Qolgan view lar o'zgarmaydi
@login_required
def project_list(request):
    projects = Project.objects.filter(user=request.user).order_by('-created_at')
    context = {'projects': projects}
    return render(request, 'admin/project/project_list.html', context)


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    context = {'project': project}
    return render(request, 'admin/project/project_detail.html', context)


@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    skill_exists = Skill.objects.filter(user=request.user).exists()
    skill_form = SkillForm(user=request.user)

    if request.method == 'POST':
        if 'add_skill' in request.POST:
            skill_form = SkillForm(request.POST, user=request.user)
            if skill_form.is_valid():
                skill = skill_form.save(commit=False)
                skill.user = request.user
                skill.save()
                messages.success(request, 'Yangi ko\'nikma muvaffaqiyatli qo\'shildi!')
                return redirect('project_update', pk=pk)

        else:
            form = ProjectForm(request.POST, instance=project, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Loyiha muvaffaqiyatli yangilandi!')
                return redirect('project_detail', pk=project.pk)
            else:
                messages.error(request, 'Iltimos, formani to\'g\'ri to\'ldiring.')
    else:
        form = ProjectForm(instance=project, user=request.user)

    context = {
        'form': form,
        'skill_form': skill_form,
        'project': project,
        'skill_exists': skill_exists,
        'object': project,
        'user_skills': Skill.objects.filter(user=request.user)
    }
    return render(request, 'admin/project/project_update.html', context)


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        project_name = project.project_name
        project.delete()
        messages.success(request, f'"{project_name}" loyihasi muvaffaqiyatli o\'chirildi!')
        return redirect('project_list')

    context = {'project': project}
    return render(request, 'admin/project/project_delete.html', context)