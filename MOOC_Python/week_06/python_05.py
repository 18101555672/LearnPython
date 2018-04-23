# jieba库的使用
# 中文分词第三方库
import jieba

# 精确模式：把文本精确的切分开，不存在冗余单词
# 全模式：把文本中所有可能的词语都扫描出来，有冗余
# 搜索引擎模式：在精确模式基础上，对长词再次切分

# 常用函数
# jieba.lcut(s,cut_all=False) 精确模式,将cut_all这是为True,启用全模式
print(jieba.lcut('九头蛇和神盾局万岁'))
print(jieba.lcut('九头蛇和神盾局万岁',cut_all=True))
# jieba.lcut_for_search(s) 搜索引擎模式
print(jieba.lcut_for_search('九头蛇和神盾局万岁'))
# jieba.add_word(s) 向分词词典增加新词
jieba.add_word('神盾局')
print(jieba.lcut('九头蛇和神盾局万岁'))