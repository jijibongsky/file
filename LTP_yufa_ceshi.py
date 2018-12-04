# 依存语法分析  最原始版本
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import Parser
from pyltp import SentenceSplitter
from time import time
import os
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


# sentence = '父母与子女间的关系，不因父母离婚而消除。离婚后，子女无论由父方或母方抚养，仍是父母双方的子女。离婚后，父母对于子女仍有抚养和教育的权利和义务。离婚后，哺乳期内的子女，以随哺乳的母亲抚养为原则。哺乳期后的子女，如双方因抚养问题发生争执不能达成协议时，由人民法院根据子女的权益和双方的具体情况判决。'
# sentence = '元芳你怎么看？我就趴窗口上看呗！'
sentence = '本法是婚姻家庭关系的基本准则。'
# sentence = '被告殴打原告。'
words = segmentor.segment(sentence)  # 分词       # print('\t'.join(words))
postags = postagger.postag(words)  # 词性标注     # print('\t'.join(postags))
arcs = parser.parse(words, postags)  # 依存句法分析(一次性不能处理太长，不然会报错)  # print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))

# print(list(words))
# print(list(postags))
# print(list(arcs))
print("====")
for i in range(len(arcs)):
    arc = arcs[i]
    print(arc.relation)
    if words[i] == '被告' and arc.relation == 'SBV':
        print(words[i] + ' ' +words[arc.head - 1])

    # print(a+'\n'+b)

segmentor.release()
postagger.release()
parser.release()
