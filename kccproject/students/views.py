from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .forms import UploadFileForms,Teacher
# from functions 
from students.models import Student,Login,Admin,Faculty,adminMessage,Course,StudentDetail,Subject,Teachers
import datetime
def index(request):
    system_user=Login.objects.all()
    # return JsonResponse({'name':'pramish'})
    return render(request,'index.html')

def adminpannel(request):
    username=request.POST.get('uname')
    password=request.POST.get('password')

    choice=request.POST.get('choose')
    print(choice)
    if choice=="Administrator":
        # admin=Admin(username=username,password="password")
        # admin.save()
        # return render(request,"AdminDetail.html")
        admin=Admin.objects.all()
        userval=Admin.objects.get(username=username)
        passval=Admin.objects.get(password=password)
        userval=str(userval)
        passval=str(passval)
        print("\n\n\n**********",type(userval),type(passval),"************\n\n\n")
        print("\n\n\n**********",type(username),type(password),"************\n\n\n")
        if userval==username and passval==password:
            return render(request,"AdminDetail.html")
        else:
            return HttpResponse("not match")
    else:
        faculty=Faculty(username=username,password=password)
        faculty.save()
        return render(request,"student_details.html")
    system_user=Login.objects.all()
    # if system_user.username==username:
    #     return render(request,'admin.html')
    # else:
    #     return render(request,'index.html',{'wrong_ip':"sorry the input is wrong"})
def studentDetails(request,pk=None):
    if pk:
        print(type(pk))
        std=StudentDetail.objects.all() 
        for dtlStd in std:
            x=int(dtlStd.id)
            print("*******\n\n",x,pk,"*****\n\n")
            print("*******\n\n",type(x),type(int(pk)),"*****\n\n")
            if x==int(pk):
                studentdata={'stddata':dtlStd}
                break
        return render(request,"student_details.html",studentdata)
       
def register(request):
    return render(request,"register.html")
def marksheet(request):
    return render(request,"marksheet.html")
def adminLogin(request):
    return render(request,"adminLogin.html")
def home(request):
    print("*******\n\n",request.method,"*******\n\n")
    if request.method=='POST':
        selectReciver=request.POST.get('selReciver','')
        aMessage=request.POST.get('message','')
        print("*******\n\n",selectReciver,aMessage,"*******\n\n")
        admindata=adminMessage(selReciver=selectReciver,message=aMessage)
        admindata.save()
    notification=adminMessage.objects.all()
    print("*********************************************************************")
    # dat={message:notification.message,selector:notification.selReciver}
    param={'adminDa':notification}
    print("*******\n\n*******\n\n")
    return render(request,"home.html",param)
def course(request):
    print("*******\n\n",request.method,"*******\n\n")
    emtDic={}
    if request.method=='POST':
        
        ccode=request.POST.get('code','')
        cname=request.POST.get('cname','')
        duration=request.POST.get('duration','')
        semister=request.POST.get('noSemYer','')
        y=0
        x=Course.objects.all()
        length=len(x)
        print("****length***\n\n",length,"*******\n\n")
        if length>1:
            rep=0
            chec=Course.objects.all()
            for i in range(length):
                print(type(chec[i].courseCode),ccode)
                if str(chec[i].courseCode)==ccode:
                    rep=rep+1
                
            print("*******\n\n",rep,"*******\n\n")
            if rep>0:
                dataexist={"alertpopup":"This "+ cname +" is already exist"}
                emtDic.update(dataexist)
            else:
                print("*******\n\n",ccode,cname,"*******\n\n")
                cdata=Course(courseCode=ccode,courseName=cname,duration=duration,noSem=semister)
                cdata.save()
    #   else
        else:
            print("*******\n\n",ccode,cname,"*******\n\n")
            cdata=Course(courseCode=ccode,courseName=cname,duration=duration,noSem=semister)
            cdata.save()
    
    coursedata=Course.objects.all()
    # dat={message:notification.message,selector:notification.selReciver}
    coursParam={'cdata':coursedata}
    coursParam.update(emtDic)
    print("*******\n\n*******\n\n")
    return render(request,"course.html",coursParam)
