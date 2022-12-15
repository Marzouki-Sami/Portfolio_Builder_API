from django import forms
from django.forms import ModelForm

from Portfolio_app.models import CareerSummary, PhilosophyStatement, Biography, Professional_Accomplishments, \
    Awards_Honors, Certifications, Volunteering_community_service, References_Testimonials, Users


class form_carrersummary(ModelForm):
    class Meta:
        model = CareerSummary
        fields = ['summary']


class form_PhilosophyStatement(ModelForm):
    class Meta:
        model = PhilosophyStatement
        fields = ['statement']


class form_Biography(ModelForm):
    class Meta:
        model = Biography
        fields = ['email', 'personal_website', 'linkedin', 'github', 'twitter', 'facebook', 'instagram', 'description']


class form_Professional_Accomplishments(ModelForm):
    class Meta:
        model = Professional_Accomplishments
        fields = ['accomplishment', 'category', 'proof_img', 'proof_pdf']


class form_Awards_Honors(ModelForm):
    class Meta:
        model = Awards_Honors
        fields = ['title', 'recognition_level', 'date', 'proof_img', 'proof_pdf']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }


class form_Certifications(ModelForm):
    class Meta:
        model = Certifications
        fields = ['title', 'link', 'description']


class form_Volunteering_community_service(ModelForm):
    class Meta:
        model = Volunteering_community_service
        fields = ['title', 'description', 'date_deb', 'date_fin']
        widgets = {
            'date_deb': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'date_fin': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }


class form_References_Testimonials(ModelForm):
    class Meta:
        model = References_Testimonials
        fields = ['name', 'email', 'phone', 'relationship', 'strengths', 'abilities', 'experience', 'recommendation_letter']


class form_User(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']
