#!/bin/python
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNumber = input("Entrer le numéro du mobile avec le code du pays: ")
mobileNumber = phonenumbers.parse(mobileNumber)

#timezone
print(timezone.time_zones_for_number(mobileNumber))
#carrier
print(carrier.name_for_number(mobileNumber,"en"))
#location
print(geocoder.description_for_number(mobileNumber,"en"))
#phone number validation
print("Validating: ", phonenumbers.is_valid_number(mobileNumber))
#Check possibility
print("Checking possibilitity for",mobileNumber,": ",phonenumbers.is_possible_number)
