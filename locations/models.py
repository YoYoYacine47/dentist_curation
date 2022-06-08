from django.db import models
from django.urls import reverse

# Create your models here.


class Wilaya(models.Model):

    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("Daira_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Daira(models.Model):
    name = models.CharField(max_length=100)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Daira_detail", kwargs={"pk": self.pk})


class Commune(models.Model):

    name = models.CharField(max_length=100)
    daira = models.ForeignKey(Daira, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Commune_detail", kwargs={"pk": self.pk})
