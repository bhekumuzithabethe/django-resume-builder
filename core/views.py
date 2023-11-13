from django.shortcuts import render,redirect
from . models import User,PersonalDetails,Education,WorkExperience,Skill,Summary,Language,Reference
from .forms import CreateUserForm,UpdateUserForm,PersonalDetailsForm,UpdatePersonalDetailsForm,EducationForm,WorkExperienceForm,SkillForm,SummaryForm,LanguageForm,LoginForm,ReferenceForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages 
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.
@login_required(login_url='dologin')
def index_view(request):
    user = request.user
    personal_details = PersonalDetails.objects.filter(user=user).first()
    educational_background = Education.objects.filter(user=user).all()
    work_experience = WorkExperience.objects.filter(user=user).all()
    skill = Skill.objects.filter(user=user).all()
    languages = Language.objects.filter(user=user).all()
    summary = Summary.objects.filter(user=user).first()
    references = Reference.objects.filter(user=user).all()
    print(personal_details)
    return render(request,'core/view_resume.html',{
        'user':user,
        'personal_details':personal_details,
        'educational_backgrounds':educational_background,
        'work_experiences':work_experience,
        'skills':skill,
        'languages':languages,
        'references':references,
        'summary':summary,
    })

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index') 
        else:
            messages.error(request, 'Invalid Login Details.')
            return redirect('dologin')
    else:
        form = LoginForm() 
        return render(request,'login/login.html',{
            'form':form,
        })
    
@login_required(login_url='dologin')
def logout_view(request):
    logout(request)
    return redirect('dologin')

def create_user_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken.')
                return redirect('sign-up') 
            else:
                if form.is_valid():
                    new_user = form.save()
                    login(request, new_user)
                    return redirect('personal-details') 
                return redirect('sign-up')
        else:
            messages.error(request, 'Passwords not matching.')
            return redirect('sign-up') 
      
    else:
        form = CreateUserForm() 
        return render(request,'registration/sign_up.html',{
            'form':form,
        })
    
@login_required(login_url='dologin')    
def update_user_view(request):
    user = request.user
    if request.method == "POST":
        form = UpdateUserForm(request.POST,instance=user)
        
        username = request.POST['username']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('update-user') 
        else:
            if form.is_valid():
                updated_user = form.save()
                messages.info(request, 'You have successfully updated you user details.')
                return redirect('index') 
            return redirect('update-user')
      
    else:
        form = UpdateUserForm(request.POST,instance=user)
        return render(request,'forms/update_user.html',{
            'form':form,
        })

@login_required(login_url='dologin')
def personal_details_view(request):
    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            profile_pic = form.cleaned_data.get('profile_pic')
            phone_number = request.POST['phone_number']
            city = request.POST['city']
            postal_code = request.POST['postal_code']
            province = request.POST['province']
            personal_details = PersonalDetails.objects.create(user=user,profile_pic=profile_pic,phone_number=phone_number,city=city,postal_code=postal_code,province=province)
            personal_details.save()
            return redirect('education')
        else:
            messages.info(request, 'You already have an personal details.')
            return redirect('personal-details') 
    else:
        form = PersonalDetailsForm()
        return render(request,'forms/personal_details.html',{
            'form':form,
        })
@login_required(login_url='dologin')
def update_personal_details_view(request,id):
    if request.method == 'POST':
        personal_details = PersonalDetails.objects.get(pk=id)
        form = UpdatePersonalDetailsForm(request.POST,request.FILES,instance=personal_details)
        if form.is_valid():
            profile_pic = form.cleaned_data.get('profile_pic')
            personal_details.phone_number = request.POST['phone_number']
            personal_details.city = request.POST['city']
            personal_details.postal_code = request.POST['postal_code']
            personal_details.province = request.POST['province']
            personal_details.save()
            messages.info(request, 'You have successfully updated your personal details.')
            return redirect('index')
        else:
            messages.info(request, 'You already have an personal details.')
            return redirect('update_personal_details',id) 
    else:
        personal_details = PersonalDetails.objects.get(pk=id)
        form = UpdatePersonalDetailsForm(instance=personal_details)
        return render(request,'forms/update_personal_details.html',{
            'form':form,
            'personal_details':personal_details,
        })
@login_required(login_url='dologin')
def delete_personal_details_view(request,id):
    info = PersonalDetails.objects.get(pk=id)
    info.delete()
    messages.info(request, 'You have successfully deleted your personal details.')
    return redirect('index')

@login_required(login_url='dologin')
def education_view(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)  
        if form.is_valid():
            user = request.user
            school_name = form.cleaned_data['school_name']
            school_address = form.cleaned_data['school_address']
            qualification = form.cleaned_data['qualification']
            field_of_study = form.cleaned_data['field_of_study']
            year_of_graduation = form.cleaned_data['year_of_graduation']
            educational_background = Education.objects.create(user=user,school_name=school_name,school_address=school_address,qualification=qualification,field_of_study=field_of_study,year_of_graduation=year_of_graduation)
            educational_background.save()
            return redirect('work-experience')
        else:
            messages.info(request, 'You already have an educational background.')
            return redirect('education')  
    else:
        form = EducationForm()
        return render(request,'forms/education.html',{
            'form':form,
        })
