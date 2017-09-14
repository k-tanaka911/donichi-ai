# donichi-ai

## 概要

シェル上で動く対話式アプリケーションで、プログラミング教育用のプロトタイプです。

## 環境

- Python 3系  
- [Mecab](http://taku910.github.io/mecab/)

## 動かし方

### import.txt準備

回答文生成用ファイル[import.txt](/library/import.txt)を作成します。
同フォルダにある[import.txt.example](/library/import.txt.example)をコピーし、import.txtという名前で同ディレクトリに保存してください。

### 起動

```console
$ git clone https://github.com/donichiPython/donichi-ai.git
$ cd donichi-ai
$ python main.py
```

### 終了

`さようなら` と入力すれば終了します。

## 機能

### パターンマッチで定型文を返す

ユーザーから入力された文章に特定のワードがマッチしたら定型文を返します。マッチさせるワードと定型文の組み合わせは [pattern.csv](/libraty/pattern.csv) で定義します。

### 形態素解析とマルコフ連鎖

起動時に、[import.txt](/library/import.txt) を形態素解析して、マルコフ連鎖テーブルを生成します。上記パターンマッチ処理で何も該当しなかった場合は、ユーザー入力を形態素解析し、その中のランダムな名詞を起点にマルコフ連鎖にて回答文を生成します。

### 教育

マルコフ連鎖の語彙を増やしたい場合、`@` で始まるテキストを入力すると、[import.txt](/library/import.txt) に以降の文章を追記します。
