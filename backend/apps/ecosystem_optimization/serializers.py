from rest_framework import serializers
from .models import OptimizationProposal, PerformanceMetric

class OptimizationProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptimizationProposal
        fields = '__all__'

class PerformanceMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceMetric
        fields = '__all__'
