from rest_framework import serializers
from .models import Clinic


class ClinicSerializer(serializers.ModelSerializer):

    commune = serializers.SerializerMethodField(read_only=True)
    wilaya = serializers.SerializerMethodField(read_only=True)
    daira = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Clinic
        fields = [
            'id',
            'name',
            'address',
            'email',
            'phone',
            'commune',
            'daira',
            'wilaya',
        ]

    def get_commune(self, obj):
        return obj.commune.name

    def get_daira(self, obj):
        return obj.commune.daira.name

    def get_wilaya(self, obj):
        return obj.commune.daira.wilaya.name
