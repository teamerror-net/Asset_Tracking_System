from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Company'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    class Meta:
        verbose_name_plural = 'Employee'
    user = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Device(models.Model):
    class Meta:
        verbose_name_plural = 'Device'
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    company = models.ForeignKey(Company,null=True, blank=True, on_delete=models.CASCADE)
    current_employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    class Meta:
        verbose_name_plural = 'Device Log'
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    company = models.ForeignKey(Company,null=True, blank=True, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out = models.DateTimeField()
    checked_in = models.DateTimeField(null=True, blank=True)
    condition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.device} - {self.employee}"

