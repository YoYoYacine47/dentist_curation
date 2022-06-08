from django.contrib import admin
from .models import (Document, Visit, Patient, ProblemCatalog, ProblemDetected,
                     Tooth, Treatment, TreatmentSteps, VisitHistory, VisitStatus, Step)
# Register your models here.
admin.site.register(Document)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(ProblemCatalog)
admin.site.register(ProblemDetected)
admin.site.register(Tooth)
admin.site.register(Treatment)
admin.site.register(TreatmentSteps)
admin.site.register(VisitHistory)
admin.site.register(VisitStatus)
admin.site.register(Step)
