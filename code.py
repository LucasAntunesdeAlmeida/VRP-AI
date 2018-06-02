 # ██╗   ██╗██████╗ ██████╗        █████╗ ██╗
 # ██║   ██║██╔══██╗██╔══██╗      ██╔══██╗██║
 # ██║   ██║██████╔╝██████╔╝█████╗███████║██║
 # ╚██╗ ██╔╝██╔══██╗██╔═══╝ ╚════╝██╔══██║██║
 #  ╚████╔╝ ██║  ██║██║           ██║  ██║██║
 #   ╚═══╝  ╚═╝  ╚═╝╚═╝           ╚═╝  ╚═╝╚═╝
 # Solucao do Problema de roteamento de veiculos utilizando savings
 # Lucas Antunes de Almeida - 161150753

from operator import itemgetter # Funcao que auxilia na ordenacao dos custos
from random import randint # Funcao resolpaser por sortear inteiros randomicos

class vrp():

    distancias = [] # Guarda as distancias das cidades
    rotas = [] # Guarda as rotas geradas
    custos = [] # Guarda os custo gerados por Sij = Ci0 + C0j - Cij

    def __init__(self): # Faz a leitura dos dados
        aux = input() # Guarda o numero de consumidores e a capaciedade de cada veiculo
        self.consumidores, self.capacidade = map(int, aux.split()) # Mapeia a linha obtida pelo input para duas veriaveis distintas

        aux = input() # Guarda as coordenadas do deposito em uma lista
        depositoX, depositoY  = map(int, aux.split()) # Mapeia a linha obtida pelo input para tres variaveis auxiliares
        self.deposito = [depositoX, depositoY, 0] # Guarda o conteudo das auxiliares em uma lista

        self.coordenadas = [] # Determina que as coordenadas de cada consumidor(ou cidade)a qual vai estar em uma lista junto de sua respectiva demanda
        self.coordenadas.append(self.deposito) # Adiciona as coordenadas do deposito para a lista de coordenadas geral
        for i in range(self.consumidores):
            aux = input()
            coordX, coordY, dem = map(int, aux.split()) # Mapeia a linha obtida pelo input para tres variaveis auxiliares
            self.coordenadas.append([coordX, coordY, dem]) # Adiciona a lista os auxiliares contendo as coordenadas e a demanda

    def exibe(self): # Exibe as informacoes lidas, contidas no objeto
        print(self.consumidores)
        print(self.capacidade)

        for i in self.coordenadas:
            print(i)

    def exibeDistancias(self): # Exibe as distancias calculadas
        for i in self.distancias:
            print(i)

    def exibeRotas(self): # Exibe as rotas encontradas
        for i in self.rotas:
            for j in i:
                print(j,'', end='')
            print()
            #print(self.returnDistancia(i), self.returnCapacidade(i))

    def exibeCustos(self): # Exibe os custos obtidos no calculo Sij = Ci0 + C0j - Cij
        for i in self.custos:
            print(i)

    def distancia(self, x1, y1, x2, y2): # Calcula as diastancias
        return ((((x2-x1)**2)+((y2-y1)**2))**(1/2)) # Usa pitagoras para calcular a distancia entre dois pontos

    def calculaDistancias(self): # Calcula a distancia entre as cidades
        for i in range(len(self.coordenadas)): # Foram usados dois for alinhados para determinar a distancia entre cada uma das cidades
            self.distancias.append([]) # Adiciona uma noma linha na matriz
            for j in range(len(self.coordenadas)):
                self.distancias[i].append(self.distancia(self.coordenadas[i][0], self.coordenadas[i][1], self.coordenadas[j][0], self.coordenadas[j][1]))

    def calculaCustoRotas(self): # Soma o custo das rotas geradas
        custo = 0
        for i in range(len(self.rotas)):
            custo += self.returnDistancia(self.rotas[i])

        print("Custo total: " + str(custo))

    def fechaRotas(self): # Fecha uma rota [i...n] com [0, i...n, 0]
        for i in self.rotas:
            i.insert(0, 0)
            i.append(0)

    def iniciaRotas(self): # Inicializa N rotas para N veiculos
        for i in range(1, len(self.coordenadas)):
            self.rotas.append([i])

    def iniciaCustos(self): # Inicializa a lista de custo utilizando a formula Sij = Ci0 + C0j - Cij para i diferente de j
        for i in range(1, len(self.coordenadas)):
            for j in range(1, len(self.coordenadas)):
                if i != j:
                    self.custos.append([i, j, (self.distancias[i][0] + self.distancias[0][j] - self.distancias[i][j])])

    def ordenaCustos(self): # Ordena os custos calculados previamente
        self.custos = sorted(self.custos, key=itemgetter(2), reverse=True) # Usa a funcao sorted para ordenar a lista de custos

    def returnCapacidade(self, list): # Verifica quanta demanda a rota esta usando
        cont = 0 # Acumulador
        for i in range(len(list)): # Soma a demanda de todas as cidades da rotas
            cont += self.coordenadas[list[i]][2]
        return cont # Retorna a demanda encontrada para a rota

    def returnDistancia(self, list):
        custo = 0
        for i in range(len(list)-1):
            custo += self.distancias[list[i]][list[i+1]]
        return custo

    def agrupaRotas(self): # Agrupa as rotas em rotas maiores
        for i in self.custos: # Percorre a lista gerada por Sij = Ci0 + C0j - Cij
            a = i[0] # Guarda o fim que sera verificado nas rotas
            b = i[1] # Guarda o inicio que sera verificado nas rotas
            cont = 0 # Auxiliar que determina quando parar o laco

            for j in self.rotas: # Percorre as rotas atuais
                if j[-1] == a: # Verifica o fim da rota atual
                    listA = j # Guarda a rota atual
                    cont+=1
                elif j[0] == b: # Verifica o inicio da rota atual
                    listB = j # Guarda a rota atual
                    cont+=1

                if cont == 2: # Quando tiver duas rotas entra aqui
                    aux = self.returnCapacidade(listA) + self.returnCapacidade(listB) # Guarda a soma das demandas da duas rotas selecionadas
                    if aux <= self.capacidade: # Checa se a soma das demandas nao ultrapassa a capacidade do caminhao
                        self.rotas.remove(listA) # Remove a rota selecionada para a primeira metade da lista de rotas
                        self.rotas.remove(listB) # Remove a rota selecionada para a segunda metade da lista de rotas
                        self.rotas.append(listA + listB) # Adiciona a lista de rotas uma nova rota constituida da unicao das rotas removidas anteriormente
                    break # Como entrou no if nao precisa mais rodar o for atual

    def trocasExternas(self): # Realiza trocas de cidades entre as rotas
        for i in range(10000): # Realiza 10000 iteracoes
            auxRota1 = randint(0,len(self.rotas)-1) # Sorteia o indice da primeira rota
            auxRota2 = randint(0,len(self.rotas)-1) # Sorteia o indice da segunda rota
            auxCidade1 = randint(0,len(self.rotas[auxRota1])-1) # Sorteia o indice de alguma cidade da primeira rota
            auxCidade2 = randint(0,len(self.rotas[auxRota2])-1) # Sorteia o indice de alguma cidade da segunda rota
            self.trocas(auxRota1, auxRota2, auxCidade1, auxCidade2) # Se possivel e vantajoso, realiza a troca das cidades


    def trocasInternas(self): # Realiza trocas de cidades internamente as rotas
        for i in range(len(self.rotas)): # Percorre a lista de rotas
            for j in range(1000): # Realiza 1000 iteracoes para cada rota
                auxCidade1 = randint(0,len(self.rotas[i])-1) # Sorteia uma cidade da rota atual
                auxCidade2 = randint(0,len(self.rotas[i])-1) # Sorteia uma cidade da rota atual
                self.trocas(i, i, auxCidade1, auxCidade2) # Se possivel e vantajoso, realiza a troca das cidades

    def trocas(self, auxRota1, auxRota2, auxCidade1, auxCidade2): # Se possivel e vantajoso, realiza a troca das cidades
        auxDistancia1_1 = self.returnDistancia(self.rotas[auxRota1]) # Guarda o valor da distancia da rota 1
        auxDistancia2_1 = self.returnDistancia(self.rotas[auxRota2]) # Guarda o valor da distancia da rota 2

        self.rotas[auxRota1][auxCidade1], self.rotas[auxRota2][auxCidade2] = self.rotas[auxRota2][auxCidade2], self.rotas[auxRota1][auxCidade1] # Troca as duas cidades selecionadas

        auxCapacidade1_2 = self.returnCapacidade(self.rotas[auxRota1]) # Guarda o novo valor da demanda da rota 1
        auxCapacidade2_2 = self.returnCapacidade(self.rotas[auxRota2]) # Guarda o novo valor da demanda da rota 2
        auxDistancia1_2 = self.returnDistancia(self.rotas[auxRota1]) # Guarda o valor da nova distancia da rota 1
        auxDistancia2_2 = self.returnDistancia(self.rotas[auxRota2]) # Guarda o valor da nova distancia da rota 2

        soma1 = auxDistancia1_1 + auxDistancia2_1 # Soma a distancias percorrida pelas rotas selecionas
        soma2 = auxDistancia1_2 + auxDistancia2_2 # Soma a distancia percorrida pelas duas novas rotas

        if not(
            (auxCapacidade1_2 <= self.capacidade) and # Checa se o valor da capacidade da rota 1 nao ultrapassa a capacidade do caminhao
            (auxCapacidade2_2 <= self.capacidade) and # Checa se o valor da capacidade da rota 2 nao ultrapassa a capacidade do caminhao
            (soma1 >= soma2)  # Checa se o novo valor da distancia eh melhor se o valor da distancia anterior
            ): # Caso algum dos teste de zero desfaz a troca
            self.rotas[auxRota1][auxCidade1], self.rotas[auxRota2][auxCidade2] = self.rotas[auxRota2][auxCidade2], self.rotas[auxRota1][auxCidade1] # desfaz a troca das duas cidades selecionadas

    def tabu(self): # Tenta melhorar as rotas geradas utilizando uma especie de busca tabu
        self.trocasExternas() # Realiza trocas de cidades entre as rotas
        self.trocasInternas() # Realiza trocas de cidades internamente as rotas

    def savings(self): # Algoritmo de Savings
        self.calculaDistancias() # Calcula as distancias entre as cidades
        self.iniciaRotas() # Chama o metodo responsavel por inicializar N rotas para N veiculos
        self.iniciaCustos() # Calcula os custo com base na formula Sij = Ci0 + C0j - Cij
        self.ordenaCustos() # Ordena a lista de custos
        self.agrupaRotas() # Agrupas as rotas com base na lista de custos ordenada acima
        #self.tabu() # Tenta melhorar as rotas geradas utilizando trocas aleatorias
        self.fechaRotas() # fecha as rotas encontradas adicionando 0 no inicio e 0 no fim
        self.exibeRotas() # Exibe as rotas geradas
        #self.calculaCustoRotas() # Calcula e exibe o custo das rotas geradas (distancia percorrida)

if __name__ == "__main__":
    vrp_ai = vrp() # Inicializa o objeto, e efetua a leitura dos dados
    vrp_ai.savings() # Utiliza o algoritmo de savings para encontrar as rotas
