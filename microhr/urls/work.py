from django.urls import path

from microhr.views import company, worker


urlpatterns = [
    path('new/', company.work_new, name='work_new'),
    path('<int:work_id>/', company.work_detail, name='work_detail'),
    path('<int:work_id>/edit', company.work_edit, name='work_edit'),
    path('<int:work_id>/delete', company.work_delete, name="work_delete"),
    path('applicant/', company.work_applicant, name="work_applicant"),
    path('<int:application_id>/evaluate', company.work_evaluate, name="work_evaluate"),
    
    path('<int:work_id>/apply', worker.apply, name="work_apply"),
    path('application/', worker.show_application, name="work_show_application"),
]
