import random
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Examiner, Subject, Round, Task

def index(request):
    return render(request, 'exam/index.html')

def new_exam(request):
    return render(request, 'exam/new_exam.html', 
                       {'subjects': Subject.objects.all(),
                        'rounds': Round.objects.all(),
                        'range50': list(range(50)),
                       })

def generate_code():
    code = ""
    for i in range(6):
        code += chr(ord('A') + random.randint(0, 25))
    return code

def create_tasks(task_names, subject, grade, round):
    order = 0
    for title in task_names:
        if not title:
            break
            # Add until the first emprty title
        Task(title=title, 
             order=order, 
             subject=Subject.objects.get(pk=subject), 
             grade=grade, 
             round=Round.objects.get(pk=round)).save()
        order += 10

def create(request):
    result = []
    task_names = request.POST.getlist('taskname[]')
    subject = request.POST["subject"]
    grade = int(request.POST["grade"])
    round = request.POST["round"]    
    fios = request.POST.getlist("fio[]")
    emails = request.POST.getlist("email[]")

    create_tasks(task_names, subject, grade, round)

    for i in range(len(fios)):
        if fios[i]:
            examiner = Examiner(subject=Subject.objects.get(pk=subject), 
                            grade=grade,
                            round=Round.objects.get(pk=round),
                            fio=fios[i],
                            email=emails[i],
                            code=generate_code())
            examiner.save()
            send_email(examiner)
            result.append(examiner)
    return render(request, 'exam/added.html',
                       {'result': result})

def send_email(examiner):
    print(examiner)
    # TODO

def login(request):
    code = request.POST["code"]
    try:
        examiner = Examiner.objects.get(code=code)
    except:
        return render(request, 'exam/check_error.html')
    request.session['subject'] = examiner.subject.pk
    request.session['round'] = examiner.round.pk
    request.session['grade'] = examiner.grade
    return render(request, 'exam/check.html', {'examiner': examiner})

def rate(request):
    round = Round.objects.get(pk=request.session.get('round'))
    grade = int(request.session.get('grade'))
    subject = Subject.objects.get(pk=request.session.get('subject'))

    try:
        code = request.POST['code']
    except:

        tasks = Task.objects.filter(grade=grade, 
                        subject=subject, round=round).order_by('order')
        return render(request, 'exam/rate.html', {'tasks':tasks})

    marks = request.POST.getlist('marks[]')   
    round = request.session.get('round')
    grade = int(request.session.get('grade'))
    subject = request.session.get('subject')
    
       
def check_error(request):
    return render(request, 'exam/check_error.html')




