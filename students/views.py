
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
def home(request):
    students = Student.objects.all()

    return render(request, 'students/home.html', {
        'students': students
    })


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {
        'form': form
    })

def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {
        'form': form
    })

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('/')

def home(request):
    query = request.GET.get('q', '')

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, 'students/home.html', {
        'students': students
    })