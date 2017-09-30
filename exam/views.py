from django.shortcuts import render

from .models import Examiner, Subject, Round

def new_exam(request):
    return render(request, 'exam/new_exam.html', 
                       {'subjects': Subject.objects.all(),
                        'rounds': Round.objects.all(),
                        'range50': list(range(50)),
                       })

def create(request):
    pass
