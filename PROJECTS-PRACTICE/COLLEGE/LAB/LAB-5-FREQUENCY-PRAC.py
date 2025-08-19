file = open('sample.txt')
text = file.read()
print(text)
words = text.split()
freq = {}
for word in words:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word]+=1
most_freq = dict(sorted(freq.items(), key = lambda elem:elem[1], reverse= True))
output = dict(list(most_freq.items())[0:10])
print(output)