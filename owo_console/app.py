import requests, json, math, fs, random, discordrpc, os, time, hashlib
from datetime import datetime
from file import phrases_dictionary
# Get the current working directory
current_dir = os.getcwd()
# Join the current directory with the filename
file_path = os.path.join(current_dir, 'data.json')
#Call cfg.json file 
with open(file_path, 'r', encoding='utf-8') as wtf:
    cfgs = json.load(wtf)

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


def random_time():
    return random.randint(0, time_error) * round(random.uniform(0, 1), 3)


print(random_time())
