#input a string
#outputs the full length palindromes in string
def pal(string):
    pals = []
    n = 1
    for i in range(len(string)):    # incriment through each character in the input string
        if (i-n) < 0 or (i+n) == len(string):   #if index out of bounds, pass
            pass
        else:   
            oddPal = findPal(string, i, False)
            if(oddPal): #if palindrome has odd number of characters
                pals.append(oddPal)
            evenPal = findPal(string, i, True)
            if(evenPal):    #if palindrome has even number of characters
                pals.append(evenPal)
    print(pals)
    return pals

#helper function to determine if the palindrome is an odd our even number of characters
def findPal(string, index, findEven):
    n = 1
    offset = 1 if findEven else 0 #set the index offset if its an even palindrome
    if (index-n) < 0 or (index+n) == len(string)+1: #if index out of bounds, pass
        pass
    else:
        while (index-n) >= 0 and (index+n) < len(string) and (string[index-n + offset] == string[index+n]): #increments n untill the palindrome is complete then returns the palindrome string. returns empty string otherwise
            if index-n==0:
                return string[index-n:index+n+1+offset]
            n += 1
    return string[(index - n+1+offset): (index+n)] if (n > 1) else ""


#pal("noonjwdmfkw,jbcekayakfdbmnmbsnoon")