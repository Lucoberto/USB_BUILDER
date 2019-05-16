import os, sys, time

opciones = "startmenu"
def startmenu():
    os.system("clear")
    global opciones  
    logo2="""
 _____ _____ _____    _____ _____ _____ __    ____  _____ _____ 
|  |  |   __| __  |  | __  |  |  |     |  |  |    \|   __| __  |
|  |  |__   | __ -|  | __ -|  |  |-   -|  |__|  |  |   __|    -|
|_____|_____|_____|  |_____|_____|_____|_____|____/|_____|__|__|
                
____________[<!>]V1.0.5 Developed by @lucoberto[<!>]_____________
                          [1] Repair USB!
                          [2] Help!
                          [3] Exit!
"""
    print(logo2)
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
    time.sleep(2.0)
    os.system("CHKDSK G: /X /F")
    time.sleep(2.0)
    os.system("CHKDSK H: /X /F")
    time.sleep(2.0)
    os.system("CHKDSK I: /X /F")
    time.sleep(2.0)
    os.system("CHKDSK J: /X /F")
    time.sleep(2.0)
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
