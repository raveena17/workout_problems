class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

#OUTPUT:

======== RESTART: /home/linuxuser/Desktop/python/OOPS/oopsTryPage.py ========
Employee.__doc__: Common base class for all employees
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: ()
Employee.__dict__: {'__module__': '__main__', 'displayCount': <function displayCount at 0x7f61a0077e60>, 'empCount': 0, 'displayEmployee': <function displayEmployee at 0x7f61a0077ed8>, '__doc__': 'Common base class for all employees', '__init__': <function __init__ at 0x7f61a0077de8>}
>>> 
