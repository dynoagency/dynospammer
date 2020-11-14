
import pyautogui, time
import os
import ctypes
import random
from colored import fg, bg, attr
from random import randint

yes = ["yes", "si", "YES", "SI", "sì", "SÌ", "s", "y", "S", "Y", "confermo", "Confermo", "CONFERMO"]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_string = ['1','2','3','4','5','6','7','8','9']

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9','.', '0']

cyan = fg("cyan")
red = fg("red")
yellow = fg("yellow")
reset = attr("reset")

default_col = fg('cyan')

count_mess = 0


def reset_terminal():
    os.system('cls')

    intro = """

▓█████▄▓██   ██▓ ███▄    █  ▒█████    ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
▒██▀ ██▌▒██  ██▒ ██ ▀█   █ ▒██▒  ██▒▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
░██   █▌ ▒██ ██░▓██  ▀█ ██▒▒██░  ██▒░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
░▓█▄   ▌ ░ ▐██▓░▓██▒  ▐▌██▒▒██   ██░  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▓  ░ ██▒▓░▒██░   ▓██░░ ████▓▒░▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒   ██▒▒▒ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒ ▓██ ░▒░ ░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░ ▒ ▒ ░░     ░   ░ ░ ░ ░ ░ ▒  ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
   ░    ░ ░              ░     ░ ░        ░                 ░  ░       ░          ░      ░  ░   ░     
 ░      ░ ░                                                                                           

"""
    print(default_col + intro + reset)




def spam(spammed_text, number_of_spam, delay, anti_block):

    number_spam = 0  # variable for count how many messages we sended
    anti_block = 0
    count_mess = 0
    many_while = 0
    i = 0

    try:

        for i in range(int(number_of_spam)):

            i += 1
            number_spam += 1
            count_mess += 1
            anti_block += 1

            if count_mess == number_of_spam:
                print("stop")
                spam_while = False
                break

            if count_mess == 25:
                print(default_col + "[+] we are at", number_spam, " messagges" + reset)
                count_mess = 0

            if anti_block == True and anti_block == 300:
                print(default_col + "The spam is interrupted for 30 sec keep your mouse in the chat" + reset)
                time.sleep(30)
                anti_blocco = 0

            time.sleep(float(delay))
            pyautogui.typewrite(spammed_text)
            pyautogui.press("enter")

        print(default_col + f"[*] Spam completed with {number_of_spam} messages!" + reset)
        input("")
        main()

    except KeyboardInterrupt:
        print(default_col + f"[*] Spam terminated with {i} messages sended!" + reset)
        input()
        main()


def random_spam(length, number_of_spam, delay, anti_block):
    length = int(length)
    
    count_mess2 = 0
    count_mess = 0
    block_mess = 0
    i = 0
    try:
        
        random_string = ""
        
        for i in range(number_of_spam):
            
            i += 1
            random_string = ""
            count_mess += 1
            block_mess +1
            count_mess2 += 1

            
            for letter in range(length):
                guess_letter = chars[randint(0, 36)]
                random_string = str(guess_letter) + str(random_string)
            
            
            if block_mess == 300 and anti_block == True:
                print(default_col + "The spam is interrupted for 30 sec keep your mouse in the chat" + reset)
                time.sleep(30)
                block_mess = 0

            if count_mess == 25:
                count_mess = 0
                print(default_col + "[+] we are at", count_mess2, " messagges" + reset)

            
            pyautogui.typewrite(random_string)
            pyautogui.press("enter")
            time.sleep(float(delay))

    

    except KeyboardInterrupt:
        print(default_col + f"[*] Spam terminated with {count_mess} messages sended!" + reset)
        main()

    print(default_col + f"[*] Spam completed with {number_of_spam} messages!" + reset)
    input()
    main()

    

def main():
    
    os.system('cls')
    reset_terminal()

    print(default_col + "[1] Normal spam")
    print(default_col + "[2] Packages spam (work in progress...)")
    print(default_col + "[3] Instructions (work in progress...)")
    print(default_col + "[4] Random spam" + reset)
    print(default_col + "-----------------" + reset)
    print("")
    option = int(input(default_col + "Choose the option: "))
    print(default_col + "-------------------" + reset)

    if option == 1:

        reset_terminal()
        spammed_text = input(default_col + "This is the spammed text: " + reset)
        number_of_spam = input(default_col + "How many times i will spam the text? (default. 100): " + reset)

        if number_of_spam == "":
            number_of_spam = 100

        timer = input(default_col + "Time before the spam (default 10 sec): " + reset)

        if timer == "":
            timer = 10

        delay = float(input(default_col + "Time between messages (es 0.0s): " + reset))
        anti_block = input(default_col + "Do you want antiblock (usefull for whatsapp)(y/n): " + reset)

        if anti_block in yes:
            anti_block = True
        else:
            anti_block = False

        confirm_spam = input(default_col + "Do you confirm the spam (y/n): " + reset)
        print(default_col + "-------------------" + reset)

        if confirm_spam not in yes:
            main()
        else:
            print(default_col + "The spam will starts in ", timer, " sec" + reset)
            time.sleep(int(timer))
            reset_terminal()

            spam(spammed_text, number_of_spam, delay, anti_block)
    

    elif option == 2:
        reset_terminal()
        print(default_col + "[1] 100 mess, 10 sec, 0.1 sec")
        print("[2] 150 mess, 10 sec, 0.1 sec")
        print("[3] 100 mess, 7 sec, 0.0 sec")
        print("[4] 200 mess, 10 sec, 0.1 sec" + reset)

        option2 = int(input(default_col + "Choose the option: "))
        print(default_col + "-------------------" + reset)

        reset_terminal()

        if option2 == 1:
            spammed_text = input(default_col + "This is the spammed text: ")
            timer = 10
            delay = 0.1
            anti_block = input(yellow + "Do you want antiblock (usefull for whatsapp)(y/n): " + reset)

            if anti_block in yes:
                anti_block = True
            else:
                anti_block = False
            print(red + "the spam will starts in ", timer, " sec" + reset)
            time.sleep(int(timer))
            reset_terminal()
            spam(spammed_text, 100, 0.1, anti_block)






    elif option == 4:
        reset_terminal()

        lenght = input(default_col + "Lenght of the random mess (default 4): "+ reset)
        
        if lenght == "":
            lenght = 4
        
    

        number_of_spam = input(default_col + "How many times i will spam the text? (default. 100): " + reset)
        
        if number_of_spam == "":
            number_of_spam = 100
        
        number_of_spam = int(number_of_spam)

        delay = float(input(default_col + "Time between messages (es 0.0s): " + reset))
        anti_block = input(default_col + "Do you want antiblock (usefull for whatsapp)(y/n): " + reset)

        if anti_block in yes:
            anti_block = True
        else:
            anti_block = False

        timer = input(default_col + "Time before the spam (default 10 sec): " + reset)

        if timer == "":
            timer = 10

        confirm_spam = input(default_col + "Do you confirm the spam (y/n): " + reset)
        print(default_col + "-------------------" + reset)

        if confirm_spam not in yes:
            main()
        else:
            print(default_col + "The spam will starts in ", timer, " sec" + reset)
            time.sleep(int(timer))
            reset_terminal()

            random_spam(lenght, number_of_spam, delay, anti_block)        

main()
