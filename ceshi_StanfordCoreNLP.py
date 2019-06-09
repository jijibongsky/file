from time import time
from stanfordcorenlp import StanfordCoreNLP


def my_ner(nlp, sentence):
    tags = ["ORGANIZATION", "FACILITY"]
    res = nlp.ner(sentence)
    # res = [('合肥', 'ORGANIZATION'), ('工业', 'ORGANIZATION'),  ('大学', 'ORGANIZATION'), ('在', 'O'), ('屯溪路', 'FACILITY'), ('193', 'FACILITY'), ('号', 'FACILITY'), ('，', 'O'), ('李勇', 'PERSON'), ('在', 'O'), ('这里', 'O'), ('上', 'O'), ('大学', 'O')]
    label = ''
    labels = []
    temp_tag = ""
    for i in range(len(res)):
        if res[i][1] in tags:
            if temp_tag == "":
                temp_tag = res[i][1]
                label += res[i][0]
            elif temp_tag == res[i][1]:
                label += res[i][0]
            else:
                labels.append(label)
                temp_tag = res[i][1]
                label = res[i][0]
        elif label != "":
            labels.append(label)
            temp_tag = ""
            label = ''
    return labels


# nlp = StanfordCoreNLP('/home/data/stanford-corenlp-full-2018-10-05/', lang='zh')
nlp = StanfordCoreNLP('D:\自己资料\软件\斯坦福句法分析\stanford-corenlp-full-2018-10-05', lang='zh')
sentence = '合肥工业大学在屯溪路193号，李勇在这里上大学'

# print(nlp.pos_tag(sentence))
begin = time()
print(nlp.ner(sentence))
print("花费时间：", time()-begin)

labels = my_ner(nlp, sentence)
print(labels)


# begin = time()
# for i in range(100):
#     a = nlp.ner(sentence)
# print("花费时间：",time()-begin)


# print(nlp.word_tokenize(sentence))
# print(nlp.pos_tag(sentence))
# print(nlp.ner(sentence))
# print(nlp.parse(sentence))
# print(nlp.dependency_parse(sentence))

nlp.close()
