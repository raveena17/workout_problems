#Composing new list from pi,e, and list operations:

pi=[3,1,4,1,5,9]
e=[2,7,1]


#list indexing, such as pi[0]
print pi[0]

#output----->3


#list slicing,such as e[1:]
print e[1:]

#output----->[7,1]


#skip-slicing,such as pi[0:6:2]
print pi[0:6:2]

#output----->[3,4,5]


#list concatenation with +, such as e[0:2]+pi[-2:]
print e[0:2]+pi[-2:]

#output----->[2,7,5,9]


# 0. Use pi and/or e to create the list [2,7,5,9].
#This example above,stored in the variable answer0.

pi=[3,1,4,1,5,9]
e=[2,7,1]
answer0= e[0:2]+pi[-2:]

print answer0

#output----->[2,7,5,9]


# 1.Use pi and/or e to create the list [7,1].
#As above,store this list in the variable answer1.

pi=[3,1,4,1,5,9]
e=[2,7,1]
answer1= e[1:] or e[1]+pi[1] or e[1]+pi[3]

print answer1

#output----->[7,1]


# 2. Use pi and/or e to create the list [9,1,1].
#store this list in the variable answer2.

pi=[3,1,4,1,5,9]
e=[2,7,1]
pi.reverse()
answer2=pi[0:-1:2]

print answer2

#output----->[9,1,1]



# 3. Use pi and/or e to create the list [1,4,1,5,9].
#store this list in the variable answer3.
pi=[3,1,4,1,5,9]
e=[2,7,1]
answer3=pi[1:]

print answer3

#output----->[1,4,1,5,9]


# 4. Use pi and/or e to create the list [1,2,3,4,5].
#store this list in the variable answer4.
pi=[3,1,4,1,5,9]
e=[2,7,1]
answer4=pi+e
x=answer4
x.sort()

print x[2:7]

#output----->[1,2,3,4,5]




