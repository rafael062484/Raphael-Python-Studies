animals = [
    """
    Switching on the camera in the camel habitat...
     ___.-''''-.
    /___  @    |
    ',,,,.     |         _.'''''''._
         '     |        /           \\
         |     \\    _.-'             \\
         |      '.-'                  '-.
         |                               ',
         |                                '',
          ',,-,                           ':;
               ',,| ;,,                 ,' ;;
                  ! ; !'',,,',',,,,'!  ;   ;:
                 : ;  ! !       ! ! ; ;    . ;
                 ; ;   ! !      ! !  ;   ; ;
                ; ;    ! !     ! !   ; ;   ;
                ; ;    !,!   !,!     ',,;
                /_I      L_I   L_I     /_I
    """,
    """
    Switching on the camera in the lion habitat...
                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
,MM:.    .'.-'   .'     ;     `\\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \\  ; ;MMMMMMMMMMW^``; __|
           /   .'            ; ;         )  )`{  \\ `"^W^`,   \\  :
          /  .'             /  (       .'  /     Ww._     `.  `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
        (--, )                `,_ / `) \\"")      ^"      `-, -;"\\:
    """,
    """
    Switching on the camera in the deer habitat...
       /|       |\\
    `__\\\\       //__'
       ||      ||
     \\__`\\     |'__/
       `_\\\\   //_'
       _.,:---;,._
       \\_:     :_/
         |@. .@|
         |     |
         ,\\.-./ \\
         ;;`-'   `---__________-----.-.
         ;;;                         \_\\
         ';;;                         |
          ;    |                      ;
           \\   \\     \\        |      /
            \\_, \\    /        \\     |\\
              |';|  |,,,,,,,,/ \\    \\ \\_
              |  |  |           \\   /   |
              \\  \\  |           |  / \\  |
               | || |           | |   | |
               | || |           | |   | |
               | || |           | |   | |
               |_||_|           |_|   |_|
              /_//_/           /_/   /_/
    """,
    """
    Switching on the camera in the goose habitat...
    
                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \\    \\
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \\
 <_  `     (  <`<            \\              `-._\\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
    """,
    """
    Switching on the camera in the bat habitat...
    _________________               _________________
     ~-.              \\  |\\___/|  /              .-~
         ~-.           \\ / o o \\ /           .-~
            >           \\\\  W  //           <
           /             /~---~\\             \\
          /_            |       |            _\\
             ~-.        |       |        .-~
                ;        \\     /        i
               /___      /\\   /\\      ___\\
                    ~-. /  \\_/  \\ .-~
                       V         V
    """,
    """
    Switching on the camera in the rabbit habitat...
             ,
            /|      __
           / |   ,-~ /
          Y :|  //  /
          | jj /( .^
          >-"~"-v"
         /       Y
        jo  o    |
       ( ~T~     j
        >._-' _./
       /   "~"  |
      Y     _,  |
     /| ;-"~ _  l
    / l/ ,-"~    \\
    \\\\//\\/      .- \\
     Y        /    Y
     l       I     !
     ]\\      _\\    /"\\
    (" ~----( ~   Y.  )
    """
]

def habitat():
    while True:
        habitat_number = input("Please enter the number of the habitat you would like to view (or type 'exit' to quit):\n")
        if habitat_number == 'exit':
            print("See you later!")
            break
        habitat_number = int(habitat_number)
        
        if 0 <= habitat_number < len(animals):
            print(animals[habitat_number])
        else:
            print("Invalid habitat number. Please try again.")
        print("---")

habitat()


