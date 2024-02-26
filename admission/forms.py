from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'contact': forms.TextInput(attrs={'class':'form-control','placeholder':'+91 00000 00000'}),
            'birth_date': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'religion': forms.Select(attrs={'class':'form-select'}),
            'category': forms.Select(attrs={'class':'form-select'}),
            'aadhar_no': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Aadhaar Number'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,'placeholder':'1234 Main St...'}),
            'state': forms.Select(attrs={'class':'form-select'}),
            'city': forms.Select(attrs={'class':'form-select'}),
            'pin': forms.NumberInput(attrs={'class':'form-control','placeholder':'000000'})
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['religion'].choices = [('', 'Choose...')] + list(self.fields['religion'].choices)[1:]
        self.fields['category'].choices = [('', 'Choose...')] + list(self.fields['category'].choices)[1:]
        self.fields['gender'].choices = list(self.fields['gender'].choices)[1:]
        self.fields['state'].choices = [('', 'Choose...')] + list(self.fields['state'].choices)[1:]
        self.fields['city'].choices = [('', 'Choose...')] + list(self.fields['city'].choices)[1:]
        

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ('student',)
        widgets = {
            'school_name': forms.TextInput(attrs={'class':'form-control','placeholder':'School Name'}),
            'stream': forms.Select(attrs={'class':'form-select'}),
            'percentage_10th': forms.NumberInput(attrs={'class':'form-control','placeholder':'10th Percentage...','min':0,'max':100.00}),
            'percentage_12th': forms.NumberInput(attrs={'class':'form-control','placeholder':'12th Percentage...','min':0,'max':100.00}),
            'college_name': forms.TextInput(attrs={'class':'form-control','placeholder':'College Name'}),
            'college_cgpa': forms.NumberInput(attrs={'class':'form-control','placeholder':'Out of 10','min':0,'max':10.00}),
        }
    
    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields['stream'].choices = [('', 'Choose...')] + list(self.fields['stream'].choices)[1:]

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ('student',)
        widgets = {
            'student_image': forms.FileInput(attrs={'class': 'form-control'}),
            'aadhar_image':forms.FileInput(attrs={'class': 'form-control'}),
            'marksheet_10th':forms.FileInput(attrs={'class': 'form-control'}),
            'marksheet_12th':forms.FileInput(attrs={'class': 'form-control'}),
            'marksheet_clg':forms.FileInput(attrs={'class': 'form-control'}),
        }
        

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ('course',)
        widgets = {
            'course' : forms.Select(attrs={'class':'form-select'})
        }


class FeedbackForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email",
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Message here...",
                "style": "height:100px",
            }
        )
    )

    class Meta:
        model = Feedback
        fields = "__all__"
