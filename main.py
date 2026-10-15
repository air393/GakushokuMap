from maps.GakushokuSample import GakushokuSample
from maps.Gakusyoku_mizoshita import Gakushoku_mizoshita

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample()]
data = [Gakushoku_mizoshita(),
        GakushokuSample()
        ]
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
