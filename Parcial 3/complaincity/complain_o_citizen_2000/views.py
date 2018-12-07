from django.shortcuts import render
from django.http import HttpResponse
from .models import User, BigComplaint, MiniComplaint

# Create your views here.
def index(request):
    all_counts = []
    for i in range(6):
        all_counts.append(BigComplaint.objects.filter(type_complaint=i+1).count())
    context = {
        'all_counts': all_counts,
    }

    return render(request, 'complain_o_citizen_2000/index.html', context)

def type_complaint(request,id):
    complaints = BigComplaint.objects.filter(type_complaint=id)
    users = User.objects.all()
    for user in users:
        for complaint in complaints:
            if len(complaint.body) > 60:
                complaint.body = complaint.body[:50] + "..."
            if user.id == complaint.user_id:
                complaint.by_username = user.username

    context = {
        'complaints': complaints
    }
    return render(request, 'complain_o_citizen_2000/type_complaint_index.html', context)
