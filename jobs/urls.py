from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_sample_jobs/', views.create_sample_jobs, name='create_sample_jobs'),
    path('<slug:job_tracking_id>/', views.job_details, name='job_details'),
    # path('', views.job_details, name='job_details'),
    # path('apply_job/<slug:job_tracking_id>/', views.apply_job, name='apply_job'),
    # path('update_job/<slug:job_tracking_id>/',views.update_job_details, name='update_job_details'),
]