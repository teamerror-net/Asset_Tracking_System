from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Company, Employee, Device, DeviceLog
import datetime


def Home(request):
    return HttpResponse('Working...')

def company_list(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'company_list.html', context)

def employee_list(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    employees = company.employees.all()
    context = {'company': company, 'employees': employees}
    return render(request, 'employee_list.html', context)

def device_list(request):
    devices = Device.objects.all()
    context = {'devices': devices}
    return render(request, 'device_list.html', context)

def device_checkout(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    employee = get_object_or_404(Employee, user=request.user)
    device.current_employee = employee
    device.save()
    device_log = DeviceLog(device=device, employee=employee, checked_out=datetime.now(), condition=request.POST['condition'])
    device_log.save()
    return HttpResponse("Device checked out successfully.")

def device_checkin(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    employee = device.current_employee
    device.current_employee = None
    device.save()
    device_log = get_object_or_404(DeviceLog, device=device, employee=employee, checked_in=None)
    device_log.checked_in = datetime.now()
    device_log.condition = request.POST['condition']
    device_log.save()
    return HttpResponse("Device checked in successfully.")
