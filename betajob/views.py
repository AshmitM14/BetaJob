from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User 
from betajob.models import Users, Jobs, Contact
from django.db.models import Q


def index(request):
    return render(request, 'betajob/index.html')

def about(request):
    return render(request, 'betajob/about.html')

def contact(request):
    return render(request, 'betajob/contact.html')

def handleSignUp(request):
    if request.method=="POST":
        semail=request.POST['semail']
        spass=request.POST['spass'] 
        myuser = User.objects.create_user(username=semail, password=spass)
        myuser.save()
        dbuser = Users(email=semail, password=spass)
        dbuser.save()
        user=authenticate(username= semail, password= spass)
        if user is not None:
            login(request, user)
            return redirect("/jobs")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def handleLogin(request):
    if request.method=="POST":
        lemail=request.POST['lemail']
        lpass=request.POST['lpass'] 
        user=authenticate(username= lemail, password= lpass)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

@login_required
def findjobs(request):
    jobz = Jobs.objects.all()
    params = {'jobs': jobz}
    return render(request, 'betajob/find-jobs.html', params)

def JobPostHandle(request):
    desig = request.POST.get('desig')
    email = request.POST.get('mail')
    comp = request.POST.get('comp')
    skills = request.POST.get('skill')
    summary = request.POST.get('sum')
    location = request.POST.get('loc')
    user = request.user
    myPost = Jobs(designation=desig, company=comp,skills=skills,summary=summary,user=user, location=location,email=email)
    myPost.save()
    messages.success(request, "Job Posted")
    return redirect('/')

def ContactHandle(request):
    if request.method == "POST":
        email = request.POST.get('mail')
        message = request.POST.get('mssg')
        myContact = Contact(email=email, message=message)
        myContact.save()
        messages.success(request, "Message Sent")
        return redirect('/')
    else:
        return HttpResponse("404- Not found")
    
def search(request):
    query = request.GET.get('query')
    if query:
        jobs = Jobs.objects.filter(
            Q(designation__icontains=query) | Q(company__icontains=query) | Q(skills__icontains=query)
        )
    else:
        jobs = []
    return render(request, 'betajob/search.html', {'jobs': jobs})

@login_required
def postJobs(request):
    return render(request, 'betajob/post-job.html')

@login_required
def dashboard(request):
    jobz = Jobs.objects.filter(user=request.user)
    params = {"jobs": jobz}
    return render(request, 'betajob/dashboard.html', params)