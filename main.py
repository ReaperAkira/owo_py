import requests, json, math, fs, random, discordrpc, os, time, hashlib, sys
from win10toast import ToastNotifier
from blessed import Terminal
from datetime import datetime
from data.file import phrases_dictionary
# Get the current working directory
current_dir = os.getcwd()
# Join the current directory with the filename
file_path = os.path.join(current_dir, 'owo_console\\data\\data.json')
#Call cfg.json file 
with open(file_path, 'r', encoding='utf-8') as wtf:
    cfgs = json.load(wtf)
#chalk
term = Terminal()
red = term.red
green = term.green
blue = term.blue
black = term.black
red = term.red
green = term.green
yellow = term.yellow
blue = term.blue
magenta = term.magenta
cyan=term.cyan
white=term.white
bright_black=term.bright_black
bright_red=term.bright_red
bright_green=term.bright_green
bright_yellow=term.bright_yellow
bright_blue=term.bright_blue
bright_magenta=term.bright_magenta
bright_cyan=term.bright_cyan
bright_white=term.bright_white
# Access the settings
setting               = cfgs["settings"]
prefix                = str(setting['prefix'])
owo                   = str(setting['owo'])
pray                  = str(setting['pray'])
curse                 = str(setting['curse'])
hunt                  = str(setting['hunt'])
battle                = str(setting['battle'])
autoquest             = str(setting['autoquest'])
extratoken            = str(setting['extratoken'])
randommess            = str(setting['randommess'])
discord_rpc           = str(setting['discord_rpc'])
#========================================================
inventory             = setting['inventory']
inventorycheck        = str(inventory['inventorycheck'])
gemcheck              = str(inventory['gemcheck'])
lootboxcheck          = str(inventory['lootboxcheck'])
fabledlootboxcheck    = str(inventory['fabledlootboxcheck'])
cratecheck            = str(inventory['cratecheck'])
#========================================================
animals               = setting['animals']
a_enable              = animals['enable']
a_type                = animals['type']
animaltype            = animals['animaltype']
common                = animaltype['common']
uncommon              = animaltype['uncommon']
rare                  = animaltype['rare']
epic                  = animaltype['epic']
mythical              = animaltype['mythical']
patreon               = animaltype['patreon']
cpatreon              = animaltype['cpatreon']
legendary             = animaltype['legendary']
gem                   = animaltype['gem']
bot                   = animaltype['bot']
distorted             = animaltype['distorted']
fabled                = animaltype['fabled']
special               = animaltype['special']
hidden                = animaltype['hidden']
#========================================================
upgradeautohunt       = setting['upgradeautohunt']
upg_enable            = upgradeautohunt['enable']
upg_type              = upgradeautohunt['upgtype']
#========================================================
gamble                = setting['gamble']
coinflip              = gamble['coinflip']
coinflip_enable       = coinflip['enable']
coinflip_amount       = coinflip['amount']

slots                 = gamble['slots']
slots_enable          = slots['enable']
slots_amount          = slots['amount']
#========================================================
main                  = cfgs['main']
main_token            = str(main['token'])
main_id               = str(main['userid'])
main_channelid        = str(main['channelid'])
main_owodmchannelid   = str(main['owodmchannelid'])
main_questchannelid   = str(main['autoquestchannelid'])

extra                 = cfgs['extra']
extra_token           = str(extra['token'])
extra_id          = str(extra['userid'])
extra_channelid       = str(extra['channelid'])
extra_owodmchannelid  = str(extra['owodmchannelid'])
extra_questchannelid  = str(extra['autoquestchannelid'])
#========================================================
timedelay             = cfgs['timedelay']
owo_time              = int(timedelay['owo'])
pray_time             = int(timedelay['pray'])
curse_time            = int(timedelay['curse'])
huntandbattle_time    = int(timedelay['huntandbattle'])
slots_time            = int(timedelay['slots'])
coinflip_time         = int(timedelay['coinflip'])
upgradeautohunt_time  = int(timedelay['upgradeautohunt'])
animals_time          = int(timedelay['animals'])
time_error            = int(timedelay['time_error'])
#========================================================
random_phrase = phrases_dictionary()[0]
#random time
def random_time():
    rdt = random.randint(0, time_error) + round(random.uniform(0, 1), 3)
    while rdt < 1:
        rdt = random.randint(0, time_error) + round(random.uniform(0, 1), 3)
        continue
    return rdt
