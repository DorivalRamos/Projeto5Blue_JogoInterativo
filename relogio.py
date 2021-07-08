class Relogio():
    def __init__(self):  # inicialização da classe relógio
        self.__horas = 6  # parâmetro pré-definido para o início do dia
        self.__minutos = 0  # parâmetro pré-definido para o início do dia

    def __str__(self):  # Função para formatar a string que será utilizada no arquivo main
        return f"{self.horas:02d}:{self.minutos:02d}"

    def avancaTempo(self, minutos):  # Método para avançar o tempo em minutos
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

    @property
    def horas(self):
        return self.__horas

    @property
    def minutos(self):
        return self.__minutos

    @horas.setter
    def horas(self, valor):
        self.__horas = valor

    @minutos.setter
    def minutos(self, valor):
        self.__minutos = valor
