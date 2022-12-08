from diaries.AbstractDiary import AbstractDiary

class  MuramatsuDiary(AbstractDiary):
    def get_date(self):
        return "2022-07-22"
    def get_summary(self):
        return "今日は誕生日だった"
    def get_author(self):
        return "村松"
