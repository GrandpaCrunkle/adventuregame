import colorama
import time
colorama.init()
blue = '\033[32m'
red = '\033[31m'
reset = '\033[0m' 

print(blue + "       .                                                      .")
print(     "         .n                   .                 .                  n.")
print(     "    .   .dP                  dP                   9b                 9b.    .")
print("   4    qXb         .       dX                     Xb       .        dXp     t")
print("  dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb")
print("  9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP")
print("   9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP")
print("    `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'")
print("      `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'")
print("          ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~")
print("                          )b.  .dbo.dP'`v'`9b.odb.  .dX(")
print("                        ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.")
print("                       dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb")
print("                      dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb")
print("                      9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP")
print("                       `'      9XXXXXX(   )XXXXXXP      `'")
print("                                XXXX X.`v'.X XXXX")
print("                                XP^X'`b   d'`X^XX")
print("                                X. 9  `   '  P )X")
print("                                `b  `       '  d'")
print("                                 `             '" + reset)

print('Welcome to treasure island please, please choose a path')

def treasure_game():
    while True:
     try:
        first_choice = int(input(blue +'You encounter a broke bridge, do you go left or right?\n1.Left 2.Right\n'+reset))
        if first_choice == 1:
                print('You turn left and run down the path.')
        else: 
            print('You trip and fall over a broken piece of the bridge landing on a jagged piece of metal')
            print(red + 'Game over.')
            return      
        second_choice = int(input(blue +'You encounter a goblin do you stay and fight or turn and run?\n1. Fight 2. Turn and Run\n'+reset))
        if second_choice == 2:
                print('You turn and run')
        else:
                print('The goblin stabs you' + red +'\nGame Over')
                return
        third_choice = (int(input(blue +'You find a wounded man on the road, do you \n 1. Help him 2.You leave the wounded man 3.You call for help\n'+reset)))
        if third_choice == 1:
               print('You save the wounded man rewarding you with gold')
               time.sleep(3)
        elif third_choice == 3:
               print('The bandit who was nearby heard the cry for help, rushes over and stabs you.')
               print(red + 'Game Over')
               time.sleep(3)
        else:
               print('A guard catches you near the old man and accosts you, you jerk suddenly and he impales you with his sword')
               print(red + 'Game Over')  
               time.sleep(3)
     except ValueError:
           print('Please enter a valid input')
           time.sleep(3)
                       
                   
treasure_game()
    
