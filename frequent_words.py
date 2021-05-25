import re
import MeCab
from collections import Counter

# ファイル読み込み
file = r'sampling_data/6_sora_12.txt'
with open(file) as f:
    text = f.read()

# URLの削除
text = re.sub('https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', text)

# RTの削除
text = re.sub('RT', '', text)

# ()の削除
text = re.sub('\(.+?\)', '', text)


# Mecab で形態素解析
#tagger = MeCab.Tagger('-Ochasen')
tagger = MeCab.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
result = tagger.parse(text)
result_lines = result.split('\n')

result_words = []
words = []

for result_line in result_lines:
    result_words.append(re.split('[\t,]', result_line))

for result_word in result_words:

    if (    result_word[0] not in ('EOS', '')
        and result_word[3] == '名詞-一般'):

            words.append(result_word[0])

# 頻出単語TOP10を抽出
counter = Counter(words)
for word, count in counter.most_common(15):
    print('%s : %s' % (word, count))