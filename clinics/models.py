from audioop import reverse
from django.db import models
from locations.models import Commune
from django.contrib.auth.models import User

# Create your models here.


class Clinic(models.Model):

    name = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    commune = models.ForeignKey(Commune, null=True, on_delete=models.SET_NULL)
    address_len = models.FloatField(blank=True, null=True)
    address_let = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Establishment_detail", kwargs={"pk": self.pk})


class Dentist(models.Model):

    card_id = models.CharField(max_length=250, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, default="qw")
    clinic = models.ForeignKey(
        Clinic, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse("dentist_detail", kwargs={"pk": self.pk})
