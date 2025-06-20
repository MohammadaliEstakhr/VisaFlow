from django.shortcuts import render, redirect
from .models import VisaApplication
from .forms import VisaApplicationForm
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
import io, csv
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
import os
from django.conf import settings

def login_view(request):
    from django.contrib.auth import authenticate, login
    from django.contrib.auth.forms import AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')

@login_required
def home(request):
    applications = VisaApplication.objects.all()
    return render(request, 'home.html', {'applications': applications})

@login_required
def submit_application(request):
    if request.method == 'POST':
        form = VisaApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VisaApplicationForm()
    return render(request, 'submit.html', {'form': form})

@login_required
def export_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    applications = VisaApplication.objects.all()
    y = 800
    for app in applications:
        p.drawString(100, y, f"{app.applicant_name} - {app.visa_type} - {app.status}")
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='applications.pdf')

@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="applications.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Type', 'Status'])
    for app in VisaApplication.objects.all():
        writer.writerow([app.applicant_name, app.visa_type, app.status])
    return response

@login_required
def dashboard(request):
    types = {}
    for app in VisaApplication.objects.all():
        types[app.visa_type] = types.get(app.visa_type, 0) + 1
    labels, data = list(types.keys()), list(types.values())
    fig, ax = plt.subplots()
    ax.bar(labels, data)
    ax.set_title("Visa Types Distribution")
    chart_path = os.path.join(settings.BASE_DIR, 'core/static/chart.png')
    plt.savefig(chart_path)
    plt.close()
    return render(request, 'dashboard.html')
