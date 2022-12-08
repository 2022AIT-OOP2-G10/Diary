
from diaries.DiarySample import DiarySample
from diaries.k21014Diary import k21014Diary
from diaries.SomekiDiary import SomekiDiary
from diaries.MuramatsuDiary import MuramatsuDiary


#↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    k21014Diary(),
    SomekiDiary(),
    MuramatsuDiary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
