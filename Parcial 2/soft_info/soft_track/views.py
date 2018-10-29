from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import SwPackage, Dept
from .forms import RawSwForm, RawDeptForm

# Create your views here.
def index(request):

    all_pkgs = SwPackage.objects.all()

    context = {
        'title': 'All Software',
        'swpkgs': all_pkgs
    }

    return render(request, 'soft_track/index.html', context)

def index_filter(request, name):
    spec_pkgs = SwPackage.objects.filter(dept=name)

    context = {
        'title': name+" Software",
        'swpkgs': spec_pkgs
    }

    return render(request, 'soft_track/index.html', context)





def details(request, id):
    swpkg = SwPackage.objects.get(id=id)

    context = {
        'swpkg': swpkg
    }

    return render(request, 'soft_track/details.html', context)


def newsw(request):
    form = RawSwForm()
    if request.method == "POST":
        form = RawSwForm(request.POST)
        if form.is_valid():
            SwPackage.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/soft_track/')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "soft_track/new_sw.html", context)

def newdept(request):
    form = RawDeptForm()
    if request.method == "POST":
        form = RawDeptForm(request.POST)
        if form.is_valid():
            Dept.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/soft_track/')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "soft_track/new_dept.html", context)
