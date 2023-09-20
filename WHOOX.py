# Whoox: a tool to find information about a person
# |> usage: <command> <options>

# Libraries & Modules
import os
import platform
import phonenumbers
from phonenumbers import carrier, geocoder
import requests
import csv

# Initialization
currentOS = platform.platform()

class whoox:
    fontClassic = "██╗    ██╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗\n██║    ██║██║  ██║██╔═══██╗██╔═══██╗╚██╗██╔╝\n██║ █╗ ██║███████║██║   ██║██║   ██║ ╚███╔╝\n██║███╗██║██╔══██║██║   ██║██║   ██║ ██╔██╗\n╚███╔███╔╝██║  ██║╚██████╔╝╚██████╔╝██╔╝ ██╗\n ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝"
    fontGhost = " █     █░ ██░ ██  ▒█████   ▒█████  ▒██   ██▒\n▓█░ █ ░█░▓██░ ██▒▒██▒  ██▒▒██▒  ██▒▒▒ █ █ ▒░\n▒█░ █ ░█ ▒██▀▀██░▒██░  ██▒▒██░  ██▒░░  █   ░\n░█░ █ ░█ ░▓█ ░██ ▒██   ██░▒██   ██░ ░ █ █ ▒\n░░██▒██▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ ▒██▒\n░ ▓░▒ ▒   ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░\n  ▒ ░ ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░░   ░▒ ░\n  ░   ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░    ░  \n    ░     ░  ░  ░    ░ ░      ░ ░   ░    ░  "
    fontBig = "▄█     █▄     ▄█    █▄     ▄██████▄   ▄██████▄  ▀████    ▐████▀\n███     ███   ███    ███   ███    ███ ███    ███   ███▌   ████▀\n███     ███   ███    ███   ███    ███ ███    ███    ███  ▐███\n███     ███  ▄███▄▄▄▄███▄▄ ███    ███ ███    ███    ▀███▄███▀\n███     ███ ▀▀███▀▀▀▀███▀  ███    ███ ███    ███    ████▀██▄\n███     ███   ███    ███   ███    ███ ███    ███   ▐███  ▀███\n███ ▄█▄ ███   ███    ███   ███    ███ ███    ███  ▄███     ███▄\n ▀███▀███▀    ███    █▀     ▀██████▀   ▀██████▀  ████       ███▄"
    fontMagic = "\n▄▄▌ ▐ ▄▌ ▄ .▄            ▐▄• ▄ \n██· █▌▐███▪▐█▪     ▪      █▌█▌▪\n██▪▐█▐▐▌██▀▐█ ▄█▀▄  ▄█▀▄  ·██· \n▐█▌██▐█▌██▌▐▀▐█▌.▐▌▐█▌.▐▌▪▐█·█▌\n ▀▀▀▀ ▀▪▀▀▀ · ▀█▄▀▪ ▀█▄▀▪•▀▀ ▀▀"
    
    if currentOS.lower().startswith("windows"):
        default = "\u001b[34m"+fontMagic+"\u001b[0m"+"\n" # 30 -> semi-transparent, 31 -> red, 32 -> green, 33 -> yellow, 34 -> blue, 35 -> pink, 36 -> cyan, 37 -> opposite semi transparent
    else:
        default = "\u001b[35m"+fontMagic+"\u001b[0m"+"\n"
    input = "\u001b[37m"+"whoox~$ "+"\u001b[0m"

    titlePrefix = "\u001b[34m"+"[*] "+"\u001b[0m"
    infoPrefix = "\u001b[37m"+"["+"\u001b[0m"+  "\u001b[35m"+"?"+"\u001b[0m"  +"\u001b[37m"+"]"+"\u001b[0m"
    errorPrefix = "\u001b[37m"+"["+"\u001b[0m"+  "\u001b[31m"+"!"+"\u001b[0m"  +"\u001b[37m"+"]"+"\u001b[0m"

if currentOS.lower().startswith("windows") == False and currentOS.lower().startswith("linux") == False:
    print(whoox.default+"\n{whoox.errorPrefix}Error, unsupported OS.")
    exit()
else:
    if currentOS.lower().startswith("windows"):
        os.system("cls")
    else:
        os.system("clear")
    print(whoox.default)

# Code
while True:
    try:
        # Command input
        command = input(whoox.input)

        # Commands code
        try:
            # System commands
            if command == "clear":
                if currentOS.lower().startswith("windows"):
                    os.system("cls")
                else:
                    os.system("clear")
                print(whoox.default)
            # Custom commands
            elif command == "--help" or command == "-h" or command == "help":
                print(f"{whoox.titlePrefix} Basic Commands:")
                print(f"{whoox.infoPrefix} clear -> Clears the terminal. Usage -> 'clear'.")
                print()
                print(f"{whoox.titlePrefix} Identity Search Commands:")
                print(whoox.infoPrefix+" {phoneNumber} -> Displays information about a phone number. Usage -> '{phoneNumber}'")
            elif command.isdigit() or command.startswith("+"):
                if command.startswith("+") == False:
                    command = "+"+command
                phoneNumber = phonenumbers.parse(command)
                valid = phonenumbers.is_valid_number(phoneNumber)
                country = geocoder.description_for_number(phoneNumber, 'en')
                provider = carrier.name_for_number(phoneNumber, 'en')
                localFormat = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.NATIONAL)
                internationalFormat = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                print(f"{whoox.infoPrefix} Valid: {valid}")
                print(f"{whoox.infoPrefix}Provider: {provider}")
                print(f"{whoox.infoPrefix}Country: {country}")
                print(f"{whoox.infoPrefix}Raw Number: {command}")
                print(f"{whoox.infoPrefix}Local Format: {localFormat}")
                print(f"{whoox.infoPrefix}International Format: {internationalFormat}")
            
            # After command space inserter
            if command != "" and command != "clear":
                print()
        except:
            print(f"{whoox.errorPrefix}Error, command '{command}' could not be executed. Check the syntax of the command.")
    # Clear terminal shortcut
    except KeyboardInterrupt:
        if currentOS.lower().startswith("windows"):
            os.system("cls")
        else:
            os.system("clear")
        print(whoox.default)
