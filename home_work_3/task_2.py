import string
from operator import itemgetter
text = "Python 3.9 is the latest version of Python. It's awesome!"
# text = 'This is a sample text without repeating words.'
# text = 'Hello world. Hello Python. Hello again.'
text = text.lower()
replace_punctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))
text = text.translate(replace_punctuation)
print(text)
a = text.split()
len_a = len(a)
count = 0

c = []
for i in a:
    if i.isdigit():
        continue
    if (i, a.count(i)) not in c:
        c.append((i, a.count(i)))

d = sorted(c, key=itemgetter(1, 0), reverse=True)

if len(d) > 10:
    d = d[:10]
print(d)
