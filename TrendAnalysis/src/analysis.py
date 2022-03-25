# 拾ってきたツイートを元に感情分析を行う
from mlask import MLAsk
# 最初，MeCabは何故かImportErrorが出て太刀打ちできなかったが，以下のリンクを参考にMecabの動作を確認．
# https://qiita.com/G1998G/items/2ad1b62c0285e478bfab


class Feeling:
    """MLAskで感情を分析するクラス"""

    def __init__():
        pass

    def feeling(self, word):
        """感情分析を行う関数，１０この感情をどう振り分けるかを検討中"""
        analyzer = MLAsk()
        ans = analyzer.analyze(word)






