from django.urls import path

from Portfolio_app import views

urlpatterns = [

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

    # path('login/', views.login, name="login"),
    path('', views.index, name="index"),
]
