print('''                          v.._                       _..v                               
                                    )\ '-.                 .-' /(                                
                                    : \   :               :   / :                                
                                     '.\   '.    ._.    .''  /.'                                 
                                       :\    i.-'   '-.i    /:                                   
                                        '\ .-'         '-. /'                                    
      _..eeaa.._                          :               :                          _..eeaa.._  
     i"T$P^T888aaa.._                    /   .-'\. ./'-.   \                    _..eee8887^T$P"i 
      '.     "T888888aa.                /   /  ()/ \()  \   \                .ee8888887"     .'  
        '      '"T8888.88a             :    '._.' . '._.'    :             e88.88887"'      '    
         i           "T8888a.          | .i'     / \     'i. |          .e8888P"           i     
         :             "T8888a.        |  '.     '-'     .'  |        .e88867"             :     
          i               T8888a.      :    i__..-=-..__i    :      .e8888P               i      
          :                "T8888a.     '.   \/       \/   .'     .e8888P"                :      
          :                  "88888a.     i-.           .-i     .e88888"                  :      
           i                  "T88888a._./   '-..___..-'   \._.e88888P"                  i       
           :                     "T88888P                   Y88888P"                     :       
           :                       'T88"                     "88P'                       :       
            i                    .__.:                         :.__.                    i        
            :               _.--'   :                           :   '--._               :        
             :         _.--'        |                           |        '--._         :         
             i___...--'             :                           :             '--...___i         
                                     :                         :                                 
                                     '.                       .'                                 
                                      '.                     .'                                  
                                        ''                 .' .                                  
                                         Y'-..         ..-'Y                                     
                                        :     '-.___.-'     :                                    
                                        |      .'87"'.      |                                    
                                        :     :  ^.   :     :                                    
                                         :   :   "^.   :   :        ._.                          
                                         |   |    "^.  |   |        )&(                          
                                         :   :      "'e:   :    .aP" ^                           
                                          : :           : : "TP"                                 
                                          | |           | |                                      
                                          : :           : :                                      
                                         /   )         (   \          fsc                        
                                      _.'   /           \   '._                                  
                                    .' _ . /             \     '.                                
                                   (_i-i/_i               i_\i-i_)                               
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You are at a crossroads. Do you want to go 'left' or 'right'? ").lower()
if choice1 == "left":
    choice2 = input("You come to a lake. Do you 'wait' for a boat or 'swim' across? ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at a house with three doors: 'red', 'blue', or 'yellow'. Which do you choose? ").lower()
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("You enter a room of fire. Game over!")
        elif choice3 == "blue":
            print("You are attacked by a monster. Game over!")
        else:
            print("You picked a door that doesn't exist. Game over!")
    else:
        print("You are eaten by a shark. Game over!")
else:
    print("You fell into a hole. Game over!")

