import phonenumbers as p

from phonenumbers  import geocoder
from phonenumbers  import carrier
num=input()

cn_num=p.parse(num)
print(geocoder.description_for_number(cn_num,"en"))
print(carrier.name_for_number(cn_num,"en"))
