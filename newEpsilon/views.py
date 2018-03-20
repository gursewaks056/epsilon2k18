from django.shortcuts import render, HttpResponse, redirect
from .models import RegistrationTable, EventTable
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def recorded(request):
    try:
        if(request.method == 'POST'):
            event = request.POST['event1']
        else:
            event = "no event1"

    except:
        event = "key error"

    return render(request, 'events.html', { 'message' : event })


def save_record(request, report_type):

    if(request.user.is_active):
        event = "user logged in"

        if(request.method == 'POST'):
            selected_event = request.POST[report_type]

            name = request.user.first_name
            email= request.user.email

            regTable = RegistrationTable.objects.get(email = email)

            mobile = regTable.mobile

            try:
                existence = EventTable.objects.get(email = email, event = selected_event)
            except:
                existence = None

            if(existence):
                event = "You already Selected this event"
                return render(request, 'events.html', { 'message' : event })




            try:
                abc = EventTable( name = name, email = email, mobile = mobile, event = selected_event )
                abc.save()
                event = "You are successfully registered for "+selected_event

            except:
                event = "Not Selected!"


        else:
                event = "no event selected"




    else:
        event = "User is not logged in!"
        return render(request, 'events.html', { 'message' : event })



    return render(request, 'events.html', { 'message' : event })


def index(request):
    return render(request, 'index.html')

def events(request):
    return render(request, 'events.html')

def about(request):
    return render(request, 'about.html')



def registrationform(request):
	return render(request, 'form.html')

def loginform(request):
    return render(request, 'login_form.html')

def postregistration(request):

    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        college = request.POST['college']
        mobile = request.POST['mobile']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if ( len(mobile) != 10):
            message = 'Mobile Number should be of 10 digits'
            return render(request, 'form.html', {'message' : message})


        if (password != confirm_password):
            message = 'Password Mismatch'
            return render(request, 'form.html', {'message' : message})

        web = RegistrationTable(name = name, email = email, mobile = mobile, college = college)

        try:
            web.save()
        except:
            message = "Registration Unsuccessful!"
            return render(request, 'form.html', {'message' : message})

        user = User.objects.create_user(email, email, password)

        user.first_name = name

        try:
            user.save()
        except:
            message = "Registration Unsuccessful!"
            return render(request, 'form.html', {'message' : message})


        message = "Registration Successful!"
        return render(request, 'index.html', {'message' : message})

    else:

        return HttpResponse("Submitted NO")

def postlogin(request):
    if(request.method=='POST'):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:

            if(email == "dcsa@puchd.com"):
                message = "Administrator cannot login here!"
                return render(request, 'index.html', {'message' : message})

            login(request, user)
        else:
                message = "Login Failed!"
                return render(request, 'index.html', {'message' : message})

        message = "Login Successful!"
        return render(request, 'index.html', {'message' : message})

    else:
        message = "Unable to get input"
        return render(request, 'index.html', {'message' : message})


def logoutG(request):

    if (request.user.is_active):
        logout(request)
    else:
        message = "User is not logged in!"
        return render(request, 'index.html', {'message' : message})

    message = "User is logged Out!"
    return render(request, 'index.html', {'message' : message })
