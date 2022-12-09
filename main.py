from diaries.DiarySample import DiarySample
from diaries.K21014Diary import K21014Diary
from diaries.SomekiDiary import SomekiDiary
from diaries.MuramatsuDiary import MuramatsuDiary
from diaries.Diary_k21091 import Diary_k21091
from diaries.k21054Diary import K21054Diary
from diaries.K20025Diary import K20025Diary

#↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    K21014Diary(),
    SomekiDiary(),
    MuramatsuDiary(),
    Diary_k21091(),
    K21054Diary(),
    K20025Diary()
]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
