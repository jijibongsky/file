

def count_lines(file_name):
    f = open(file_name, "r", encoding="utf8")
    sentences = []
    sentence=[]
    for line in f:
        line = line.strip()
        if line != "":
            sentence.append(line)
        else:
            sentences.append(sentence)
            sentence = []
    return sentences

file_name = "train_data"
sentences = count_lines(file_name)
sentences_len = [len(sentence) for sentence in sentences]

print("句子总个数：", len(sentences))
print("最大长度：", max(sentences_len))


for i in sorted(sentences_len):
    print(i)


