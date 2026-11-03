print ("Boiling Water and add to Mug")
print ("1. Tea 2. Coffee 3. Hot Choc")

Drink = input()
if Drink == 1 :
    print ("Add Teabag to mug")
elif Drink == 2 :
    print ("Add Coffee Granules to mug")
elif Drink == 3 :
    print ("Add Hot Chocolate powder to mug")


Sugar_Count= 0
print ("Do you want Sugar ?")
sugar= input()

while sugar == ("yes") and Sugar_Count < 3 :
    print ("Add Sugar to mug")
    Sugar_Count= Sugar_Count + 1
    if Sugar_Count >= 3 :
        pass
        # Skip further prompt if maximum reached
    else:
        print ("Do you want another Sugar ?")
        sugar= input()
    


Milk_Count= 0
print ("Do you want Milk?")
Milk= input()

while Milk == ("yes") and Milk_Count < 3 :
    print ("Add Milk to mug")
    Milk_Count= Milk_Count + 1
    if Milk_Count >= 3 :
        pass
        # Skip further prompt if maximum reached
    else:
        print ("Do you want another Milk shot?")
        Milk= input()
    


if Drink == 1 :
    print ("Remove Teabag")


print ("Stir Mug")
