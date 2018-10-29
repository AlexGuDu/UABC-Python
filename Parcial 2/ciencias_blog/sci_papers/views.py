from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Paper
from .forms import PaperForm, RawPaperForm

# Create your views here.
def index(request):

    all_papers = Paper.objects.all()

    context = {
        'title': 'All Papers',
        'papers': all_papers
    }

    return render(request, 'sci_papers/index.html', context)

def cat01(request):

    spec_papers = Paper.objects.filter(category='Ciencias Computacionales')

    context = {
        'title': 'Ciencias Computacionales',
        'papers': spec_papers
    }

    return render(request, 'sci_papers/index_filter.html', context)

def cat02(request):

    spec_papers = Paper.objects.filter(category='Ciencias de la Tierra')

    context = {
        'title': 'Ciencias de la Tierra',
        'papers': spec_papers
    }

    return render(request, 'sci_papers/index_filter.html', context)

def cat03(request):

    spec_papers = Paper.objects.filter(category='Ciencias Naturales')

    context = {
        'title': 'Ciencias Naturales',
        'papers': spec_papers
    }

    return render(request, 'sci_papers/index_filter.html', context)

def cat04(request):

    spec_papers = Paper.objects.filter(category='Ciencias Sociales')

    context = {
        'title': 'Ciencias de Sociales',
        'papers': spec_papers
    }

    return render(request, 'sci_papers/index_filter.html', context)

def cat05(request):

    spec_papers = Paper.objects.filter(category='Ciencias Medicas')

    context = {
        'title': 'Ciencias Medicas',
        'papers': spec_papers
    }

    return render(request, 'sci_papers/index_filter.html', context)


def details(request, id):
    paper = Paper.objects.get(id=id)
    if paper.category == 'Ciencias Computacionales':
        cat = 'cat01'
    elif paper.category == 'Ciencias de la Tierra':
        cat = 'cat02'
    elif paper.category == 'Ciencias Naturales':
        cat = 'cat03'
    elif paper.category == 'Ciencias Sociales':
        cat = 'cat04'
    elif paper.category == 'Ciencias Medicas':
        cat = 'cat05'
    context = {
        'paper': paper,
        'cat': cat
    }

    return render(request, 'sci_papers/details.html', context)


def create(request):
    form = RawPaperForm()
    if request.method == "POST":
        form = RawPaperForm(request.POST)
        if form.is_valid():
            Paper.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/papers/')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "sci_papers/create.html", context)
