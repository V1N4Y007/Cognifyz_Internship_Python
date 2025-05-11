from collections import Counter
with open('./Level 2/vinay.txt','r') as f:
    data = f.read()
    print(data)
   
words = data.split()
print(words)
wcounts = Counter(words)
for word in sorted(wcounts):
    print(f"{word}: {wcounts[word]}")

