import os, json, time
#import keyboard

def banner():
    os.system("clear")
    logo = """
╔═╗╦ ╦╔╦╗╔═╗   ╔═╗╔═╗╔╦╗╦ ╦╔═╗
╠═╣║ ║ ║ ║ ║───╚═╗║╣  ║ ║ ║╠═╝
╩ ╩╚═╝ ╩ ╚═╝   ╚═╝╚═╝ ╩ ╚═╝╩  
"""
    print(logo,"\nCreated by.mobile-mining\n")
    print("---------------------------------------------------")
    print("\033[96mสนับสนุนนักพัมนา\033[00m\n"
        + " กสิกรไทย: 0608905863\n"
        + "     LTC:  LTT2X57ervCMpfNva5uo1JBzT2UJVBiEZu\n"
        + "    DOGE:  DFwUqKS3j3RMMkqQF8z6kbYZ652M8VCFVs")
    print("---------------------------------------------------\n")

def install():
    pkg_list = ["libcurl4-openssl-dev","libssl-dev","libjansson-dev","auomake","autotools-dev","build-essential"]
    for list in range(5):
        select_list = pkg_list[list]
        os.system(f"apt-get install {select_list}")
    os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
    os.system("chmod +x compiler.sh")
    os.system("sh compiler.sh")

def run():
    banner()
    with open("set-miner/miner.json", encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        pool = loads['Pool']
        wallet = loads['Wallet']
        password = loads['Pass']
        cpu = loads['Cpu']
    # dely = 17
    # while dely > 1:
    #     dely -= 1
    #     print("\nโปรแกรมจะเร่มในอีก 033[96m%d033[00m กด f เพื่่อหยุด"%(dely))
    #     # if keyboard.is_pressed('f'):
    #     #     break
          # time.sleep(1.5)
    os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet} -p {password} -t {cpu}")

def set_miner():
    banner()
    pool = None
    wallet = None
    password = None
    cpu = None
    try:
        pool = input("Pool[-o]: ")
        wallet = input("Wallet[-u]: ")
        password = input("Password[-p]: ")
        cpu = int(input("CPU[-t]: "))
        if pool == "" or wallet == "":
            raise Exception()
        if password == "":
            password = "x"
        if cpu == "":
            cpu = 1
    except:
        print("\nเกิดข้อผิดพลาด")
    puts = {
        'Pool': pool,
        'Wallet': wallet,
        'Pass': password,
        'Cpu': cpu
    }
    with open("set-miner/miner.json", "w") as set:
        json.dump(puts, set, indent=4)

while True:
    if os.path.exists("ccminer") == False:
        install()
    if os.path.exists("set-miner") == True:
        if os.path.isfile("set-miner/miner.json") == True:
            run()
        else:
            set_miner()
    else:
        os.system("mkdir set-miner")
    