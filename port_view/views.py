from django.shortcuts import render
from account.models import CustomUser
from education.models import Education
from language.models import Language
from skill.models import Skill
from projects.models import Project

def home(request):
    user = CustomUser.objects.first()

    # Education
    educations = Education.objects.filter(user=user).order_by('start_year')

    # Language
    languages = Language.objects.filter(user=user)

    # Skills: category bo'yicha guruhlash
    CATEGORY_ORDER = ['programming', 'database', 'framework', 'devops', 'other']
    skill_categories = []

    for category in CATEGORY_ORDER:
        skills = Skill.objects.filter(category=category)
        if skills.exists():
            skill_categories.append({
                'name': category,
                'display_name': dict(Skill.CATEGORY_CHOICES)[category],
                'skills': skills
            })

    # Projects
    real_projects = Project.objects.filter(user=user, project_type='real').order_by('-created_at')
    practice_projects = Project.objects.filter(user=user, project_type='practice').order_by('-created_at')

    context = {
        'user': user,
        'educations': educations,
        'languages': languages,
        'skill_categories': skill_categories,
        'real_projects': real_projects,
        'practice_projects': practice_projects,
    }
    return render(request, 'base.html', context)
