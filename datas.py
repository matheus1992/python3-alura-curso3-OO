# EXERCICIO FORMATAR DATA COM CLASSE.METODO
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        return "{}/{}/{}".format(self.dia, self.mes, self.ano)