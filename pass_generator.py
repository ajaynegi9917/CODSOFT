#RANDOM PASSWORD 
import random
import string

pass_len=18
charvalues =string.ascii_letters +string.digits+string.punctuation


password=""
for i in range (pass_len):

 password+= random.choice(charvalues)

print("uhr randoom pass word is :-",password )
