from .models import JobAdvert

from django.core.paginator import Paginator



def jobs_advertised(request):
    """
    Context processor to add job adverts to the context.
    This allows job adverts to be accessed in templates without explicitly passing them in views.
    """
    job_adverts = JobAdvert.objects.all().order_by('-created_at') # Fetch latest 5 active job adverts
    paginator = Paginator(job_adverts, 6)  # Show 5 job adverts per page

    page_numer = request.GET.get('page')
    job_adverts = paginator.get_page(page_numer)

    return {
        'job_adverts': job_adverts
    }