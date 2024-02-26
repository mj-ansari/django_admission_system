from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course,Student
from .forms import *


def index(request):
    top_courses = Course.objects.all()[:3]
    return render(request, "admission/index.html",{'courses':top_courses})


@login_required(login_url="login")
def feedback(request):
    form = FeedbackForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.email = request.user.email
            form.save()
            messages.success(request, "Your feedback has been submitted successfully.")
        else:
            messages.error(request, "There is an issue in posting your feedback !!")
    return render(request, "admission/feedback.html", {"form": form})


def about(request):
    return render(request, "admission/about.html")


def courses(request):
    all_courses = Course.objects.all()
    return render(request, "admission/courses.html", {"courses": all_courses})


@login_required(login_url="login")
def admission(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        education_form = EducationForm(request.POST)
        document_form = DocumentForm(request.POST, request.FILES)
        admission_form = AdmissionForm(request.POST)
        if all(
            [
                student_form.is_valid(),
                education_form.is_valid(),
                document_form.is_valid(),
                admission_form.is_valid()
            ]
        ):
            student = student_form.save(commit=False)
            student.user = request.user
            student.save()
            education = education_form.save(commit=False)
            education.student = student
            education.save()
            document = document_form.save(commit=False)
            document.student = student
            document.save()
            adm = admission_form.save(commit=False)
            adm.student = student
            adm.status = 'Pending'
            adm.save()
            messages.success(request, "Application For The Admission Send Successfully." )
            return redirect("profile")
    else:
        if Student.objects.filter(user=request.user).exists():
            student_data = Student.objects.filter(user=request.user)
            return render(request,'admission/admission.html',{'student_data':student_data})
        
        student_form = StudentForm()
        education_form = EducationForm()
        document_form = DocumentForm()
        admission_form = AdmissionForm()
    return render(
        request,
        "admission/admission.html",
        {
            "student_form": student_form,
            "education_form": education_form,
            "document_form": document_form,
            'admission_form': admission_form,
        },
    )
