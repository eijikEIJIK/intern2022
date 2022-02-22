from django.shortcuts import render
from microhr.models import Work
from logging import getLogger
logger = getLogger(__name__)


def home(request):
    """HOME"""
    logger.debug("display home")
    works = Work.objects.all()
    context = {"works": works}
    return render(request, "home.html", context)
