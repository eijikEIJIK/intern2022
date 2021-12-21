from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from microhr.forms import WorkerProfileForm
from microhr.decorators import worker_required

@login_required
@worker_required
def resume(request):
    """履歴書表示(GET)・編集(POST)"""

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
    """求人へ応募する（未実装）"""

    if request.method == 'POST':
        # 多分ここに応募URLにPOSTされたときの処理を書かないといけない
        pass
    else:
        # それ以外の時は多分ここに何かを書かなければいけない
        # form = ApplyForm()     
        pass
    
    # 本当はこんな感じになるような気がする
    # return render(request, 'work/apply.html', {'form': form})
    return HttpResponse("apply work")

