import re

phonenumber= "5161112222"

regex= "(\w{3})\w{3}-\w{4}"

if re.search(regex, phonenumber):
    print("Valid phone number")
else:
    print("Invalid phone number")
