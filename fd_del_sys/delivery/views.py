from django.shortcuts import render, redirect
from accounts.forms import LoginTableForm
from .forms import *
from core.views import homepage

# Create your views here.
#-------------------------------------Registration Form------------------------------------------------------
def delivery_agent_form(request):
    if request.method == 'GET':
        form_obj_user = LoginTableForm()
        form_obj_delivery_agent = DeliveryAgentProfileForm()
        return render(request,'delivery/delivery_agent_form.html', {'user':form_obj_user, 'delivery':form_obj_delivery_agent})
    
    elif request.method == 'POST':
        form_obj_user = LoginTableForm(request.POST)
        form_obj_delivery_agent = DeliveryAgentProfileForm(request.POST, request.FILES) 
        print('before if')       
        if form_obj_user.is_valid() and form_obj_delivery_agent.is_valid():
            print('after if condition')
            #save the logintable
            form_obj_user = form_obj_user.save(commit = False)
            form_obj_user.is_delivery = True   #assigning role
            form_obj_user.set_password(form_obj_user.password)  #hashing password
            form_obj_user.save()

            #save delivery_agent profile 
            form_obj_delivery_agent = form_obj_delivery_agent.save(commit= False)
            form_obj_delivery_agent.agent = form_obj_user   #link to logintable instance
            form_obj_delivery_agent.save()
        return redirect(homepage)
    
    else:        
        return redirect(delivery_agent_form)

#---------------------------------------Dashboard------------------------------------------------------------    
from django.utils.timezone import now
def delivery_agent_dashboard(request):
    today = now().date()
    delivery_assignments = request.user.delivery_assignments.filter(assigned_at__date=today)
    total_assignments = delivery_assignments.count()
    out_of_delivery = delivery_assignments.filter(status = 'picked_up').count()
    cancelled = delivery_assignments.filter(status = 'cancelled').count()
    earning_per_delivery = 50 #Rs.50/order
    earning_today = earning_per_delivery * total_assignments

    return render(request, 'delivery/delivery_agent_dashboard.html', 
                  {'total_deliveries':total_assignments, 'out_of_delivery':out_of_delivery,
                   'cancelled':cancelled, 'earning':earning_today})

#-------------------------------------------My Deliveries------------------------------------------------------------
def delivery_agent_mydeliveries(request):
    if request.method == 'GET':     
        current_assignments = request.user.delivery_assignments.filter(status__in = ['assigned', 'picked_up'])        
        completed_assignments = request.user.delivery_assignments.filter(status__in = ['delivered', 'cancelled'])

        return render(request, 'delivery/delivery_agent_mydeliveries.html', {
            'current_assignments':current_assignments, 'completed_assignments':completed_assignments
        })

    elif request.method == 'POST':
        assignment_id = request.POST['assignment_id']
        new_status = request.POST.get('status')
        is_cancel = request.POST.get('cancel')  # Check if Cancel button was clicked
        current_assignment = DeliveryAssignment.objects.get(id=assignment_id)
        
        if is_cancel == 'true':
            new_status = 'cancelled'

        if new_status in ['picked_up', 'delivered', 'cancelled']:
            current_assignment.status = new_status
            current_assignment.save()
        return redirect(delivery_agent_mydeliveries)

#--------------------------------------------Profile----------------------------------------------------------
def delivery_agent_profile(request):
    return render(request, 'delivery/delivery_agent_profile.html')

def delivery_agent_edit_profile(request):    
    form_obj_user = LoginTableForm(instance=request.user)
    form_obj_delivery = DeliveryAgentProfileForm(instance=request.user.deliveryagentprofile)
    if request.method == 'GET':
        return render(request, 'delivery/delivery_agent_edit_profile.html', 
                    {'form_user':form_obj_user, 'form_delivery':form_obj_delivery})
    elif request.method == 'POST':
        form_obj_user = LoginTableForm(request.POST, instance=request.user)
        form_obj_delivery = DeliveryAgentProfileForm(request.POST, request.FILES, instance=request.user.deliveryagentprofile)
        
        if form_obj_user.is_valid() and form_obj_delivery.is_valid():
            form_obj_user.save()
            form_obj_delivery.save()
            return redirect('delivery_agent_profile')  # Redirect to the same profile page after saving

    return render(request, 'delivery/delivery_agent_profile.html', {
        'form_user': form_obj_user,
        'form_delivery': form_obj_delivery,        
    })