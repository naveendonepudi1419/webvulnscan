import socket
import os
import requests
import platform

def back():
    print()
    back = input('\033[92mDo you want to continue? [Yes/No]: ')
    if back[0].upper() == 'Y':
        print()
        iseeverything()
    elif back[0].upper() == 'N':
        print('\033[92mRemember https://github.com/naveendonepudi1419')
        exit
    else:
        print('\033[92m?')
        exit

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def bill():
    clear()
    print("""\033[92m   
              _               
__      _____| |____   ___   _| |_ __  ___  ___ __ _ _ __  
\ \ /\ / / _ \ '_ \ \ / / | | | | '_ \/ __|/ __/ _` | '_ \ 
 \ V  V /  __/ |_) \ V /| |_| | | | | \__ \ (_| (_| | | | |
  \_/\_/ \___|_.__/ \_/  \__,_|_|_| |_|___/\___\__,_|_| |_|
                                                           

 Website Vulnerability Scanner""")
    print()

def banner():
    print("""\033[92m
 1) NIKTO                 
 2) Grabber               
 3) joomscan              
 4) About webinfo            
 5) Exit Out Of Here""")         

    print()

def iseeverything():
    try:
        what = input('\033[92mDo you want to collect information of a website or IP address? [website/IP]: ')
        if what[0].upper() == 'W':
            victim = input('Enter the website address: ')
            banner()
        elif what[0].upper() == 'I':
            victim = input('Enter the IP address (or domain to get IP address of that domain): ')
            victim = socket.gethostbyname(victim)
            print('The IP address of target is:',victim)
            banner()
        else:
            print('?')
            iseeverything()

        choose = input('What information would you like to collect? (1-20): ')

        if choose == '1':
            clear()
            os.system('nikto -h '+victim)
            back()

        elif choose == '2':
            clear()
            os.system('grabber --spider 1 --sql --xss --url '+victim)
            back()

        elif choose == '3':
            clear()
            os.system('joomscan -u '+victim)
            back()


        elif choose == '4':
            print("""\033[webvulnscan 1 - Website Vulnerability Scanner

AUTHOR: https://github.com/naveendonepudi1419
        https://twitter.com/DonepudiNaveen""")
            back()

        elif choose == '5':
            exit

        else:
            print('?')
            iseeverything()
            
    except socket.gaierror:
        print('Name or service unknown!\033[93m')
        print()
        iseeverything()
    except UnboundLocalError:
        print('The information you entered is incorrect')
        print()
        iseeverything()
    except requests.exceptions.ConnectionError:
        print('Your Internet Offline')
        exit
    except IndexError:
        print('?')
        print()
        iseeverything()

bill()
iseeverything()


