class ClaculaTrocoComCedula:

    def __init__(self):
        self.__cedulas = [0.05, 0.10, 0.25, 0.50, 1, 2, 5, 10, 20, 50, 100, 200]
    
    def troco_com_cedula(self, entrada, custo):
        troco = entrada - custo
        index = len(self.__cedulas) - 1
        cedulas_selecionadas = []
        print(f"TROCO INICIAL: {troco}")

        while index > -1:
            if troco == 0.00:
                break
            elif troco / self.__cedulas[index] >= 1:
                cedulas_selecionadas.append(self.__cedulas[index])
                troco = troco - self.__cedulas[index]
                print(f"TROCO: {troco} CEDULA: {self.__cedulas[index]}")

            index += self.ler_cedula_novamente(troco, self.__cedulas[index])
            
            index -= 1
        
        return cedulas_selecionadas

    def ler_cedula_novamente(self, troco, cedula):
        if troco >= cedula:
            return 1
        else:
            return 0