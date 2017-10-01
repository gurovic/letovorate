import random
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Examiner, Subject, Round

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

def create(request):
    result = []
    subject = request.POST["subject"]
    grade = int(request.POST["grade"])
    round = request.POST["round"]    
    fios = request.POST.getlist("fio[]")
    emails = request.POST.getlist("email[]")
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
    return render(request, 'exam/check.html', {'examiner': examiner})

def rate(request):
    pass

def check_error(request):
    return render(request, 'exam/check_error.html')




