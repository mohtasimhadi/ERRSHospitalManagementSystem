"""hospitalmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),

    path('adminclick', views.adminclick_view),
    path('doctorclick', views.doctorclick_view),
    path('patientclick', views.patientclick_view),

    path('adminsignup', views.admin_signup_view),
    path('doctorsignup', views.doctor_signup_view,name=''),
    path('patientsignup', views.patient_signup_view),

    path('adminlogin', LoginView.as_view(template_name='')),
    path('doctorlogin', LoginView.as_view(template_name='')),
    path('patientlogin', LoginView.as_view(template_name='')),

    path('afterlogin', views.afterlogin_view, name=''),
    path('logout', LogoutView.as_view(template_name=''), name=''),


    path('admin-dashboard', views.admin_dashboard_view,name=''),

    path('admin-doctor', views.admin_doctor_view,name=''),
    path('admin-view-doctor', views.admin_view_doctor_view,name=''),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name=''),
    path('update-doctor/<int:pk>', views.update_doctor_view,name=''),
    path('admin-add-doctor', views.admin_add_doctor_view,name=''),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name=''),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name=''),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name=''),
    path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name=''),


    path('admin-patient', views.admin_patient_view,name=''),
    path('admin-view-patient', views.admin_view_patient_view,name=''),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name=''),
    path('update-patient/<int:pk>', views.update_patient_view,name=''),
    path('admin-add-patient', views.admin_add_patient_view,name=''),
    path('admin-approve-patient', views.admin_approve_patient_view,name=''),
    path('approve-patient/<int:pk>', views.approve_patient_view,name=''),
    path('reject-patient/<int:pk>', views.reject_patient_view,name=''),
    path('admin-discharge-patient', views.admin_discharge_patient_view,name=''),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name=''),
    path('download-pdf/<int:pk>', views.download_pdf_view,name=''),


    path('admin-appointment', views.admin_appointment_view,name=''),
    path('admin-view-appointment', views.admin_view_appointment_view,name=''),
    path('admin-add-appointment', views.admin_add_appointment_view,name=''),
    path('admin-approve-appointment', views.admin_approve_appointment_view,name=''),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name=''),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name=''),
]
]
