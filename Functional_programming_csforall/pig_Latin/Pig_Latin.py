#[4 E.C. points] The real pig latin challenge:

def spamLatin(s): 
        ans=(s[3:]+s[0:3]+'ay')
        return ans

def spamLatin1(s):
        ans=(s[0:]+'way')
        return ans
    
def spamLatin2(s):
        ans=(s[::-1]+'ay')
        return ans
    




>>> spamLatin("string")
'ingstray'
>>> spamLatin1("yttrium")
'yttriumway'
>>> spamLatin2("yoohoo")
'oohooyay'



