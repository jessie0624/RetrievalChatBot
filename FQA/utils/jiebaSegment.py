import os, sys
import jieba
import codecs
sys.path.append("..")
import config 
class Seg(object):
    stopword_filepath = config.stop_words_path

    def __init__(self):
        self.stopwords = set()
        self.read_in_stopword()

    def load_userdict(self,file_name):
        jieba.load_userdict(file_name)

    def read_in_stopword(self):
        file_obj = codecs.open(self.stopword_filepath, 'r', 'utf-8')
        while True:
            line = file_obj.readline()
            line=line.strip('\r\n')
            if not line:
                break
            self.stopwords.add(line)
        file_obj.close()

    def cut(self, sentence, stopword= True, cut_all = False):
        seg_list = jieba.cut(sentence, cut_all)
        results = []
        for seg in seg_list:
            if stopword and seg in self.stopwords:
                continue
            results.append(seg)

        return results

    def cut_for_search(self,sentence, stopword=True):
        seg_list = jieba.cut_for_search(sentence)

        results = []
        for seg in seg_list:
            if stopword and seg in self.stopwords:
                continue
            results.append(seg)

        return results