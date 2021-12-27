import re

varstr = "dass1212121 dffggf    ddfg"
# varstr = re.sub('[^a-z]/  +/g', ' ', varstr)
varstr = re.sub('[^a-z]', ' ', varstr)
varstr = re.sub(' +', ' ', varstr)

print(varstr)