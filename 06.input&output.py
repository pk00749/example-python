from collections import defaultdict
import re, time

d = defaultdict(int)
d2 = defaultdict(int)


with open('text.txt', 'w') as fpre:
    for i in range(0,100):
        fpre.write('hello world '+str(time.time())+'\n')

# normal version
def parse(text, dict):
    text = text.lower()
    word_list = re.findall(r'\w+', text)
    for word in word_list:
        dict[word] += 1
    return dict


# with open('text.txt', 'r') as fin:
#     line = fin.readline()
#     while line:
#         d = parse(line, d)
#         line = fin.readline()

#  filter version
with open('text.txt', 'r') as fin2:
    line = fin2.readline()
    while line:
        for word in filter(lambda x:x, re.split(r'\s', line)):
            d2[word] += 1
        line = fin2.readline()
print(d2)


