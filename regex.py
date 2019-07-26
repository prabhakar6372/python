import re
P = input()
#results = re.match(r"^\d[1-9]\d\d\d\d\d$", P)
results = re.match(r"^[1-9]\d\d\d\d\d$", P)
results1 = re.match(r"", P)
print(results)
print(results1)
#([1-9])(\d)
i(?


i!\1)
iimport re
s=input()
print (bool(re.match(r'^[1-9][\d]{5}$',s) and len(re.findall(r'(\d)(?=\d\1)',s))<2 ))
iregex_integer_in_range = r"^[1-9]\d\d\d\d\d$"
regex_alternating_repetitive_digit_pair = r"(.)(?=.\1)"
