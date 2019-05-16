import os, sys, time, random

opciones = "startmenu"
def startmenu():
    os.system("clear")
    global opciones  
    logo2="""
 _____ _____ _____    _____ _____ _____ __    ____  _____ _____ 
|  |  |   __| __  |  | __  |  |  |     |  |  |    \|   __| __  |
|  |  |__   | __ -|  | __ -|  |  |-   -|  |__|  |  |   __|    -|
|_____|_____|_____|  |_____|_____|_____|_____|____/|_____|__|__|"""
    logo3="""
 _     ____  ____    ____  _     _  _     ____  _____ ____ 
/ \ /\/ ___\/  __\  /  __\/ \ /\/ \/ \   /  _ \/  __//  __\*
| | |||    \| | //  | | //| | ||| || |   | | \||  \  |  \/|
| \_/|\___ || |_\\  | |_\\| \_/|| || |_/\| |_/||  /_ |    /
\____/\____/\____/  \____/\____/\_/\____/\____/\____\\_/\_\ """
    logo4="""
 _    _  _____ ____    ____  _    _ _____ _      _____  ______ _____  
| |  | |/ ____|  _ \  |  _ \| |  | |_   _| |    |  __ \|  ____|  __ \ 
| |  | | (___ | |_) | | |_) | |  | | | | | |    | |  | | |__  | |__) |
| |  | |\___ \|  _ <  |  _ <| |  | | | | | |    | |  | |  __| |  _  / 
| |__| |____) | |_) | | |_) | |__| |_| |_| |____| |__| | |____| | \ \ 
 \____/|_____/|____/  |____/ \____/|_____|______|_____/|______|_|  \_\ """
    logo5="""
 __  __  ___  ____    ____  __  __  ____  __    ____  ____  ____ 
(  )(  )/ __)(  _ \  (  _ \(  )(  )(_  _)(  )  (  _ \( ___)(  _ \*
 )(__)( \__ \ ) _ <   ) _ < )(__)(  _)(_  )(__  )(_) ))__)  )   /
(______)(___/(____/  (____/(______)(____)(____)(____/(____)(_)\_)"""
    logo6="""
 _   _ ___________  ______ _   _ _____ _    ______ ___________ 
| | | /  ___| ___ \ | ___ \ | | |_   _| |   |  _  \  ___| ___ \*
| | | \ `--.| |_/ / | |_/ / | | | | | | |   | | | | |__ | |_/ /
| | | |`--. \ ___ \ | ___ \ | | | | | | |   | | | |  __||    / 
| |_| /\__/ / |_/ / | |_/ / |_| |_| |_| |___| |/ /| |___| |\ \ 
 \___/\____/\____/  \____/ \___/ \___/\_____/___/ \____/\_| \_|"""
    menuopciones="""
____________[<!>]V1.0.7 Developed by @lucoberto[<!>]_____________
                          [1] Repair USB!
                          [2] Help!
                          [3] Exit!"""
    logos=random.choice([logo2,logo3,logo4,logo5,logo6])
    print(logos)
    print(menuopciones)
    print("Choose the most appropriate option.")
    op = input("Usb@usb$~> ")
    if op == "1":
        opciones = "reparacion"
    elif op == "2":
        opciones="ayuda"
    elif op == "3":
        sys.exit()
def ayuda():
    global opciones
    ayuda1="""-> This program tries to repair basic errors at the logical level in the USB memory (s).
    -> We recommend making a backup.
    -> We do not take care of the damages caused by the program.
    -> Thanks for trusting us."""
    print(ayuda1)
    os.system("pause")
    opciones = "startmenu"
def reparacion():
    global opciones
    os.system("clear")
    os.system("CHKDSK F: /X /F")
    time.sleep(1.0)
    os.system("CHKDSK G: /X /F")
    time.sleep(1.0)
    os.system("CHKDSK H: /X /F")
    time.sleep(1.0)
    os.system("CHKDSK I: /X /F")
    time.sleep(1.0)
    os.system("CHKDSK J: /X /F")
    time.sleep(1.0)
    os.system("clear")
    logo=""" 
                               __ __ __ 
 _____ _____ _____ ____  __ __|  |  |  |
| __  |   __|  _  |    \|  |  |  |  |  |
|    -|   __|     |  |  |_   _|__|__|__|
|__|__|_____|__|__|____/  |_| |__|__|__|
     """
    print(logo)
    time.sleep(5.0)
    opciones = "startmenu"
def operaciones():
    try:
        while True:
            if opciones == "startmenu":
                startmenu()
            elif opciones == "reparacion":
                reparacion()
            elif opciones == "ayuda":
                ayuda()
    except KeyboardInterrupt:
        sys.exit()
if __name__=="__main__":
    operaciones()
