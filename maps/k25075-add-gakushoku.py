from maps.AbstractGakushoku import AbstractGakushoku
class GakushokuSample(AbstractGakushoku):
    def get_menu(self):
        return "AITランチ"

    def get_summary(self):
        return "量が多く３種類のおかずが乗っていてお腹いっぱいになります。"

    def get_author(self):
        return "鈴木"