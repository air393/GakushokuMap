from maps.Gakusyoku_mizoshita import Gakushoku_mizoshita
from maps.AiraOsusume import AiraOsusume
from maps.k25075addgakushoku import k25075addgakushoku
from maps.k25067 import k25067

data = [Gakushoku_mizoshita(),
        AiraOsusume(),
        k25075addgakushoku(),
        k25067()
       ]
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
