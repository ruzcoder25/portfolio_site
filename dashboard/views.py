from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from education.models import Education
from language.models import Language
from projects.models import Project
from skill.models import Skill

@login_required(login_url='login_admin')
def dashboard(request):
    user = request.user

    # Ob'ektlar sonini hisoblash
    education_count = Education.objects.count()
    language_count = Language.objects.count()
    project_count = Project.objects.count()
    skill_count = Skill.objects.count()

    context = {
        'user': user,
        'education_count': education_count,
        'language_count': language_count,
        'project_count': project_count,
        'skill_count': skill_count,
    }
    return render(request, 'admin_dashbord.html', context)
