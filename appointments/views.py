from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils import timezone
# pagination 
from django.core.paginator import Paginator


# authentication >> sign up view 
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'authentication/signup.html')



# login view 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'authentication/login.html')

# logout view 
def logout_view(request):
    logout(request)
    return redirect('login')


def landing_page(request):
    return render(request, 'landing.html')



@login_required
def home_view(request):
    # Show only the next 3 upcoming appointments
    upcoming_appointments = Appointment.objects.filter(
        user=request.user,
        date__gte=timezone.now().date()
    ).order_by('date', 'time')[:3]

    return render(request, 'appointments/home.html', {
        'upcoming_appointments': upcoming_appointments
    })


# List all appointments for logged-in user
@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    service = request.GET.get('service')
    date = request.GET.get('date')

    if service:
        appointments = appointments.filter(service=service)

    if date:
        appointments = appointments.filter(date=date)

    # Pagination: Show 5 appointments per page
    paginator = Paginator(appointments, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'appointments/appointment_list.html', {
        'appointments': page_obj,
        'selected_service': service,
        'selected_date': date,
    })




# Create new appointment
@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, "Appointment booked successfully!")

            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {'form': form})

# Update appointment
@login_required
def appointment_update(request, pk):
    appointment = Appointment.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment updated successfully!")
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/appointment_form.html', {'form': form})

# Delete appointment
@login_required
def appointment_delete(request, pk):
    appointment = Appointment.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, "Appointment deleted successfully!")
        return redirect('appointment_list')
    return render(request, 'appointments/appointment_delete.html', {'appointment': appointment})



def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error generating PDF <pre>" + html + "</pre>")
    return response

# PDF for all appointments
def appointments_pdf(request):
    appointments = Appointment.objects.filter(user=request.user)
    context = {'appointments': appointments}
    return render_to_pdf('appointments/appointment_pdf.html', context)

# PDF for single appointment
def appointment_pdf_single(request, pk):
    appointment = Appointment.objects.get(pk=pk, user=request.user)
    context = {'appointment': appointment}
    return render_to_pdf('appointments/appointment_pdf.html', context)
