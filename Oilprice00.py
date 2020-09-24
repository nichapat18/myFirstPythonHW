while True :
    print("            MENU  ")
    print(" GASOLINE 95 price 29.16 bath")
    print(" GASOLINE 91 price 25.30 bath")
    print(" GASOHOL  91 price 21.68 bath")
    print(" GASOHOL E20 price 20.2  bath")
    print(" GASOHOL  95 price 21.2 bath")
    print(" DIESEL      price 21.1 bath")
    print("Select 'Price to liter' or 'Liter to price' ")
    a = (input("select = "))
    b = (input("Oil select = "))
    c = int(input("Amount = "))
    d = b.upper ()
    e = 0
    Oil = ['Gasoline 95','Gasoline 91','Gasohol 91','Gasohol E20','Gasohol 95','Diesel']
    Price = (29.16,25.30,21.68,20.2,21.2,21.1)
    if "Price to liter" in a :
        if "GASOLINE 95" in d :
            e = e+(c/29.16)
            print ("Oil" , '%.2f' %e , "Liter")
        elif "GASOLINE 91" in d :
            e = e+(c/25.30)
            print ("Oil" , '%.2f' %e , "Liter")
        elif "GASOHOl 91" in d :
            e = e+(c/21.68)
            print ("Oil" , '%.2f' %e , "Liter")
        elif "GASOHOL E20" in d :
            e = e+(c/20.2)
            print ("Oil" , '%.2f' %e , "Liter")
        elif "GASOHOL 95" in d :
            e = e+(c/21.2)
            print ("Oil" , '%.2f' %e , "Liter")
        elif "DIESEL" in d :
            e = e+(c/21.1)
            print ("Oil" , '%.2f' %e , "Liter")
        else  :
            print ("Please selice new oil type")
    elif "Liter to price" in a :
        if "GASOLINE 95" in d :
            e = e+(c*29.16)
            print("price" , e , "Bath")
        elif "GASOLINE 91" in d :
            e = e+(c*25.30)
            print("price" , e , "Bath")
        elif "GASOHOL  91" in d :
            e = e+(c*21.68)
            print("price" , e , "Bath")
        elif "GASOHOL E20" in d :
            e = e+(c*20.2)
            print("price" , e , "Bath")
        elif "GASOHOL 95" in d :
            e = e+(c*21.2)
            print("price" , e , "Bath")
        elif "DIESEL" in d :
            e = e+(c*21.1)
            print("price" , e , "Bath")
        else :
            print("Please select a new liter type")
    else :
        print("Please calculate again")
        while True :
            print("spacebar back to menu")
            g = ""
            h = input( )
            if not g in h :
                break
