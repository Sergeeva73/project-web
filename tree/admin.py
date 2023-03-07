from django.contrib import admin
from tree.models import Student, Discipline, Group, Mark, Lesson


class MarkAdmin(admin.ModelAdmin):
    list_display = ('student','mark','lesson')
    list_display_links = ('student','lesson')
    search_fields = ('mark','student__name')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'group')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('discipline','date', 'group')

admin.site.register(Student,StudentAdmin)
admin.site.register(Discipline)
admin.site.register(Group)
admin.site.register(Mark,MarkAdmin)
admin.site.register(Lesson,LessonAdmin)