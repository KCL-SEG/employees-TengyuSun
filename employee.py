"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthlySal, hourlySal, workingHours, contractCommission, contractNum, bounsCommission):
        self.name = name
        self.monthlySal = monthlySal
        self.hourlySal = hourlySal
        self.workingHours = workingHours
        self.contractCommission = contractCommission
        self.contractNum = contractNum
        self.bounsCommison = bounsCommission


    def get_pay(self):
        return self.monthlySal + self.hourlySal * self.workingHours + self.contractCommission * self.contractNum + self.bounsCommison

    def __str__(self):
        str = f"{self.name} works on a "
        if self.monthlySal != 0:
            str += f"monthly salary of {self.monthlySal}"
        else:
            str += f"contract of {self.workingHours} hours at {self.hourlySal}/hour"

        if self.bounsCommison != 0:
            str += f" and receives a bonus commission of {self.bounsCommison}"
        elif self.contractCommission != 0:
            str += f" and receives a commission for {self.contractNum} contract(s) at {self.contractCommission}/contract"

        str += f".  Their total pay is {self.get_pay()}."

        return str


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 100, 25, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 200, 4, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 150, 25, 220, 3, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 0, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 120, 30, 0, 0, 600)
