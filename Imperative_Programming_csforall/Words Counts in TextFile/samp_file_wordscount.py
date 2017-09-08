import re
import string
frequency = {}
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print words, frequency[words]





#output:

>>> 
 RESTART: /home/linuxuser/Desktop/python/Assessment/Imperative Programming/samp_file_wordscount.py 
code 7
less 1
developed 1
over 1
baskin 1
symbols 4
prefix 4
paper 1
entropy 1
methods 1
sorted 1
huffman 10
its 1
shorter 1
unique 1
based 1
with 3
character 1
better 1
source 4
combine 1
input 4
has 1
founding 1
string 2
frequencies 1
possible 1
lzw 1
often 1
cruz 1
not 2
using 1
bit 2
now 1
lossless 1
produced 1
school 1
university 1
generally 1
accidentally 1
specific 1
these 1
common 2
each 2
output 1
where 1
smaller 1
occurrence 1
some 1
computer 2
design 1
are 3
choosing 1
estimated 1
linear 1
even 1
widely 1
for 13
although 1
uniform 1
adapt 1
example 1
expresses 1
method 5
creating 1
theory 1
power 1
derived 1
equivalent 1
never 1
free 3
produce 1
california 1
term 2
santa 1
found 1
refers 1
both 1
actual 2
graduation 1
david 1
length 2
became 1
resulting 1
published 1
block 1
useful 1
characters 1
probability 3
encoding 3
simple 1
coding 10
number 2
set 1
type 1
table 2
precisely 1
size 1
use 1
statistics 1
compression 3
probabilities 2
create 1
arbitrary 1
two 1
been 1
way 1
was 5
more 1
that 3
capability 1
part 1
optimality 1
particular 2
known 3
representing 2
than 1
those 1
bits 2
this 2
science 2
when 3
value 1
will 1
while 1
individual 1
can 2
distribution 2
members 1
agree 1
and 6
sometimes 1
have 1
stated 1
engineering 1
minimum 1
file 1
ascii 1
any 1
information 1
redundancy 1
efficient 2
latter 1
able 1
member 2
also 1
other 2
which 2
department 1
optimal 1
widespread 1
mit 2
arithmetic 1
used 4
binary 1
symbol 8
upon 1
mapping 1
most 2
codes 2
uses 1
student 1
faculty 1
variable 2
such 3
data 1
synonym 1
algorithm 2
average 1
later 2
construction 1
weights 1
time 1
representation 1
the 22
strings 2
>>> 
