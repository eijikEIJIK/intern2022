from asyncio.windows_events import NULL
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from microhr.models import Work,Application
from accounts.models import User
from accounts.models import WorkerProfile
from microhr.forms import WorkForm, WorkerProfileForm
from microhr.decorators import company_required
from logging import getLogger
from django.conf import settings
logger = getLogger(__name__)


@login_required
@company_required
def work_new(request):
    """新規の求人を登録する"""
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.company = request.user
            work.save()
            return redirect(work_detail, work_id=work.pk)
    else:
        form = WorkForm()
    return render(request, 'work/new.html', {'form': form})


def work_detail(request, work_id):
    """求人を詳細表示する"""
    logger.debug("show work detail")
    work = get_object_or_404(Work, pk=work_id)
    return render(request, 'work/detail.html', {'work': work})


@login_required
@company_required
def work_edit(request, work_id):
    """求人を編集する"""
    work = get_object_or_404(Work, pk=work_id)
    if work.company_id != request.user.id:
        return HttpResponseForbidden("この求人は編集できません")

    if request.method == 'POST':
        form = WorkForm(request.POST, instance=work)
        if form.is_valid():
            work = form.save()
            work.save()
            return redirect(work_detail, work_id=work_id)
    else:
        form = WorkForm(instance=work)
    return render(request, 'work/edit.html', {'form': form})


@login_required
@company_required
def work_delete(request, work_id):
    """求人を削除する"""
    work = get_object_or_404(Work, pk=work_id)
    if work.company_id != request.user.id:
        return HttpResponseForbidden("この求人は削除できません")

    if request.method == 'POST':
        work.delete()

    return redirect('/')

@login_required
@company_required
def work_applicant(request):
    user = get_object_or_404(User, pk=request.user.id)
    applications=Application.objects.select_related('work').exclude(work=None).filter(work__company_id=user.id)
    return render(request, 'work/applicant.html',{'applications': applications})

@login_required
@company_required
def work_evaluate(request, application_id):
    user = get_object_or_404(User, pk=request.user.id)
    application = get_object_or_404(Application, id=application_id)
    work=Work.objects.get(id=application.work.id)
    applicant=User.objects.get(id=application.user.id)
    return render(request, 'work/evaluation.html',{'work':work,'application': application,'applicant': applicant})
 

@login_required
@company_required
def work_evaluation(request, application_id):
    
    if request.method == 'POST':
        eval=request.POST.get("evaluation")
        application=Application.objects.get(id=application_id)
        if eval=="合格":
            application.is_passed=True
            application.save()
        elif eval=="不合格":
            application.is_passed=False
            application.save()

    return redirect('/')

