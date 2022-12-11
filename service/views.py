from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'index.html')


def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/login')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = Profile.objects.filter(username=username, password=password).first()
        if user is not None:
            request.session['username'] = username
            request.session['firstName'] = user.first_name
            request.session['userId'] = user.pk
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect'})
    if request.method == "GET":
        return render(request, 'login.html', {'error': ''})


def signup(request):
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if Profile.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        user = Profile.objects.create(username=username, email=email, password=password, first_name=username)
        user.save()
        return HttpResponseRedirect('/login')

    if request.method == "GET":
        return render(request, 'signup.html', {'error': error})


def profile(request):
    if request.method == "POST":
        userId = request.session['userId']
        user = Profile.objects.get(pk=userId)
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        if firstName:
            user.first_name = firstName
        if lastName:
            user.last_name = lastName
        if email:
            user.email = email
        user.save()
        request.session['firstName'] = user.first_name
        return HttpResponseRedirect('/profile')

    if request.method == "GET":
        userId = request.session.get('userId', None)
        if not userId:
            return HttpResponseRedirect('/login')
        user = Profile.objects.get(pk=userId)
        return render(request, 'profile.html', {'user': user})


def leaflet_map(request):
    return render(request, 'map.html')


def change_password(request):
    if request.method == "POST":
        userId = request.session['userId']
        user = Profile.objects.get(pk=userId)
        oldPassword = request.POST['oldPassword']
        newPassword = request.POST['newPassword']
        if oldPassword == user.password:
            user.password = newPassword
            user.save()
            return HttpResponseRedirect('/profile')
        else:
            return render(request, 'password.html', {'error': 'Old password is incorrect'})

    if request.method == "GET":
        userId = request.session.get('userId', None)
        if not userId:
            return HttpResponseRedirect('/login')
        return render(request, 'password.html', {'error': ''})
