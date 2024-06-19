# PROGRAM OF PASSWORD GENERATOR

import random
import string
print("Welcome to the random password generator")

def main():
    lenght=int(input("enter the length of password you want : "))

    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolD=string.punctuation

    combine = lowerD+upperD+digitD+symbolD

    x=random.sample(combine,lenght)

    password="".join(x)
    print(password)
    main()
main()
