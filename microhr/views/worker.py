from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from microhr.models import Work
from microhr.forms import WorkForm, WorkerProfileForm
from microhr.decorators import worker_required

@login_required
@worker_required
def resume(request):
    # if request.method == 'POST':        
    #     form = WorkForm(request.POST, instance=work)
    #     if form.is_valid():
    #         work = form.save()
    #         work.save()
    #         return redirect(work_detail, work_id=work_id)
    # else:
    #    form = WorkForm(instance=work)

    if request.method == 'POST':
        form = WorkerProfileForm(request.POST, instance=request.user.workerprofile)
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
    if request.method == 'POST':
        # 多分ここに応募URLにPOSTされたときの処理を書かないといけない
        pass
    else:
        # それ以外の時は多分ここに何かを書かなければいけない
        # form = ApplyForm()     
        pass
    
    # 本当はこんな感じになるような気がする
    # return render(request, 'works/apply.html', {'form': form})
    return HttpResponse("apply work")

