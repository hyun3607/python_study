from wordcloud import WordCloud 
import matplotlib.pyplot as plt # 데이터 시각화
from collections import Counter # 텍스트,빈도수 추출
from konlpy.tag import Okt # 한국어 처리 형태소 분석 패키지
from PIL import Image # 그림 불러오는 패키지
import numpy as np # 그림을 배열로 나타내어 처리할 수 있도록 도와주는 패키지

# file_path = 'C:/Users/hyun/Desktop/word_cloud/대한민국헌법.txt'
# image_path = 'C:/Users/hyun/Desktop/cloud.png'
# wc_font_path = 'C:/Windows/Fonts/Arial.ttf'
 
a = 'C:/Users/hyun/Desktop/word_cloud/대한민국헌법.txt'
b = 'C:/Users/hyun/Desktop/cloud.png'
c = 'C:/Windows/Fonts/batang.ttc'
 
class Word_Cloud:
    # def __init__(self, file_path, image_path, wc_font_path):
    def __init__(self):
        # self.file_path = file_path
        # self.image_path = image_path
        # self.wc_font_path = wc_font_path
        self.file_path = 'C:/Users/hyun/Desktop/word_cloud/대한민국헌법.txt'
        self.image_path = 'C:/Users/hyun/Desktop/cloud.png'
        self.wc_font_path = 'C:/Windows/Fonts/batang.ttc'
        self.text = ""
        self.c = ""
    
    # def open(self):
    #     f = open(self.file_path, 'r')
    #     text = f.read()
    
    def get_file(self): 
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.text = f.read()
        
    def get_noun(self):
        okt = Okt() # 형태소 분석기 객체 생성
        nouns = okt.nouns(self.text) # 명사만 추출
        words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외
        self.c = Counter(words) # 단어별 빈도수 형태의 딕셔너리 데이터를 구함

    def visualize(self):
        img = Image.open(self.image_path)
     
        img_array = np.array(img)
        
        wc = WordCloud(font_path=self.wc_font_path, width=400, height=400, scale=2.0, max_font_size=250, mask=img_array)
        
        gen = wc.generate_from_frequencies(self.c) # 빈도수에 따라 단어 크기 결정됨
        
        plt.figure()
        plt.imshow(gen)
        plt.show()
        
        wc.to_file('New_law1.png')

# wc = Word_Cloud(a, b, c)
# wc.get_file()
# wc.get_noun()
# wc.visualize()

wc = Word_Cloud()

wc

