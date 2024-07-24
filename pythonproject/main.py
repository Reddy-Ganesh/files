import phonenumber
from test import number
from phonenumber import geocoder
cn_num=phonenumber.parse(number,"ch")
print(geocoder.description_for_number(cn_num,"en"))

