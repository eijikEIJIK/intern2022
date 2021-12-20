from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from microhr.models import Work
from microhr.forms import WorkForm
from microhr.decorators import worker_required

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
