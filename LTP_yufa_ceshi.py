# 依存语法分析  最原始版本
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import Parser
from time import time

t = time()
# 分词
segmentor = Segmentor()
segmentor.load('D:/ProgramData/ltp_data/cws.model')
# 词性标注
postagger = Postagger()
postagger.load('D:/ProgramData/ltp_data/pos.model')
# 依存语法分析
parser = Parser() # 初始化实例
parser.load('D:/ProgramData/ltp_data/parser.model')  # 加载模型

sentence = '元芳你怎么看？我就趴窗口上看呗！'
words = segmentor.segment(sentence)  # 分词       # print('\t'.join(words))
postags = postagger.postag(words)  # 词性标注     # print('\t'.join(postags))
arcs = parser.parse(words, postags)  # 依存句法分析(一次性不能处理太长，不然会报错)

print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))

# print(list(words))
# print(list(postags))
# print(list(arcs))
print("====")
for i in range(len(arcs)):
    arc = arcs[i]
    print(words[i], arc.relation)

segmentor.release()
postagger.release()
parser.release()
