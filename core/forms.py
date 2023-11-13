from django import forms
from . models import User,PersonalDetails,Education,WorkExperience,Skill,Summary,Language,Reference
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CreateUserForm(UserCreationForm):
    model = User
    fields = '__all__'


class UpdateUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

    def __init__(self,*args, **kwargs):
        super(UpdateUserForm,self).__init__(*args, **kwargs)
        self.fields['username'].required = False

class Dateinput(forms.DateInput):
    input_type = 'date'

class PersonalDetailsForm(forms.ModelForm):
    first_name = forms.CharField(required=True,widget=forms.TextInput())
    last_name = forms.CharField(required=True,widget=forms.TextInput())
    email = forms.CharField(required=True,widget=forms.EmailInput())

    class Meta:
        model = PersonalDetails
        fields = ('first_name','last_name','email','profile_pic','phone_number','city','postal_code','province') 

    def __init__(self,*args, **kwargs):
        super(PersonalDetailsForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['email'].required = False
        self.fields['profile_pic'].required = False
        self.fields['phone_number'].required = False
        self.fields['city'].required = False
        self.fields['postal_code'].required = False
        self.fields['province'].required = False

class UpdatePersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('profile_pic','phone_number','city','postal_code','province') 

    def __init__(self,*args, **kwargs):
        super(UpdatePersonalDetailsForm,self).__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False
        self.fields['phone_number'].required = False
        self.fields['city'].required = False
        self.fields['postal_code'].required = False
        self.fields['province'].required = False

class EducationForm(forms.ModelForm):
    
    class Meta:
        model = Education
        fields = ('school_name','school_address','qualification','field_of_study','year_of_graduation')
        labels ={
            'qualification': 'Qualification/Highest Grade Passed'
        }
        widgets ={
            'year_of_graduation': Dateinput,

        }

    def __init__(self,*args, **kwargs):
        super(EducationForm,self).__init__(*args, **kwargs)
        self.fields['school_name'].required = False
        self.fields['school_address'].required = False
        self.fields['qualification'].required = False
        self.fields['field_of_study'].required = False
        self.fields['year_of_graduation'].required = False


class WorkExperienceForm(forms.ModelForm):
    
    class Meta:
        model = WorkExperience
        fields = ('job_title','employer','city','province','start_date','end_date','currently_work_here')
        widgets ={
            'start_date': Dateinput,
            'end_date': Dateinput,

        }
    
    def __init__(self,*args, **kwargs):
        super(WorkExperienceForm,self).__init__(*args, **kwargs)
        self.fields['job_title'].required = False
        self.fields['employer'].required = False
        self.fields['city'].required = False
        self.fields['province'].required = False
        self.fields['start_date'].required = False
        self.fields['end_date'].required = False
        self.fields['currently_work_here'].required = False


class SkillForm(forms.ModelForm):
    
    class Meta:
        model = Skill
        fields = ('skill',)

    def __init__(self,*args, **kwargs):
        super(SkillForm,self).__init__(*args, **kwargs)
        self.fields['skill'].required = False

class SummaryForm(forms.ModelForm):
    
    class Meta:
        model = Summary
        fields = ('summary',)

    def __init__(self,*args, **kwargs):
        super(SummaryForm,self).__init__(*args, **kwargs)
        self.fields['summary'].required = False

class LanguageForm(forms.ModelForm):
    
    class Meta:
        model = Language
        fields = ('language','language_type')

    def __init__(self,*args, **kwargs):
        super(LanguageForm,self).__init__(*args, **kwargs)
        self.fields['language'].required = False
        self.fields['language_type'].required = False

class LoginForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput())
    password = forms.CharField(required=True,widget=forms.PasswordInput())

class ReferenceForm(forms.ModelForm):
    
    class Meta:
        model = Reference
        fields = ('first_name','last_name','relationship','company','email','cellphone_number')

    def __init__(self,*args, **kwargs):
        super(ReferenceForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['relationship'].required = False
        self.fields['company'].required = False
        self.fields['email'].required = False
        self.fields['cellphone_number'].required = False
