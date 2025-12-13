#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#Example (Input => Output): #1. 35231 => [1,3,2,5,3]   #2. 0 => [0]
#below is the first solution
def digitize(n):  
    digit = [int(d) for d in str(n)] #change the n into a string and keep in under d variable, then change it into an integer
    nsl = []                         #list for storing the reverse digit
    j = len(digit)                   
    while j > 0:
        nsl.append(digit[j-1])
        j -= 1
    return(nsl)

#below is the second solution
def digitize(n):
    return = [int(d) for d in str(n)[::-1]] #[::-1] tells python to reverse a string
digitize(35231)
digitize(0)
