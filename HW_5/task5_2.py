#Создайте программу для игры с конфетами человека против человека.
# Первый ход определяется жеребьевкой.
# За первый ход можно забрать не более чем 28 конфет.
# Все конфеты опонента достаются сделавшему последний ход.

candy = 2021
player1 = True
print(candy,'Сandy is on the table\n')

while (candy > 0):
    if(player1):
        print("Fist player goes")
        player1 = False
    else:
        print("Second player goes")
        player1 = True

    candy-=int(input("Inpit number of 1 to 28\n"))
    print(candy, "candy laft on the table\n")
    
    if (not player1):
        print("Player1 wins!\n")
    else:
        print("Player2 wins!\n")   
