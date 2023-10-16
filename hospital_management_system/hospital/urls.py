from django.urls import path
from hospital import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient/add', views.patient_add, name='patient_add'),
    path('patient/list', views.patient_list, name='patient_list'),
    path('patient_detail/<int:id>', views.patient_detail, name='patient_detail'),
    path('patient_edit/<int:id>', views.patient_edit, name='patient_edit'),
    path('doctor/add', views.doctor_add, name='doctor_add'),
    path('doctor/details', views.doctor_detail, name='doctor_detail'),
    path('about_doctor/<int:id>', views.about_doctor, name='about_doctor'),
    path('doctor_edit/<int:id>', views.doctor_edit, name='doctor_edit'),
    path('add_appointment', views.add_appointment, name='add_appointment'),
    path('appointment_list', views.appointment_list, name='appointment_list'),
    path('appointment_detail/<int:id>', views.appointment_detail, name='appointment_detail'),
    path('appointment_edit/<int:id>', views.appointment_edit, name='appointment_edit'),
    path('appointment_cancel/<int:id>', views.appointment_cancel, name='appointment_cancel'),
    path('visit_patient', views.visit_patient, name='visit_patient'),
    path('visited_patient/<int:id>', views.visited_patient, name='visited_patient'),
    path('visit_pending', views.visit_pending, name='visit_pending'),
    path('room_allotment', views.roomallotment, name='room_allotment'),
    path('room_alloted', views.rooms_alloted, name='rooms_alloted'),\
    path('edit_room_allotment/<int:id>', views.edit_roomallotment, name='edit_room_allotment'),







    
]
