def hőmérséklet():
    homersekletC =int(input("Kérek egy hőmérséklet értéket: "))
    
#selekcios utasitások
#globalis valtozó
    if homersekletC <= 0:
        homerseklet=0
        #lokális
        print("Szilárd halnazállapot.") #igaz ág

    elif homersekletC < 100:
        print("Folyakony halmazállapot.")

    else:
        print("Lénemú halnazállapot.")  #hamis ág     

hőmérséklet()   

#eljárás 
# , ha van benne return függvény!