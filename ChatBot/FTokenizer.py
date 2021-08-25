class FTokenizer():
    def __init__(self,bi_gram_list):
        self.bi_gram_list=bi_gram_list

    def bi_gram_checker(self,bi_gram_word):
        for i in self.bi_gram_list:
            if (bi_gram_word==i):
                return True
        return False
    
    def fit_on_text(self,data):
        word_to_index={}
        index_to_word={}
        word_to_index["<PAD>"]=0
        word_to_index["<OOV>"]=1
        index_to_word[0]="<PAD>"
        index_to_word[1]="<OOV>"
        myContinue=False
        tokens=[]
        for eachseq in data:
            listtokens=eachseq.lower().split(" ")
            listtokens.append("")
            for i in range(0,len(listtokens)-1):
                if (myContinue):
                    myContinue=False
                    continue
                if (listtokens[i+1]!=""):
                    pairtext=listtokens[i]+"_"+listtokens[i+1]
                    if (self.bi_gram_checker(pairtext)):
                        myContinue=True
                        if (tokens.count(pairtext)==0):
                            tokens.append(pairtext)
                if (myContinue==False):  
                    if (tokens.count(listtokens[i])==0):
                        tokens.append(listtokens[i])
        for index,word in enumerate(tokens):
            word_to_index[word]=index+2
            index_to_word[index+2]=word
        self.word_to_index=word_to_index
        self.index_to_word=index_to_word

    def fit_on_text2(self,data):
        word_to_index={}
        index_to_word={}
        word_to_index["<PAD>"]=0
        word_to_index["<OOV>"]=1
        index_to_word[0]="<PAD>"
        index_to_word[1]="<OOV>"
        myContinue=False
        tokens=[]
        for eachseq in data:
            listtokens=eachseq.lower().split(" ")
            listtokens.append("")
            for i in range(0,len(listtokens)-1):
                if (listtokens[i+1]!=""):
                    pairtext=listtokens[i]+"_"+listtokens[i+1]
                    if (self.bi_gram_checker(pairtext)):
                        if (tokens.count(pairtext)==0):
                            tokens.append(pairtext)
                if (tokens.count(listtokens[i])==0):
                    tokens.append(listtokens[i])
        for index,word in enumerate(tokens):
            word_to_index[word]=index+2
            index_to_word[index+2]=word
        self.word_to_index=word_to_index
        self.index_to_word=index_to_word
    
    def get_word_to_index(self):
        return self.word_to_index
    
    def get_index_to_word(self):
        return self.index_to_word

    def get_max_length(self,data):
        maxsen=0
        for i in data:
            if maxsen<len(i):
                maxsen=len(i)
        return maxsen

    def text_to_sequence(self,textdata):
        d_continue=False
        output=[]
        for text in textdata:
            text=text.lower().split(" ")
            text.append("")
            sth=[]
            d_continue=False
            for i in range(0,len(text)-1):
                if d_continue==True:
                    d_continue=False
                    continue
                if (text[i+1]!=""):
                    pairtext=text[i]+"_"+text[i+1]
                    for j in self.word_to_index:
                        if pairtext.lower()==j:
                            sth.append(self.word_to_index[j])
                            d_continue=True
                            break
                if d_continue==False:
                    for count,j in enumerate(self.word_to_index):
                        if text[i].lower()==j:
                            sth.append(self.word_to_index[j])
                            break
                        if count==len(self.word_to_index)-1:
                            sth.append(1)
            output.append(sth)
        return output
    
    def intseq_to_index(self,sequence):
        output=[]
        for i in sequence:
            output.append(self.index_to_word[i])
        return output

    def pad_sequence(self,datasequence,maxlen):
        for i in datasequence:
            while len(i)!=maxlen:
                i.insert(0,0)
        return datasequence
