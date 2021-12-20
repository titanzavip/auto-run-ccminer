import os, json, time
from progress.spinner import MoonSpinner

def banner():
    os.system("clear")
    logo = """
███████╗██████╗ ██╗████████╗
██╔════╝██╔══██╗██║╚══██╔══╝
█████╗  ██║  ██║██║   ██║ 
██╔══╝  ██║  ██║██║   ██║ 
███████╗██████╔╝██║   ██║   
╚══════╝╚═════╝ ╚═╝   ╚═╝"""
    print(logo,"\nCreated by.mobile-mining")
    print("---------------------------------------------------")
    print("\033[96mสนับสนุนนักพัมนา\033[00m\n"
        + " กสิกรไทย: 0608905863\n"
        + "     LTC:  LTT2X57ervCMpfNva5uo1JBzT2UJVBiEZu\n"
        + "    DOGE:  DFwUqKS3j3RMMkqQF8z6kbYZ652M8VCFVs")
    print("---------------------------------------------------\n")

def set_miner():
    banner()
    pool = None
    wallet = None
    password = None
    cpu = None
    try:
        print("ตัวอย่าง: stratum+tcp://ap.luckpool.net:3956")
        pool = input("Pool[-o]: ")

        print("ตัวอย่าง: RQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.OMG-MINER")
        wallet = input("Wallet[-u]: ")

        print("ตัวอย่าง: x หรือ ( hybrid เฉพาะ luckpool )")
        password = input("Password[-p]: ")

        print(" 0 ขึ้นไป หรือ เท่ากับจำนวณเธรดCPUท่าน เช็ค 'lscpu'")
        cpu = int(input("CPU[-t]: "))
        
        if pool == "" or wallet == "":
            raise Exception()
        if password == "":
            password = "x"
        if cpu == "":
            cpu = 1
    except:
        print("\nเกิดข้อผิดพลาด มีบางอย่างไม่ถุูกต้อง!")
    puts = {
        'Pool': pool,
        'Wallet': wallet,
        'Pass': password,
        'Cpu': cpu
    }
    with open("set-miner/miner.json", "w") as set:
        json.dump(puts, set, indent=4)

os.system("clear")
with MoonSpinner("กำลังทำงาน...") as bar:
        for i in range(150):
            time.sleep(0.05)
            bar.next()
if os.path.exists("set-miner") == True:
    set_miner()
else:
    os.system("mkdir set-miner")
    