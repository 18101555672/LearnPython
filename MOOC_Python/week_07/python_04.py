# wordcloud库的基本使用
import wordcloud,jieba
# 创建一个wordcloud对象：w = wordcloud.WordCloud()
# w.generate(txt) 向wordcloud对象w中加载文本txt
# w.to_file(filename) 将词云输出为图像文件（png或jpg格式）
# w = wordcloud.WordCloud(<参数>)
# width 指定词云对象生成图片的宽度，默认400像素
# hight 指定词云对象生成图片的高度，默认200像素
# min_font_size 指定词云中字体的最小字号，默认4号
# max_font_size 指定词云中字体的最大字号，根据高度自动调节
# font_step 指定词云中字体字号的步进间隔，默认为1
# font_path 指定字体文件路径，默认None
# max_words 指定词云显示的最大单词数量，默认200
# stop_words 指定词云的排除词列表，即不显示的单词列表
# mask 指定词云形状，默认为长方形，需要引用imread()函数
# background_color 指定词云图片的背景颜色，默认为黑色

txt = 'life is short, you need python'
w = wordcloud.WordCloud(background_color = 'white')
w.generate(txt)
w.to_file('pywcloud.png')

txt = '程序设计语言是计算机能够理解和' \
      '识别用户操作意图的一种交互体系，他按照' \
      '特定规则组织计算机指令，使计算机能够自' \
      '动进行何种运算处理。'
w = wordcloud.WordCloud(width=1000,height=700,font_path='msyh.ttf')
w.generate(' '.join(jieba.lcut(txt)))
w.to_file('pywcloudcn.png')
