class Employee:
    raise_amount = 1.04
    num_employee =0
    def __init__(self, name, last,pay):
        self.name = name
        self.last = last
        self.email = name +'.'+ last + '@gmail.com'
        self.pay = pay
        Employee.num_employee +=1
    def fullname(self):
        #print(self.name,self.last)
        return('{} {}'.format(self.name, self.last))
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_employee)
emp1 = Employee('corey','schafer',5000)
emp2 = Employee('test','user',2000)
print(Employee.num_employee)
print(emp1.raise_amount)
print(Employee.raise_amount)