#========================================================
def nonce():
    return 1098393848631590 + math.floor(round(random.uniform(0, 1), 3) * 9999)

def autoseed(token) :
    seed = hashlib.sha256(f"seedaccess-entropyverror-apiv10.{token}".encode()).digest()
    random.seed(int.from_bytes(seed, byteorder="big"))
    return random.random()
def sleepy(tokentype):
    print(f"{datetime.now().strftime('%H:%M:%S')} [{tokentype}]{"Waiting..."}")
#========================================================
def sayowo(token, tokentype, channelid):
    headers = {
        "authorization": token,
    }
    url = f"https://discord.com/api/v9/channels/{channelid}/messages"
    data = {
         "content": "owo",        
         'nonce': nonce(),
         "tts": False,
         "flags": 0,
    }
    requests.post(url, headers=headers, json=data)
    headers = {
            "authorization": token,
    }
    print(
        red(f"{datetime.now().strftime('%H:%M:%S')}") +
        magenta(f"[{tokentype}]") +     
        blue(" OwO ✅ ")    
        )
    



#========================================================
def checkinv(token, channelid, tokentype):
    if gemcheck == "true":
        headers = {
            "authorization": token,
        }
        url = f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1"
        response = requests.get(url, headers=headers)
        body = response.text
        bod = json.loads(body)
        cont = bod[0]['content']
        if "You found:" in cont or "and caught a" in cont:
            collection = ["alulu"]
            print(
                f"{datetime.now().strftime('%H:%M:%S')} [{tokentype}] inventory checking 🔍 (type-1)"
            )
            if "gem1" not in cont:
                collection.append("huntgem")
            if "gem3" not in cont:
                collection.append("empgem")
            if "gem4" not in cont:
                collection.append("luckgem")
            if "gem1" in cont and "gem3" in cont and "gem4" in cont:
                getinv(token, channelid, tokentype, "nogem", ["nocollection"])
            else:
                getinv(token, channelid, tokentype, "gemvar", collection)
    else:
        print(
            f"{datetime.now().strftime('%H:%M:%S')} [{tokentype}] inventory checking 🔍 (type-2)"
        )
        getinv(token, channelid, tokentype, "nogem", ["nocollection"])
