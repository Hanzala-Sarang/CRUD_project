from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    
    class Meta:
        
        model = Student
        fields = '__all__'
        widgets = {
            
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
        
        