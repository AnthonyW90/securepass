from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from random import choice, shuffle
from string import ascii_lowercase, ascii_uppercase

# Create your views here.


def index(request):
    passwords = models.Password.objects.all()

    context = {
        'message': 'Hello Curt',
        'passwords': passwords
    }
    return render(request, 'pwapp/index.html', context)


def gen_password(request):

    name = request.POST['name']
    url = request.POST['url']
    username = request.POST['username']

    lowercase = int(request.POST['lowercase'])
    uppercase = int(request.POST['uppercase'])

    pw = ""

    for i in range(lowercase):
        pw += choice(ascii_lowercase)
    for i in range(uppercase):
        pw += choice(ascii_uppercase)

    pw = list(pw)
    shuffle(pw)
    pw = "".join(pw)

    password = models.Password(
        username=username,
        name=name,
        url=url,
        password=pw,
        lowercase=lowercase,
        uppercase=uppercase
    )
    password.save()

    return HttpResponseRedirect(reverse('pwapp:index'))


def delete(request, pass_id):
    password = models.Password.objects.get(id=pass_id)
    password.delete()

    return HttpResponseRedirect(reverse('pwapp:index'))


def edit(request, pass_id):
    pw = models.Password.objects.get(id=pass_id)

    context = {'pw': pw}
    return render(request, 'pwapp/edit.html', context)


def save(request, pass_id):
    PW = models.Password.objects.get(id=pass_id)
    print(request.POST)

    name = request.POST['pw_name']
    url = request.POST['url']
    username = request.POST['username']
    password = request.POST['password']

    PW.name = name
    PW.url = url
    PW.username = username

    if 'rando' in request.POST:
        lowercase = PW.lowercase
        uppercase = PW.uppercase

        pw = ""

        for i in range(lowercase):
            pw += choice(ascii_lowercase)
        for i in range(uppercase):
            pw += choice(ascii_uppercase)

        pw = list(pw)
        shuffle(pw)
        pw = "".join(pw)
        PW.password = pw
    else:
        PW.password = password

    PW.save()
    return HttpResponseRedirect(reverse('pwapp:index'))
