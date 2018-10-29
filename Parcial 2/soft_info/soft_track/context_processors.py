from .models import Dept

def get_depts(request):
    all_depts = Dept.objects.all()
    return {
        'depts': all_depts
    }
