from django.contrib import auth, messages
from django.shortcuts import render, redirect

from Portfolio_app.forms import form_carrersummary
from Portfolio_app.models import CareerSummary, PhilosophyStatement, Biography, Professional_Accomplishments, \
    Awards_Honors, Certifications, Volunteering_community_service, References_Testimonials
from .forms import form_PhilosophyStatement, form_Biography, form_Professional_Accomplishments, \
    form_Awards_Honors, form_Certifications, form_Volunteering_community_service, form_References_Testimonials, \
    form_User


def createCareerSummary(request):
    data = CareerSummary.objects.all()

    form = form_carrersummary()

    if request.method == 'POST':
        form = form_carrersummary(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_career_summary')
    context = {'form': form,
               'data': data}

    return render(request, 'Career Summary/CareerSummaryPage.html', context)


def updateCareerSummary(request, pk):
    data = CareerSummary.objects.get(id=pk)
    form = form_carrersummary(instance=data)

    if request.method == 'POST':
        form = form_carrersummary(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('create_career_summary')
    context = {'form': form}
    return render(request, 'Career Summary/CareerSummaryUpdatePage.html', context)


def deleteCareerSummary(request, pk):
    data = CareerSummary.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('create_career_summary')
    context = {'item': data}
    return render(request, 'Career Summary/CareerSummaryDeletePage.html', context)


def createPhilosophyStatement(request):

    data = PhilosophyStatement.objects.all()

    form = form_PhilosophyStatement()

    if request.method == 'POST':
        form = form_PhilosophyStatement(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_philosophy_statement')
    context = {'form': form,
               'data': data}

    return render(request, 'Philosophy Statement/PhilosophyStatementPage.html', context)


def updatePhilosophyStatement(request, pk):
    data = PhilosophyStatement.objects.get(id=pk)
    form = form_PhilosophyStatement(instance=data)

    if request.method == 'POST':
        form = form_PhilosophyStatement(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('create_philosophy_statement')
    context = {'form': form}
    return render(request, 'Philosophy Statement/PhilosophyStatementUpdatePage.html', context)


def deletePhilosophyStatement(request, pk):
    data = PhilosophyStatement.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('create_philosophy_statement')
    context = {'item': data}
    return render(request, 'Philosophy Statement/PhilosophyStatementDeletePage.html', context)


def createBiography(request):

    data = Biography.objects.all()

    form = form_Biography()

    if request.method == 'POST':
        form = form_Biography(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_biography')
    context = {'form': form,
               'data': data}

    return render(request, 'Biography/BiographyPage.html', context)


def updateBiography(request, pk):
    data = Biography.objects.get(id=pk)
    form = form_Biography(instance=data)

    if request.method == 'POST':
        form = form_Biography(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('create_biography')
    context = {'form': form}
    return render(request, 'Biography/BiographyUpdatePage.html', context)


def deleteBiography(request, pk):
    data = Biography.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('create_biography')
    context = {'item': data}
    return render(request, 'Biography/BiographyDeletePage.html', context)


def createProfessional_Accomplishments(request):

    data = Professional_Accomplishments.objects.all()

    form = form_Professional_Accomplishments()

    if request.method == 'POST':
        form = form_Professional_Accomplishments(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_professional_accomplishments')
    context = {'form': form,
               'data': data}

    return render(request, 'Professional Accomplishments/Professional_AccomplishmentsPage.html', context)


def updateProfessional_Accomplishments(request, pk):
    data = Professional_Accomplishments.objects.get(id=pk)
    form = form_Professional_Accomplishments(instance=data)

    if request.method == 'POST':
        form = form_Professional_Accomplishments(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('create_professional_accomplishments')
    context = {'form': form}
    return render(request, 'Professional Accomplishments/Professional_AccomplishmentsUpdatePage.html', context)


def deleteProfessional_Accomplishments(request, pk):
    data = Professional_Accomplishments.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('create_professional_accomplishments')
    context = {'item': data}
    return render(request, 'Professional Accomplishments/Professional_AccomplishmentsDeletePage.html', context)


def createAwards_Honors(request):
    award_honors = Awards_Honors.objects.all()
    context = {'list_award_honors': award_honors}

    form = form_Awards_Honors()

    if request.method == 'POST':
        form = form_Awards_Honors(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_awards_honors')
    context = {'form': form, 'list_award_honors': award_honors}

    return render(request, 'Awards And Honors/Awards_HonorsPage.html', context)


def updateAwards_Honors(request, pk):
    award_honors = Awards_Honors.objects.get(id=pk)
    form = form_Awards_Honors(instance=award_honors)

    if request.method == 'POST':
        form = form_Awards_Honors(request.POST, instance=award_honors)
        if form.is_valid():
            form.save()
            return redirect('create_awards_honors')
    context = {'form': form}

    return render(request, 'Awards And Honors/Awards_HonorsUpdatePage.html', context)


def deleteAwards_Honors(request, pk):
    award_honors = Awards_Honors.objects.get(id=pk)
    if request.method == 'POST':
        award_honors.delete()
        return redirect('create_awards_honors')
    return render(request, 'Awards And Honors/Awards_HonorsDeletePage.html', {'item': award_honors})



def createCertifications(request):

    data = Certifications.objects.all()

    form = form_Certifications()

    if request.method == 'POST':
        form = form_Certifications(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_certifications')
    context = {'form': form,
               'data': data}

    return render(request, 'Certifications/CertificationsPage.html', context)


def updateCertifications(request, pk):
    data = Certifications.objects.get(id=pk)
    form = form_Certifications(instance=data)

    if request.method == 'POST':
        form = form_Certifications(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('create_certifications')
    context = {'form': form}
    return render(request, 'Certifications/CertificationsUpdatePage.html', context)


def deleteCertifications(request, pk):
    data = Certifications.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('create_certifications')
    context = {'item': data}
    return render(request, 'Certifications/CertificationsDeletePage.html', context)


def createVolunteering_community_service(request):

    data = Volunteering_community_service.objects.all()

    form = form_Volunteering_community_service()

    if request.method == 'POST':
        form = form_Volunteering_community_service(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_volunteering_community_service')
    context = {'form': form,
               'data': data}

    return render(request, 'Volunteering community service/Volunteering_community_servicePage.html', context)


def updateVolunteering_community_service(request, pk):
    data = Volunteering_community_service.objects.get(id=pk)
    form = form_Volunteering_community_service(instance=data)

    if request.method == 'POST':
        form = form_Volunteering_community_service(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('create_volunteering_community_service')
    context = {'form': form}
    return render(request, 'Volunteering community service/Volunteering_community_serviceUpdatePage.html', context)


def deleteVolunteering_community_service(request, pk):
    data = Volunteering_community_service.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('create_volunteering_community_service')
    context = {'item': data}
    return render(request, 'Volunteering community service/Volunteering_community_serviceDeletePage.html', context)


def createReferences_Testimonials(request):

    data = References_Testimonials.objects.all()

    form = form_References_Testimonials()

    if request.method == 'POST':
        form = form_References_Testimonials(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_references_testimonials')
    context = {'form': form,
               'data': data}

    return render(request, 'References Testimonials/References_TestimonialsPage.html', context)


def updateReferences_Testimonials(request, pk):
    data = References_Testimonials.objects.get(id=pk)
    form = form_References_Testimonials(instance=data)

    if request.method == 'POST':
        form = form_References_Testimonials(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('create_references_testimonials')
    context = {'form': form}
    return render(request, 'References Testimonials/References_TestimonialsUpdatePage.html', context)


def deleteReferences_Testimonials(request, pk):
    data = References_Testimonials.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('create_references_testimonials')
    context = {'item': data}
    return render(request, 'References Testimonials/References_TestimonialsDeletePage.html', context)


def login(request):
    if request.method == 'POST':
        form_login = form_User(request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('login')


def index(request):
    return render(request, 'index.html')
