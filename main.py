import random
#starting variables
day=1
ORANGE = "\033[38;5;208m"
GREEN="\033[32m"
RESET="\033[0m"
RED="\033[31m"
YELLOW="\033[33m"
bank_balance=100
working_income=20
bills=50
#bollan
Orthopedic_Shoes=True
Espresso_Thermos=True
Premium_Uniform=True
Pocket_Organizer=True
Charisma_Handbook=True
Electric_Scooter=True
#job menu
print("welcome to work life simulater".center(160))
job_choice=input(f"{RED}pick your minumum wage job                            1.grocary store employee               2. restraunt waiter         3.hotel housekeeper{RESET}")
if job_choice=="1":
    print("you now work as a grocary store employee ")
if job_choice=="2":
    print("you now work as a grocary store restraunt waiter ")
if job_choice=="3":
    print("you now work as a grocary store hotel house housekeeper ")
#loop
while bank_balance > 0 and bank_balance < 10000:
    print(f"day:{day}".center(330))
    day+=1

    #menu code

    print("menu".center(130))
    print(f"{GREEN}your bank balance is  {bank_balance}{RESET}")
    menu_choice=input("what do you chose for today                                     1. work                     2.shop              3.lottery            ")
    if menu_choice=="1":
        print(f"{YELLOW}you've gained {working_income}{RESET} ")
        bank_balance+=working_income
        print(f"{GREEN}your current bank balance is now {bank_balance}{RESET}")











#item menu    
    if menu_choice=="2":
        while True:
            item_choice = input(f""" {ORANGE}
            =================== ITEM SHOP ===================
            1. Orthopedic Shoes ($100)
               - High-quality nonslip shoes for fast, pain-free movement.
               - Effect: 1.2x daily income multiplier.
            
            2. Espresso Thermos ($150)
               - Keeps you fully energized and focused through the rush.
               - Effect: 1.3x daily income multiplier.
            
            3. Premium Uniform ($200)
               - A crisp, professional look that impresses everyone.
               - Effect: 1.5x tip multiplier.
            
            4. Pocket Organizer ($120)
               - Keeps all your work tools perfectly sorted and ready.
               - Effect: 1.15x daily income multiplier.
            
            5. Charisma Handbook ($180)
               - Quick tricks to master small talk and charm customers.
               - Effect: 1.4x customer-interaction multiplier.
            
            6. Electric Scooter ($250)
               - Arrive to your shifts early, fresh, and ready to work.
               - Effect: 1.6x base wage multiplier.
            
            0. Exit Shop
            =================================================
            Choose an item to buy (0-6):{RESET} """)
            if item_choice=="0":
                day-=1
                break
           
            
            #Orthopedic Shoes code
            if item_choice=="1":
                if Orthopedic_Shoes==True:
                    if bank_balance>=101:
                        bank_balance-=100
                        print(f"you bought Orthopedic Shoes your income is now multiplied by 1.2 its now {working_income*1.2} every time you work a shift")
                        working_income*=1.2
                        Orthopedic_Shoes=False
                    else:
                        print(f"{YELLOW}not enough money{RESET}")
                        day-=1
                else:
                    print("you allready own Orthopedic Shoes")
                    day-=1
             
            #Espresso Thermos code
            if item_choice=="2":
                if Espresso_Thermos==True:
                    if bank_balance>=151:
                        bank_balance-=150
                        print(f"you bought Espresso Thermos your income is now multiplied by 1.2 its now {working_income*1.3} every time you work a shift")
                        working_income*=1.3
                        Espresso_Thermos=False
                    else:
                        print(f"{YELLOW}not enough money{RESET}")
                        day-=1
                else:
                    print("you allready own Espresso Thermos")
                    day-=1
             
             
             #Premium Uniform code
            if item_choice=="3":
                if Premium_Uniform==True:
                    if bank_balance>=201:
                        bank_balance-=200
                        print(f"you bought Premium Uniform your income is now multiplied by 1.2 its now {working_income*1.5} every time you work a shift")
                        working_income*=1.5
                        Espresso_Thermos=False
                    else:
                        print(f"{YELLOW}not enough money{RESET}")
                        day-=1
                else:
                    print("you allready own Premium Uniform")
                    day-=1
                    
                    
                    
                    #Pocket Organizer code
            if item_choice=="4":
                if Pocket_Organizer==True:
                    if bank_balance>=121:
                        bank_balance-=120
                        print(f"you bought Pocket Organizer your income is now multiplied by 1.2 its now {working_income*1.15} every time you work a shift")
                        working_income*=1.15
                        Pocket_Organizer=False
                    else:
                        print(f"{YELLOW}not enough money{RESET}")
                        day-=1
                else:
                    print("you allready own Pocket Organizer")
                    day-=1
                    
                    
                    
                    #Charisma_Handbook code
            if item_choice=="5":
                if Charisma_Handbook==True:
                    if bank_balance>=181:
                        bank_balance-=180
                        print(f"you bought Charisma Handbook your income is now multiplied by 1.2 its now {working_income*1.4} every time you work a shift")
                        working_income*=1.4
                        Charisma_Handbook=False
                    else:
                        print(f"{YELLOW}not enough money{RESET}")
                        day-=1
                else:
                    print("you allready own Charisma Handbook")
                    day-=1
                    
                    
                    
               #Electric Scooter code
            if item_choice=="6":
                if Electric_Scooter==True:
                    if bank_balance>=251:
                        bank_balance-=250
                        print(f"you bought Electric Scooter your income is now multiplied by 1.2 its now {working_income*1.6} every time you work a shift")
                        working_income*=1.6
                        Electric_Scooter=False
                    else:
                        print(f"{YELLOW}not enough money{RESET}")
                        day-=1
                else:
                    print("you allready own Electric_Scooter")
                    day-=1
            break
        
        #lottery sys
        
    if menu_choice=="3":
        while True:
            lottery_optians=input(f"{GREEN}what amount do you wanna gamble with                                         1.100                       2. 1000                             3.5000                     0.leave    {RESET}")
            
            if lottery_optians=="0":
                day-=1
                break
                
            
            
            
            
            
            if lottery_optians=="1":
                bank_balance-=100
                cheap_random_chance=random.randint(1,100)
                if cheap_random_chance<=40:
                    print(f"{YELLOW}you won the easy lottery {RESET}")
                    bank_balance+=200
                else:
                    print("you've lost the lototery")
            
            
            
            
            if lottery_optians=="2":
                bank_balance-=1000
                mid_lottery_chance=random.randint(1,100)
                if mid_lottery_chance<=20:
                    print(f"{YELLOW}you won the mid lottery {RESET}")
                    bank_balance+=2000
                else:
                    print("you've lost the lototery")
            
            
            
            
            
            if lottery_optians=="3":
                bank_balance-=5000
                high_chance_chance=random.randint(1,100)
                if high_chance_chance<=10:
                    print(f"{YELLOW}you won the high lottery {RESET}")
                    bank_balance+=10000
                else:
                    print("you've lost the lototery")
                    
                    
            break
                
         
         
         
         
         
         
         
         
    if bank_balance>=10000:
        print(f"{ORANGE}YOU'VE WON THE GAME YOUR RICH NOW XDDDDDD{RESET}")
    elif bank_balance==0:
        print(f"{YELLOW} YOU LOST BROKE BOY LOLLLLL{RESET}")
    
        
        
        
        
        
        
        
        
        
        
        
          
          
                    
                    
                      
                            
                        
        
    






       
           
    
                
            
                
            
               
                    
           
            
