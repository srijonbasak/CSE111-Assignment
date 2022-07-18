class Vaccine:
    def __init__(self,name,lc,day):
        self.name = name
        self.location = lc
        self.day = day

class Person:
    def __init__(self,name,age,job='General Citizen'):
        self.name = name
        self.age = age
        self.job = job
        self.v_name = None
        self.dose1 = None
        self.dose2 = None
        self.days = 0
    def pushVaccine(self, vacc, dose = '1st dose'):
        if self.age <25 and self.job != "Student":
            print(f'Sorry {self.name}, Minimum age for taking vaccines is 25 years now.')
        elif dose == '1st dose' and self.v_name == None:
            self.v_name = vacc.name
            self.dose1 = 'Given'
            self.dose2 = f'Please come after {vacc.day} days'
            print(f'1st dose done for {self.name}')
        elif self.dose1 == 'Given' and self.v_name == vacc.name:
            self.dose2 = 'Given'
            print(f'2nd dose done for {self.name}')
        else:
            print(f'Sorry {self.name}, you can’t take 2 different vaccines')
    def showDetail(self):
        print(f'Name: {self.name} Age: {self.age} Type: {self.job}\nVaccine name: {self.v_name}\n1st dose: {self.dose1}\n2nd dose: {self.dose2}')
        
        
        


astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
print("=================================")
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")
