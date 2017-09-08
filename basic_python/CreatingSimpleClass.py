class Employee:
    empCount=0

    def __init__(self, name, salary):
        self.name =name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary : ",self.salary



emp1= Employee("raveena", 8000)
emp2= Employee("vanitha", 14000)
emp3= Employee("ravivarma", 9000)
emp4= Employee("sritha", 16000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
print "Total Employee %d" % Employee.empCount
    
    


#OUTPUT:

Name :  raveena , Salary :  8000
Name :  vanitha , Salary :  14000
Name :  ravivarma , Salary :  9000
Name :  sritha , Salary :  16000
Total Employee 4
>>> 
