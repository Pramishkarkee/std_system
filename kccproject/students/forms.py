# from django import forms
from students.models import Student,Login,Admin,Faculty,adminMessage,Course,StudentDetail,Teachers
# class admin(forms.ModelForm):
#     username=forms.CharField(max_length=30)
#     password=forms.CharField(max_length=30)
# class Student(forms.ModelForm):
#     class Meta:
#         model=Student
#         fields=('S_name','S_id','S_faculty','S_parents_name','S_contact_no')

    
# class Login(forms.ModelForm):
#     username=forms.CharField(max_length=30)
#     password=forms.CharField(max_length=30)
    

# class Faculty(forms.ModelForm):
#     username=forms.CharField(max_length=30)
#     password=forms.CharField(max_length=30)
   
# class Admin(forms.ModelForm):
#     username=forms.CharField(max_length=30)
#     password=forms.CharField(max_length=30)
  
# class adminMessage(forms.ModelForm):
#     selReciver=forms.CharField(max_length=30)
#     message=forms.CharField(max_length=300)
    
    
# class Course(forms.ModelForm):
#     courseCode=forms.CharField(max_length=30)
#     courseName=forms.CharField(max_length=30)
#     duration=forms.CharField(max_length=30)
#     noSem=forms.CharField(max_length=30)
from django import forms

class UploadFileForms(forms.Form):
    class Meta:
        model=StudentDetail
        fields=('studentid','cName','Semister','firstName','lastName','emailAdd','ContactNo','gender','BirthDate','District','village','fatherName',
        'fatherOccupation','motherName','motherOccupation','parentEmail','parentContactNo','studentPicture','courseId')
class Teacher(forms.Form):
    class Meta:
        model=Teachers
        fields=('coursename','semNo','firstname','lname','emailAdd','contactNo','age','gender','tmpAdd','parAdd','timeTeach','subject','teacherPic')
