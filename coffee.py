print("#"*50)
print("#                COFFEE BREWING                 #")
print("#"*50)

print("="*50)
userName = input(f"Input Your Name!!! ").upper()
print("="*50)

print(f'''Hello,
{userName}, Welcome To Coffee Brewing! ''')

Confirm = input(f"Do You Want To Brew Your Own Cofee Today? [Y/N]: ").upper()

if Confirm == "N":
    print(f"See Your Frindly Local Barista")
    exit()
elif Confirm == "Y":
    Confirm_Next = input(f"Do You Prefer Milk In Your Coffee? [Y/N]: ").upper()
    if Confirm_Next == "N":
        Confirm_Next_Two = input(f"Do You Like To Get Creative With Recipes? [Y/N]: ").upper()
        if Confirm_Next_Two == "N":
            Confirm_Next_Four = input(f"Do You Want Stay Nice And Basic? [Y/GET LITTLE/N]: ").upper()
            if Confirm_Next_Four == "Y":
                print("Brench Press")
                exit()
            elif Confirm_Next_Four == "GET LITTLE":
                print("No, I Want To Get A Little Geek")
                Confirm_Next_Six = input("Are You A Science Geek? [Y/N]: ").upper()
                if Confirm_Next_Six == "N":
                    print(f"Clever Dripper")
                    exit()
                elif Confirm_Next_Six == "Y":
                    Confirm_Next_eight = input(f"Do You Want Your Coffee Brewing To Be Dramatic? [TOTALLY/A LITTE]: ").upper()
                    if Confirm_Next_eight == "TOTALLY":
                        print(f"Siphor Coffe")
                    elif Confirm_Next_eight == "A LITTLE":
                        print(f"Chemex")
            elif Confirm_Next_Four == "N":
                print(f"Clever Dripper")
                exit()
        elif Confirm_Next_Two == "Y":
            print(f"Acropress")
            exit()    
    elif Confirm_Next == "Y":
       Confirm_Next_One = input(f"Do You Own Expresso Machine? [Y/N]: ").upper()
       if Confirm_Next_One == "N":
           print(f"Bialetti")
           exit()
       elif Confirm_Next_One == "Y":
           Confirm_Next_Tree = input(f"Do You Dream Of Your Semester Abroad In Australia Or Nee Zealand? [Y/N]: ").upper()
           if Confirm_Next_Tree == "N":
               Confirm_Next_Five = input(f"Do You A Lot Of Milk? [Y/N]: ").upper()
               if Confirm_Next_Five =="Y":
                   print(f"""Yess, Milk It Up!
 Latte""")
               elif Confirm_Next_Five =="N":
                   print(f"""No, Not Really"
Capuccino""")
           elif Confirm_Next_Tree == "Y":
               print(f"Flat White")
               exit()
else:
    print(f"INCORRECT INPUT CODE, PLEASE REPEAT AGAIN")
    exit()