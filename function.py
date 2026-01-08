a = 'my name NAME is USMAN'
def check(a):
    count_lower = 0     
    count_upper = 0    
    b = a.split()
    for i in b:
        if i.islower():
            count_lower += 1
        elif i.isupper():
            count_upper += 1

    print("Lowercase words:", count_lower)
    print("Uppercase words:", count_upper)

check(a)
# problem 02 
a=[1,2,3,3,3,4,4,1,2,3,5,5,6,6]
def unique(a):
  s=set(a)
  a=list(s)
  print(a)
unique(a)
#problem 03
def ispalindrome(a):
  if a[::-1]==a:
    print("palindrome")
  else :
    print("not palindrome")
a='helleh'
b='hello'
ispalindrome(a)
ispalindrome(b)