def student(request):
    if request.method=='POST':
        ModelForm=UploadFileForms(request.POST,request.FILES)
        print("****hdhdhhdh***\n\n\n",ModelForm.is_valid(),"\n\n\n******")
        if ModelForm.is_valid():
            print("****hdhdhhdh***\n\n\n",ModelForm.is_valid(),"\n\n\n******")
            cName=request.POST.get('coursename','')
            Semister=request.POST.get('semNo','')
            firstName=request.POST.get('firstname','')
            lastName=request.POST.get('lname','')
            emailAdd=request.POST.get('emailAdd','')
            ContactNo=request.POST.get('contactNo','')
            BirthDate=request.POST.get('birthDate','')
            Gender=request.POST.get('gender','')
            District=request.POST.get('district','')
            village=request.POST.get('village','')
            fatherName=request.POST.get('fname','')
            fatherOccupation=request.POST.get('foccupation','')
            motherName=request.POST.get('mname','')
            motherOccupation=request.POST.get('moccupation','')
            parentEmail=request.POST.get('pemail','')
            parentContactNo=request.POST.get('pcno','')
            studentPicture = request.FILES.get('studentPic','')

            courseIdSearch=Course.objects.all()
            # courseId=0
            year = datetime.datetime.today().year
            year=str(year)
            
            for i in range(len(courseIdSearch)):
               
                if courseIdSearch[i].courseCode==cName:
                    courseId=cName
                    
                    break
            # print("*************\n\n",courseId,"\n\n\n***********************************")
           
            studentsId=StudentDetail.objects.all()     
            l=len(studentsId)    
            l=l+1
            l=str(l)
            studentid=courseId+year+l

            print("*****student id g********8\n\n",studentid,"\n\n\n***********************************")

            stddtl=StudentDetail(studentid=studentid,cName=cName,Semister=Semister,firstName=firstName,
            lastName=lastName,emailAdd=emailAdd,ContactNo=ContactNo,BirthDate=BirthDate,
            District=District,gender=Gender,village=village,fatherName=fatherName,
            fatherOccupation=fatherOccupation,motherName=motherName,motherOccupation=motherOccupation,
            parentEmail=parentEmail,parentContactNo=parentContactNo,studentPicture=studentPicture,courseId=courseId)
            stddtl.save()
    
    coursedata=Course.objects.all()
    params=StudentDetail.objects.all()
   
    # print(params)
    senddata={'courseall':coursedata,'fetchstd':params}
    return render(request,"student.html",senddata)
def subjects(request):
    sub=0
    sub=False

    if request.method=='POST':
        faculty=request.POST.get('faculty','')
        semister=request.POST.get('semister','')
        
        sub=True
        print("\n\n*********************",faculty,type(sub),sub,"\n\n******************************")
        # fac=faculty
        # sem=semister
        coursedata=Course.objects.all()
        print("\n\n***********",coursedata[0].courseCode,"\n\n***********************")
        courseSub={"faculty":coursedata,"subj":sub,"fac":faculty,"sem":semister}
        return render(request,"subject.html",courseSub)
    else:
        coursedata=Course.objects.all()
        print("\n\n***********",coursedata[0].courseCode,"\n\n***********************")
        courseSub={"faculty":coursedata,"subj":sub}
        return render(request,"subject.html",courseSub)
def addSubjects(request):
    if request.method=='POST':
        faculty=request.POST.get('faculty','')
        semister=request.POST.get('semister','')
        subjectcode1=request.POST.get('subjectcode1','')
        subject1=request.POST.get('subject1','')
        subjectcode2=request.POST.get('subjectcode2','')
        subject2=request.POST.get('subject2','')
        subjectcode3=request.POST.get('subjectcode3','')
        subject3=request.POST.get('subject3','')
        subjectcode4=request.POST.get('subjectcode4','')
        subject4=request.POST.get('subject14','')
        subjectcode5=request.POST.get('subjectcode5','')
        subject5=request.POST.get('subject5','')
        subjectcode6=request.POST.get('subjectcode6','')
        subject6=request.POST.get('subject6','')
        subjectcode7=request.POST.get('subjectcode7','')
        subject7=request.POST.get('subject7','')
        sub=Subject(faculty=faculty,semister=semister,subjectcode1=subjectcode1,subject1=subject1,subjectcode2=subjectcode2,subject2=subject2,
        subjectcode3=subjectcode3,subject3=subject3,subjectcode4=subjectcode4,subject4=subject4,subjectcode5=subjectcode5,
        subject5=subject5,subjectcode6=subjectcode6,subject6=subject6,subjectcode7=subjectcode7,subject7=subject7)
        sub.save()
        subAll=Subject.objects.all()
        coursedata=Course.objects.all()
        courseSub={"faculty":coursedata,"subj":sub,'subData':subAll}
        # showData={'subData':subAll}
        print("***this is data******\n\n",faculty,semister,"\n\n*****")
        
        return render(request,"subject.html",courseSub)
    else:
        subAll=Subject.objects.all()
        showData={'subData':subAll}
        return render(request,"subject.html",showData)
