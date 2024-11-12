from django.shortcuts import render, redirect

from .models import Blog, AddCourse
from .forms import BlogForm, AddCourseForm


# Create your views here.
def FacultyHomePage(request):
    return render(request, 'facultyapp/FacultyHomePage.html')


def blogpost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:blogpost')
    else:
        form = BlogForm()

    blogs = Blog.objects.all()
    return render(request, 'facultyapp/blogpost.html', {'form': form, 'blogs': blogs})


def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:FacultyHomePage')
    else:
        form = AddCourseForm()
    return render(request, 'facultyapp/add_course.html', {'form': form})


from .models import AddCourse
from adminapp.models import StudentList


def view_student_list(request):
    course = request.GET.get('course')
    section = request.GET.get('section')
    student_courses = AddCourse.objects.all()
    if course:
        student_courses = student_courses.filter(course=course)
    if section:
        student_courses = student_courses.filter(section=section)
    students = StudentList.objects.filter(id__in=student_courses.values('student_id'))
    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES
    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }
    return render(request, 'facultyapp/view_student_list.html', context)