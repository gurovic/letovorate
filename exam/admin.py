from django.contrib import admin

from .models import Examiner, Subject, Round, Task

admin.site.register(Examiner)
admin.site.register(Subject)
admin.site.register(Round)
admin.site.register(Task)
