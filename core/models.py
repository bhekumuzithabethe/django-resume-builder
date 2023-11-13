from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

PROVINCE_CHOICES = (
    ('','----Select----'),
    ('GP','GAUTENG'),
    ('MP','MPUMALANGA'),
    ('LP','LIMPOPO'),
    ('KZN','KWAZULU NATAL'),
    ('EC','EASTERN CAPE'),
    ('WC','WESTERN CAPE'),
    ('NC','NORTHEN CAPE'),
    ('NW','NORTH WEST'),
    ('FS','FREE STATE'),

)

QUALIFICATION_CHOICES = (
    ('','----Select----'),
    ('Grade 8','Grade 8'),
    ('Grade 9','Grade 9'),
    ('Grade 10','Grade 10'),
    ('Grade 11','Grade 11'),
    ('National Senior Certificate',' National Senior Certificate'),
    ('Higher certificate','Higher certificate'),
    ('National diploma','National diploma'),
    ("Bachelor's degree","Bachelor's degree"),
    ('Honours degree','Honours degree'),
    ("Master's degree","Master's degree"),
    ('Doctoral degree','Doctoral degree'),
)

LANGUAGE_TYPE_CHOICES = (
    ('','----Select----'),
    ('Home Language','Home Language'),
    ('First Additional Language','First Additional Language'),
    ('Second Additional Language','Second Additional Language'),
    ('Third Additional Language','Third Additional Language'),

)
LANGUAGE_CHOICES = (
    ('','----Select----'),
    ('ENG','English'),
    ('AFK','Afrikaans'),
    ('ZULU','IsiZulu'),
    ('SWATI','IsiSwati'),
    ('NDEBELE','Isindebele'),
    ('XHOSA','IsiXhosa'),
    ('VENDA','TshiVenda'),
    ('Tsonga','XiTsonga'),
    ('SOTHO','SeSotho'),
    ('PEDI','SePedi'),
    ('TSWANA','SeTswana'),

)

class PersonalDetails(models.Model):
    user =models.OneToOneField(User, verbose_name=("Personal Details"), on_delete=models.CASCADE)
    profile_pic =models.ImageField(upload_to='profile_pictures',null=True,blank=True)
    phone_number = models.CharField(default='+27',max_length=13,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    postal_code = models.CharField(max_length=4,null=True,blank=True)
    province = models.CharField(max_length=20,choices=PROVINCE_CHOICES,null=True,blank=True)

    class Meta:
        verbose_name = ("Personal Details")
        verbose_name_plural = ("Personal Details")

    def __str__(self):
        return f'Username {self.user.username} : Name {self.user.first_name} {self.user.last_name}'

class Education(models.Model):

    user =models.ForeignKey(User, verbose_name=("Personal Details"), on_delete=models.CASCADE)
    school_name = models.CharField(max_length=50,null=True,blank=True)
    school_address = models.CharField(max_length=50,null=True,blank=True)
    qualification = models.CharField(max_length=50,choices=QUALIFICATION_CHOICES,null=True,blank=True)
    field_of_study = models.CharField(max_length=50,null=True,blank=True)
    year_of_graduation = models.DateField(null=True,blank=True)

    class Meta:
        verbose_name = ("Educational Background")
        verbose_name_plural = ("Educational Background")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} School: {self.school_name}'

class WorkExperience(models.Model):
    user =models.ForeignKey(User, verbose_name=("Personal Details"), on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50,null=True,blank=True)
    employer = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    province = models.CharField(max_length=20,choices=PROVINCE_CHOICES,null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    currently_work_here = models.BooleanField(default=False,null=True,blank=True)
    

    class Meta:
        verbose_name = ("Work Experience")
        verbose_name_plural = ("Work Experiences")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Employer: {self.employer}'

class Skill(models.Model):
    user =models.ForeignKey(User, verbose_name=("Personal Details"), on_delete=models.CASCADE)
    skill = models.CharField(max_length=50,null=True,blank=True)
    
    class Meta:
        verbose_name = ("Skill")
        verbose_name_plural = ("Skills")

    def __str__(self):
        return self.skill

class Summary(models.Model):
    user =models.ForeignKey(User, verbose_name=("Personal Details"), on_delete=models.CASCADE)
    summary = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = ("Summary")
        verbose_name_plural = ("Summaries")

    def __str__(self):
        return self.summary



class Language(models.Model):
    user =models.ForeignKey(User, verbose_name=("Personal Details"), on_delete=models.CASCADE)
    language = models.CharField(max_length=50,choices=LANGUAGE_CHOICES,null=True,blank=True)
    language_type = models.CharField(max_length=50,blank=True,null=True,choices=LANGUAGE_TYPE_CHOICES)
   
    class Meta:
        verbose_name = ("Language")
        verbose_name_plural = ("Languages")

    def __str__(self):
        return self.home_language

class Reference(models.Model):
    user =models.ForeignKey(User, verbose_name=("Personal Details"), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    relationship = models.CharField(max_length=50,null=True,blank=True)
    company = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    cellphone_number = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        verbose_name = ("Reference")
        verbose_name_plural = ("References")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

