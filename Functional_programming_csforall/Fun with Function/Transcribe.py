def transcribe(a):
    b = ' '
    if len(a) == 0:
        return ' '
    if a[0] == ' ':
        return transcribe(a[1:]) 
    if a[0] == 'A':
        return 'U' + transcribe(a[1:])
    if a[0] == 'C':
        return 'G' + transcribe(a[1:])
    if a[0] == 'G':
        return 'C' + transcribe(a[1:])
    if a[0] == 'T':
        return 'A' + transcribe(a[1:])
    else:
        return ''



#output:

>>> transcribe('ACGT TGCA')
'UGCAACGU '
>>> transcribe('GATTACA')
'CUAAUGU '
>>> transcribe('cs5')
''
>>> transcribe('')
' '
>>> transcribe('ACG TGCA')
'UGCACGU '
