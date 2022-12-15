from django.urls import path

from Portfolio_app import views

urlpatterns = [
    path('addcareersummary', views.add_careersummary),
    path('addphilosophystatement', views.add_philosophystatement),
    path('addbiography', views.add_biography),
    path('addprofessionalaccomplishments', views.add_professional_accomplishments),
    path('addawardshonors', views.add_awards_honors),
    path('addcertifications', views.add_certifications),
    path('addvolunteeringcommunityservice', views.add_volunteering_community_service),
    path('addreferencestestimonials', views.add_references_testimonials),
    path('addportfolio', views.retrieve_or_add_portfolio),
    path('adduser', views.retrieve_or_add_user),

    path('findcareersummary/<int:careersummary_id>', views.update_or_delete_or_retrieve_careersummary),
    path('findphilosophystatement/<int:philosophystatement_id>', views.update_or_delete_or_retrieve_PhilosophyStatement),
    path('findbiography/<int:biography_id>', views.update_or_delete_or_retrieve_biography),
    path('findprofessionalaccomplishments/<int:professionalaccomplishments_id>', views.update_or_delete_or_retrieve_professional_accomplishments),
    path('findawardshonors/<int:awardshonors_id>', views.update_or_delete_or_retrieve_Awards_Honors),
    path('findcertifications/<int:certifications_id>', views.update_or_delete_or_retrieve_certifications),
    path('findvolunteeringcommunityservice/<int:volunteeringcommunityservice_id>', views.update_or_delete_or_retrieve_volunteering_community_service),
    path('findreferencestestimonials/<int:referencestestimonials_id>', views.update_or_delete_or_retrieve_references_testimonials),
    path('findportfolio/<int:portfolio_id>', views.update_or_delete_or_retrieve_portfolio),
    path('finduser/<int:user_id>', views.update_or_delete_or_retrieve_user),

    path('upadatecareersummary/<int:careersummary_id>', views.update_or_delete_or_retrieve_careersummary),
    path('updatephilosophystatement/<int:philosophystatement_id>', views.update_or_delete_or_retrieve_PhilosophyStatement),
    path('updatebiography/<int:biography_id>', views.update_or_delete_or_retrieve_biography),
    path('updateprofessionalaccomplishments/<int:professionalaccomplishments_id>', views.update_or_delete_or_retrieve_professional_accomplishments),
    path('updateawardshonors/<int:awardshonors_id>', views.update_or_delete_or_retrieve_Awards_Honors),
    path('updatecertifications/<int:certifications_id>', views.update_or_delete_or_retrieve_certifications),
    path('updatevolunteeringcommunityservice/<int:volunteeringcommunityservice_id>', views.update_or_delete_or_retrieve_volunteering_community_service),
    path('updatereferencestestimonials/<int:referencestestimonials_id>', views.update_or_delete_or_retrieve_references_testimonials),
    path('updateportfolio/<int:portfolio_id>', views.update_or_delete_or_retrieve_portfolio),
    path('updateuser/<int:user_id>', views.update_or_delete_or_retrieve_user),

    path('deletecareersummary/<int:careersummary_id>', views.update_or_delete_or_retrieve_careersummary),
    path('deletephilosophystatement/<int:philosophystatement_id>', views.update_or_delete_or_retrieve_PhilosophyStatement),
    path('deletebiography/<int:biography_id>', views.update_or_delete_or_retrieve_biography),
    path('deleteprofessionalaccomplishments/<int:professionalaccomplishments_id>', views.update_or_delete_or_retrieve_professional_accomplishments),
    path('deleteawardshonors/<int:awardshonors_id>', views.update_or_delete_or_retrieve_Awards_Honors),
    path('deletecertifications/<int:certifications_id>', views.update_or_delete_or_retrieve_certifications),
    path('deletevolunteeringcommunityservice/<int:volunteeringcommunityservice_id>', views.update_or_delete_or_retrieve_volunteering_community_service),
    path('deletereferencestestimonials/<int:referencestestimonials_id>', views.update_or_delete_or_retrieve_references_testimonials),
    path('deleteportfolio/<int:portfolio_id>', views.update_or_delete_or_retrieve_portfolio),
    path('deleteuser/<int:user_id>', views.update_or_delete_or_retrieve_user),

    path('findallportfolio', views.retrieve_or_add_portfolio),
    path('findalluser', views.retrieve_or_add_user),




    path('createCareerSummary/', views.createCareerSummary, name="create_career_summary"),
    path('updateCareerSummary/<int:pk>', views.updateCareerSummary, name="update_career_summary"),
    path('deleteCareerSummary/<int:pk>', views.deleteCareerSummary, name="delete_career_summary"),

    path('createPhilosophyStatement/', views.createPhilosophyStatement, name="create_philosophy_statement"),
    path('updatePhilosophyStatement/<int:pk>', views.updatePhilosophyStatement, name="update_philosophy_statement"),
    path('deletePhilosophyStatement/<int:pk>', views.deletePhilosophyStatement, name="delete_philosophy_statement"),

    path('createBiography/', views.createBiography, name="create_biography"),
    path('updateBiography/<int:pk>', views.updateBiography, name="update_biography"),
    path('deleteBiography/<int:pk>', views.deleteBiography, name="delete_biography"),

    path('createProfessionalAccomplishments/', views.createProfessional_Accomplishments, name="create_professional_accomplishments"),
    path('updateProfessionalAccomplishments/<int:pk>', views.updateProfessional_Accomplishments, name="update_professional_accomplishments"),
    path('deleteProfessionalAccomplishments/<int:pk>', views.deleteProfessional_Accomplishments, name="delete_professional_accomplishments"),

    path('createAwardsHonors/', views.createAwards_Honors, name="create_awards_honors"),
    path('updateAwardsHonors/<int:pk>', views.updateAwards_Honors, name="award_honor_update"),
    path('deleteAwardsHonors/<int:pk>', views.deleteAwards_Honors, name="award_honor_delete"),

    path('createCertifications/', views.createCertifications, name="create_certifications"),
    path('updateCertifications/<int:pk>', views.updateCertifications, name="update_certifications"),
    path('deleteCertifications/<int:pk>', views.deleteCertifications, name="delete_certifications"),

    path('createVolunteeringCommunityService/', views.createVolunteering_community_service, name="create_volunteering_community_service"),
    path('updateVolunteeringCommunityService/<int:pk>', views.updateVolunteering_community_service, name="update_volunteering_community_service"),
    path('deleteVolunteeringCommunityService/<int:pk>', views.deleteVolunteering_community_service, name="delete_volunteering_community_service"),

    path('createReferencesTestimonials/', views.createReferences_Testimonials, name="create_references_testimonials"),
    path('updateReferencesTestimonials/<int:pk>', views.updateReferences_Testimonials, name="update_references_testimonials"),
    path('deleteReferencesTestimonials/<int:pk>', views.deleteReferences_Testimonials, name="delete_references_testimonials"),

    path('', views.index)
]
