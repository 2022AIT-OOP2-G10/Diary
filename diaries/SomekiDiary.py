from diaries.AbstractDiary import AbstractDiary
class  SomekiDiary(AbstractDiary):
    def get_date(self):
        return "2022-12-13"
    def get_summary(self):
        return "今日はアーキテクチャのテストがあった。難しくてやりたくなかったが、頑張ってやるしかなかった。今日は自分にご褒美として甘いものを買って帰ろう。"
    def get_author(self):
        return "そめき"
