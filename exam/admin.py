from django.contrib import admin

from .models import Examiner, Subject, Round, Task, Mark

class MarkAdmin(admin.ModelAdmin):
    fields = ('value', 'task', 'student_id', 'examiner', 'time',) 
    readonly_fields = ('time',)

admin.site.register(Examiner)
admin.site.register(Subject)
admin.site.register(Round)
admin.site.register(Task)
admin.site.register(Mark, MarkAdmin)
