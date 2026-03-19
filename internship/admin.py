from django.contrib import admin
from .models import Student, Supervisor, Report, Feedback

admin.site.register(Student)
admin.site.register(Supervisor)
admin.site.register(Report)
admin.site.register(Feedback)