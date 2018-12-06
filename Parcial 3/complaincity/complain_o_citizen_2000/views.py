from django.shortcuts import render
from django.http import HttpResponse
from .models import User, BigComplaint, MiniComplaint

# Create your views here.
def index(request):
    return render(request, 'complain_o_citizen_2000/index.html')

def type_complaint(request,id):
    complaints = BigComplaint.objects.filter(type_complaint=id)
    context = {
        'complaints': complaints
    }
    return render(request, 'complain_o_citizen_2000/type_complaint_index.html', context)
