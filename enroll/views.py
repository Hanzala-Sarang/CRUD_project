from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
# Create your views here.


# Add New Student
def add_student(request):
    
    if request.method == 'POST':
        
        form = StudentForm(request.POST)
        
        if form.is_valid():
            
            
            nm = request.POST.get('name')
            em = request.POST.get('email')
            pw = request.POST.get('password')
            
            # other option
            
            # nm = form.cleaned_data['name']
            # em = form.cleaned_data['email']
            # pw = form.cleaned_data['password']
            
            
            stud = Student(name=nm,email=em,password=pw)
            
            stud.save()
            
            reg = True
            
            form = StudentForm()
            
            studs = Student.objects.all()
            
            return render(request,'enroll/display.html',{'reg':reg,'form':form,'studs':studs})
    
    else: 
        
        form = StudentForm()
        
    studs = Student.objects.all()
        
    return render(request,'enroll/display.html',{'form':form,'studs':studs})


def update_student(request):
    
    return render(request,'enroll/update.html')

# Remove Student
def remove_student(request,id):
    
    if request.method == 'POST':
        
        stud = Student.objects.get(id=id)
        
        stud.delete()
        
        return redirect('/')
    

# Update Student
def update_student(request,id):
    
    if request.method == 'POST':
        
        st = Student.objects.get(pk=id)
        
        form = StudentForm(request.POST,instance=st)
        
        if form.is_valid():
            
            form.save()
            
        update = True
        
        return render(request,'enroll/update.html',{'form':form,'update':update})
    else:
        
        st = Student.objects.get(pk=id)
        
        form = StudentForm(instance=st)
        
    return render(request,'enroll/update.html',{'form':form})