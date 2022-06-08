from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from patients.models import Patient, ProblemDetected, Tooth, Visit

# Create your views here.


def test(request):
    problems = {}
    tooth = request.POST['tooth']
    patient_id = request.POST['patient']
    patient = Patient.objects.get(id=patient_id)
    visits = Visit.objects.filter(patient=patient.id)
    problems = ProblemDetected.objects.filter(visit__in=visits, tooth=tooth)
    print(problems)
    return render(request, 'patients/tooth.html', {"tooth_problems": problems, "tooth": tooth})


@login_required(login_url='/clinic/login')
def index(request):

    context = {}
    visits = None
    patient = None
    problems = None
    otherPB = None

    if request.method == 'POST':

        card_id = request.POST['card_id']

        patient = Patient.objects.filter(card_id=card_id).first()

        if not patient:
            messages.info(request, 'there is no user with this card Id !!')
        else:
            visits = Visit.objects.filter(patient=patient.id)
            if not visits:
                messages.info(request, 'this patient has no data !!')
            else:
                problems = ProblemDetected.objects.filter(visit__in=visits)
                otherPB = ProblemDetected.objects.filter(
                    visit__in=visits, tooth=None)
        context = {
            'patient': patient,
            'visits': visits,
            'problems': problems,
            'otherPB': otherPB,
        }

    return render(request, 'patients/index.html', context=context)
