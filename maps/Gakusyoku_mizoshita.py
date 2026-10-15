from maps.AbstractGakushoku import AbstractGakushoku
class Gakushoku_mizoshita(AbstractGakushoku):
    def get_menu(self):
        return "すき家"

    def get_summary(self):
        return "安くて早い"

    def get_author(self):
        return "溝下穣"