'''
HashScan - By Shandyman
Version: 2.0
Last Update: 09/12/20
'''
import os
import sys
import csv
import time
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
global filebreak
global count

filebreak = "================"
varbreak = "-----------------"


os.system('color')
class colors:
	orange = '\033[9m'
	grey = '\033[90m'
	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	magenta = '\033[95m'
	cyan = '\033[96m'
	white = '\033[97m'
	default = '\033[0m'
    
def hashes(target_hash):
    
    
    api_key = "<API KEY GOES HERE!>"
    
    base_url = "https://hashes.org/api.php?key="
    query_url = "&query="
    
    final_url = base_url + api_key + query_url + target_hash
    
    print(f"{colors.cyan}" + varbreak*3 + f"{colors.default}")
    print(f"\nSearching for: {colors.green}" + str(target_hash) + f"{colors.default}\n")
    
    try:

        response = requests.get(final_url, verify=False, timeout=10)
        info = json.loads(response.content)

            
        try:
            plain_pass = info["result"][target_hash]["plain"]
            plain_alg = info["result"][target_hash]["algorithm"]
            
            print(filebreak)
            print("Algorithm: " + str(plain_alg))
            print("Password: " + str(plain_pass))
            print(filebreak + "\n")
        except:
            print(filebreak)
            print(f"{colors.yellow}Couldn't find anything about that Hash!{colors.default}")
            print(filebreak + "\n")
    except:
        print("Error finding that Hash!")
        print(filebreak)

def help():
    
    print(f"{colors.cyan}" + f"{colors.default}")
    print(f"{colors.yellow}SYNTAX:{colors.default}")
    print("hashscan.py <HASH/FILE>")
    print("")
    print(f"{colors.yellow}EXAMPLE:{colors.default}")
    print("hashscan.py 5f4dcc3b5aa765d61d8327deb882cf99")
    print("hashscan.py list_of_hashes.txt")
    

if __name__ == "__main__":
    print(f"{colors.cyan}  _   _           _     ____                  ")
    print(" | | | | __ _ ___| |__ / ___|  ___ __ _ _ __  ")
    print(" | |_| |/ _` / __| '_  \\___ \ / __/ _` | '_ \ ")
    print(" |  _  | (_| \__ \ | | |___) | (_| (_| | | | |")
    print(" |_| |_|\__,_|___/_| |_|____/ \___\__,_|_| |_|")
    print(f"{colors.default}")
    try:
        target_hash = sys.argv[1]
    except:
        print("Check that input bro....")
        sys.exit()
        
    if target_hash.endswith(".txt"):
        x = 0
        print(f"You have selected the file: {colors.green}" + target_hash + f"{colors.default}")
        with open(str(target_hash),'r') as fileopen:
            reader = csv.reader(fileopen) 
            for row in reader:
                if x < 20:
                    firststrip = str(row).lstrip("['")
                    target_hash = firststrip.rstrip("']")
                    hashes(str(target_hash))
                    x = x+1
                else:
                    print(f"{colors.red}Rate Limit Reached. Continuing Scan in 60 seconds.{colors.default}")
                    time.sleep(60)
                    x = 0
                    hashes(str(target_hash))

    else:
        if target_hash.endswith(".csv"):
            x = 0
            print(f"You have selected the file: {colors.green}" + target_hash + f"{colors.default}")
            with open(str(target_hash),'r') as fileopen:
                reader = csv.reader(fileopen)
                for row in reader:
                    if x < 20:
                        firststrip = str(row).lstrip("['")
                        target_hash = firststrip.rstrip("']")
                        hashes(target_hash)
                        x = x+1
                    else:
                        print(f"{colors.red}Rate Limit Reached. Continuing Scan in 60 seconds.{colors.default}")
                        time.sleep(60)
                        x = 0
                        hashes(str(target_hash))
        else:
            if target_hash == "-h":
                help()
            else:
                if target_hash == "--new-lists":
                    get_new_lists()
                else:
                    hashes(target_hash)
