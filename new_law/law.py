from wordcloud import WordCloud 
import matplotlib.pyplot as plt # 데이터 시각화
from collections import Counter # 텍스트,빈도수 추출
from konlpy.tag import Okt # 한국어 처리 형태소 분석 패키지
from PIL import Image # 그림 불러오는 패키지
import numpy as np # 그림을 배열로 나타내어 처리할 수 있도록 도와주는 패키지

with open('C:/Users/user/Desktop/word_cloud/대한민국헌법.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# jvmpath= "C:/Program File/java/jdk-18.0.2/bin/server/jvm.dll"

okt = Okt() # 형태소 분석기 객체 생성
nouns = okt.nouns(text) # 명사만 추출

words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외

c = Counter(words) # 단어별 빈도수 형태의 딕셔너리 데이터를 구함


img = Image.open('C:/Users/user/Desktop/cloud.png')
img_array = np.array(img) # 이미지 픽셀 값 수치 변환

wc = WordCloud(font_path='H2PIRL', width=400, height=400, scale=2.0, max_font_size=250, mask=img_array) # 한글 폰트 지정
gen = wc.generate_from_frequencies(c) # 빈도수에 따라 단어 크기 결정됨
plt.figure()
plt.imshow(gen)

wc.to_file('law.png') # 파일로 추출


