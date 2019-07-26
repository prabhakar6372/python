from collections import Counter
import datetime
import re
#s = 'How many times does each word show up in this sentence word times each each word'

#words = s.split()
#print(words)
#c = Counter(words)

#print(Counter(words))
#print(list(c))
#print(set(c))
#print(dict(c))
#print(c.most_coimmon())
#today = datetime.date.today()
#print(today)

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sddddibchdsbs...... iasbabcicanck.... s..s.s.s.ssss.sdsdsssd....dsdsdssss....'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]
for pattern in test_patterns:
 print(re.findall(pattern,test_phrase))

