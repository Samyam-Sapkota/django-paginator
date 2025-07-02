from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.http import HttpResponseForbidden
from jobs.models import JobAdvert
# from jobs.models import JobAdvert,Application,thirtY_days_from_now
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
# from users.models import ApplicantProfile
import json

# Create your views here.
def job_details(request, job_tracking_id=None):
    if job_tracking_id:
        try:
            job_advert_details = JobAdvert.objects.get(job_tracking_id=job_tracking_id)

            if job_advert_details.deadline < date.today() and job_advert_details.is_active:
                job_advert_details.is_active = False
                job_advert_details.save()
            elif job_advert_details.deadline > date.today() and not job_advert_details.is_active:
                job_advert_details.is_active = True
                job_advert_details.save()


           
            
            
            context = {'job_advert_details': job_advert_details,}
            return render(request, 'jobs/job_details.html', context)
        except JobAdvert.DoesNotExist:
            messages.error(request, "Job advert not found.")
            return redirect('home')  # Replace 'home' with your actual home URL name
    else:
        messages.error(request, "No job ID provided.")
        return redirect('home')  # Replace 'home' with your actual home URL name










def home(request):
    # Fetch all job adverts from the database
    jobs = JobAdvert.objects.filter(is_active=True).order_by('-deadline')
    job_data = []

    for job in jobs:
        days_diff = (date.today() - job.deadline).days
        if days_diff == 0:
            posted_ago = "Today"
        elif days_diff == 1:
            posted_ago = "1 day ago"
        else:
            posted_ago = f"{days_diff} days ago"

        # Append job and its extra info into a dictionary
        job_data.append({
            'job': job,
            'posted_ago': posted_ago
        })
    
    
    return render(request, 'home.html',{'posted_ago': job_data})   























import random
from datetime import datetime, timedelta



















def create_sample_jobs(request):
    # Ensure only superuser or dev can run this
    print("=== create_sample_jobs function called ===")
    print(f"Request method: {request.method}")
    print(f"Request path: {request.path}")

    job_titles = [
        "Software Engineer", "Data Scientist", "Frontend Developer", "Backend Developer", "UI/UX Designer",
        "Product Manager", "System Administrator", "DevOps Engineer", "QA Tester", "Technical Writer",
        "Cloud Engineer", "Machine Learning Engineer", "AI Researcher", "Database Administrator", "Cybersecurity Analyst",
        "Mobile App Developer", "Game Developer", "IT Support Specialist", "Network Engineer", "Site Reliability Engineer",
        "Business Analyst", "Scrum Master", "Project Coordinator", "Full Stack Developer", "BI Developer",
        "Research Engineer", "Embedded Systems Developer", "Data Engineer", "IT Manager", "Blockchain Developer"
    ]

    job_types = [choice[0] for choice in JobAdvert.EmploymentType]
    location_types = [choice[0] for choice in JobAdvert.LocationTypeChoice]
    experience_levels = [choice[0] for choice in JobAdvert.ExperienceLevel]
    
    print(f"Available job types: {job_types}")
    print(f"Available location types: {location_types}")
    print(f"Available experience levels: {experience_levels}")
    
    core_skills_pool = [
        "Python", "Django", "JavaScript", "React", "SQL", "Git", "Linux", "Docker", "Kubernetes", "AWS",
        "TensorFlow", "C++", "Java", "Agile", "REST APIs", "HTML", "CSS", "MongoDB", "Azure", "GCP"
    ]
    nice_skills_pool = [
        "CI/CD", "GraphQL", "Node.js", "SASS", "TypeScript", "PostgreSQL", "Flutter", "Rust", "Scala", "Elasticsearch"
    ]

    print("Starting job creation loop...")

    try:
        jobs_created = 0
        for i in range(29):
            title = job_titles.pop(0)
            print(f"Creating job {i+1}: {title}")
            
            job = JobAdvert(
                title=title,
                job_type=random.choice(job_types),
                location_type=random.choice(location_types),
                experience_level=random.choice(experience_levels),
                no_of_vacancies=random.randint(1, 5),
                deadline=(datetime.now() + timedelta(days=random.randint(15, 45))).date(),
                salary=random.randint(30000, 150000),
                description=f"We are looking for a {title} to join our team. You will work on exciting projects and help scale our platform.",
                key_responsibilities=f"As a {title}, you will be responsible for system design, development, and collaboration with cross-functional teams.",
                core_skills=random.sample(core_skills_pool, k=4),
                nice_to_have_skills=random.sample(nice_skills_pool, k=2),
            )
            job.save()
            jobs_created += 1
            print(f"Successfully created job: {job.title} with ID: {job.job_tracking_id}")

        print(f"=== Successfully created {jobs_created} job adverts ===")
        return HttpResponse(f"✅ Successfully created {jobs_created} job adverts.")
        
    except Exception as e:
        print(f"Error creating jobs: {str(e)}")
        return HttpResponse(f"❌ Error creating jobs: {str(e)}")