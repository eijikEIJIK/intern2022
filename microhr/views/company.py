from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from microhr.models import Work
from microhr.forms import WorkForm

def top(request):
    works = Work.objects.all()
    context = {"works": works}
    return render(request, "works/top.html", context)

@login_required
def work_new(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.company = request.user
            work.save()
            return redirect(work_detail, work_id=work.pk)
    else:
        form = WorkForm()     
    return render(request, 'works/new.html', {'form': form})

def work_detail(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    return render(request, 'works/detail.html', {'work': work})

@login_required
def work_edit(request, work_id):
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
    return render(request, 'works/edit.html', {'form': form})

@login_required
def work_delete(request, work_id):
    return HttpResponse("delete work")
