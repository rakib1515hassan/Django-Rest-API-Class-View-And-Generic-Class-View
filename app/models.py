from django.db import models

# Create your models here.
STUDENT_CLASS = [
    ('vi'   , 'vi'  ),
    ('vii'  , 'vii' ),
    ('viii' , 'viii'),
    ('ix'   , 'ix'  ),
    ('x'    , 'x'   ),
]
GENDER = [
    ('Male'  , 'Male'  ),
    ('Female', 'Female'),
]

class Student(models.Model):
    name          = models.CharField(max_length = 100, null=True, blank=True)
    student_class = models.CharField(choices=STUDENT_CLASS, max_length=20, default='vi')
    gender        = models.CharField(choices=GENDER, max_length=20, default='Male')

    roll          = models.IntegerField(null=True, blank=True)

    picture       = models.ImageField(upload_to='Profile', null=True, blank=True)

    email         = models.EmailField(max_length=50, unique=True)

    waiver        = models.BooleanField(default=False)

    description   = models.TextField(max_length=200)

    date_of_birth = models.DateField()
    created_at    = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']



class Teacher(models.Model):
    name       = models.CharField(max_length=50)
    age        = models.PositiveIntegerField()
    salary     = models.IntegerField()
    experience = models.BooleanField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']

