from django.db import models
import random
import string
import uuid 
class Patient(models.Model):
    patient_name = models.CharField(max_length=255, null=False, blank=False)#indian_names
    Date_of_birth = models.CharField(max_length=255)#dob_list
    Age = models.IntegerField()#age_list
    phone_number = models.IntegerField()#ten_digit_numbers
    Email = models.EmailField()#indian_gmail_addresses
    gender = models.CharField(max_length=255)
    Address = models.TextField()#indian_addresses
    def __str__(self):
        return self.patient_name 


class specialization(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
        STATUS = (('Available', 'Available'), ( 'Not Available' ,  'Not Available' ), ('On Leave', 'On Leave'))
        doctor_name = models.CharField(max_length=255)
        date_of_birth = models.CharField(max_length=255)
        specialization = models.ForeignKey(specialization, on_delete=models.CASCADE)
        experience = models.IntegerField()
        age = models.IntegerField()
        phone_nnumber = models.IntegerField()
        email =models.EmailField()
        gender = models.CharField(max_length=255)
        about_doctor = models.TextField()
        address = models.TextField()
        image = models.ImageField(upload_to='doctor_image')
        resume = models.FileField(upload_to='doctor_resume')
        status = models.CharField(max_length=50, choices=STATUS, default='Available')
        consultation_fee = models.IntegerField(default=1500)

        def __str__(self):
            return self.doctor_name
    

class Appointment(models.Model):
    APPOINTMENT_STATUSES = (
    ('Scheduled', 'Scheduled'),
    ('Confirmed', 'Confirmed'),
    ('Pending', 'Pending'),
    ('Cancelled', 'Cancelled'),
    ('Rescheduled', 'Rescheduled'),
    )

    TIME_SLOT = (('10AM-11AM', '10AM-11AM'),('11AM-12pm', '11AM-12pm'),('12PM-01PM', '12PM-01PM'),('2PM-3PM', '2PM-3PM'),('3PM-4PM', '3PM-4PM'),('4PM-5PM', '4PM-5PM'),('6PM-7PM', '6PM-7PM'),('7PM-8PM', '7PM-8PM'),('8PM-9PM', '8PM-9PM')) 
    registration_no = models.CharField(('registration_number'), max_length=50, null=True, blank=True, unique=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)#a
    Department = models.ForeignKey(specialization, on_delete=models.CASCADE)#b
    Doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)#c
    Time_Slot = models.CharField(max_length=200, choices=TIME_SLOT)
    Token_Number = models.CharField(max_length=255)
    Problem = models.TextField() #medical_problems
    visit_date = models.CharField(max_length=255, default='') 
    status = models.CharField(max_length=255, choices=APPOINTMENT_STATUSES,default='Pending')
    visit = models.BooleanField(default=False)



    def save(self):
        self.registration_no = uuid.uuid4().hex[:6].upper()
        self.Token_Number = 100 + self.id      
        super().save()


    def __str__(self):
        return self.Patient.patient_name
    
# room_number = models.CharField(max_length=20, default='001')
class Room_Info(models.Model):
    types_of_room = models.CharField(max_length=255, default='General Ward Room')
    

    def __str__(self) -> str:
        return self.types_of_room 
    

class RoomNumber(models.Model):
    room_number = models.CharField(max_length=20, default='001') 
    type_of_room = models.ForeignKey('Room_Info', on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.room_number 
    


class room_allotment(models.Model):
       room_number = models.ForeignKey("RoomNumber", on_delete=models.CASCADE)
       room_type = models.ForeignKey("Room_Info", on_delete=models.CASCADE)
       patient_name = models.ForeignKey("Patient", on_delete=models.CASCADE)
       allotment_date = models.CharField(max_length=255)
       discharged_date = models.CharField(max_length=255)
       doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)

       def __str__(self):
           return self.room_number.room_number + "--" + self.patient_name.patient_name
       
