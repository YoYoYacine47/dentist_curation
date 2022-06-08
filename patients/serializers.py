from rest_framework import serializers
from .models import ProblemDetected


class ProblemDetectedSerializer(serializers.ModelSerializer):

    problem = serializers.SerializerMethodField(read_only=True)
    tooth = serializers.SerializerMethodField(read_only=True)
    suggested = serializers.SerializerMethodField(read_only=True)
    selected = serializers.SerializerMethodField(read_only=True)
    selected_final_step = serializers.SerializerMethodField(read_only=True)
    suggested_final_step = serializers.SerializerMethodField(read_only=True)
    visit_time = serializers.SerializerMethodField(read_only=True)
    visit_date = serializers.SerializerMethodField(read_only=True)
    patient_id = serializers.SerializerMethodField(read_only=True)
    patient_commune = serializers.SerializerMethodField(read_only=True)
    patient_daira = serializers.SerializerMethodField(read_only=True)
    patient_wilaya = serializers.SerializerMethodField(read_only=True)
    dentist_id = serializers.SerializerMethodField(read_only=True)
    clinic_id = serializers.SerializerMethodField(read_only=True)
    clinic_name = serializers.SerializerMethodField(read_only=True)
    clinic_commune = serializers.SerializerMethodField(read_only=True)
    clinic_wilaya = serializers.SerializerMethodField(read_only=True)
    clinic_daira = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProblemDetected
        fields = [
            'problem',
            'tooth',
            'suggested',
            'selected',
            'selected_final_step',
            'suggested_final_step',
            'visit_time',
            'visit_date',
            'patient_id',
            'patient_commune',
            'patient_daira',
            'patient_wilaya',
            'dentist_id',
            'clinic_id',
            'clinic_name',
            'clinic_commune',
            'clinic_daira',
            'clinic_wilaya',
        ]

    def get_problem(self, obj):
        return obj.problem.name

    def get_tooth(self, obj):
        if not obj.tooth:
            return None
        return obj.tooth.universal

    def get_selected(self, obj):
        return obj.selected.name

    def get_suggested(self, obj):
        return obj.suggested.name

    def get_selected_final_step(self, obj):
        return obj.selected.final_step.name

    def get_suggested_final_step(self, obj):
        return obj.suggested.final_step.name

    def get_visit_time(self, obj):
        return obj.visit.timestamp.time()

    def get_visit_date(self, obj):
        return obj.visit.timestamp.date()

    def get_patient_id(self, obj):
        return obj.visit.patient.id

    def get_patient_commune(self, obj):
        return obj.visit.patient.commune.name

    def get_patient_daira(self, obj):
        return obj.visit.patient.commune.daira.name

    def get_patient_wilaya(self, obj):
        return obj.visit.patient.commune.daira.wilaya.name

    def get_dentist_id(self, obj):
        return obj.visit.dentist.id

    def get_clinic_id(self, obj):
        return obj.visit.dentist.clinic.id

    def get_clinic_name(self, obj):
        return obj.visit.dentist.clinic.name

    def get_clinic_commune(self, obj):
        return obj.visit.dentist.clinic.commune.name

    def get_clinic_daira(self, obj):
        return obj.visit.dentist.clinic.commune.daira.name

    def get_clinic_wilaya(self, obj):
        return obj.visit.dentist.clinic.commune.daira.wilaya.name
