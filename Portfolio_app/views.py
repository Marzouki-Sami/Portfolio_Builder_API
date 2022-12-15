from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import *
from .forms import CareerSummary, form_PhilosophyStatement, form_Biography, form_Professional_Accomplishments, \
    form_Awards_Honors, form_Certifications, form_Volunteering_community_service, form_References_Testimonials
from Portfolio_app.forms import form_carrersummary
from Portfolio_app.models import Portfolio, CareerSummary, PhilosophyStatement, Biography, Professional_Accomplishments, \
    Awards_Honors, Certifications, Volunteering_community_service, References_Testimonials, Users
from Portfolio_app.serializers import PortfolioSerializer, CareerSummarySerializer, PhilosophyStatementSerializer, \
    BiographySerializer, Professional_AccomplishmentsSerializer, Awards_HonorsSerializer, CertificationsSerializer, \
    Volunteering_community_serviceSerializer, References_TestimonialsSerializer, UserSerializer


@api_view(['GET', 'POST'])
def retrieve_or_add_user(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['PUT', 'PATCH', 'DELETE', 'GET'])
def update_or_delete_or_retrieve_user(request, id):
    try:
        user = Users.objects.get(pk=id)
    except Users.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)
    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data, status=200)
    elif request.method == 'PUT' or request.method == 'PATCH':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=200)
        return JsonResponse(user_serializer.errors, status=400)
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status=200)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['GET', 'POST'])
def retrieve_or_add_portfolio(request):
    if request.method == 'GET':
        portfolios = Portfolio.objects.all()
        if len(portfolios) == 0:
            return JsonResponse({'message': 'No portfolios found'}, status=204)
        portfolios_serializer = PortfolioSerializer(portfolios, many=True)
        return JsonResponse(portfolios_serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        portfolio_data = JSONParser().parse(request)
        portfolio_serializer = PortfolioSerializer(data=portfolio_data)
        if portfolio_serializer.is_valid():
            portfolio_serializer.save()
            return JsonResponse(portfolio_serializer.data, status=201)
        return JsonResponse(portfolio_serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def update_or_delete_or_retrieve_portfolio(request, portfolio_id):
    try:
        portfolio = Portfolio.objects.get(pk=portfolio_id)
    except Portfolio.DoesNotExist:
        return JsonResponse({'message': 'Portfolio not found'}, status=404)
    if request.method == 'GET':
        portfolio_serializer = PortfolioSerializer(portfolio)
        return JsonResponse(portfolio_serializer.data, status=200)
    elif request.method == 'PUT' or request.method == 'PATCH':
        portfolio_data = JSONParser().parse(request)
        portfolio_serializer = PortfolioSerializer(portfolio, data=portfolio_data)
        if portfolio_serializer.is_valid():
            portfolio_serializer.save()
            return JsonResponse(portfolio_serializer.data, status=200)
        return JsonResponse(portfolio_serializer.errors, status=400)
    elif request.method == 'DELETE':
        portfolio.delete()
        return JsonResponse({'message': 'Portfolio deleted successfully'}, status=200)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['POST'])
def add_careersummary(request):
    if request.method == 'POST':
        careersummary_data = JSONParser().parse(request)
        careersummary_serializer = CareerSummarySerializer(data=careersummary_data)
        if careersummary_serializer.is_valid():
            careersummary_serializer.save()
            return JsonResponse(careersummary_serializer.data, status=201)
        return JsonResponse(careersummary_serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def update_or_delete_or_retrieve_careersummary(request, careersummary_id):
    try:
        careersummary = CareerSummary.objects.get(pk=careersummary_id)
    except CareerSummary.DoesNotExist:
        return JsonResponse({'message': 'CareerSummary not found'}, status=404)
    if request.method == 'GET':
        careersummary_serializer = CareerSummarySerializer(careersummary)
        return JsonResponse(careersummary_serializer.data, status=200)
    elif request.method == 'PUT' or request.method == 'PATCH':
        careersummary_data = JSONParser().parse(request)
        careersummary_serializer = CareerSummarySerializer(careersummary, data=careersummary_data)
        if careersummary_serializer.is_valid():
            careersummary_serializer.save()
            return JsonResponse(careersummary_serializer.data, status=200)
        return JsonResponse(careersummary_serializer.errors, status=400)
    elif request.method == 'DELETE':
        careersummary.delete()
        return JsonResponse({'message': 'CareerSummary deleted successfully'}, status=200)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['POST'])
def add_philosophystatement(request):
    if request.method == 'POST':
        philosophystatement_data = JSONParser().parse(request)
        philosophystatement_serializer = PhilosophyStatementSerializer(data=philosophystatement_data)
        if philosophystatement_serializer.is_valid():
            philosophystatement_serializer.save()
            return JsonResponse(philosophystatement_serializer.data, status=201)
        return JsonResponse(philosophystatement_serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def update_or_delete_or_retrieve_PhilosophyStatement(request, PhilosophyStatement_id):
    try:
        philosophystatement = PhilosophyStatement.objects.get(pk=PhilosophyStatement_id)
    except PhilosophyStatement.DoesNotExist:
        return JsonResponse({'message': 'PhilosophyStatement not found'}, status=404)
    if request.method == 'GET':
        philosophystatement_serializer = PhilosophyStatementSerializer(philosophystatement)
        return JsonResponse(philosophystatement_serializer.data, status=200)
    elif request.method == 'PUT' or request.method == 'PATCH':
        philosophystatement_data = JSONParser().parse(request)
        philosophystatement_serializer = PhilosophyStatementSerializer(philosophystatement,
                                                                       data=philosophystatement_data)
        if philosophystatement_serializer.is_valid():
            philosophystatement_serializer.save()
            return JsonResponse(philosophystatement_serializer.data, status=200)
        return JsonResponse(philosophystatement_serializer.errors, status=400)
    elif request.method == 'DELETE':
        philosophystatement.delete()
        return JsonResponse({'message': 'PhilosophyStatement deleted successfully'}, status=200)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['POST'])
def add_biography(request):
    if request.method == 'POST':
        biography_data = JSONParser().parse(request)
        biography_serializer = BiographySerializer(data=biography_data)
        if biography_serializer.is_valid():
            biography_serializer.save()
            return JsonResponse(biography_serializer.data, status=201)
        return JsonResponse(biography_serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def update_or_delete_or_retrieve_biography(request, biography_id):
    try:
        biography = Biography.objects.get(pk=biography_id)
    except Biography.DoesNotExist:
        return JsonResponse({'message': 'Biography not found'}, status=404)
    if request.method == 'GET':
        biography_serializer = BiographySerializer(biography)
        return JsonResponse(biography_serializer.data, status=200)
    elif request.method == 'PUT' or request.method == 'PATCH':
        biography_data = JSONParser().parse(request)
        biography_serializer = BiographySerializer(biography, data=biography_data)
        if biography_serializer.is_valid():
            biography_serializer.save()
            return JsonResponse(biography_serializer.data, status=200)
        return JsonResponse(biography_serializer.errors, status=400)
    elif request.method == 'DELETE':
        biography.delete()
        return JsonResponse({'message': 'Biography deleted successfully'}, status=200)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['POST'])
def add_professional_accomplishments(request):
    if request.method == 'POST':
        professional_accomplishments_data = JSONParser().parse(request)
        professional_accomplishments_serializer = Professional_AccomplishmentsSerializer(
            data=professional_accomplishments_data)
        if professional_accomplishments_serializer.is_valid():
            professional_accomplishments_serializer.save()
            return JsonResponse(professional_accomplishments_serializer.data, status=201)
        return JsonResponse(professional_accomplishments_serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def update_or_delete_or_retrieve_professional_accomplishments(request, professional_accomplishments_id):
    try:
        professional_accomplishments = Professional_Accomplishments.objects.get(pk=professional_accomplishments_id)
    except Professional_Accomplishments.DoesNotExist:
        return JsonResponse({'message': 'Professional_Accomplishments not found'}, status=404)
    if request.method == 'GET':
        professional_accomplishments_serializer = Professional_AccomplishmentsSerializer(professional_accomplishments)
        return JsonResponse(professional_accomplishments_serializer.data, status=200)
    elif request.method == 'PUT' or request.method == 'PATCH':
        professional_accomplishments_data = JSONParser().parse(request)
        professional_accomplishments_serializer = Professional_AccomplishmentsSerializer(professional_accomplishments,
                                                                                         data=professional_accomplishments_data)
        if professional_accomplishments_serializer.is_valid():
            professional_accomplishments_serializer.save()
            return JsonResponse(professional_accomplishments_serializer.data, status=200)
        return JsonResponse(professional_accomplishments_serializer.errors, status=400)
    elif request.method == 'DELETE':
        professional_accomplishments.delete()
        return JsonResponse({'message': 'Professional_Accomplishments deleted successfully'}, status=200)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['POST'])
def add_awards_honors(request):
    if request.method == 'POST':
        awards_honors_data = JSONParser().parse(request)
        awards_honors_serializer = Awards_HonorsSerializer(data=awards_honors_data)
        if awards_honors_serializer.is_valid():
            awards_honors_serializer.save()
            return JsonResponse(awards_honors_serializer.data, status=201)
        return JsonResponse(awards_honors_serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def update_or_delete_or_retrieve_Awards_Honors(request, awards_honors_id):
    try:
        awards_honors = Awards_Honors.objects.get(pk=awards_honors_id)
    except Awards_Honors.DoesNotExist:
        return JsonResponse({'message': 'Awards_Honors not found'}, status=404)
    if request.method == 'GET':
        awards_honors_serializer = Awards_HonorsSerializer(awards_honors)
        return JsonResponse(awards_honors_serializer.data, status=200)
    elif request.method == 'PUT' or request.method == 'PATCH':
        awards_honors_data = JSONParser().parse(request)
        awards_honors_serializer = Awards_HonorsSerializer(awards_honors, data=awards_honors_data)
        if awards_honors_serializer.is_valid():
            awards_honors_serializer.save()
            return JsonResponse(awards_honors_serializer.data, status=200)
        return JsonResponse(awards_honors_serializer.errors, status=400)
    elif request.method == 'DELETE':
        awards_honors.delete()
        return JsonResponse({'message': 'Awards_Honors deleted successfully'}, status=200)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['POST'])
def add_certifications(request):
    if request.method == 'POST':
        certifications_data = JSONParser().parse(request)
        certifications_serializer = CertificationsSerializer(data=certifications_data)
        if certifications_serializer.is_valid():
            certifications_serializer.save()
            return JsonResponse(certifications_serializer.data, status=201)
        return JsonResponse(certifications_serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def update_or_delete_or_retrieve_certifications(request, certifications_id):
    try:
        certifications = Certifications.objects.get(pk=certifications_id)
    except Certifications.DoesNotExist:
        return JsonResponse({'message': 'Certifications not found'}, status=404)
    if request.method == 'GET':
        certifications_serializer = CertificationsSerializer(certifications)
        return JsonResponse(certifications_serializer.data, status=200)
    elif request.method == 'PUT' or request.method == 'PATCH':
        certifications_data = JSONParser().parse(request)
        certifications_serializer = CertificationsSerializer(certifications, data=certifications_data)
        if certifications_serializer.is_valid():
            certifications_serializer.save()
            return JsonResponse(certifications_serializer.data, status=200)
        return JsonResponse(certifications_serializer.errors, status=400)
    elif request.method == 'DELETE':
        certifications.delete()
        return JsonResponse({'message': 'Certifications deleted successfully'}, status=200)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['POST'])
def add_volunteering_community_service(request):
    if request.method == 'POST':
        volunteering_community_service_data = JSONParser().parse(request)
        volunteering_community_service_serializer = Volunteering_community_serviceSerializer(
            data=volunteering_community_service_data)
        if volunteering_community_service_serializer.is_valid():
            volunteering_community_service_serializer.save()
            return JsonResponse(volunteering_community_service_serializer.data, status=201)
        return JsonResponse(volunteering_community_service_serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def update_or_delete_or_retrieve_volunteering_community_service(request, volunteering_community_service_id):
    try:
        volunteering_community_service = Volunteering_community_service.objects.get(
            pk=volunteering_community_service_id)
    except Volunteering_community_service.DoesNotExist:
        return JsonResponse({'message': 'Volunteering_community_service not found'}, status=404)
    if request.method == 'GET':
        volunteering_community_service_serializer = Volunteering_community_serviceSerializer(
            volunteering_community_service)
        return JsonResponse(volunteering_community_service_serializer.data, status=200)
    elif request.method == 'PUT' or request.method == 'PATCH':
        volunteering_community_service_data = JSONParser().parse(request)
        volunteering_community_service_serializer = Volunteering_community_serviceSerializer(
            volunteering_community_service, data=volunteering_community_service_data)
        if volunteering_community_service_serializer.is_valid():
            volunteering_community_service_serializer.save()
            return JsonResponse(volunteering_community_service_serializer.data, status=200)
        return JsonResponse(volunteering_community_service_serializer.errors, status=400)
    elif request.method == 'DELETE':
        volunteering_community_service.delete()
        return JsonResponse({'message': 'Volunteering_community_service deleted successfully'}, status=200)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['POST'])
def add_references_testimonials(request):
    if request.method == 'POST':
        references_testimonials_data = JSONParser().parse(request)
        references_testimonials_serializer = References_TestimonialsSerializer(data=references_testimonials_data)
        if references_testimonials_serializer.is_valid():
            references_testimonials_serializer.save()
            return JsonResponse(references_testimonials_serializer.data, status=201)
        return JsonResponse(references_testimonials_serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def update_or_delete_or_retrieve_references_testimonials(request, references_testimonials_id):
    try:
        references_testimonials = References_Testimonials.objects.get(pk=references_testimonials_id)
    except References_Testimonials.DoesNotExist:
        return JsonResponse({'message': 'References_Testimonials not found'}, status=404)
    if request.method == 'GET':
        references_testimonials_serializer = References_TestimonialsSerializer(references_testimonials)
        return JsonResponse(references_testimonials_serializer.data, status=200)
    elif request.method == 'PUT' or request.method == 'PATCH':
        references_testimonials_data = JSONParser().parse(request)
        references_testimonials_serializer = References_TestimonialsSerializer(references_testimonials,
                                                                               data=references_testimonials_data)
        if references_testimonials_serializer.is_valid():
            references_testimonials_serializer.save()
            return JsonResponse(references_testimonials_serializer.data, status=200)
        return JsonResponse(references_testimonials_serializer.errors, status=400)
    elif request.method == 'DELETE':
        references_testimonials.delete()
        return JsonResponse({'message': 'References_Testimonials deleted successfully'}, status=200)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


def createCareerSummary(request):
    data = CareerSummary.objects.all()

    form = form_carrersummary()

    if request.method == 'POST':
        form = form_carrersummary(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
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
            return redirect('index')
    context = {'form': form}
    return render(request, 'Career Summary/CareerSummaryUpdatePage.html', context)


def deleteCareerSummary(request, pk):
    data = CareerSummary.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('index')
    context = {'item': data}
    return render(request, 'Career Summary/CareerSummaryDeletePage.html', context)


def createPhilosophyStatement(request):

    data = PhilosophyStatement.objects.all()

    form = form_PhilosophyStatement()

    if request.method == 'POST':
        form = form_PhilosophyStatement(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
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
            return redirect('index')
    context = {'form': form}
    return render(request, 'Philosophy Statement/PhilosophyStatementUpdatePage.html', context)


def deletePhilosophyStatement(request, pk):
    data = PhilosophyStatement.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('index')
    context = {'item': data}
    return render(request, 'Philosophy Statement/PhilosophyStatementDeletePage.html', context)


def createBiography(request):

    data = Biography.objects.all()

    form = form_Biography()

    if request.method == 'POST':
        form = form_Biography(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
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
            return redirect('index')
    context = {'form': form}
    return render(request, 'Biography/BiographyUpdatePage.html', context)


def deleteBiography(request, pk):
    data = Biography.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('index')
    context = {'item': data}
    return render(request, 'Biography/BiographyDeletePage.html', context)


def createProfessional_Accomplishments(request):

    data = Professional_Accomplishments.objects.all()

    form = form_Professional_Accomplishments()

    if request.method == 'POST':
        form = form_Professional_Accomplishments(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
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
            return redirect('index')
    context = {'form': form}
    return render(request, 'Professional Accomplishments/Professional_AccomplishmentsUpdatePage.html', context)


def deleteProfessional_Accomplishments(request, pk):
    data = Professional_Accomplishments.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('index')
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
            return redirect('index')
    context = {'form': form, 'list_award_honors': award_honors}

    return render(request, 'Awards And Honors/Awards_HonorsPage.html', context)


def createCertifications(request):

    data = Certifications.objects.all()

    form = form_Certifications()

    if request.method == 'POST':
        form = form_Certifications(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
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
            return redirect('index')
    context = {'form': form}
    return render(request, 'Certifications/CertificationsUpdatePage.html', context)


def deleteCertifications(request, pk):
    data = Certifications.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('index')
    context = {'item': data}
    return render(request, 'Certifications/CertificationsDeletePage.html', context)


def createVolunteering_community_service(request):

    data = Volunteering_community_service.objects.all()

    form = form_Volunteering_community_service()

    if request.method == 'POST':
        form = form_Volunteering_community_service(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
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
            return redirect('index')
    context = {'form': form}
    return render(request, 'Volunteering community service/Volunteering_community_serviceUpdatePage.html', context)


def deleteVolunteering_community_service(request, pk):
    data = Volunteering_community_service.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('index')
    context = {'item': data}
    return render(request, 'Volunteering community service/Volunteering_community_serviceDeletePage.html', context)


def createReferences_Testimonials(request):

    data = References_Testimonials.objects.all()

    form = form_References_Testimonials()

    if request.method == 'POST':
        form = form_References_Testimonials(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
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
            return redirect('index')
    context = {'form': form}
    return render(request, 'References Testimonials/References_TestimonialsUpdatePage.html', context)


def deleteReferences_Testimonials(request, pk):
    data = References_Testimonials.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('index')
    context = {'item': data}
    return render(request, 'References Testimonials/References_TestimonialsDeletePage.html', context)


def affAward_Honors(request):
    award_honors = Awards_Honors.objects.all()
    context = {'list_award_honors': award_honors}
    return render(request, 'Awards And Honors/Awards_HonorsPage.html', context)


def updateAwards_Honors(request, pk):
    award_honors = Awards_Honors.objects.get(id=pk)
    form = form_Awards_Honors(instance=award_honors)

    if request.method == 'POST':
        form = form_Awards_Honors(request.POST, instance=award_honors)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}

    return render(request, 'Awards And Honors/Awards_HonorsUpdatePage.html', context)


def deleteAwards_Honors(request, pk):
    award_honors = Awards_Honors.objects.get(id=pk)
    if request.method == 'POST':
        award_honors.delete()
        return redirect('Awards_HonorsPage.html')
    return render(request, 'Awards And Honors/Awards_HonorsDeletePage.html', {'item': award_honors})


def index(request):
    return render(request, 'index.html')
