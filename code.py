class vrp():

    distancias = []
    rotas = []
    visitado = []

    def __init__(self): # Faz a leitura dos dados
        aux = input() # Guarda o numero de consumidores e a capaciedade de cada veiculo
        self.consumidores, self.capacidade = map(int, aux.split()) # Mapeia a linha obtida pelo input para duas veriaveis distintas

        aux = input() # Guarda as coordenadas do deposito em uma lista
        depositoX, depositoY  = map(int, aux.split()) # Mapeia a linha obtida pelo input para tres variaveis auxiliares
        self.deposito = [depositoX, depositoY, 0] # Guarda o conteudo das auxiliares em uma lista

        self.coordenadas = [] # Determina que as coordenadas de cada consumidor(ou cidade)a qual vai estar em uma lista junto de sua respectiva demanda
        self.coordenadas.append(self.deposito) # Aciona as coordenadas do deposito para a lista de coordenadas geral
        for i in range(self.consumidores):
            aux = input()
            coordX, coordY, dem = map(int, aux.split()) # Mapeia a linha obtida pelo input para tres variaveis auxiliares
            self.coordenadas.append([coordX, coordY, dem]) # Adiciona a lista os auxiliares contendo as coordenadas e a demanda

    def exibe(self): # Exibe as informacoes lidas contidas no objeto
        print(self.consumidores)
        print(self.capacidade)

        for i in self.coordenadas:
            print(i)

    def calculaDistancias(self): # Calcula a distancia entre as cidades
        for i in range(len(self.coordenadas)): # Foram usados dois for alinhados para determinar a distancia entre cada uma das cidades
            self.distancias.append([]) # Adiciona uma noma linha na matriz
            self.visitado.append(0)
            for j in range(len(self.coordenadas)):
                self.distancias[i].append(self.distancia(self.coordenadas[i][0], self.coordenadas[i][1], self.coordenadas[j][0], self.coordenadas[j][1]))

    def exibeDistancias(self): # Exibe as distancias calculadas
        for i in self.distancias:
            print(i)

    def distancia(self, x1, y1, x2, y2): # Calcula as diastancias
        return ((((x2-x1)**2)+((y2-y1)**2))**(1/2)) # Usa pitagoras para calcular a distancia entre dois pontos

    def confirmVisitado(self): # Procura se existe alguma cidade para visitar
        for i in self.visitado:
            if i == 0: # Caso encontre alguma cidade valida retorn 1
                return 1
        return 0 # Caso nao encontre nenhuma cidade valida retorna 0

    def geraRotas(self): # Gera as rotas dos veiculos
        atual = 0 # Guarda a cidade atual
        aux = 99999 # Guarda a melhor relacao entre distancia e demanda encontrada
        prox = atual # Guarda a proxima cidade a ser visitada
        cont = 0 # Um dos possiveis criterios de parada do while()
        rota = 0 # Indica a rota atual
        caminhao = int(self.capacidade) # Guarda a capacidade do caminhao

        self.rotas.append([]) # Adiciona uma linha na matriz de rotas

        while self.confirmVisitado() > 0: # Enquanto tiver alguma cidade visitavel continua a executar
            self.visitado[atual] = 1 # Define que a cidade atual ja foi visitada
            prox = atual # Reseta o valor da proxima cidade
            #peso = 0

            for i in range(len(self.coordenadas)): # Percorre todas as cidades ligadas a cidade atual
                if self.visitado[i] == 0: # Se a cidade nao tiver sido visitada
                    peso = int(self.coordenadas[i][2]) # Converte o valor demanda da cidade e salva em um auxiliar
                    #print("peso convertido: "+str(peso) + " i " +str(i))
                    #print((caminhao - peso))
                    if (caminhao - peso) >= 0: # Verifica se o caminhao possui carga para fazer a entrega naquela cidade
                        #print("entrou "+str(caminhao)+" - "+str(peso) +" >= 0")
                        x1 = float(self.distancias[atual][i]) # Salva o valor da distancia da cidade atual para a proxima selecionada
                        aux2 = x1#/peso) # Calcula a relacao entre distancia e demanda
                        if aux > aux2: # Verifica se a relacao encontrada eh melhor que a encontrada anteriormente
                            #print("escolheu "+ str(aux)+ " > "+str(aux2) + " i "+str(i))
                            aux = aux2 # Atualiza a melhor relacao encontrada
                            prox = i # Atualiza a proxima cidade

            #print("atual "+str(atual)+" prox "+str(prox))
            #print("carga "+str(caminhao) + " peso " +str(peso))
            if atual != prox: # Adiciona a proxima cidade na rota atual e reseta os auxiliares
                #print("atual != prox")
                self.rotas[rota].append(atual) # Adiciona a cidade atual a lista de rotas
                caminhao-=self.coordenadas[prox][2]
                atual = prox
                aux = 99999
            else: # Reseta os auxiliares e muda a rota atual
                #print("atual == prox")
                self.rotas[rota].append(atual) # Adiciona a cidade atual para a lista de rotas
                self.rotas.append([])
                caminhao = int(self.capacidade)
                atual = 0
                aux = 99999
                self.rotas[rota].append(0) # Fecha a rota atual com o deposito
                rota+=1
            #print("carga "+str(caminhao))


        self.rotas.pop()
        self.exibeRotas()
        self.calculaCustoRotas()

    def exibeRotas(self): # Exibe as rotas encontradas
        for i in self.rotas:
            print(i)

    def exibeVisitado(self): # Exibe quais cidades foram ou nao visitadas
        print(self.visitado)

    def calculaCustoRotas(self):
        custo = 0;
        cont = 0;
        for i in range(len(self.rotas)):
            for j in range(len(self.rotas[i])-1):
                custo += self.distancias[self.rotas[i][j]][self.rotas[i][j+1]]

        print("Custo total: " + str(custo))


if __name__ == "__main__":
    vrp_ai = vrp()
    #vrp_ai.exibe()
    vrp_ai.calculaDistancias()
    #vrp_ai.exibeDistancias()
    vrp_ai.geraRotas()
