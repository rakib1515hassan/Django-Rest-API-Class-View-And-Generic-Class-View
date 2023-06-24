from django.contrib import admin
from app.models import Teacher, Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'gender', 'roll', 'email', 'waiver', 'description', 'date_of_birth', 'created_at' )



# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'salary', 'experience')