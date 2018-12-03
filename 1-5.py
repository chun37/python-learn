### 比較の式
# 何かしらの方法で比較を行うとbool型が返ってくる
# 比較が正しければTrue、正しくなければFalse

## int型の比較
# イコール
# 右と左が同じか否か
10 == 5 # 10は5と等しい -> 正しくないのでFalse
10 == 10 # 10は10と等しい -> 正しいのでTrue
# print関数で確認してみる
print("数字が同じか確認")
print(10 == 5)
print(10 == 10)

# 大なり、小なり
# 小学校で習ったものと内容は変わらない
10 > 5 # 10は5より大きい -> 正しいのでTrue
10 < 5 # 10は5より小さい -> 正しくないのでFalse
# print関数で確認してみる
print("大なり小なりの確認")
print(10 > 5)
print(10 < 5)

# 大なりイコール(≧)、小なりイコール(≦)
# > や < の後ろに = を付ける
10 <= 5 # 10は5以下 -> 正しくないのでFalse
10 >= 5 # 10は5以上 -> 正しいのでTrue
# print関数で確認
print("大なりイコール、小なりイコールの確認")
print(10 <= 5)
print(10 >= 5)

## str型の比較
# 右と左が同じか否か
"Python" == "Twitter" # PythonとTwitterは同じじゃないのでFalse
"Python" == "Python" # PythonとPythonは同じなのでTrue
# print関数で確認
print("文字が同じか確認")
print("Python" == "Twitter")
print("Python" == "Python")

