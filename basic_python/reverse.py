def reverse(s):
    if s=="":
        return ""
    else:
        fst_symbol=s[0]
        return reverse(s[1:])+fst_symbol

#output:
    
#fn call ----> reverse("raveena")
'aneevar'


              or


a[::-1]
'aneevar'

              or
              
reverse("raveena")
'aneevar'
