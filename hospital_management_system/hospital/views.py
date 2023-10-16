from django.shortcuts import render, redirect
from django.contrib import messages
from hospital.models import specialization, Doctor, Patient, Appointment, Room_Info, RoomNumber, room_allotment
from hospital.forms import DoctorForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'base.html')
def patient_add(request):
    if request.method == "POST":
        name = request.POST.get('patient_name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        print(name, dob, age, phone, email, gender, address)
        if name == "":
            messages.success(request, 'Write the name of the patient')
            return render(request, 'patient/add_patient.html')

        try:
            a = Patient(patient_name=name, Date_of_birth=dob, Age=age, phone_number=phone, Email=email, gender=gender, Address=address)
            a.save()
            messages.success(request, 'Patient added sucess')

        except Exception as error:
            messages.error(request, {'error':error})
            messages.error(request, 'please try again')
    return render(request, 'patient/add_patient.html')

def patient_list(request):
    patient_info = Patient.objects.all()
    context = {
        'patient_info' :patient_info
    }
    return render(request, 'patient/patient_list.html', context)


def patient_detail(request, id):
    try:
        patient = Patient.objects.filter(id=id).first()
        
    except Exception as error:
        messages.error(request, error)
    doctor = Appointment.objects.filter(Patient=patient)
    
    if len(doctor) != None:
        
        print(doctor)
        context = {
            'patient':patient,
            'doctor':doctor
        }
    else:
        context = {
            'patient':patient,
        }

    return render(request,  'patient/patient_details.html', context)

@login_required(login_url="/login")

def patient_edit(request, id):
    patient = Patient.objects.filter(id=id).first()
    if request.method == "POST":
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        try:
            patient.Date_of_birth = dob
            patient.Age =age
            patient.phone_number =phone
            patient.Email =email
            patient.Address = address
            patient.save()
            messages.success(request, 'sucess')
        except Exception as error:
            messages.error(request, error)
        return redirect('patient_detail', patient.id)
    context = {
        'patient' : patient

    }
    return render(request, 'patient/patient_edit.html', context)


def doctor_add(request):
    if request.method == "POST":
        doctor_name = request.POST.get('doctor_name')#doctor_names
        date_of_birth = request.POST.get('date_of_birth')#dob_list
        Specialization = request.POST.get('specialization')
        experience = request.POST.get('experience')#experience
        age = request.POST.get('age')#age_list
        phone_number = request.POST.get('phone_nnumber')#phone_numbers
        email = request.POST.get('email')#gmail_addresses
        gender = request.POST.get('gender')
        about_doctor = request.POST.get('about_doctor')#doctor_descriptions
        address = request.POST.get('address')#addresses
        image = request.FILES['image']#images
        resume = request.FILES['resume']
        a = specialization.objects.filter(name=Specialization).first()
        try:
            b = Doctor(doctor_name=doctor_name, date_of_birth=date_of_birth, specialization=a,experience=experience, age=age, phone_nnumber=phone_number, email=email, gender=gender, about_doctor=about_doctor,address=address, image= image, resume=resume )
            b.save()
            messages.success(request, 'Patient added sucess')
        except Exception as error:
            messages.error(request, {'error':error})
            messages.error(request, 'please try again')

    specializations = specialization.objects.all()
    context = {
        'specialization' :specializations
    }
    return render(request, 'doctor/add_doctor.html', context)

def doctor_detail(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors' : doctors
    }
    return render(request, 'doctor/doctor_details.html', context)

def about_doctor(request, id):
    doctor = Doctor.objects.filter(id=id).first()
    appointment = Appointment.objects.filter(Doctor_name=doctor)
    print(appointment)

    context = {
        'doctor' :doctor,
        'appointment':appointment
    }
    return render(request, 'doctor/about_doctor.html', context)


@login_required(login_url="/login")
def doctor_edit(request, id):
    doctor = Doctor.objects.filter(id=id).first()
    if request.method == "POST":
        date_of_birth = request.POST.get('date_of_birth')#dob_list
        Specialization = request.POST.get('specialization')
        experience = request.POST.get('experience')#experience
        age = request.POST.get('age')#age_list
        phone_number = request.POST.get('phone_nnumber')#phone_numbers
        email = request.POST.get('email')#gmail_addresses
        about_doctor = request.POST.get('about_doctor')#doctor_descriptions
        address = request.POST.get('address')#addresses
        a = specialization.objects.filter(name=Specialization).first()
        try:
            doctor.date_of_birth=date_of_birth
            doctor.specialization=a
            doctor.experience=experience
            doctor.age=age
            doctor.phone_nnumber=phone_number 
            doctor.email=email 
            doctor.address=address
            doctor.about_doctor=about_doctor
            doctor.save()
            messages.success(request, 'Patient added sucess')
        except Exception as error:
            messages.error(request, {'error':error})
            messages.error(request, 'please try again')

    
    specializations = specialization.objects.all()
    context = {
        'specialization' :specializations,
        'doctor' :doctor,
        
    }
    return render(request, 'doctor/edit_doctor.html', context)







def add_appointment(request):
    if request.method == "POST":
        patient_name = request.POST.get('patient_name')
        department = request.POST.get('department')
        department_doctor = request.POST.get('department_doctor')
        appointment_date = request.POST.get('appointment_date')
        time_slot = request.POST.get('time_slot')
        problem = request.POST.get('problem')
        patient_info_ = Patient.objects.filter(id=patient_name).first()
        Specialization_ = specialization.objects.filter(id=department).first()
        doctor_ = Doctor.objects.filter(id=department_doctor).first()
        try:
            app = Appointment(Patient=patient_info_, Department=Specialization_,Doctor_name=doctor_, Time_Slot=time_slot, Problem=problem ,visit_date=appointment_date)
            app.save()
            messages.success(request, 'sucess')
        except Exception as error:
            messages.error(request, error)
    patient_info = Patient.objects.all()
    Specialization = specialization.objects.all()
    doctor = Doctor.objects.all()
    context = {
        'patient':patient_info,
        'Specialization' :Specialization,
        'doctor':doctor,
    }
    return render(request, 'appointment/add_appointment.html', context)

def appointment_list(request):
    appointment = Appointment.objects.all()
    context = {
        'appointment' : appointment
    }
    return render(request, 'appointment/appointment_list.html', context)

def appointment_detail(request, id):
    print(id)
    a = Appointment.objects.get(id=id)
    context = {
                'appointment' : a,
                "appid": a.id
            }
            
    return render(request, 'appointment/appointment_detail.html', context)
    # else:
    
    #     return render(request, '404.html')


@login_required(login_url="/login")
def appointment_edit(request, id):
    a = Appointment.objects.filter(id=id).first()
    if request.method == "POST":
        print("POSt")
        department = request.POST.get('department')
        department_doctor = request.POST.get('department_doctor')
        appointment_date = request.POST.get('appointment_date')
        time_slot = request.POST.get('time_slot')
        Specialization_ = specialization.objects.filter(id=department).first()
        doctor_ = Doctor.objects.filter(id=department_doctor).first()
        print(Specialization_, doctor_, appointment_date, time_slot)
        try:
            a.Department = Specialization_
            a.Doctor_name = doctor_
            a.visit_date = appointment_date
            a.Time_Slot = time_slot
            a.save()
            messages.success(request, 'Your appointment has been updated')
        except Exception as error:
            messages.error(request, error)

    patient_info = Patient.objects.all()
    Specialization = specialization.objects.all()
    doctor = Doctor.objects.all()


    context = {
        'appointment' : a,
        'patient':patient_info,
        'Specialization' :Specialization,
        'doctor':doctor,
    }
    return render(request, 'appointment/edit_appointment.html', context)
@login_required(login_url="/login")
def appointment_cancel(request, id):
    try:
        a = Appointment.objects.filter(id=id).first()
        a.delete()
        messages.success(request, 'you have sucessfully cancel your appointment')
    except Exception as error:
        messages.error(request, error)
    return redirect('appointment_list')

@login_required(login_url="/login")
def visit_patient(request):
        
    appointment = Appointment.objects.all()
    context = {
        'appointment' :appointment
    }
    return render(request, 'visit/visit_patient.html', context)


@login_required(login_url="/login")
def visited_patient(request, id):
    if id != 0:
        try:
            appointment = Appointment.objects.filter(id=id).first()
            appointment.visit = True
            appointment.save()
        except Exception as error:
            pass
    appointment = Appointment.objects.filter(visit=True)
    context = {
        'appointment' :appointment
    }
    return render(request, 'visit/visit_patient.html', context)

def visit_pending(request):
    appointment = Appointment.objects.filter(visit=False)
    context = {
        'appointment' :appointment
    }
    return render(request, 'visit/visit_patient.html', context)


@login_required(login_url="/login")
def roomallotment(request):
    if request.method == "POST":
        room_number = request.POST.get('room_number')
        room_type = request.POST.get('room_type')
        patient_name = request.POST.get('patient_name')
        allotment_date = request.POST.get('allot_date')
        discharged_date = request.POST.get('discharge_date')
        doctor = request.POST.get('doctor_name')
        print(room_number, room_type)
        a = RoomNumber.objects.filter(id=room_number).first()
        b = Room_Info.objects.filter(id=room_type).first()
        c = Patient.objects.filter(patient_name=patient_name).first()
        d = Doctor.objects.filter(doctor_name=doctor).first()
        print(a, b, c, d)
        try:
            e = room_allotment(room_number=a, room_type=b, patient_name=c, allotment_date=allotment_date, discharged_date=discharged_date, doctor=d)
            e.save()
            a.booked = True
            a.save()
            messages.success(request, 'You have sucessfully done')
        except Exception as error:
            messages.error(request, error)

    patient = Patient.objects.all()
    doctor = Doctor.objects.all()
    room_info = Room_Info.objects.all()
    room_num = RoomNumber.objects.filter(booked=False)
    context = {
        'patient':patient, 
        'doctor':doctor, 
        'room_info':room_info,
        'room_num':room_num
    }
    return render(request, 'rooms/room_allotment.html', context)

@login_required(login_url="/login")
def rooms_alloted(request):
    rooms = room_allotment.objects.filter(room_number__booked=True)
    print(rooms)
    context = {
        'rooms' :rooms
    }
    return render(request, 'rooms/rooms.html', context)

@login_required(login_url="/login")
def edit_roomallotment(request, id):
    x = room_allotment.objects.filter(id=id).first()
    if request.method == "POST":
        room_number = request.POST.get('room_number')
        room_type = request.POST.get('room_type')
        allotment_date = request.POST.get('allot_date')
        discharged_date = request.POST.get('discharge_date')
        doctor = request.POST.get('doctor_name')
        print(room_number, room_type)
        a = RoomNumber.objects.filter(id=room_number).first()
        b = Room_Info.objects.filter(id=room_type).first()
        d = Doctor.objects.filter(doctor_name=doctor).first()
        try:
            x.room_number = a
            x.room_type = b
            x.allotment_date = allotment_date
            x.discharged_date = discharged_date
            x.doctor = d
            x.save()
            a.booked = True
            a.save()
            messages.success(request, 'You have sucessfully done')
        except Exception as error:
            messages.error(request, error)

    patient = Patient.objects.all()
    doctor = Doctor.objects.all()
    room_info = Room_Info.objects.all()
    room_num = RoomNumber.objects.filter(booked=False)
    context = {
        'patient':patient, 
        'doctor':doctor, 
        'room_info':room_info,
        'room_num':room_num,
        'x':x
    }
    return render(request, 'rooms/edit_room_allotment.html', context)
