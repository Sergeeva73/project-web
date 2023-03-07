from django.shortcuts import render
from django.http import HttpResponse
from tree.models import Student
from tree.models import Discipline
from tree.models import Group
from tree.models import Mark
from tree.models import Lesson


def index(request):
    html = 'список студентов<br><br>'
    new = Student.objects.all()
    for i in new:
        html += f"{i.name} {i.age} <br>"

    return HttpResponse(html)


def main(request):
    return render(request, 'main.html')


def main_discipline(request):
    disciplines = Discipline.objects.order_by('discipline')
    context = {'data': disciplines}
    return render(request, 'disciplines.html', context)


def main_student(request):
    students = Student.objects.order_by('name')
    context = {'data2': students}
    return render(request, 'students.html', context)


def main_group(request):
    groups = Group.objects.order_by('group')
    context = {'data3': groups}
    return render(request, 'groups.html', context)


def stud_by_group(request, group_id):
    students = Student.objects.filter(group=group_id)
    context = {'data2': students}
    return render(request, 'students.html', context)


def stud_info(request, stud_id):
    student = Student.objects.get(id=stud_id)
    marks = Mark.objects.filter(student=stud_id)
    lessons = Lesson.objects.filter(group=student.group)
    disciplines = set([x.discipline.discipline for x in lessons])
    result = dict()

    for discipline in disciplines:
        discipline_marks = dict()
        for lesson in lessons:
            if lesson.discipline.discipline == discipline:
                discipline_marks[lesson.date] = ''
        for mark in marks:
            if mark.lesson.date in discipline_marks.keys():
                discipline_marks[mark.lesson.date] = mark.mark
        result[discipline] = discipline_marks
    context = {'student': student, 'result': result}
    return render(request, 'infostudent.html', context)
