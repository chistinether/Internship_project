from django.shortcuts import render, redirect
from .forms import ReportForm, FeedbackForm, StudentRegistrationForm
from .models import Student, Report, Supervisor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    return render(request,'home.html')


@login_required
def redirect_dashboard(request):
    user = request.user
    if hasattr(user, 'student'):
        return redirect('student_dashboard')
    elif user.is_staff:
        return redirect('supervisor_dashboard')
    else:
        # fallback
        return redirect('home')

@login_required
def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.student = Student.objects.get(user=request.user)
            report.save()
            return redirect('submit_report')
    else:
        form = ReportForm()

    return render(request, 'submit_report.html', {'form': form})

@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    reports = student.report_set.all().select_related('feedback')

    return render(request, 'student_dashboard.html', {
        'reports': reports
    })


@login_required
def supervisor_dashboard(request):

    reports = Report.objects.all()

    context = {
        'reports': reports
    }

    return render(request, 'supervisor_dashboard.html', context)

@login_required
def give_feedback(request, report_id):

    report = Report.objects.get(id=report_id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.report = report
            feedback.supervisor = Supervisor.objects.get(user=request.user)
            feedback.save()

            return redirect('supervisor_dashboard')

    else:
        form = FeedbackForm()

    return render(request, 'give_feedback.html', {
        'form': form,
        'report': report
    })

def student_register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})