from django.contrib import admin
from .models import Student,Login,Faculty,Admin,adminMessage,Course,StudentDetail,Subject,Teachers
# # Register your models here.
admin.site.register(Student)
admin.site.register(Login)
admin.site.register(Faculty)
admin.site.register(Admin)
admin.site.register(adminMessage)
admin.site.register(Course)
admin.site.register(StudentDetail)
admin.site.register(Subject)
admin.site.register(Teachers)