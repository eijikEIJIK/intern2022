from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from microhr.models import Work
from accounts.models import User
from logging import getLogger
logger = getLogger(__name__)

@login_required
def home(request):
    """HOME"""
    user = get_object_or_404(User, pk=request.user.id)
    if user.is_company:
        works = Work.objects.filter(company=user)
        context = {"works": works}
    else:
        works = Work.objects.all()
        context = {"works": works}
    return render(request, "home.html", context)