def subData(request):
    if request.method=='POST':
        
        codeCourse=request.POST.get('codeCourse','')
        semister=request.POST.get('semister','')
        subAll=Subject.objects.all()
        subd={}
        data=False
        for sub in subAll:
            if sub.faculty==codeCourse and sub.semister==semister:
                data=True
                subd={'semSub':sub,'data':data}
                break
        return render(request,"subData.html",subd)
    else:
        # data=False
        return render(request,"subData.html",{'data':False})
def faculties(request):
    if request.method=='POST':
        formValid=Teacher(request.POST,request.FILES)
        # print("****hdhdhhdh***\n\n\n",formValid.is_valid(),"\n\n\n******")
        if formValid.is_valid():
            coursename=request.POST.get('coursename','')
            semNo=request.POST.get('semNo','')
            firstname=request.POST.get('firstname','')
            lname=request.POST.get('lname','')
            emailAdd=request.POST.get('emailAdd','')
            contactNo=request.POST.get('contactNo','')
            age=request.POST.get('age','')
            gender=request.POST.get('gender','')
            tmpAdd=request.POST.get('tmpAdd','')
            parAdd=request.POST.get('parAdd','')
            timeTeach=request.POST.get('timeTeach','')
            subject=request.POST.get('subject','')
            teacherPic=request.FILES.get('teacherPic','')
            
            pushdb=Teachers(coursename=coursename,semNo=semNo,firstname=firstname,lname=lname,emailAdd=emailAdd,contactNo=contactNo,age=age,gender=gender,tmpAdd=tmpAdd,parAdd=parAdd,
            timeTeach=timeTeach,subject=subject,teacherPic=teacherPic)
            pushdb.save()
            department=Course.objects.all()
            teacher=Teachers.objects.all()
            sendData={'department':department,'teacher':teacher}
            return render(request,"faculties.html",sendData)

    else:
        department=Course.objects.all()
        teacher=Teachers.objects.all()
        sendData={'department':department,'teacher':teacher}
        return render(request,"faculties.html",sendData)
def TeacherDetail(request,pk=None):
    if pk:
        pk=int(pk)
        teacherData=Teachers.objects.all()
        for tid in teacherData:
            if tid.id==pk:
                tdata={'selectData':tid}
                break
        return render(request,'teacherDetail.html',tdata)

def timeTable(request):
    
    return render(request,'timeTabe.html')
def users(request):
    if request.method=='POST':
        admin=request.POST.get('admin','')
        aid=request.POST.get('aid','')
        
        teacher=request.POST.get('teacher','')
        tid=request.POST.get('tid','')
        
        student=request.POST.get('student','')
        sid=request.POST.get('sid','')
        uA=Admin.objects.all()
        uS=StudentDetail.objects.all()
        uT=Teachers.objects.all()
        
        print("*******************\n\n",admin,aid,type(aid),"\n\n**************")
        print("*******************\n\n",teacher,tid,type(tid),"\n\n**************")
        if admin=='Admin':
            aid=int(aid)
            getData=Admin.objects.get(id=aid)  
            getData.delete()
        if teacher=='Teachers':
            teid=int(tid)
            print("*******inside if************\n\n",teacher,teid,type(teid),"\n\n**************")
            print("*******inside if db type************\n\n",type(uT[0].id),"\n\n**************")
            getteach=Teachers.objects.get(id=teid)  
            
            getteach.delete()
        if teacher=='Students':
            sid=int(sid)
            getstd=Students.objects.get(id=sid)  
            getstd.delete()
        data={"uAdmin":uA,"uStudent":uS,"uTeacher":uT}
        return render(request,'user.html',data)

    else:
        uA=Admin.objects.all()
        uS=StudentDetail.objects.all()
        uT=Teachers.objects.all()
        data={"uAdmin":uA,"uStudent":uS,"uTeacher":uT}
        return render(request,'user.html',data)
def studentFine(request):
    return HttpResponse("<h1>Student Fine page<?h1>")
def projectReport(request):
    return HttpResponse("<h1>Project Report page<?h1>")
def syllabus(request):
    return HttpResponse("<h1>Syllabus page<?h1>")
def assignments(request):
    return HttpResponse("<h1>Assignment page<?h1>")
def assignSubject(request):
    return HttpResponse("<h1>assign subject page<?h1>")
def enterMarks(request):
    return HttpResponse("<h1>enter marks page<?h1>")
def markAttendance(request):
    return HttpResponse("<h1>markAttendance page<?h1>")
def attendanceReport(request):
    return HttpResponse("<h1>attendanceReport page<?h1>")
def searchStudent(request):
    return HttpResponse("<h1>searchStudent page<?h1>")
    
    