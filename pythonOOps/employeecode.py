class Employee:
    def __init__(self,empName = None, empSalary = None, empId = None):
        self.empName = empName
        self.empSalary = empSalary
        self.empId = empId
    #You can also use getter and setter to set and get the attributes of Instance class
    def setEmpName(self,EMpname):
        self.empName = EMpname
    def getEmpName(self):
        return self.empName
    def setEmpId(self,Empid):
        self.EmpId = Empid
    def getEmpId(self):
        return self.EmpId

emp1 = Employee("Abdulrafy",23000,23)
print(emp1.getEmpId(),emp1.getEmpName())
emp2 = Employee()
emp2.setEmpName("Abdul Rafay")
emp2.setEmpId(56)
print(emp2.getEmpName(),emp2.getEmpId())
