import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import time
import os
import pyfiglet
blue = "\033[1;0;34m"
green = "\033[1;92m"

time.sleep(2)
os.system("cls")
banner = pyfiglet.figlet_format("maidcoder", font = "standard")
print(banner)
print("coder: ABDULGEE")
print(f"""{blue}
                                         MOBILE_NUMBER_SCANNER
                                         """)
print("start with your country code eg. +234XXXXXXXXX, +92XXXXXXXXXX, +1519XXXXXX")
mobileNo = input(f"""{green}
target number: """)
time.sleep(3)
print("""
checking phone number
               
               """)
mobileNo = phonenumbers.parse(mobileNo)

time.sleep(3)
print("addrease: ", timezone.time_zones_for_number(mobileNo))

time.sleep(3)
print("network: ", carrier.name_for_number(mobileNo, "en"))

time.sleep(3)
print("country: ", geocoder.description_for_number(mobileNo, "en"))

time.sleep(3)
print("live moble number :", phonenumbers.is_valid_number(mobileNo))

time.sleep(3)
print("possibility of number :", phonenumbers.is_possible_number(mobileNo))

print("thank you for using our tool")