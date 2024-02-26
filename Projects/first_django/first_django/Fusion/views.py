from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime
from django import forms
from django.urls import reverse

tasks = ["foo", "bar", "baz"]


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.
def index(request):
    return render(request, 'welcome/index.html')


def login(request):
    now = datetime.datetime.now()
    return render(request, 'welcome/login.html', {
        "newyear": now.month == 1 and now.day == 1
    })


def greet(request, name):
    return render(request, 'welcome/greet.html', {
        'name': name.capitalize()
    })


def todotask(request):
    return render(request, 'welcome/tasks.html', {
        "todotasks": tasks
    })


def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("todotask:fusion"))
        else:
            return render(request, "welcome/add.html", {
                "form": form

    return render(request, 'welcome/add.html', {
        "form": NewTaskForm()
    })
