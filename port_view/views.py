from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from account.models import CustomUser
from education.models import Education
from language.models import Language
from skill.models import Skill
from projects.models import Project


def home(request):
    """
    Portfolio asosiy sahifasi
    User mavjud bo'lmasa ham ishlaydi
    """
    # Agar user login qilgan bo'lsa, uning ma'lumotlarini ko'rsatish
    if request.user.is_authenticated:
        user = request.user
    else:
        # Login qilmagan holat uchun birinchi userni olish
        user = CustomUser.objects.first()

    # Agar umuman user yo'q bo'lsa, bo'sh context yuborish
    if not user:
        context = {
            'user': None,
            'educations': None,
            'languages': None,
            'skill_categories': None,
            'real_projects': None,
            'practice_projects': None,
            'has_education_or_languages': False,
        }
        return render(request, 'base.html', context)

    # Education - faqat mavjud bo'lsagina
    educations = Education.objects.filter(user=user).order_by('-start_year')

    # Language - faqat mavjud bo'lsagina
    languages = Language.objects.filter(user=user).order_by('level')

    # Skills: category bo'yicha guruhlash
    CATEGORY_ORDER = ['programming', 'database', 'framework', 'devops', 'other']
    CATEGORY_NAMES = {
        'programming': 'Dasturlash tillari',
        'database': 'Ma\'lumotlar bazasi',
        'framework': 'Framework va kutubxonalar',
        'devops': 'DevOps vositalari',
        'other': 'Boshqa ko\'nikmalar'
    }

    skill_categories = []
    for category in CATEGORY_ORDER:
        skills = Skill.objects.filter(category=category)
        if skills.exists():
            skill_categories.append({
                'name': category,
                'display_name': CATEGORY_NAMES.get(category, category),
                'skills': skills
            })

    # Projects - turi bo'yicha ajratish
    real_projects = Project.objects.filter(
        user=user,
        project_type='real'
    ).order_by('-created_at')

    practice_projects = Project.objects.filter(
        user=user,
        project_type='practice'
    ).order_by('-created_at')

    context = {
        'user': user,
        'educations': educations if educations.exists() else None,
        'languages': languages if languages.exists() else None,
        'skill_categories': skill_categories if skill_categories else None,
        'real_projects': real_projects if real_projects.exists() else None,
        'practice_projects': practice_projects if practice_projects.exists() else None,
        'has_education_or_languages': educations.exists() or languages.exists(),
    }

    return render(request, 'base.html', context)

# @login_required
# def dashboard_view(request):
#     """
#     Dashboard - faqat login qilgan foydalanuvchilar uchun
#     """
#     user = request.user
#
#     # Statistikalar
#     stats = {
#         'total_education': Education.objects.filter(user=user).count(),
#         'total_languages': Language.objects.filter(user=user).count(),
#         'total_skills': Skill.objects.count(),
#         'total_projects': Project.objects.filter(user=user).count(),
#         'real_projects': Project.objects.filter(user=user, project_type='real').count(),
#         'practice_projects': Project.objects.filter(user=user, project_type='practice').count(),
#     }
#
#     context = {
#         'user': user,
#         'stats': stats,
#     }
#
#     return render(request, 'dashboard.html', context)