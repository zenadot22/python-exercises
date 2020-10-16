
def pal_str(w):

    if len(w) < 1: 
        return True
    else:
        if w[0] == w[-1]: 
            return pal_str(w[1:-1]) 
        else: 
            return False
word=str(input("Enter a word"))
if(pal_str(word)==True): 
    print("This is a palindrome!")
else:
    print("This is not a palindrome!")
     











