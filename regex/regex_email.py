import re



pattern= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.?[A-Z|a-z]{2,7}?\b'

def match(text):
    if(re.fullmatch(pattern,text)):
        print("Valid Email")
 
    else:
        print("Invalid Email")

text="rimshalaraib33@gmail"
match(text)
