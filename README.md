# Python100knock
Pythonを修得するための100本ノック

エディタatomで，Markdownのリアルタイムプレビュー機能としてmarkdown-previewというパッケージを
入れている場合，Ctrl-Shift-mでプレビューできる．


# 趣旨
簡単な問題を解きつつ，Python流のコーディング技術を学ぶレッスンです．

1. 画面にHello worldと表示する．
[ソース](./hello.py)

2. 1から10までの和を求める．
[ソース](./sum1to10.py)

3. 整数の階乗を計算する．
[ソース](./int_factorial.py)

4. 文字列を合成してhelloworldを表示する．
[ソース](./compstr.py)

5. キーボードから文字列を入力
[ソース](./inputStr.py)

6. キーボードから数値を入力
[ソース](./inputInt.py)

7. ポンドを入力すると，キログラムに変換する関数を持つプログラムを作成しなさい．1ポンドは0.45359237キログラムである．
[ソース](./pound2kg.py)

8. 以前，3の倍数と3が付く数値のときだけアホになるというギャグがあった．
彼のギャグが本当に計算間違いなく，上記の条件でアホになっていたか検証したい．
ただし作成するプログラムにおいて，「アホ」という言葉は教育上ふさわしくない．
そこで3の倍数と3が付く数値のときは「いまでしょ!」と出力し，それ以外の数値では
「いつやるか?」と出力することにする．
調べる数値は1からnまでとし，nは標準入力で与える．
[ソース](./imadesho.py)

9. 文字列を入力し，その文字列の単語の数をカウントする．"Just a moment please."
の場合，4と出力される．
[ソース](./countWards.py)

10. 一番素朴にファイル入力を行う．ファイル内容を1行ずつ読み取って出力する．
[ソース](./inputFile.py)

11. csvファイルをpandasで読み込む．
[ソース](./inputCSV.py)

12. 10進数を2進数に変換.
[ソース](./10to2.py)

13. リストに0から9までの数値を代入し，ランダムシャッフルして出力する．
[ソース](./randomshuffle.py)

14. 次の学籍番号を生成し，それをファイル出力するプログラムを作成せよ．
a8701, a8702, ... , a8740
[ソース](./makenumber.py)

15. 学籍番号データが与えられている．この学籍番号を隠すために，別の数値を割り当てる．一方，
別の数値から，元の学籍番号を参照できるようにしたい．そのような変換テーブルを作れ．
例えば，
a8701,4
a8702,5
a8703,1
a8704,3
a8705,2
のような対応表を作ることになる．
[データ](./number.csv)
[ソース](./maketable.py)

16. user1からuser40までのディレクトリを作成しなさい．
[ソース](./makedir.py)

17. ファイル40個作成せよ．ファイル名はa8701からa8740とする．内容は'hello world. a8701'とファイル名が記述された内容とする．
[ソース](./makefile40.py)

18. 学籍番号でネーミングされたファイルa8701からa8740がある．これらのファイルはrenameディレクトリ以下にある．
これらのファイル名を変換テーブルに
したがってリネームするプログラムを作成せよ．変換テーブルファイルはrename/henkan.csvで与えられる．
40人のうち何人かのファイルは紛失して可能性がある点に注意すること．
[データ](./rename/henkan.csv)
[ソース](./rename.py)

19. 2×2の行列に0~1までのランダムな値(一様乱数)をセットする．
[ソース](./random_matrix.py)

20. matplotlibを使って，y = 3*x**2 - 1のグラフを描画．
[ソース](./plotline.py)

21. RPGのゲームを作りたい．そこでキャラクターの属性をランダムに与え，キャラクターを作ることにする．属性は以下の7種類とする．クラスを使わなくてよい．
HP, MP，攻撃力，防御力，素早さ，知性，運
[ソース](./player.py)

22. 21問目に引き続きRPGのゲームを作りたい．今度はクラスを定義してキャラクターを3体生成する．
[ソース](./playerClass.py)

23. プログラムへの引数として，13桁のISBNコード（例えば，9784873116556）を文字列で渡す．そして，その数字の和を求める．
[ソース](./getISBN.py)

23. 13桁のISBNコード（例えば，9784873116556）を文字列として入力し，チェックデジットの値が正しいかチェックする．チェックデジットについては，以下のURLで調べよ．
https://ja.wikipedia.org/wiki/ISBN
[ソース](./checkISBN.py)
