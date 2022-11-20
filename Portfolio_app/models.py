import django
from django.db import models


relationship = (
    ('company', 'company'),
    ('university', 'university'),
    ('client', 'client'),
)

title_8 = (
    ('Transcript', 'Transcript'),
    ('Certificate', 'Certificate'),
    ('Diploma', 'Diploma'),
    ('license', 'license'),
)


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False, blank=False, default='')
    password = models.CharField(max_length=50, null=False, blank=False, default='')
    personal_email = models.CharField(unique=True, max_length=50, null=False, blank=False, default='')
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


class careerSummary(models.Model):
    id = models.AutoField(primary_key=True)
    summary = models.TextField()

    def __str__(self):
        return self.summary

    class Meta:
        db_table = 'Career Summary'


class PhilosophyStatement(models.Model):
    id = models.AutoField(primary_key=True)
    statement = models.TextField()

    def __str__(self):
        return self.statement

    class Meta:
        db_table = 'Philosophy Statement'


class Biography(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    personal_website = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Biography'


class Professional_Accomplishments(models.Model):
    id = models.AutoField(primary_key=True)
    accomplishment = models.TextField()
    category = models.CharField(max_length=50, choices=relationship, blank=False, null=False, default='')
    proof_img = models.ImageField(null=True, blank=True)
    proof_pdf = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.accomplishment

    class Meta:
        db_table = 'Professional Accomplishments'


class Awards_Honors(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False, default='')
    recognition_level = models.CharField(max_length=50, null=False, blank=False, default='')
    date = models.DateField()
    proof_img = models.ImageField(null=True, blank=True)
    proof_pdf = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Awards and Honors'


class certifications(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False, default='', choices=title_8)
    link = models.URLField()
    discrition = models.TextField(max_length=500, null=False, blank=False, default='')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'certifications'


class Volunteering_community_service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False, default='')
    description = models.TextField()
    date_deb = models.DateField(null=False, blank=False, default=django.utils.timezone.now)
    date_fin = models.DateField(null=False, blank=False, default=django.utils.timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Volunteering and community service'


class References_Testimonials(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False, default='')
    email = models.EmailField()
    phone = models.IntegerField()
    relationship = models.TextField(choices=relationship, null=False, blank=False, default='')
    strengths = models.TextField()
    abilities = models.TextField()
    experience = models.TextField()
    recommendation_letter = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'References and Testimonials'


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False, default='')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    career_summary = models.ForeignKey(careerSummary, on_delete=models.CASCADE)
    philosophy_statement = models.ForeignKey(PhilosophyStatement, on_delete=models.CASCADE)
    biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
    professional_accomplishments = models.ForeignKey(Professional_Accomplishments, on_delete=models.CASCADE)
    awards_honors = models.ForeignKey(Awards_Honors, on_delete=models.CASCADE)
    certifications = models.ForeignKey(certifications, on_delete=models.CASCADE)
    volunteering_community_service = models.ForeignKey(Volunteering_community_service, on_delete=models.CASCADE)
    references_testimonials = models.ForeignKey(References_Testimonials, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Portfolio'
