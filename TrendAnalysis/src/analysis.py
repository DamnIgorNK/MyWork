from mlask import MLAsk
import re
import janome



class AnalyzeSentence:
    """MLAskで感情を分析するクラス"""

    def __init__(self):
        pass
        self.feeling("今日は仕事だったんだけど，大変だったよ．")
        self.feeling("後輩がめちゃくちゃ頑張ってくれて，おれは嬉しいよ")
        self.feeling("うあーーー")

    def feeling(self, sentence):
        """感情分析を行う関数，１０この感情をどう振り分けるかを検討中"""
        analyzer = MLAsk()
        emotion_dict = analyzer.analyze(sentence)
        print(emotion_dict)
        try:
            emotion_orientation = emotion_dict['orientation']
            emotion = emotion_dict["emotion"]
        except KeyError:
            print("NEUTRAL")
        
        return emotion_dict


t = AnalyzeSentence()







