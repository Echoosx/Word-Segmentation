import jieba.posseg as pseg

if __name__=="__main__":
    while(True):
        sentence=input("输入要分词的语句：")
        words = pseg.cut(sentence)
        for word, flag in words:
            print('%s %s' % (word, flag))
        print("----------------------------")
