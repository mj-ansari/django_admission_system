from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.core.validators import MaxValueValidator,MinValueValidator

GENDER_CHOICES = (
    ('MALE', "Male"),
    ('FEMALE', "Female"),
    ('OTHER', "Other"),
)

RELIGION_CHOICES = (
    ('HINDU', "HINDU"),
    ('MUSLIM', "MUSLIM"),
    ('CHRISTIAN', "CHRISTIAN"),
    ('JAIN', "JAIN"),
    ('SPIRITUAL', "SPIRITUAL"),
    ('OTHER', "OTHER"),
)

STREAM_CHOICES = (
    ('Science','Science'),
    ('Commerce','Commerce'),
    ('Arts','Arts'),
    ('Diploma','Diploma'),
)

CATEGORY_CHOICES = (
    ('SC','SC'),
    ('ST','ST'),
    ('OBC','OBC'),
    ('GENERAL','GENERAL'),
    ('OTHER','OTHER'),
)

STUDENT_STATUS = (
    ('Pending','Pending'),
    ('Active','Active'),
    ('Disable','Disable'),
)

# This is base Model to Manage Date
class BaseClass(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(BaseClass):
    course_name = models.CharField(max_length=50)
    duration = models.IntegerField()
    percent_criteria = models.FloatField(default=50.00)
    fee = models.IntegerField()
    seats = models.PositiveSmallIntegerField()
    description = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to='Course/', height_field=None, width_field=None, max_length=None)

    def image_tag(self):
        return format_html('<img src="/media/Student/{}" style="width:150px; border-radius:20px">'.format(self.image))

    def __str__(self) -> str:
        return self.course_name


class State(BaseClass):
    state_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return (self.state_name)


class City(BaseClass):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return (self.city_name)


class Student(BaseClass):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=13)
    gender = models.CharField(max_length=15,choices=GENDER_CHOICES)
    aadhar_no = models.CharField(max_length=12,unique=True)
    birth_date = models.DateField()
    address = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    pin = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(999999)])
    religion = models.CharField(max_length=15, choices=RELIGION_CHOICES)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self) -> str:
        return (self.first_name + " " + self.last_name)


class Education(BaseClass):
    student = models.OneToOneField(Student,on_delete=models.CASCADE,related_name='education')
    school_name = models.CharField(max_length=255)
    stream = models.CharField(max_length=15, choices=STREAM_CHOICES)
    percentage_10th = models.DecimalField(max_digits=5,decimal_places=2,validators=[MaxValueValidator(100),MinValueValidator(0)])
    percentage_12th = models.DecimalField(max_digits=5,decimal_places=2,validators=[MaxValueValidator(100),MinValueValidator(0)])
    college_name = models.CharField(max_length=255,null=True,blank=True)
    college_cgpa = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True,validators=[MaxValueValidator(10),MinValueValidator(0)])

class Document(BaseClass):
    student = models.OneToOneField(Student,on_delete=models.CASCADE,related_name='document')
    student_image = models.ImageField(upload_to='Student/image')
    aadhar_image = models.ImageField(upload_to='Student/aadhar')
    marksheet_10th = models.ImageField(upload_to='Student/10th')
    marksheet_12th = models.ImageField(upload_to='Student/12th')
    marksheet_clg = models.ImageField(upload_to='Student/college',null=True,blank=True)

class Admission(BaseClass):
    student= models.OneToOneField(Student,default='Student Deleted',on_delete=models.SET_DEFAULT,related_name='admission')
    course = models.OneToOneField(Course,default='Course Deleted',on_delete=models.SET_DEFAULT,related_name='course')
    status = models.CharField(max_length=10,choices=STUDENT_STATUS,default=STUDENT_STATUS[2])   

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name}'

class Feedback(models.Model):
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email