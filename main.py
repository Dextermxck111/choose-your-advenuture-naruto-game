print("Welcome to the Naruto Adventure Game")
print("Your mission is to bring Sasuke back to the leaf.")

leaving_konaha = input("We are leaving konaha... Which direction should we go? Type L or R. ")

if leaving_konaha == "R".lower():
    print("You walked into a trap of shinobi from the Akatski, you didn't survive.")
elif leaving_konaha == "L".lower():
    layer = input("We made it to Orochimarus' layer, should we wait or go in? Type Wait or Go. ")
    if layer == "Wait".lower():
        print("You were spotted, and trapped by paper bombs.")
    elif layer == "Go".lower():
        sasuke = input("I see Sasuke, but he appears to be in pain... there is also Orichimarus men surrounding... Type Save to help Sasuke or Wait. ")
        if sasuke == 'Wait'.lower():
            print("You were spotted and ambushed.")
        elif sasuke == "Save".lower():
            print("Sasuke is undergoing curse mark transformation... He attacked and you died.")