from django.contrib import admin

# Register your models here.
from .models import JobAdvert

class JobAdvertAdmin(admin.ModelAdmin):

    list_display = ('job_tracking_id','title','is_active')
    list_editable=('is_active',)
    search_fields = ('job_tracking_id',)
    # ordering = ('-created_at',)

# class AdvertisementTracker(admin.ModelAdmin):
#     list_display = ('job', 'applied_at',)


# admin.site.register(Application, AdvertisementTracker)

admin.site.register(JobAdvert, JobAdvertAdmin)