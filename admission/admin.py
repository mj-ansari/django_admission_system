from django.contrib import admin
from . models import *

class StudentInline(admin.StackedInline):
    model = Education
    can_delete = False
    verbose_name_plural = 'Education Detail'

class EducationInline(admin.TabularInline):
    model = Education
    can_delete = False
    verbose_name_plural = 'Education Detail'

class DocumentInline(admin.StackedInline):
    model = Document
    can_delete = False
    verbose_name_plural = 'Documents'

class StudentAdmin(admin.ModelAdmin):
    inlines = (EducationInline, DocumentInline)

admin.site.register(Student, StudentAdmin)

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('id','student','course','status')
    list_filter = ("id","student","course","status")
    list_editable = ('status',)

@admin.register(Course)
class A_Course(admin.ModelAdmin):
    list_display = ("course_name","duration","percent_criteria","fee","created","modified")
    list_filter = ("course_name",)


@admin.register(State)
class A_State(admin.ModelAdmin):
    list_display = ("state_name","created","modified")


@admin.register(City)
class A_City(admin.ModelAdmin):
    list_display = ("city_name","state","created","modified")


@admin.register(Feedback)
class A_Feedback(admin.ModelAdmin):
    readonly_fields = ("email","message","created_at")
    list_display = ("email","message","created_at")