'''
class Sick:
    pass
class cancer(Sick):
    def __init__(self,medicine,consult_fee):
        self.medicine = medicine
        self.consult_fee = consult_fee
    def TreatmentAmount(self,medicine,consult_fee):
        if self.consult_fee>600:
            print("sorry we cannot treat you")
        else:
            amount = self.medicine + self.consult_fee
            print(amount)
in1 = cancer('medicine','consult_fee')
in1.consult_fee = int(input("enter amount\n"))
in1.medicine = 400
in1.TreatmentAmount('medicine','consult_fee')
'''
class Sick:
    pass
class influenza(Sick):
    def __init__(self,medicine,consult_fee):
        self.medicine = medicine
        self.consult_fee = consult_fee
    def TreatmentAmount(self,medicine,consult_fee):
        if self.consult_fee>600:
            amount = self.medicine + self.consult_fee * (0.98)
            print(amount)
        else:
            print("you get no discount")

in1 = influenza('medicine','consult_fee')
in1.consult_fee = float(input("enter amount\n"))
in1.medicine = 350.50
in1.TreatmentAmount('medicine','consult_fee')