@login_required(login_url='dologin')
def update_education_view(request,id):
    if request.method == 'POST':
        educational_background = Education.objects.get(pk=id)
        form = EducationForm(request.POST,instance=educational_background)  
        if form.is_valid():
            educational_background.user = request.user
            educational_background.school_name = form.cleaned_data['school_name']
            educational_background.school_address = form.cleaned_data['school_address']
            educational_background.qualification = form.cleaned_data['qualification']
            educational_background.field_of_study = form.cleaned_data['field_of_study']
            educational_background.year_of_graduation = form.cleaned_data['year_of_graduation']
            educational_background.save()
            messages.info(request, 'You have successfully updated your educational background.')
            return redirect('index')
        else:
            return redirect('update_education',id)  
    else:
        educational_background = Education.objects.get(pk=id)
        form = EducationForm(instance=educational_background)
        return render(request,'forms/update_education.html',{
            'form':form,
            'educational_background':educational_background,
        })

@login_required(login_url='dologin')
def delete_education_view(request,id):
    education = Education.objects.get(pk=id)
    education.delete()
    messages.info(request, 'You have successfully deleted your educational background.')
    return redirect('index')
@login_required(login_url='dologin')  
def work_experience_view(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)  
        if form.is_valid():
            user = request.user
            job_title = form.cleaned_data['job_title']
            employer = form.cleaned_data['employer']
            city = form.cleaned_data['city']
            province = form.cleaned_data['province']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            currently_work_here = form.cleaned_data['currently_work_here']

            work_experience = WorkExperience.objects.create(user=user,job_title=job_title,employer=employer,city=city,province=province,start_date=start_date,end_date=end_date,currently_work_here=currently_work_here)
            work_experience.save()
            return redirect('skill')
        else:
            return redirect('work-experience')  
    else:
        form = WorkExperienceForm()
        return render(request,'forms/work_experience.html',{
            'form':form,
        })
@login_required(login_url='dologin')
def update_work_experience_view(request,id):
    if request.method == 'POST':
        work_experience = WorkExperience.objects.get(pk=id)
        form = WorkExperienceForm(request.POST,instance=work_experience)  
        if form.is_valid():
            work_experience.user = request.user
            work_experience.job_title = form.cleaned_data['job_title']
            work_experience.employer = form.cleaned_data['employer']
            work_experience.city = form.cleaned_data['city']
            work_experience.province = form.cleaned_data['province']
            work_experience.start_date = form.cleaned_data['start_date']
            work_experience.end_date = form.cleaned_data['end_date']
            work_experience.currently_work_here = form.cleaned_data['currently_work_here']
            work_experience.save()
            return redirect('index')
        else:
            return redirect('update_work_experience',id)  
    else:
        work_experience = WorkExperience.objects.get(pk=id)
        form = WorkExperienceForm(instance=work_experience)
        return render(request,'forms/update_work_experience.html',{
            'form':form,
            'work_experience':work_experience,
        })
@login_required(login_url='dologin')
def delete_work_experience_view(request,id):
    work_xp = WorkExperience.objects.get(pk=id)
    work_xp.delete()
    messages.info(request, 'Work experience deleted successfully.')
    return redirect('index')    
@login_required(login_url='dologin')
def skill_view(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)  
        if form.is_valid():
            user = request.user
            skill = form.cleaned_data['skill']

            skill = Skill.objects.create(user=user,skill=skill)
            skill.save()
            return redirect('language')
        else:
            #messages.info(request, 'You already have work experience.')
            return redirect('skills')  
    else:
        form = SkillForm()
        return render(request,'forms/skill.html',{
            'form':form,
        })
    

@login_required(login_url='dologin')
def update_skill_view(request,id):
    if request.method == 'POST':
        skill = Skill.objects.get(pk=id)
        form = SkillForm(request.POST,instance=skill)  
        if form.is_valid():
            skill.user = request.user
            skill.skill = form.cleaned_data['skill']
            skill.save()
            messages.info(request, 'Skill updated successfully.')
            return redirect('index')
        else:
            #messages.info(request, 'You already have work experience.')
            return redirect('update_skill',id)  
    else:
        skill = Skill.objects.get(pk=id)
        form = SkillForm(instance=skill)  
        return render(request,'forms/update_skill.html',{
            'form':form,
            'skill':skill,
        })
@login_required(login_url='dologin')    
def delete_skill_view(request,id):
    skill = Skill.objects.get(pk=id)
    skill.delete()
    messages.info(request, 'Skill deleted successfully.')
    return redirect('index') 
