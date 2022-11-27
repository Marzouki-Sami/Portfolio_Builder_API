from rest_framework import serializers

from Portfolio_app.models import Users, CareerSummary, Biography, PhilosophyStatement, Professional_Accomplishments, \
    Awards_Honors, Certifications, Portfolio, Volunteering_community_service, References_Testimonials


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CareerSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerSummary
        fields = '__all__'


class PhilosophyStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhilosophyStatement
        fields = '__all__'


class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class Professional_AccomplishmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional_Accomplishments
        fields = '__all__'


class Awards_HonorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards_Honors
        fields = '__all__'


class CertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certifications
        fields = '__all__'


class Volunteering_community_serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteering_community_service
        fields = '__all__'


class References_TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = References_Testimonials
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
