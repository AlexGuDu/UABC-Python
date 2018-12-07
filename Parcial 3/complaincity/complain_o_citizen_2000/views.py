from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import User, BigComplaint, MiniComplaint

# Create your views here.
def sign_in_valid(request):
    if 'username' in request.session:
        return True
    else:
        return False


def register_f(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create(
            username = username,
            password = password
        )
        return HttpResponse('')

def login_f(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        users = User.objects.all()
        for user in users:
            if (username == user.username) and (password == user.password):
                request.session['username'] = user.username
                return JsonResponse({
                    'username': request.session['username']
                })

    return JsonResponse({
        'username': "no_match"
    })

def login(request):
    if sign_in_valid(request):
        return redirect('index')
    else:
        return render(request, 'complain_o_citizen_2000/login.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def index(request):
    if sign_in_valid(request):
        all_counts = []
        for i in range(6):
            all_counts.append(BigComplaint.objects.filter(type_complaint=i+1).count())
        context = {
            'user': request.session['username'],
            'all_counts': all_counts,
        }
        return render(request, 'complain_o_citizen_2000/index.html', context)
    else:
        return redirect('login')

def type_complaint(request,id):
    if sign_in_valid(request):
        did_they_complain = True
        if id == 1:
            title = "Good Examples"
        if id == 2:
            title = "Urbanism & Transport"
        if id == 3:
            title = "Business"
        if id == 4:
            title = "Social Matters"
        if id == 5:
            title = "Government"
        if id == 6:
            title = "Social Communities and Lost Items"

        complaints = BigComplaint.objects.filter(type_complaint=id)
        for complaint in complaints:
            reply_count = MiniComplaint.objects.filter(bigcomplaint_id=complaint.id).count()
            complaint.reply_count = reply_count
        if not complaints.last():
            did_they_complain = False
        users = User.objects.all()
        for user in users:
            for complaint in complaints:
                if len(complaint.body) > 60:
                    complaint.body = complaint.body[:50] + "..."
                if user.id == complaint.user_id:
                    complaint.by_username = user.username

        context = {
            'user': request.session['username'],
            'title': title,
            'type_id': id,
            'complaints': complaints,
            'did_they_complain': did_they_complain
        }
        return render(request, 'complain_o_citizen_2000/type_complaint_index.html', context)
    else:
        return redirect('login')

def bigcomplaint(request, id):
    if sign_in_valid(request):
        complaint = BigComplaint.objects.get(id=id)
        user = User.objects.get(id=complaint.user_id)
        complaint.by_username = user.username
        minicomplaints = MiniComplaint.objects.filter(bigcomplaint_id=complaint.id)
        users = User.objects.all()
        for user in users:
            for minicomplaint in minicomplaints:
                if user.id == minicomplaint.user_id:
                    minicomplaint.by_username = user.username

        context = {
            'user': request.session['username'],
            'complaint': complaint,
            'minicomplaints': minicomplaints,
        }
        return render(request, 'complain_o_citizen_2000/bigcomplaint.html', context)
    else:
        return redirect('login')

def submit_complaint(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        type_id = request.POST['type_id']
        by_user = User.objects.get(username=request.session['username'])


        BigComplaint.objects.create(
            title = title,
            body = body,
            type_complaint = type_id,
            user_id = by_user.id,
        )
        return HttpResponse('')

def submit_minicomplaint(request):
    if request.method == 'POST':
        body = request.POST['body']
        bigcomplaint_id = request.POST['bigcomplaint_id']
        by_user = User.objects.get(username=request.session['username'])


        MiniComplaint.objects.create(
            body = body,
            bigcomplaint_id = bigcomplaint_id,
            user_id = by_user.id,
        )
        return HttpResponse('')

def thumbup(request):
    if request.method == 'POST':
        bigcomplaint_id = request.POST['bigcomplaint_id']

        votes = BigComplaint.objects.get(id=bigcomplaint_id).upvotes
        BigComplaint.objects.filter(id=bigcomplaint_id).update(upvotes = (votes + 1))

        return HttpResponse('')

def thumbdown(request):
    if request.method == 'POST':
        bigcomplaint_id = request.POST['bigcomplaint_id']

        votes = BigComplaint.objects.get(id=bigcomplaint_id).downvotes
        BigComplaint.objects.filter(id=bigcomplaint_id).update(downvotes = (votes + 1))

        return HttpResponse('')
