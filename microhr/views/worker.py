from asyncio.windows_events import NULL
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from microhr.forms import WorkerProfileForm
from microhr.models import Application,Work
from accounts.models import User
from microhr.decorators import worker_required
from logging import getLogger
logger = getLogger(__name__)


@login_required
@worker_required
def resume(request):
    """履歴書表示(GET)・編集(POST)"""

    if request.method == 'POST':
        form = WorkerProfileForm(request.POST,
                                 instance=request.user.workerprofile)
        if form.is_valid():
            worker_profile = form.save()
            worker_profile.save()
            return redirect('home')
    else:
        form = WorkerProfileForm(instance=request.user.workerprofile)
    return render(request, 'resume/edit.html', {'form': form})


@login_required
@worker_required
def apply(request, work_id):
    """求人へ応募する（未実装）"""
    logger.warn("unimplemented")

    # そもそもこのPOSTかGETの条件分岐を毎回描かないといけないのはどうにかならないのか？
    # デコレーターとかを上手く使えないのか…？
    user = get_object_or_404(User, pk=request.user.id)
    work = get_object_or_404(Work, pk=work_id)
    if request.method == 'POST':
        Application.objects.create(
            work=work,
            user=user,
            is_passed=None)
    else:
        # それ以外の時は多分ここに何かを書かなければいけない
        # form = ApplyForm()
        pass

    # 本当はこんな感じになるような気がする
    # return render(request, 'work/apply.html', {'form': form})
    return redirect('/work/application')


@login_required
@worker_required
def show_application(request):
    user = get_object_or_404(User, pk=request.user.id)
    applications=Application.objects.filter(user=user)
    return render(request, 'application/application.html',{'applications':applications})
