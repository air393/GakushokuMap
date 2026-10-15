from maps.GakushokuSample import GakushokuSample
from maps.AiraOsusume import AiraOsusume
from maps.Gakusyoku_mizoshita import Gakushoku_mizoshita
from maps.k25075addgakushoku import k25075addgakushoku

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [Gakushoku_mizoshita(),
        AiraOsusume(),
        k25075addgakushoku(),
        GakushokuSample()
        
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
