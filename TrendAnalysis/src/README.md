# Twitter感情分析
Twitterでトレンドになっている項目を適宜ピックアップして，感情分析を行う．
嬉しいニュース・悲しいニュースと言ったようにカテゴリ分けを行って，webアプリ形式で共有を試みるのがいいかなと思った．

## 1. 情報収集
基本的な情報収集はTwitterから行う．Twitterでは条件付きではあるがAPI機能を使用することができるためGETリクエストを用いてトレンドを取得する．

## 2．感情分析
感情分析はPythonライブラリにあるML-Askと，AWSが提供しているフルマネージドサービスであるAmazon Comprehendを用いる．

### 2.1. ML-Ask
Pythonライブラリである．

### 2.2. Amazon Comprehend
Amazonが提供している感情分析サービスである．任意の文章を入力すると感情や構造解析結果が出力されるものである．
本プログラムで上げる程度なら，料金の問題は特に必要ないかなと思う．<br>詳細については以下の公式リンク．<br>https://aws.amazon.com/jp/comprehend/


