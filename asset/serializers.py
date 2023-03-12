from rest_framework import serializers
from asset.models import Company,Employee,Device,DeviceLog

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'user', 'company']



class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'serial_number', 'current_employee']



class DeviceLogSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(source='device.name', read_only=True)
    employee_name = serializers.CharField(source='employee.name', read_only=True)

    class Meta:
        model = DeviceLog
        fields = ['id', 'device', 'employee', 'checked_out', 'checked_in', 'condition']
