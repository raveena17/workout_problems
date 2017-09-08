import questions
import tkMessageBox

class User:
    userCount = 0
    
    def __init__(self,year, month, day,name,qualification,language):
        self.year, self.month, self.day = year, month, day
        self.name = name
        self.qualification = qualification
        self.language = language
        User.userCount += 1

    def displayCount(self):
        print "Total User %d" % User.userCount

    def displayUser(self):
        print "Date : ", self.year, self.month, self.day, "Name : ", self.name,  ", qualification: ", self.qualification, ", language: ", self.language
        


class ExamResult:
    
    def Validate(questions):                 # answer validation
        correct,wrong,skip = 0,0,0
        for qus_no, qus in questions.iteritems():
		valid = True
		print str(qus_no) + ':' + qus['QUS'] 
		for opt, ans in qus['OPTIONS'].iteritems():
			print opt + ':' + ans
		while valid:
			ans = raw_input("Choose your answer: ")
			if ans in qus['OPTIONS'].keys():
			    valid = False
			elif ans == "":
			    valid = False
			else:
				tkMessageBox.showinfo(title="INVALID OPTION", message="Plz check Your option!")
		if ans == qus['ANS']:
			correct += 1 
		elif ans == "":
			skip += 1		
		else:
			wrong += 1

        
    print "\n RESULT:"
    print "Total Questions: 10"
    print "Correct Answer: " + str(correct)
    print "Wrong Answer: " + str(wrong)
    print "Skip Questions: " + str(skip)

	

class Test:

    def Take_Test(self):
        
        tkMessageBox.showinfo(title="UserDetais", message="Plz Enter Your Details!")
        print "\n"
        user_name = raw_input("Enter the name: ")
        user_qualification = raw_input("Enter the qualification: ")
        user_mailid = raw_input("Enter the  mail-ID: ")
        user_mobile_no = input("Enter the mobile no: ")
        
        print 'Languages  :  Python ,Java'
        userchoice_ques = raw_input("Choose which language: ")
        
        if userchoice_ques == 'Python':
             valid.Validate(python_questions)
                    
        elif userchoice_ques == 'Java':
             valid.Validate(java_questions)


    
user1=User(2017,03,2, "saraswathi", "BE", "python")
user2=User(2017,03,16, "aarthi", "BCA", "python")
user3=User(2017,04,23, "harsha", "BE", "java")
user1.displayUser()
user2.displayUser()
user3.displayUser()
user1.displayCount()

test=Test()
test.Take_Test()

exam=ExamResult()
exam.Validate()


        
