from django.shortcuts import render,redirect
from stdapp.models import student

# Create your views here.
def index(request):
    return render(request,'Welcome.html')
def cm(request):
    return render(request,'student.html')
def std(request):
    if request.method=='POST':
        sname=request.POST['std_name']
        saddr=request.POST['std_addr']
        sage=request.POST['std_age']
        semail=request.POST['std_em']
        sdate=request.POST['std_date']
        sedu=request.POST['std_edu']
        sgender=request.POST['stdgen']
        snumber=request.POST['std_num']
        shobby=request.POST.getlist('hobby')
        prd=student(StudentName=sname,Address=saddr,Age=sage,Emailid=semail,JoiningDate=sdate,Qualification=sedu,Gender=sgender,Mobile=snumber,Hobby=shobby)
        prd.save()
        return redirect('stdshow')
def stdshow(request):
    student1=student.objects.all()
    return render(request,'stdshow.html',{'std':student1})
def edit(request,pk):
    std=student.objects.get(id=pk)
    return render(request, 'edit.html', {'student': std})
    
def editstd(request,pk):
    if request.method=='POST':
        std=student.objects.get(id=pk)
        std.StudentName=request.POST.get('std_name')
        std.Address=request.POST.get('std_addr')
        std.Age=request.POST.get('std_age')
        std.Emailid=request.POST.get('std_ema')
        std.JoiningDate=request.POST.get('std_dat')
        std.Qualification=request.POST.get('std_edu')
        std.Gender=request.POST.get('std_gen')
        std.Mobile=request.POST.get('std_mob')
        std.save()
        return redirect('stdshow')
    return render(request,"edit.html")
def deletepage(request,pk):
    prd=student.objects.get(id=pk)
    prd.delete()
    return redirect('stdshow')
def show_students(request,sid):
    stu=student.objects.get(id=sid)
    return render(request,'studentdetails.html',{'student':stu})
