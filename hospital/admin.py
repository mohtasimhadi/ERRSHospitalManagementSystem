from django.contrib import admin

# Register your models here.
from hospital.models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    pass


# create the Doctor class later
admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    pass


# create the Patient class later
admin.site.register(Patient, PatientAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    pass


# create the Appointment class later
admin.site.register(Appointment, AppointmentAdmin)


class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass


# create the PatientDischargeDetails class later
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)
