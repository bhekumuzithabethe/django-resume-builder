from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login_view,name='dologin'),
    path('logout/',views.logout_view,name='dologout'),

    path('sign-up/',views.create_user_view,name='sign-up'),
    path('update-user/',views.update_user_view,name='update-user'),
    path('accounts/',include('django.contrib.auth.urls')),

    path('index/',views.index_view,name='index'),

    path('personal-details/',views.personal_details_view,name='personal-details'),
    path('update-personal-details/<int:id>/',views.update_personal_details_view,name='update_personal_details'),
    path('delete-personal-details/<int:id>/',views.delete_personal_details_view,name='delete_personal_details'),

    path('education/',views.education_view,name='education'),
    path('update-education/<int:id>/',views.update_education_view,name='update_education'),
    path('delete-education/<int:id>/',views.delete_education_view,name='delete_education'),

    path('work-experience/',views.work_experience_view,name='work-experience'),
    path('update-work-experience/<int:id>/',views.update_work_experience_view,name='update_work_experience'),
    path('delete-work-experience/<int:id>/',views.delete_work_experience_view,name='delete_work_experience'),

    path('skill/',views.skill_view,name='skill'),
    path('update-skill/<int:id>/',views.update_skill_view,name='update_skill'),
    path('delete-skill/<int:id>/',views.delete_skill_view,name='delete_skill'),

    path('language/',views.language_view,name='language'),
    path('update-language/<int:id>/',views.update_language_view,name='update_language'),
    path('delete-language/<int:id>/',views.delete_language_view,name='delete_language'),

    path('summary/',views.summary_view,name='summary'),
    path('update-summary/<int:id>/',views.update_summary_view,name='update_summary'),
    path('delete-summary/<int:id>/',views.delete_summary_view,name='delete_summary'),

    path('reference/',views.reference_view,name='reference'),
    path('update-reference/<int:id>/',views.update_reference_view,name='update_reference'),
    path('delete-reference/<int:id>/',views.delete_reference_view,name='delete_reference'),


    path('view-resume/',views.resume_view,name='resume-view'),
]