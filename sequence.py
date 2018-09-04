n = int(input("Enter the length of the sequence: ")) # Do not change this line

if n == 1:          # Harðkóða fyrir n=1, 2 og 3
    print("1")
elif n == 2:
    print("1\n2")
elif n == 3:
    print("1\n2\n3")
elif n > 3:
    a = 1   # Bý til breyturnar a b og c fyrir for lykkjuna
    b = 2
    c = 3
    print("1\n2\n3")
    for i in range(3,n):        # by til forlykkju sem tekur summuna af a b og c og hækkar svo um einn í sequenceinu með því að gera a = b, b = c og c = d
        d = (a + b + c)
        a = b
        b = c
        c = d
        print(d)
