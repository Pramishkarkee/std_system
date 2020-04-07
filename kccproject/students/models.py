from djongo import models
# from students.functions import datadd

# Create your models here.
class Student(models.Model):
    S_name=models.CharField(max_length=30,default="")
    S_id=models.CharField(max_length=30,default="")
    S_faculty=models.CharField(max_length=100,default="")
    S_parents_name=models.CharField(max_length=100,default="")
    S_contact_no=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name
class Login(models.Model):
    username=models.CharField(max_length=30,default="")
    password=models.CharField(max_length=30,default="")
    def __str__(self):
        return self.username

class Faculty(models.Model):
    username=models.CharField(max_length=30,default="")
    password=models.CharField(max_length=30,default="")
    def __str__(self):
        return self.username
class Admin(models.Model):
    username=models.CharField(max_length=30,default="")
    password=models.CharField(max_length=30,default="")
    def __str__(self):
        return self.username
class adminMessage(models.Model):
    selReciver=models.CharField(max_length=30,default="")
    message=models.CharField(max_length=300,default="")
    def __str__(self):
        return self.selReciver
class Course(models.Model):
    courseCode=models.CharField(max_length=30,default="")
    courseName=models.CharField(max_length=30,default="")
    duration=models.CharField(max_length=30,default="")
    noSem=models.CharField(max_length=30,default="")
    def __str__(self):
        return self.courseName
class StudentDetail(models.Model):
    studentid=models.CharField(max_length=50,default="")
    cName=models.CharField(max_length=50,default="")
    courseId=models.CharField(max_length=50,default="")
    Semister=models.CharField(max_length=50,default="")
    firstName=models.CharField(max_length=50,default="")
    lastName=models.CharField(max_length=50,default="")
    emailAdd=models.CharField(max_length=50,default="")
    ContactNo=models.CharField(max_length=50,default="")    
    BirthDate=models.DateField()
    gender=models.CharField(max_length=50,default="")
    District=models.CharField(max_length=50,default="")
    village=models.CharField(max_length=50,default="")
    fatherName=models.CharField(max_length=50,default="")
    fatherOccupation=models.CharField(max_length=50,default="")
    motherName=models.CharField(max_length=50,default="")
    motherOccupation=models.CharField(max_length=50,default="")
    parentEmail=models.CharField(max_length=50,default="")
    parentContactNo=models.CharField(max_length=50,default="")
    studentPicture=models.FileField(upload_to="uploadfile/")
    def __str__(self):
        return self.firstName

class Subject(models.Model):
    faculty=models.CharField(max_length=50,default="")
    semister=models.CharField(max_length=50,default="")
    subjectcode1=models.CharField(max_length=50,default="")
    subject1=models.CharField(max_length=50,default="")
    subjectcode2=models.CharField(max_length=50,default="")
    subject2=models.CharField(max_length=50,default="")
    subjectcode3=models.CharField(max_length=50,default="")
    subject3=models.CharField(max_length=50,default="")
    subjectcode4=models.CharField(max_length=50,default="")
    subject4=models.CharField(max_length=50,default="")
    subjectcode5=models.CharField(max_length=50,default="")
    subject5=models.CharField(max_length=50,default="")
    subjectcode6=models.CharField(max_length=50,default="")
    subject6=models.CharField(max_length=50,default="")
    subjectcode7=models.CharField(max_length=50,default="")
    subject7=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.faculty
class Teachers(models.Model):
    coursename=models.CharField(max_length=50,default="")
    semNo=models.CharField(max_length=50,default="")
    firstname=models.CharField(max_length=50,default="")
    lname=models.CharField(max_length=50,default="")
    emailAdd=models.CharField(max_length=50,default="")
    contactNo=models.CharField(max_length=50,default="")
    age=models.CharField(max_length=50,default="")
    gender=models.CharField(max_length=50,default="")
    tmpAdd=models.CharField(max_length=50,default="")
    parAdd=models.CharField(max_length=50,default="")
    timeTeach=models.CharField(max_length=50,default="")
    subject=models.CharField(max_length=50,default="")
    teacherPic=models.FileField(upload_to="Teacher/")
    def __str__(self):
        return self.firstname

    

