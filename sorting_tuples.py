txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
    t.sort(reverse=True)

    res = list()
    sent = ''
for length, word in t:
    res.append(word)
    sent += ' ' + word
print(res)
print(sent)