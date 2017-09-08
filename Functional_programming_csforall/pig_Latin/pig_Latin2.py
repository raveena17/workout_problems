# One way to use recursion to assist in this is to write a function
#  def initial_consonants( s ):
# that returns a string of all of the initial consonants in the input string s.
# Thus, if s starts with a vowel, the empty string '' will be returned. 

def initial_consonants( s ):
    vowel_char=['a','e','i','o','u']
    for x in s:
        if x[0] in vowel_char:
            return ''
        else:
            return s
    

#OUTPUT:
        
>>> initial_consonants("upper")
''
>>> initial_consonants("hi")
'hi'
