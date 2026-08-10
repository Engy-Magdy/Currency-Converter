currency_dic={
    "USD":1.0,
    "EGP":49.88,
    "EUR":0.87,
    "RMB":6.75
}
def conversion(amount,currency,converted_currency):
                  return amount/currency_dic[currency]*currency_dic[converted_currency]
def clear():
    import os
    os.system("cls"if os.name=="nt" else "clear")


ascii__art=("""
Welcome to 'Currency Converter':

⠀⠀ ||====================================================================||
   ||//$\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                  \\$//||
   ||<< /        /$\\             // ____ \\\\                           |>>||
   ||>>|  12    //L\\            // ///..) \\\\         L38036133B   12  |<<||
   ||<<|        \\ //           || <||  >\\ ||                          |>>||
   ||>>|         \\/            ||  $$ --/  ||        One Hundred      |<<||
||====================================================================||>||
||//$\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\\\$//||>|||
||<<//        /$\\              // ____ \\\\                       |>>||
||>>|  12    //L\\            // ///..) \\\\         L38036133B   1|<<||
||<<|        \\ //           || <||  >\\ ||                       |>>||
||>>|         \\/            ||  $$ --/  ||        One Hundred   |<<||
||<<|      L38036133B        *\\  |\\_/  //* series               |>>||
||>>|  12                     *\\/___\\_//*   1989                |<<||
||<<\\      Treasurer     ______/Franklin\\________   Secretary 12|>>||
||//$\\                 ~|UNITED STATES OF AMERICA|~             |\\\\||
||(100)===================  ONE HUNDRED DOLLARS ==============(100)||
||\\$//\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\\\/\\||
||=================================================================||

_______________________________________________________________________________________________________________________

USD: 1.0
EUR: 0.87
EGP: 49.88
RMB: 6.75

  """)

 

while True:
     print(ascii__art)
     the_currency=input("Chosse a currency to convert from: "). upper()
     the_amount= float(input("Enter the amount: "))
     confirm=input(f"You entered {the_amount} {the_currency}. Confirm? (Y/N):").upper()
     if confirm!="Y":
        continue
     else:
        clear()
        print(ascii__art)
        currency_to_convert=input("choose a currency to convert to: ").upper()
        import time
        print("Analyzing your request.....Please, wait.")
        time.sleep(3)
        print(f"Checking for {currency_to_convert}'s best rates available.....Please, wait.")
        time.sleep(3)
        print(f"Getting a discount price for{the_currency}.....Please wait ")
        clear()
        print(f"Preparing the deal from {the_currency} to {currency_to_convert}.....Please wait.")
        time.sleep(3)
        if the_currency not in currency_dic or currency_to_convert not in currency_dic :
            print("Invalid currency.Conversion canceled")
           

        else:
             exchange_rate=conversion(1,the_currency,currency_to_convert)
             total_amount=conversion(the_amount,the_currency,currency_to_convert)
             print(f"Exchange Rate: 1 {the_currency} = {round(exchange_rate,3)}  {currency_to_convert} ")
             print(f"{the_amount} {the_currency} is equal to {round(total_amount,3)} {currency_to_convert}")
             accepting=input("Did you accept this transaction? (Y/N): ").upper()
             if accepting!="Y":
                  print("Transaction canceled.")
             else:
                  print("Transaction completed") 
        another_conversion=input("Do you perform another conversion? (Y/N):").upper()
        if another_conversion!='Y':
              print("Exiting.....")
              break
             
             
           
  
