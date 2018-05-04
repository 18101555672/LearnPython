# 实例：政府工作报告
import jieba,wordcloud
with open('zgtsshzy.txt','r',encoding='gbk') as f:
    t = f.read()
    txt = ' '.join(jieba.lcut(t))
    w = wordcloud.WordCloud(font_path='msyh.ttf',width=1000,height=1000,background_color='white')
    w.generate(txt)
    w.to_file('zgtsshzy.png')
with open('xczxzl.txt','r',encoding='gbk') as f:
    txt = ' '.join(jieba.lcut(f.read()))
    w = wordcloud.WordCloud(font_path='msyh.ttf',width=1000,height=700,background_color='white')
    w.generate(txt)
    w.to_file('xczxzl.png')