from diaries.DiarySample import DiarySample
from diaries.Diary_k21091 import Diary_k21091

#のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    Diary_k21091(),
    ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()