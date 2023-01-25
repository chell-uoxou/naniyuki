# https://qiita.com/shimajiroxyz/items/81452afdedaed767f436

import MeCab
import jaconv

#記号を削除する関数
#(以下
#http://prpr.hatenablog.jp/entry/2016/11/23/Python%E3%81%A7%E5%85%A8%E8%A7%92%E3%83%BB%E5%8D%8A%E8%A7%92%E8%A8%98%E5%8F%B7%E3%82%92%E3%81%BE%E3%81%A8%E3%82%81%E3%81%A6%E6%B6%88%E3%81%97%E5%8E%BB%E3%82%8B
#よりそのまま引用)
import unicodedata
import string

def format_text(text):
    text = unicodedata.normalize("NFKC", text)  # 全角記号をざっくり半角へ置換（でも不完全）

    # 記号を消し去るための魔法のテーブル作成
    table = str.maketrans("", "", string.punctuation  + "「」、。・")
    text = text.translate(table)

    return text
#(引用ここまで)

m = MeCab.Tagger() #形態素解析用objectの宣言

def getPronunciation(text):
    m_result = m.parse(text).splitlines() #mecabの解析結果の取得
    m_result = m_result[:-1] #最後の1行は不要な行なので除く

    pro = '' #発音文字列全体を格納する変数
    for v in m_result:
        if '\t' not in v: continue
        surface = v.split('\t')[0] #表層形
        # p = v.split('\t')[1].split(',')[-1] #発音を取得したいとき
        p = v.split('\t')[1].split(',')[-2] #ルビを取得したいとき
        #発音が取得できていないときsurfaceで代用
        if p == '*': p = surface
        pro += p
 
    pro = jaconv.hira2kata(pro) #ひらがなをカタカナに変換
    pro = format_text(pro) #余計な記号を削除

    return pro