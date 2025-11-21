from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Session
from .forms import StudentForm, SessionForm


def create_test_data():
    """Создает тестовых студентов если их нет в базе"""
    if Student.objects.count() == 0:
        # Создаем студентов
        student1 = Student.objects.create(name="Иванов Иван", group="ИСП-101")
        student2 = Student.objects.create(name="Петров Петр", group="ИСП-102")
        student3 = Student.objects.create(name="Сидорова Анна", group="ИСП-101")

        # Создаем оценки
        Session.objects.create(student=student1, math=5, physics=4, programming=5)
        Session.objects.create(student=student2, math=3, physics=4, programming=5)
        Session.objects.create(student=student3, math=4, physics=5, programming=4)


def student_list(request):
    # Автоматически создаем тестовых студентов при первом заходе
    if Student.objects.count() == 0:
        create_test_data()

    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})


def edit_session(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    session, created = Session.objects.get_or_create(student=student)

    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = SessionForm(instance=session)
    return render(request, 'edit_session.html', {'form': form, 'student': student})


def create_test_data_view(request):
    create_test_data()
    return redirect('student_list')