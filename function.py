a = 'my name NAME is USMAN'
def check(a):
    count_lower = 0     # lowercase words
    count_upper = 0    # uppercase words
    b = a.split()
    for i in b:
        if i.islower():
            count_lower += 1
        elif i.isupper():
            count_upper += 1

    print("Lowercase words:", count_lower)
    print("Uppercase words:", count_upper)

check(a)