#========================================================
def getinv(token, channelid, tokentype, gemc, collectc):
    headers = {
        "authorization": token,
    }
    url = f"https://discord.com/api/v9/channels/{channelid}/messages"
    data = {
        "content": prefix + "inv",
        "tts": False,
        "flags": 0,
    }
    requests.post(url, headers=headers, json=data)
    time.sleep(3)
    headers = {
        "authorization": token,
    }
    url = f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1"
    response = requests.get(url, headers=headers)
    body = response.text
    bod = json.loads(body)
    cont = bod[0]['content']
    if gemc == "gemvar":
        empgem = ""
        empgemstatus = False
        luckgem = ""
        luckgemstatus = False
        huntgem = ""
        huntgemstatus = False
        specialgem = ""
        specialgemstatus = False
        gem = ""
        gemusebro = False

        if "huntgem" in collectc:
            if "`057`" in cont:
                huntgem = "57"
                huntgemstatus = True
            elif "`056`" in cont:
                huntgem = "56"
                huntgemstatus = True
            elif "`055`" in cont:
                huntgem = "55"
                huntgemstatus = True
            elif "`054`" in cont:
                huntgem = "54"
                huntgemstatus = True
            elif "`053`" in cont:
                huntgem = "53"
                huntgemstatus = True
            elif "`052`" in cont:
                huntgem = "52"
                huntgemstatus = True
            elif "`051`" in cont:
                huntgem = "51"
                huntgemstatus = True

        if "empgem" in collectc:
            if "`071`" in cont:
                empgem = "71"
                empgemstatus = True
            elif "`070`" in cont:
                empgem = "70"
                empgemstatus = True
            elif "`069`" in cont:
                empgem = "69"
                empgemstatus = True
            elif "`068`" in cont:
                empgem = "68"
                empgemstatus = True
            elif "`067`" in cont:
                empgem = "67"
                empgemstatus = True
            elif "`066`" in cont:
                empgem = "66"
                empgemstatus = True
            elif "`065`" in cont:
                empgem = "65"
                empgemstatus = True

        if "luckgem" in collectc:
            if "`078`" in cont:
                luckgem = "78"
                luckgemstatus = True
            elif "`077`" in cont:
                luckgem = "77"
                luckgemstatus = True
            elif "`076`" in cont:
                luckgem = "76"
                luckgemstatus = True
            elif "`075`" in cont:
                luckgem = "75"
                luckgemstatus = True
            elif "`074`" in cont:
                luckgem = "74"
                luckgemstatus = True
            elif "`073`" in cont:
                luckgem = "73"
                luckgemstatus = True
            elif "`072`" in cont:
                luckgem = "72"
                luckgemstatus = True

        if "specialgem" in collectc:
            if "`085`" in cont:
                specialgem = "85"
                specialgemstatus = True
            elif "`084`" in cont:
                specialgem = "84"
                specialgemstatus = True
            elif "`083`" in cont:
                specialgem = "83"
                specialgemstatus = True
            elif "`082`" in cont:
                specialgem = "82"
                specialgemstatus = True
            elif "`081`" in cont:
                specialgem = "81"
                specialgemstatus = True
            elif "`080`" in cont:
                specialgem = "80"
                specialgemstatus = True
            elif "`079`" in cont:
                specialgem = "79"
                specialgemstatus = True

        if huntgemstatus:
            gem += f" {huntgem}"
            gemusebro = True
        if empgemstatus:
            gem += f" {empgem}"
            gemusebro = True
        if luckgemstatus:
            gem += f" {luckgem}"
            gemusebro = True
        if specialgemstatus:
            gem += f" {specialgem}"
            gemusebro = True
        if gemusebro:
            gemuse(token, gem, channelid, tokentype)

    if lootboxcheck == "true":
        if "`050`" in cont:
            time.sleep(2)
            boxuse(token, "lootbox all", channelid, tokentype)

    if fabledlootboxcheck == "true":
        if "`049`" in cont:
            time.sleep(2)
            boxuse(token, "lootbox fabled all", channelid, tokentype)

    if cratecheck == "true":
        if "`100`" in cont:
            time.sleep(2)
            boxuse(token, "crate all", channelid, tokentype)
#========================================================
def boxuse(token, box, channelid, tokentype):
    headers = {
        "authorization": token,
    }
    url = f"https://discord.com/api/v9/channels/{channelid}/messages"
    data = {
         "content": prefix + box,        
         'nonce': nonce(),
         "tts": False,
         "flags": 0,
    }
    requests.post(url, headers=headers, json=data)
    headers = {
            "authorization": token,
    }
    print(
        red(f"{datetime.now().strftime('%H:%M:%S')}") +
        magenta(f"[{tokentype}]") +     
        yellow(box + " ✅")    
        )

def gemuse(token, gem, channelid, tokentype):
    headers = {
        "authorization": token,
    }
    url = f"https://discord.com/api/v9/channels/{channelid}/messages"
    data = {
         "content": prefix + "use " + gem,        
         'nonce': nonce(),
         "tts": False,
         "flags": 0,
    }
    requests.post(url, headers=headers, json=data)
    headers = {
            "authorization": token,
    }
    print(
        red(f"{datetime.now().strftime('%H:%M:%S')}") 
        + magenta(f"[{tokentype}]") + 
        yellow(" Gem ✅")
            )
#========================================================
print(extra_token)
print(main_token)
print(autoseed(main_token))
print(autoseed(extra_token))
print(random_time())
print(nonce())
x = 0
while x < 50:
    x = x + 1
    print(random_time())
print(random_phrase)
