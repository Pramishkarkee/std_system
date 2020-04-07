# from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .import views
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static



urlpatterns = [
    path('',views.index,name='index'),
    url(r'adminLogin',views.adminLogin,name="adminLogin"),
    url(r'adminpannel',views.adminpannel,name="adminpannel"),
    url(r'^studentDetails/(?P<pk>\d+)/$',views.studentDetails,name="student_details"),
    url(r'register',views.register,name="register"),
    url(r'marksheet',views.marksheet,name="marksheet"),   
   
    url(r'home',views.home,name="home"),
    url(r'course',views.course,name="course"),
    url(r'student',views.student,name="student"),
    url(r'subjects',views.subjects,name="subjects"),
    url(r'addSubject',views.addSubjects,name="addSubjects"),
    url(r'subData',views.subData,name="subData"),
    url(r'faculties',views.faculties,name="faculties"), 
    url(r'^TeacherDetail/(?P<pk>\d+)/$',views.TeacherDetail,name="TeacherDetail"), 
    url(r'timeTable',views.timeTable,name='timeTable'),
    url(r'^users',views.users,name="users"),
    url(r'studentFine',views.studentFine,name="studentFine"),
    url(r'projectReport',views.projectReport,name="projectReport"),
    url(r'syllabus',views.syllabus,name="syllabus"),
    url(r'assignments',views.assignments,name="assignments"),  

    url(r'assignSubject',views.assignSubject,name="assignSubject"),
    url(r'enterMarks',views.enterMarks,name="enterMarks"),  
    url(r'markAttendance',views.markAttendance,name='markAttendance'),
    url(r'attendanceReport',views.attendanceReport,name="attendanceReport"),
    url(r'searchStudent',views.searchStudent,name="searchStudent"),
  
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
