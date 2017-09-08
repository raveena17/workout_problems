class StackOverflowUser:
        def __init__(self, name, userid, rep): 
            self.name = name
            self.userid = userid
            self.rep = rep

name = raw_input("Enter name: ")
userid = int(raw_input("Enter user id: "))
rep = int(raw_input("Enter rep: "))

dave = StackOverflowUser(name, userid, rep)
