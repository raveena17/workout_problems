def DNA_matching(string1, string2,res):
    a = string2

    if len(string1) == 0:
        return res
    
    if string1[0] not in a:
        return (DNA_matching(string1[1:], string2[0:],res))
    
    if string1[0] in a:
        b=string1[0]
        res=res+b
        return (DNA_matching(string1[1:], string2[1:],res))
    

    
#output:

>>> DNA_matching('human', 'chimp',res='')
'hm'
>>> DNA_matching( 'gattaca', 'tacgaacta',res='')
'gattaca'
>>> DNA_matching( 'wow', 'whew', res='' )
'ww'
>>> DNA_matching( '', 'whew', res='' )
''
>>> DNA_matching('abcdefgh', 'efghabcd',res='')
'abcd'
>>> 
