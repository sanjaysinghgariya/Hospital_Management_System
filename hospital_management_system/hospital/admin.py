from django.contrib import admin
from hospital import models

admin.site.register([models.specialization, models.Doctor, models.Patient, models.Appointment, models.Room_Info, models.RoomNumber, models.room_allotment])

