from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'complain_o_citizen_2000/index.html')

def type_complaint(request):
    return sender(request, 'complain_o_citizen_2000/type_complaint_hindex.html')
