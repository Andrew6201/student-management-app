from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Student
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not username or not email or not password or not password2:
            messages.info(request, 'All fields must be filled out')
            return redirect('register')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already Used')
                return redirect('register')

            elif len(password)<6:
                messages.info(request,'The password should be greater than 6 characters')
                return redirect('register')
            elif len(username)==0:
                messages.info(request,'The username  should not be empty')
                return redirect('register')
            elif len(email)==0:
                messages.info(request,'The email  should not be empty')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                return redirect('login')
        
        else:
            messages.info(request,'Passwords do not match')
            return redirect('register')
    
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('mainpage')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')






def mainpage(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        country = request.POST['country']
        email = request.POST['email']
        course = request.POST['course']
        gpa = request.POST['gpa']
        number = request.POST['number']
        mobile = request.POST['mobile']

        try:
            gpa = float(gpa)
            number = int(number)
            mobile = int(mobile)

        except ValueError:
            messages.error(request, 'GPA or number or mobile number  must be valid numbers!!!.')
            return redirect('mainpage')

        
        new = Student(
            user = request.user,
            firstname=firstname,
            lastname=lastname,
            address=address,
            country=country,
            email=email,
            course=course,
            gpa=gpa,
            number=number,
            mobile=mobile,
        )
        new.save()
        return redirect('data')

    all = Student.objects.filter(user=request.user) 
    return render(request, 'mainpage.html', {"all": all})



def data(request):
    all = Student.objects.filter(user=request.user) 
    return render(request, 'data.html', {"all": all})




def delete(request, pk):
        student = Student.objects.get(id=pk)
        student.delete()
        return redirect('data')

    



def logout(request):
    auth.logout(request)
    return redirect('home')

def update(request,pk):
    student= Student.objects.get(pk=pk)
    if student.user == request.user:
        if request.method == "POST":
            student.firstname = request.POST['firstname']
            student.lastname = request.POST['lastname']
            student.address = request.POST['address']
            student.country = request.POST['country']
            student.email = request.POST['email']
            student.course = request.POST['course']
            student.gpa = float(request.POST['gpa'])
            student.number = int(request.POST['number'])
            student.mobile = int(request.POST['mobile'])
            student.save()

            return redirect('data')
        

    return render(request, "update.html",{'student':student})

