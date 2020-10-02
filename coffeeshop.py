water = 400
milk = 540
coffeebeans = 120
disposablecups = 9
money = 550

def printAll() :
	print(" The coffee machine has : ")
	print(water," of water ")
	print(milk," of milk ")
	print(coffeebeans," of coffee beans ")
	print(disposablecups," of disposable cups ")
	print(money," of money ")

printAll()
while True :

        a = ' '
        while not(a in ["buy" , "fill" , "take"]) :
                a = input("Write action (buy , fill , take) :\n>")
        if a == 'buy' :
                b = 0
                while not (b in ["1" ,"2" ,"3"]) :
                        b = input("What do you want to buy? 1 - Espresso , 2 - Latte , 3 - cappucino :\n")
                if b == '1' :
                        water = water - 250
                        milk = milk - 0
                        coffeebeans = coffeebeans - 16
                        disposablecups = disposablecups - 1
                        money = money + 7
                if b == '2' :
                        water = water - 350
                        milk = milk - 75
                        coffeebeans = coffeebeans - 20
                        disposablecups = disposablecups - 1
                        money = money + 7
                if b == '3' :
                        water = water - 200
                        milk = milk - 100
                        coffeebeans = coffeebeans - 12
                        disposablecups = disposablecups - 1
                        money = money + 6
                printAll()
        if a == 'fill' :
                water += int(input('Write how many ml of water do you want to add :\n> '))
                milk += int(input('Write how many ml of milk do you want to add :\n> '))
                coffeebeans += int(input('Write how many grams of coffeebeans do you want to add :\n> '))
                disposablecups += int(input('Write how many disposable cups do you want to add :\n> '))
                printAll()

        if a == 'take' :
                print('I gave $' , money)
                money = 0
                printAll()

        c = ''
        while not(c in ["1" , ["2"]) :
                c = input("1 - Exit , 2 - Return :\n> ")
        if c == '1' :
                  break
