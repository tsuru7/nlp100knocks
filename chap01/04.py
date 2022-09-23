# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. 
# Arthur King Can.”
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
# 連想配列（辞書型もしくはマップ型）を作成せよ

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ones = [1, 5, 6, 7, 8, 9, 15, 16, 19]
words = s.split()
elems = {}
for idx, word in enumerate(words):
    if idx + 1 in ones:
        elems[idx+1] = word[:1]
    else:
        elems[idx+1] = word[:2]
for k, v in elems.items():
    print(k, v)


