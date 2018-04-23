# 哈姆雷特词频统计
def getEnTxt():
    with open('hamlet.txt','r') as f:
        f = f.read().lower()
        for i in '|"#$%&()*+,-_/;:<=>?@[]\\^{}!’\'.~':
            f = f.replace(i,' ')
        return f
def getTop(n=10):
    hamlet = getEnTxt()
    words = hamlet.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(n):
        print(i+1,':',items[i])
getTop(15)
getTop()
