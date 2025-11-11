from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Project

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  # user avtomatik kiritiladi
            project.save()
            form.save_m2m()  # skill kabi ManyToMany maydonlar uchun
            messages.success(request, 'Loyiha muvaffaqiyatli yaratildi.')
            return redirect('project_list')
    else:
        form = ProjectForm()

    context = {'form': form}
    return render(request,'admin/project/project_create.html', context)

@login_required
def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request,'admin/project/project_list.html', context)

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {'project': project}
    return render(request, 'admin/project/project_detail.html', context)

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mahsulot muvaffaqiyatli yangilandi!')
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)

    context = {'form': form, 'project': project}
    return render(request, 'admin/project/project_update.html', context)

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Mahsulot muvaffaqiyatli o\'chirildi!')
        return redirect('project_list')

    context = {'project': project}
    return render(request, 'admin/project/project_delete.html', context)