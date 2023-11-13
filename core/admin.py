from django.contrib import admin
from . models import PersonalDetails,Education,WorkExperience,Skill,Summary,Language,Reference

# Register your models here.
admin.site.register(PersonalDetails)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(Summary)
admin.site.register(Language)
admin.site.register(Reference)