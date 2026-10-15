from maps.AbstractGakushoku import AbstractGakushoku
class AiraOsusume(AbstractGakushoku):
    def get_menu(self):
        return "馬鹿坊の100円朝食"

    def get_summary(self):
        return "安くて量が多いので、朝からお腹いっぱいになれます。飲み物も付いてきます。"

    def get_author(self):
        return "まつおか"