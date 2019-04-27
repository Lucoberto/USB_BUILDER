import os, sys, time

opciones = "startmenu"
def startmenu():
    global opciones
    os.system("clear")
    logo2="""
 _   _ ___________  ______ _   _ _____ _    ______ ___________ 
| | | /  ___| ___ \ | ___ \ | | |_   _| |   |  _  \  ___| ___ \*
| | | \ `--.| |_/ / | |_/ / | | | | | | |   | | | | |__ | |_/ /
| | | |`--. \ ___ \ | ___ \ | | | | | | |   | | | |  __||    / 
| |_| /\__/ / |_/ / | |_/ / |_| |_| |_| |___| |/ /| |___| |\ \ 
 \___/\____/\____/  \____/ \___/ \___/\_____/___/ \____/\_| \_|
                
____________[<!>]V1.0.1 Developed by @lucoberto[<!>]_____________
                          [1] Repair USB!
                          [2] Help!
                          [3] Exit!
"""
    print(logo2)
    op = input("Choose the most appropriate option: ")
    if op == "1":
        opciones = "reparacion"
    elif op == "2":
        opciones = "ayuda"
    elif op == "3":
        sys.exit()
def ayuda():
    global opciones
    ayuda="""-> This program tries to repair basic errors at the logical level in the USB memory (s).
    -> We recommend making a backup.
    -> We do not take care of the damages caused by the program.
    -> Thanks for trusting us."""
    print(ayuda)
    os.system("pause")
    opciones = "startmenu"
def reparacion():
    global opciones
    os.system("clear")
    os.system("CHKDSK F: /X /F")
    os.system("CHKDSK G: /X /F")
    os.system("CHKDSK H: /X /F")
    os.system("CHKDSK I: /X /F")
    os.system("CHKDSK J: /X /F")
    os.system("clear")
    logo=""" 
______ _____  ___ ________   __  _____ _   _ _____ _   _ _    ______   _    _  ___________ _   ___ _ _ 
| ___ \  ___|/ _ \|  _  \ \ / / /  ___| | | |  _  | | | | |   |  _  \ | |  | ||  _  | ___ \ | / / | | |
| |_/ / |__ / /_\ \ | | |\ V /  \ `--.| |_| | | | | | | | |   | | | | | |  | || | | | |_/ / |/ /| | | |
|    /|  __||  _  | | | | \ /    `--. \  _  | | | | | | | |   | | | | | |/\| || | | |    /|    \| | | |
| |\ \| |___| | | | |/ /  | |   /\__/ / | | \ \_/ / |_| | |___| |/ /  \  /\  /\ \_/ / |\ \| |\  \_|_|_|
\_| \_\____/\_| |_/___/   \_/   \____/\_| |_/\___/ \___/\_____/___/    \/  \/  \___/\_| \_\_| \_(_|_|_)
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