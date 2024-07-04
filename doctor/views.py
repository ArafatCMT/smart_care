from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import pagination, filters

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    pagination_class = DoctorPagination


class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor =doctor_id)
        return queryset
        
        

class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] # authenticated user cara kau avabletime dakte parbe na, , import kora hoi ca 5 no line e
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]

class ReviewsForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        # print(request.query_params)
        if doctor_id:
            return queryset.filter(doctor = doctor_id)
        return queryset


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly] # ek jon authenticated user e shudu review dete parbe , import kora hoi ca 6 no line e
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_backends = [ReviewsForSpecificDoctor]

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     doctor_id = self.request.query_params.get('doctor_id')
    #     print(self.request.query_params)
    #     if doctor_id:
    #         queryset = queryset.filter(doctor_id=doctor_id)
    #     return queryset