@login_required(login_url='dologin')
def language_view(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)  
        if form.is_valid():
            user = request.user
            language = form.cleaned_data['language']
            language_type = form.cleaned_data['language_type']
           
            language = Language.objects.create(user=user,language=language,language_type=language_type)
            language.save()
            return redirect('reference')
        else:
            #messages.info(request, 'You already have work experience.')
            return redirect('language')  
    else:
        form = LanguageForm()
        return render(request,'forms/language.html',{
            'form':form,
        })
@login_required(login_url='dologin')
def update_language_view(request,id):
    if request.method == 'POST':
        language = Language.objects.get(pk=id)
        form = LanguageForm(request.POST,instance=language)  
        if form.is_valid():
            language.user = request.user
            language.language = form.cleaned_data['language']
            language.language_type = form.cleaned_data['language_type']
            language.save()
            return redirect('index')
        else:
            #messages.info(request, 'You already have work experience.')
            return redirect('update_language',id)  
    else:
        language = Language.objects.get(pk=id)
        form = LanguageForm(instance=language)  
        return render(request,'forms/update_language.html',{
            'form':form,
            'languages':language,
        })

@login_required(login_url='dologin')
def delete_language_view(request,id):
    language = Education.objects.get(pk=id)
    language.delete()
    messages.info(request, 'Language deleted successfully.')
    return redirect('index') 
@login_required(login_url='dologin')
def summary_view(request):
    if request.method == 'POST':
        form = SummaryForm(request.POST)  
        if form.is_valid():
            user = request.user
            summary = form.cleaned_data['summary']

            summary = Summary.objects.create(user=user,summary=summary)
            summary.save()
            return redirect('resume-view')
        else:
            #messages.info(request, 'You already have work experience.')
            return redirect('summary')  
    else:
        form = SummaryForm()
        return render(request,'forms/summary.html',{
            'form':form,
        })
@login_required(login_url='dologin')
def update_summary_view(request,id):
    if request.method == 'POST':
        summary = Summary.objects.get(pk=id)
        form = SummaryForm(request.POST,instance=summary)  
        if form.is_valid():
            summary.user = request.user
            summary.summary = form.cleaned_data['summary']
            summary.save()
            return redirect('index')
        else:
            #messages.info(request, 'You already have work experience.')
            return redirect('update_summary',id)  
    else:
        summary = Summary.objects.get(pk=id)
        form = SummaryForm(instance=summary)  
        return render(request,'forms/update_summary.html',{
            'form':form,
            'summary':summary,
        })
@login_required(login_url='dologin')    
def delete_summary_view(request,id):
    summary = Summary.objects.get(pk=id)
    summary.delete()
    messages.info(request, 'Summary deleted successfully.')
    return redirect('index') 
@login_required(login_url='dologin')
def resume_view(request):
    template_path = 'core/resume.html'
    user = request.user
    personal_details = PersonalDetails.objects.filter(user=user).first()
    educational_background = Education.objects.filter(user=user).all()
    work_experience = WorkExperience.objects.filter(user=user).all()
    skill = Skill.objects.filter(user=user).all()
    languages = Language.objects.filter(user=user).all()
    summary = Summary.objects.filter(user=user).first()
    references = Reference.objects.filter(user=user).all()

    context = {
        'user':user,
        'personal_details':personal_details,
        'educational_backgrounds':educational_background,
        'work_experiences':work_experience,
        'skills':skill,
        'languages':languages,
        'summary':summary,
        'references':references,

    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="resume.pdf"' #'attachment; filename="resume.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required(login_url='dologin')
def reference_view(request):
    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            user = request.user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            relationship = form.cleaned_data['relationship']
            company = form.cleaned_data['company']
            email = form.cleaned_data['email']
            cellphone_number = form.cleaned_data['cellphone_number']
            reference = Reference.objects.create(user=user,first_name=first_name,last_name=last_name,relationship=relationship,company=company,email=email,cellphone_number=cellphone_number)
            reference.save()
            return redirect('summary') 
        else:
            return redirect('reference') 
    else:
        form = ReferenceForm()
        return render(request,'forms/reference.html',{
            'form':form,
        })


@login_required(login_url='dologin')
def delete_reference_view(request,id):
    reference = Reference.objects.get(pk=id)
    reference.delete()
    return redirect('index')


@login_required(login_url='dologin')
def update_reference_view(request,id):
    if request.method == 'POST':
        reference = Reference.objects.get(pk=id)
        form = ReferenceForm(request.POST,instance=reference)  
        if form.is_valid():
            reference.user = request.user
            reference.first_name = form.cleaned_data['first_name']
            reference.last_name = form.cleaned_data['last_name']
            reference.relationship = form.cleaned_data['relationship']
            reference.company = form.cleaned_data['company']
            reference.email = form.cleaned_data['email']
            reference.cellphone_number = form.cleaned_data['cellphone_number']
            reference.save()
            return redirect('index')
        else:
            #messages.info(request, 'You already have work experience.')
            return redirect('reference')  
    else:
        reference = Reference.objects.get(pk=id)
        form = ReferenceForm(instance=reference)  
        return render(request,'forms/update_reference.html',{
            'form':form,
            'reference':reference,
        })
