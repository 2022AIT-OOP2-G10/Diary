# -*- coding: utf-8 -*-
from diaries.DiarySample import DiarySample
<<<<<<< Updated upstream
from diaries.Diary_k21091 import Diary_k21091
=======
from diaries.MuramatsuDiary import MuramatsuDiary
>>>>>>> Stashed changes

#のリストには、メンバーの各日記が格納されます。
diaries = [
<<<<<<< Updated upstream
    DiarySample(),
    Diary_k21091(),
    ]
=======
    DiarySample(), 
    MuramatsuDiary(),
]
>>>>>>> Stashed changes
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()