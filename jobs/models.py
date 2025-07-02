from django.db import models
from datetime import date,timedelta
from datetime import datetime
import random



def thirtY_days_from_now():
    return date.today() + timedelta(days=30)

def generate_unique_job_id():
    while True:
        job_id = str(random.randint(1000, 9999))
        if not JobAdvert.objects.filter(job_tracking_id=job_id).exists():
            return job_id



class JobAdvert(models.Model):
    # advertisor_company = models.ForeignKey(EmployerProfile,on_delete=models.CASCADE, related_name='job_adverts', help_text="Employer who created the job advert")
    job_tracking_id = models.CharField(max_length=4, unique=True, editable=False ,default='')

    def save(self, *args, **kwargs):
        if not self.job_tracking_id:
            self.job_tracking_id = generate_unique_job_id()

        # Convert string to date if necessary
        if isinstance(self.deadline, str):
            self.deadline = datetime.strptime(self.deadline, "%Y-%m-%d").date()

        # Automatically deactivate job if deadline has passed
        if self.deadline and self.deadline < date.today():
            self.is_active = False

        super().save(*args, **kwargs)



    EmploymentType=[
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
    ]

    LocationTypeChoice = [
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
        ('on_site', 'On-site'),
    ]

    ExperienceLevel = [
        ('intern', 'Intern'),
        ('traineeship', 'Traineeship'),
        ('entry_level', 'Entry Level'),
        ('mid_level', 'Mid Level'),
        ('senior', 'Senior'),
        ('director', 'Director'),
        ('executive', 'Executive'),
    ]

    # Models field will be here :     

    title = models.CharField(max_length=150)

    job_type = models.CharField(max_length=50, choices=EmploymentType)
    location_type = models.CharField(max_length=50, choices=LocationTypeChoice)
    experience_level = models.CharField(max_length=50, choices=ExperienceLevel,null=True,blank=True, help_text="Experience level required for the job")

    no_of_vacancies = models.PositiveIntegerField(default=1)

    deadline = models.DateField(default=thirtY_days_from_now, help_text="Deadline for job application")

    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    description = models.TextField()

    key_responsibilities = models.TextField()

    core_skills = models.JSONField(default=list, help_text="List of skills")

    nice_to_have_skills = models.JSONField(default=list, help_text="List of skills", blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, help_text="Date when the job was created")    
    # applicants_count = models.PositiveIntegerField(default=0, help_text="Number of applicants for the job advert")

    def __str__(self):
        return f"{self.job_tracking_id}-{self.title}"
    
    class Meta:
        ordering = ['-created_at']

    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('job_details', args=[self.job_tracking_id])




# class Application(models.Model):
#     job = models.ForeignKey(JobAdvert, on_delete=models.CASCADE, related_name='applications')
#     # applicant = models.ForeignKey(ApplicantProfile,on_delete=models.CASCADE, related_name='job_applicant', help_text="Applicant who applied the job advert")
#     applicant = models.ForeignKey(ApplicantProfile,on_delete=models.CASCADE, related_name='job_applicant', help_text="Applicant who applied the job advert")
  
#     applied_at = models.DateTimeField(auto_now_add=True)
#     applicants_cv = models.FileField(upload_to='applicant_cvs/', help_text="CV of the applicant",null=False)

    
#     class Meta:
#         unique_together = ('job', 'applicant')  # Prevent duplicate applications

#     def __str__(self):
#         return f"{self.applicant} applied to {self.job.title}"