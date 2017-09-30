from django.contrib import admin

from .models import Examiner, Subject, Round

admin.site.register(Examiner)
admin.site.register(Subject)
admin.site.register(Round)
