check = True
while check:
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 35 + "WELCOME" + " " * 36 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)
    i = input("Enter")

    print("#" * 80) #เลือกชนิดน้ำมัน
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 35 + "MENU OIL" + " " * 35 + "#")
    print("#" + " " * 23 + "1.Gasoline 95  Price 29.16 Baht" + " " * 24 + "#")
    print("#" + " " * 23 + "2.Gasoline 91  Price 25.30 Baht" + " " * 24 + "#")
    print("#" + " " * 23 + "3.Gasohol  91  Price 21.68 Baht" + " " * 24 + "#")
    print("#" + " " * 23 + "4.Gasohol E20  Price 20.2  Baht" + " " * 24 + "#")
    print("#" + " " * 23 + "5.Gasohol  95  Price 21.2  Baht" + " " * 24 + "#")
    print("#" + " " * 23 + "6.Diesel       Price 21.1  Baht" + " " * 24 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)
    s = input("Select oil 1-6 : ")

    print("#" * 80) #เลือกราคาเป็นลิตรหรือลิตรเป็นราคา
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 36 + "SELECT" + " " * 36 + "#")
    print("#" + " " * 31 + "1.price to liter" + " " * 31 + "#")
    print("#" + " " * 31 + "2.liter to price" + " " * 31 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)
    n = input("Select 1.price to liter or 2.liter to price : ")
    pricetoliter = "1"
    litertoprice = "2"
    if pricetoliter in n:
        l = int(input("price =  "))
    elif litertoprice in n:
        l = int(input("liter =  "))
    g = n.upper()
    e = 0
    if pricetoliter in n: #คำนวนราคาเป็นลิตร
        if "1" in g:
            e = e + (l / 29.16)
            print("oil", '%.2f' % e, "Liter")
        elif "2" in g:
            e = e + (l / 25.30)
            print("oil", '%.2f' % e, "Liter")
        elif "3" in g:
            e = e + (l / 21.68)
            print("oil", '%.2f' % e, "Liter")
        elif "4" in g:
            e = e + (l / 20.2)
            print("oil", '%.2f' % e, "Liter")
        elif "5" in g:
            e = e + (l / 21.2)
            print("oil", '%.2f' % e, "Liter")
        elif "6" in g:
            e = e + (l / 21.1)
            print("oil", '%.2f' % e, "Liter")
        else:
            print("Please calculate again")
    elif litertoprice in n: #คำนวนลิตรเป็นราคา
        if "1" in g:
            e = e + (l * 29.16)
            print("price", e, "Baht")
        elif "2" in g:
            e = e + (l * 25.30)
            print("price", e, "Baht")
        elif "3" in g:
            e = e + (l * 21.68)
            print("price", e, "Baht")
        elif "4" in g:
            e = e + (l * 20.2)
            print("price", e, "Baht")
        elif "5" in g:
            e = e + (l * 21.2)
            print("price", e, "Baht")
        elif "6" in g:
            e = e + (l * 21.1)
            print("price", e, "Baht")
        else:
            print("Please calculate again")
    else:
        print("Please calculate again")
        
    print("#" * 80) #เลือกว่าจะ Exit หรือ Back to menu
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 36 + "SELECT" + " " * 36 + "#")
    print("#" + " " * 30 + "0.Exit the program" + " " * 30 + "#")
    print("#" + " " * 31 + "1.Back the menu" + " " * 32 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)
    print("0.Exit the program or 1.back the menu")
print(" 0. Exit or 1. Back to menu : ")
p = '0'
while (p not in '01') :
        p = input()
        if (p == '0'):
                check = False
