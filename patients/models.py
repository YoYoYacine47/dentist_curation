from django.db import models
from django.urls import reverse
from clinics.models import Dentist
from locations.models import Commune
# Create your models here.


GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
)


class Patient(models.Model):

    card_id = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.BooleanField(choices=GENDER_CHOICES)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=20)
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='patients', default='no_picture.png')

    def __str__(self):
        return self.card_id

    def get_absolute_url(self):
        return reverse("Patient_detail", kwargs={"pk": self.pk})


class VisitStatus(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("VisitStatus_detail", kwargs={"pk": self.pk})


class Visit(models.Model):

    timestamp = models.DateTimeField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.timestamp}'

    def get_absolute_url(self):
        return reverse("Visit_detail", kwargs={"pk": self.pk})


class VisitHistory(models.Model):

    timestamp = models.DateTimeField(null=True)
    status = models.ForeignKey(
        VisitStatus, on_delete=models.SET_NULL, null=True)
    visit = models.ForeignKey(Visit, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.timestamp

    def get_absolute_url(self):
        return reverse("VisitHistory_detail", kwargs={"pk": self.pk})


class Document(models.Model):

    description = models.TextField(max_length=5000)
    path = models.FileField(upload_to='docs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    visit = models.ForeignKey(Visit, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Document_detail", kwargs={"pk": self.pk})


class Step(models.Model):

    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Step_detail", kwargs={"pk": self.pk})


class Treatment(models.Model):

    name = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    final_step = models.ForeignKey(Step, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Treatment_detail", kwargs={"pk": self.pk})


class TreatmentSteps(models.Model):

    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return f'{self.order}'

    def get_absolute_url(self):
        return reverse("TreatmentSteps_detail", kwargs={"pk": self.pk})


class Tooth(models.Model):

    universal = models.CharField(max_length=250, unique=True)
    fdi = models.CharField(max_length=250, unique=True, null=True)
    palmer = models.CharField(max_length=250, unique=True, null=True)

    def __str__(self):
        return self.universal

    def get_absolute_url(self):
        return reverse("tooth_detail", kwargs={"pk": self.pk})


class ProblemCatalog(models.Model):

    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProblemCatalog_detail", kwargs={"pk": self.pk})


class ProblemDetected(models.Model):

    tooth = models.ForeignKey(
        Tooth, on_delete=models.SET_NULL, null=True, blank=True)
    problem = models.ForeignKey(
        ProblemCatalog, on_delete=models.SET_NULL, null=True)
    visit = models.ForeignKey(Visit, on_delete=models.SET_NULL, null=True)
    suggested = models.ForeignKey(
        Treatment, on_delete=models.SET_NULL, null=True, related_name='suggested')
    selected = models.ForeignKey(
        Treatment, on_delete=models.SET_NULL, null=True, related_name='selected')

    def __str__(self):
        return f'{self.id}'

    def get_absolute_url(self):
        return reverse("ProblemDetected_detail", kwargs={"pk": self.pk})
