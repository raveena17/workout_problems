def list_max(list):
    high=list[0]
    i=0
    while True:
	if(list[i]>high):            # if(list[i]<low):------display lowest value
	    high=list[i]
	
	if len(list)-1==i:
	    break

	i+=1
    return high



list_max([5,17,8,9,23,6])
	    