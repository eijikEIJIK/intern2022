from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from microhr.models import Work
from accounts.models import User
from logging import getLogger
logger = getLogger(__name__)


def home(request):
    """HOME"""
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
        if user.is_company:
            works = Work.objects.filter(company=user)
        else:
            works = Work.objects.all()
    else:
        works = Work.objects.all()
    context = {"works": works}
    
    return render(request, "home.html", context)
