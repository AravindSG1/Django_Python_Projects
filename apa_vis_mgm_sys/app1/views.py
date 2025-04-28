from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from datetime import date, timedelta
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required #for login to work on all pages


# Create your views here.
def loginpage(request):
    if request.method=='GET':
        return render(request,'login.html')        
    elif request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            #providing all data as same as login page
            return redirect('index')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def user_logout(request):
    logout(request)    #this line is must to end session otherwise, function just renders loginpage
    return redirect('login')

@login_required(login_url='login')
def homepage(request):
    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    lastweek = date.today() - timedelta(days=7)

    todays_visitor = Visitor.objects.filter(date_time__date = today).count()
    yesterdays_visitor = Visitor.objects.filter(date_time__date = yesterday).count()    
    week_visitor = Visitor.objects.filter(date_time__date__range=[lastweek, yesterday]).count()
    total_visitors = Visitor.objects.count()
    total_pass = Pass.objects.count()    
    return render(request,'index.html',{'todays_visitor':todays_visitor,
                                        'yesterdays_visitor':yesterdays_visitor,'week_visitor':week_visitor,
                                        'total_visitors':total_visitors, 'total_pass':total_pass})

@login_required(login_url='login')
def visitor_form(request):
    if request.method == 'GET':
        return render(request,'add_visitor.html')
    elif request.method == 'POST':
        category = request.POST['category']
        full_name = request.POST['name']
        email_input = request.POST['email']
        phone_number = request.POST['phone_no']
        address = request.POST['address']
        apartment_no = request.POST['apartment_no']
        floor = request.POST['floor']
        person_to_meet = request.POST['person_to_meet']
        reason_to_meet = request.POST['reason_to_meet']

        if Visitor.objects.filter(email=email_input).exists(): #checking if email already exists
            return render(request, 'add_visitor.html', {
                'message': 'This email is already registered. Please use a different one.'})

        try:
            obj = Visitor.objects.create(
                category = category, name=full_name, email=email_input, phone_number=phone_number,
                address=address, apartment_number=apartment_no, floor=floor,to_meet=person_to_meet,
                reason=reason_to_meet
            )
            # return HttpResponse('id = '+str(obj.id))
            return render(request,'add_visitor.html',{'message':'Visitor details added Successfully'})
        except Exception:  #if data is not able to insert in database this error is thrown
            return render(request, 'add_visitor.html', {
                'message': 'There was a problem saving the visitor. Please try again.'
            })
    
@login_required(login_url='login')
def pass_form(request):
    if request.method == 'GET':
        return render(request,'pass_form.html')
    elif request.method == 'POST':
        category = request.POST['category']
        name = request.POST['name']    
        phone_number = request.POST['phone_no']
        address = request.POST['address']
        apartment_no = request.POST['apartment_no']
        from_date = request.POST['from_date']
        floor = request.POST['floor']
        to_date = request.POST['to_date']
        pass_desc = request.POST['pass_desc']    

        try:
            obj = Pass.objects.create(
                category = category, name=name,  phone_number=phone_number,
                address=address, apartment_number=apartment_no, floor=floor,
                from_date=from_date, to_date=to_date, pass_desc=pass_desc
            )
            # return HttpResponse('id = '+str(obj.id))
            return render(request,'pass_form.html',{'message':'Visitor pass created Successfully'})
        except Exception:
            return render(request, 'pass_form.html', {
                'message': 'There was a problem saving the visitor. Please try again.'})            
    
@login_required(login_url='login')
def update_visitor(request,id):
    obj = Visitor.objects.get(pk=id)
    if request.method == 'GET':  #doubt
        context = {}
        # obj = Todo.objects.get(pk=id)
        context['form'] = VisitorForm(instance = obj)  #only one dictionary is possible to pass on render
        context['visitor_details'] = obj               #so visitor object is also adding on same dictionary
        return render(request, 'update.html',context)
    
    elif request.method == 'POST':        
        todo = VisitorForm(data=request.POST,instance=obj)
        if todo.is_valid():            
            todo.save()
            obj = Visitor.objects.all
            
            return render(request, 'manage_visitor.html',{'visitor_data':obj})
        else:
            print('not valued form')
            print(todo.errors)
            return HttpResponse("Not Updated")
    else:
        return render(request, 'manage_visitor.html',context)   

@login_required(login_url='login')
def delete_visitor(request, id):
    obj = Visitor.objects.get(pk = id)
    obj.delete()
    obj = Visitor.objects.all()
    return render(request, 'manage_visitor.html',{'visitor_data':obj})

@login_required(login_url='login')
def delete_pass(request, id):
    obj = Pass.objects.get(pk = id)
    obj.delete()
    obj = Pass.objects.all()
    return render(request, 'manage_pass.html',{'pass_data':obj})

@login_required(login_url='login')
def manage_visitor(request):
    obj = Visitor.objects.all()
    return render(request,'manage_visitor.html',{'visitor_data':obj})

@login_required(login_url='login')
def manage_pass(request):
    obj = Pass.objects.all()
    return render(request,'manage_pass.html',{'pass_data':obj})

@login_required(login_url='login')
def search_visitor(request):
    if request.method == 'GET':
        return render(request,'search_visitor.html')
    elif request.method == 'POST':
        searchkey = request.POST['searchkey']
        # obj = Visitor.objects.filter(phone_number=searchkey)
        obj = Visitor.objects.filter(Q(phone_number=searchkey)|Q(name=searchkey))
        return render(request,'search_visitor.html',{'filtered_data':obj})
    

@login_required(login_url='login')
def search_pass(request):
    if request.method == 'GET':
        return render(request,'search_pass.html')
    elif request.method == 'POST':
        searchpass = request.POST['searchpass']
        # obj = Pass.objects.filter(phone_number=search_pass)
        obj = Pass.objects.filter(Q(phone_number=searchpass)|Q(name=searchpass))
        return render(request,'search_pass.html',{'filtered_data':obj})

@login_required(login_url='login')
def visitor_report(request):
    if request.method == 'GET':
        return render(request,'visitor_report.html')
    elif request.method == 'POST':
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        # Check if both dates are provided
        if from_date and to_date:
            try:
                #here date_time__range is the field name in database
                obj = Visitor.objects.filter(date_time__range=(from_date,to_date)) 
                return render(request,'visitor_report.html',{'filtered_data':obj,'from_date':from_date,'to_date':to_date})
            except Exception as e:
                return render(request, 'visitor_report.html', {'message': str(e)})
        else:
            return render(request,'visitor_report.html',{'message':"Please select dates"})
        

@login_required(login_url='login')
def pass_report(request):
    if request.method == 'GET':
        return render(request,'pass_report.html')
    elif request.method == 'POST':
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        if from_date and to_date:
            try:
                obj = Pass.objects.filter(created_datetime__range=(from_date,to_date))
                return render(request,'pass_report.html',{'filtered_data':obj,'from_date':from_date,'to_date':to_date})
            except Exception as e:
                return render(request, 'pass_report.html', {'message': str(e)})
        else:
            return render(request,'pass_report.html',{'message':"Please select dates"})
    
@login_required(login_url='login')
def pass_details(request,id):
    obj = Pass.objects.get(pk = id)
    return render(request,'pass_details.html',{'pass_details':obj})