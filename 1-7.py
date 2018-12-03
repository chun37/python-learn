### if文の応用その1

# 条件を増やしたい時
#例
number = 10
if number > 10:
    print("numberは10より大きいです")
elif number < 5:
    print("numberは5より小さいです")
else:
    print("numberは10以下で5以上です")

# 付け足したい比較の式をelifのあとに記述する
# コロンの次の行に4つスペースを入れるのは同じ
# ifの条件にあてはまったらelifの後やelseの後の処理は行われない
# elifも然り
# 例のnumberの数字を変えてみて確かめてみよう

