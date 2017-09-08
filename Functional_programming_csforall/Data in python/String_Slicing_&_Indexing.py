
#Strings! Slicing and indexing


# 5.Create "hey" and store this string in the variable answer5. (3 ops.)

h = 'harvey'
m = 'mudd'
c = 'college'

answer5= h[0]+h[-2:]

print answer5


# 6. Create "collude" and
#store this string in the variable answer6. (our best: 5 ops.) 

h = 'harvey'
m = 'mudd'
c = 'college'

answer6=c[0:4]+m[1:3]+c[-1] 
 
print answer6


# 7. Create "arveyudd" and
# store this string in the variable answer7. (our best: 3 ops.)

h = 'harvey'
m = 'mudd'
c = 'college'

answer7= h[1:]+m[1:] 
 
print answer7


# 8. Create "hardeharharhar" and
# store this string in the variable answer8. (our best: 8 ops.)

h = 'harvey'
m = 'mudd'
c = 'college'

answer8= h[0:3]+m[-1]+c[-1]+(h[0:3]*3)

print answer8


#9. Create "legomyego" and
# store this string in the variable answer9. (our best: 8 ops.)

h = 'harvey'
m = 'mudd'
c = 'college'

answer9= c[3:6]+c[1]+m[0]+h[-1]+c[4:6]+c[1]

print answer9



# 10. Create "clearcall" and
# store this string in the variable answer10. (our best: 9 ops.) 

h = 'harvey'
m = 'mudd'
c = 'college'

answer10= c[0:5:2]+h[1:3]+c[0]+h[1]+c[2:4]

print answer10




