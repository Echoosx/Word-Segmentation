import jieba

if __name__=="__main__":
    while(True):
        sentence=input("输入要分词的语句：")
        seg_list = jieba.cut(sentence, cut_all=True)
        print("【全模式】" + " / ".join(seg_list))  # 全模式

        seg_list = jieba.cut(sentence, cut_all=False)
        print("【精确模式】" + " / ".join(seg_list))  # 精确模式

        seg_list = jieba.cut_for_search(sentence)
        print("【搜索引擎模式】" + " / ".join(seg_list))  # 精确模式
