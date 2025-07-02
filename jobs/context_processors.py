from .models import JobAdvert


def jobs_advertised(request):
    """
    Context processor to add job adverts to the context.
    This allows job adverts to be accessed in templates without explicitly passing them in views.
    """
    job_adverts = JobAdvert.objects.all().order_by('-created_at') # Fetch latest 5 active job adverts
    return {
        'job_adverts': job_adverts
    }