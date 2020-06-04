import jieba
# using jieba to segment chinese language
chinese_text = '''仍然沉迷于长达数小时的远景，
穿越玫瑰照亮的积云，房屋和谷仓，
如雪谷中深处的斑点，看上去像十二月的所有滚动国家—棕色和黑色的山丘上散布着雪，
闪烁 在冰雪覆盖的湖泊中，一条长长的辫子在峡谷底部闪闪发光。 
在机翼上方，天空已经深深地变成了蓝色，如此纯净，他知道，如果他看上去足够长，就会流下眼泪
'''

seg_list = jieba.cut (chinese_text , cut_all = True )
print ( " Full Mode: "  +  " / " .join (seg_list))

# Typography is the art of making a written language readable and legible. It includes
# placing letters after each other, letter-spacing, line length.

# Suprasegmental is a feature where words are differentiated even based on the tone that is used while pronouncing the words
# or word joints that accompanies or is added over consonants and vowels

# Orthography is a set convention that is used for writing a language,
# it can be set of spellings put together, punctuations or even the grammar