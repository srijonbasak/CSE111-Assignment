class Hospital():
    #init
    def __init__(self,hospital):
        self.hospital = hospital
        self.doctors = {}
        self.patients = {}
        self.msg = ''

    #doctor
    def addDoctor(self, id1):
        self.doctors[id1.id] = [id1.name, id1.type ]

    def getDoctorByID(self, id1):
        return f'Doctor\'s ID: {id1}\nName:{self.doctors[id1][0]}\nSpeciality:{self.doctors[id1][1]}'

    #patient
    def addPatient(self, id2):
        self.patients[id2.id] = [id2.name, id2.age, id2.no]

    def getPatientByID(self, id2):
        return f'Patient\'s ID: {id2}\nName:{self.patients[id2][0]}\nAge:{self.patients[id2][1]}\nPhone no.:{self.patients[id2][2]}'

    #print all
    def allDoctors(self):
        print(f'All Doctors:\nNumber of Doctors: {len(self.doctors)}\n{self.doctors}')

    def allPatients(self):
        print(f'All Patients:\nNumber of Patients: {len(self.patients)}\n{self.patients}')

class Doctor():
    def __init__(self, id, job, name, type):
        self.id = id
        self.job = job
        self.name = name
        self.type = type

class Patient():
    def __init__(self, id, job, name, age, no):
        self.id = id
        self.job = job
        self.name = name
        self.age = age
        self.no = no

h = Hospital("Evercare")
d1 = Doctor("1d","Doctor", "Samar Kumar", "Neurologist")
h.addDoctor(d1)
print("=================================")
print(h.getDoctorByID("1d"))
print("=================================")
p1 = Patient("1p","Patient", "Kashem Ahmed", 35, 12345)
h.addPatient(p1)
print("=================================")
print(h.getPatientByID("1p"))
print("=================================")
p2 = Patient ("2p","Patient", "Tanina Haque", 26, 33456)
h.addPatient(p2)
print("=================================")
print(h.getPatientByID("2p"))
print("=================================")
h.allDoctors()
h.allPatients()
