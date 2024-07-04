from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated

class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset() # 7 number line ke niye aslam ba parent ke inherit korlam
        # print(self.request.query_params)
        patient_id = self.request.query_params.get('patient_id')
        # print(patient_id)
        if patient_id:
            # ak jon patient er total koto gula appointment ase ta filter kora hocca
            queryset = queryset.filter(patient_id=patient_id)
        else:
            doctor_id = self.request.query_params.get('doctor_id')
            print(doctor_id)
            if doctor_id:
                # ak jon doctor er total koto gula appointment ase ta filter kora hocca
                queryset = queryset.filter(doctor_id=doctor_id)
        return queryset

