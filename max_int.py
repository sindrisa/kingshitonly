num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
<<<<<<< HEAD
if num_int < 0:  # checka fyrst hvort fyrsta talan sem slegin inn er neikvæð
    print("The maximum is", max_int)
else:
    while num_int >= 0:   # While lykkja sem ber saman töluna sem slegin er inn við max_int
        if num_int > max_int:   # Ef talan sem slegin var inn er hærri en max_int er talan sem slegin var inn sett sem nýja max_int
            max_int = num_int    
=======
if num_int < 0:  # checka fyrst hvort fyrsta talan sem slegin inn er neikvæð og prenta hana þá beint
    print("The maximum is", num_int)
else:
    while num_int >= 0:  # While lykkja sem ber saman töluna sem slegin er inn við max_int
        if num_int > max_int:  # Ef talan sem slegin var inn er hærri en max_int er talan sem slegin var inn sett sem nýja max_int
            max_int = num_int
>>>>>>> 383652d64c8277d42dafdf323ae8f3781198acc8
        num_int = int(input("Input a number: "))
    
print("The maximum is", max_int)    # Do not change this line
