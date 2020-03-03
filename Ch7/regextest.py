import re

def regextest(x):
    var = re.compile(r'^([A-Za-z]+)$')
    answer = var.sub(r''''\1',''',x)
    return answer

value = ["jaydon","will","bobby"]

for i in range (len(value)):
    print (regextest(value[i]))
