from rest_framework import serializers
from tracker.models import Company, User, Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField()
    logs = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = '__all__'

    def get_employees(self, obj):
        employees = obj.user_set.all()
        serializer = UserSerializer(employees, many = True)

        return serializer.data

    def get_logs(self, obj):
        logs = obj.log_set.all()
        serializer = LogSerializer(logs, many = True)

        return serializer.data