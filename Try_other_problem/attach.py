import tkMessageBox

def questions():

    global Questions
    global ans
 
    
    
    Questions={"python":
             {1:"1. python is a ? \n  a.Development environment\n  b.Programming language \n c.Set of editing tools ",
             2:"2. Which of these statements is true \n a.CPython is an implementation of python\n b.Pyhon code must be always compiled\n c.Python 1.7 is the most widely used version",
             3:"3. Which line code produces an error?\n a.str(7)+'eight' \n b.'5'+6 \n c. 3+4",
             4:"4. What are anonymous functions called \n a.lamdas\n b.lombdas\n c.lambdas",
             5:"5. What statement is used in funcions to turn them into generators\n a.yield\n b.generate\n c.return",
             6:"6. Which of the following data types does not allow duplicate values\n a.Dictionaries\n b.Tuples\n c.Sets",
             7:"7. What is the result of this code ?\n a.0\n b.1\n c.7",
             8:"8.What type of object is a method ?\n a.Integer\n b.class\n c.Function",
             9:"9.What error is caused by trying to access unknown attributes ?\n a.NameError\n b.ValueError\n c.AttributeError",
             10:"10.What is the superclass of a class ?\n a.The class it inherits from\n b.The class it is an instance of\n c.The first class that inherits from it"},
             "Java":
            {1:"Can we compare int variable with a boolean variable?\n a.True\n b.False",
             2:"What is the size of boolean variable?\n a.8 bit\n b.16 bit\n C.32 bit",
             3:"What is the default value of String variable?\n a. ""\n b. '' \n c. null",
             4:"Which of the following is false about String?\n a.String is immutable\n b.String can be created using new operator\n c.String is a primary data type",
             5:"What is local variable?\n a.Variables defined inside methods, constructors or blocks are called local variables\n b.Variables defined outside methods, constructors or blocks are called local variables\n c.Static variables defined outside methods, constructors or blocks are called local variables",
             6:"What is static block?\n a.It is used to create syncronized code\n b.There is no such block\n c.It is used to initialize the static data member., It is excuted before main method at the time of class loading",
             7:"When static binding occurs?\n a.Static binding occurs during Compile time\n b.Static binding occurs during load time\n c.Static binding occurs during runtime",
             8:"What is Serialization?\n a.Serialization is the process of writing the state of an object to another object\n b.Serialization is the process of writing the state of an object to a byte stream\n c.Both of the above",
             9:"Can constructor be inherited?\n a.True\n  b.False",
             10:"What is a marker interface?\n  a.marker interface is an interface with no method\n b.marker interface is an interface with single method, mark()\n c.marker interface is an interface with single method, marker()"}
            }
    ans={"python":{1:"b",2:"a",3:"b",4:"c",5:"a",6:"c",7:"b",8:"c",9:"c",10:"a"},
	    "Java":{1:"b",2:"b",3:"c",4:"c",5:"a",6:"c",7:"a",8:"b",9:"b",10:"a"}}

questions()
                       

class Examresult:

    def Quiz(subject):
        total=10
        correct=0
        wrong=0
        
        print subject
        #global subject
        global questions
        
        for i in range(len(questions.Questions.get(subject))):
            print questions.Questions.get(subject).get(i+1)
            answer=raw_input("Enter the answer: ")
            
            result=questions.ans.get(subject).get(i+1)
            #print result
            
            if result == answer:
                correct += 1
            elif result != answer:
                wrong += 1       # system counting (user skip the questions-> system takes, it's Wrong ans)


        tkMessageBox.showinfo(title="Result", message="Display Your Result !")
        print "\n"
        print "RESULT:"
        print "Total answer is: ",total
        print "Correct answer is: ",correct
        print "Wrong answer is: ",wrong

Exam = Examresult()
Exam.Quiz(subject)

class Student:
    
    def __init__(self,name,exam):
        self.name = name
        self.exam = exam

kavi=Student('jeevi','Python')

class Details:
        
    global subject 
    def Userdetails(self):   # it's main function
        
       
        tkMessageBox.showinfo(title="UserDetais", message="Plz Enter Your Details!")
        user_name = raw_input("Enter the name: ")
        user_qualification = raw_input("Enter the qualification: ")
        user_mailid = raw_input("Enter the  mail-ID: ")
        user_mobile_no = input("Enter the mobile no: ")
        
        tkMessageBox.showinfo(title="Language", message="Language Display")
        print("(1) Python")
        print("(2) Java")

        
        while True:
            
               
            userchoice=input("Choose an Language: ")

            
            if userchoice == 1:
                subject="python"
                Exam.Quiz(subject)
                break

            if userchoice == 2:
                subject="Java"
                Exam.Quiz(subject)
                break
            
            else:
                print(userchoice, "?")




details=Details()
details.Userdetails()
    
