class vrp():

    # Faz a leitura dos dados
    # Recebe self para que tenha acesso aos dados do objeto
    def __init__(self):
        # Guarda o numero de consumidores e a capaciedade de cada veiculo
        aux = input("Digite => Consumidores Capacidade:")
        print()
        # Mapeia a linha obtida pelo input para duas veriaveis distintas
        self.consumidores, self.capacidade = map(int, aux.split())
        # Guarda as coordenadas do deposito em uma lista
        aux = input("Digite => X Y")
        print()
        # Mapeia a linha obtida pelo input para tres variaveis auxiliares
        depositoX, depositoY  = map(int, aux.split())
        # Guarda o conteudo das auxiliares em uma lista
        self.deposito = [depositoX, depositoY]

        # Determina que as coordenadas de cada consumidor(ou cidade)a qual vai
        # estar em uma lista junto de sua respectiva demanda
        self.coordenadas = []
        for i in range(self.consumidores):
            aux = input("Digite => X Y Demanda")
            print()
            # Mapeia a linha obtida pelo input para tres variaveis auxiliares
            coordX, coordY, dem = map(int, aux.split())
            # Adiciona a lista os auxiliares contendo as coordenadas e a demanda
            self.coordenadas.append([coordX, coordY, dem])


    # Exibe as informacoes contidas no objeto
    # Recebe self para que tenha acesso aos dados do objeto
    def exibe(self):
        print(self.consumidores)
        print(self.capacidade)
        print(self.deposito)

        for i in self.coordenadas:
            print(i)



if __name__ == "__main__":
    vrp_ai = vrp()
    #vrp_ai.exibe()
