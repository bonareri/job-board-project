from django.shortcuts import render, redirect
from .models import JobListing
from .forms import JobListingForm

# View to display all job listings
def job_list(request):
    jobs = JobListing.objects.all()
    return render(request, 'joblistings/job_list.html', {'jobs': jobs})

# View to create a new job listing
def job_create(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Redirect to the job listing page after saving
    else:
        form = JobListingForm()
    return render(request, 'joblistings/job_form.html', {'form': form})
