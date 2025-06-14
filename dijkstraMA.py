from re import I
# -- coding: latin-1 --

import sys  # Importa o m�dulo sys para controle do sistema.
import networkx as nx  # Importa a biblioteca networkx para manipula��o de grafos.
import matplotlib.pyplot as plt  # Importa o matplotlib para visualiza��o de grafos.

def dijkstra(ini, fin, grafo):  # Grafo como MA.
    if ini == fin:
        return "Somente o vértice inicial está no caminho", 0

    n = len(grafo)
    resolvido = [False] * n
    resolvido[ini] = True
    distancia = [sys.maxsize] * n
    distancia[ini] = 0
    anterior = [-1] * n

    while not resolvido[fin]:
        menorDistancia = sys.maxsize
        proximo = -1
        for i in range(n):
            if resolvido[i]:  # Só considera vértices já resolvidos
                for j in range(n):
                    peso = grafo[i][j]
                    if peso > 0 and not resolvido[j]:
                        novaDistancia = distancia[i] + peso
                        if novaDistancia < distancia[j]:
                            distancia[j] = novaDistancia
                            anterior[j] = i
        # Escolhe o próximo vértice com menor distância não resolvido
        for j in range(n):
            if not resolvido[j] and distancia[j] < menorDistancia:
                menorDistancia = distancia[j]
                proximo = j

        if proximo == -1:
            return "Não há caminho possível.", None

        resolvido[proximo] = True

    # Reconstrução do caminho
    caminho = []
    verticeAtual = fin
    while verticeAtual != ini:
        caminho.insert(0, verticeAtual)
        verticeAtual = anterior[verticeAtual]
        if verticeAtual == -1:
            return "Caminho Inexistente", None
    caminho.insert(0, ini)

    return caminho, distancia[fin]


# Fun��o para plotar os grafos original e resultante de Dijkstra.
# 'grafo' cont�m a matriz de adjac�ncias e 'caminho' cont�m o menor caminho.
# 'ini' e 'fin' s�o os v�rtices inicial e final respectivamente.
# 'desig' s�o as designa��es dos v�rtices (nomes).
def plot_grafos(grafo, caminho, ini, fin, desig, Comp):
   G = nx.Graph()  # Grafo original.
   G_result = nx.Graph()  # Grafo resultante.

   # Adiciona as arestas do grafo original.
   for i in range(len(grafo)):  # Percorre os v�rtices.
      for j in range(len(grafo[i])):  # Percorre os vizinhos.
         if grafo[i][j] > 0:  # Se existe uma aresta.
            G.add_edge(i, j, weight=grafo[i][j])  # Aresta no grafo original.
            G_result.add_edge(i, j, weight=grafo[i][j])  # Aresta no grafo resultante.

   pos = nx.spring_layout(G, seed=24)  # Define a disposi��o dos n�s no gr�fico.

   # Plota o grafo original.
   plt.figure(figsize=(10, 5))
   plt.subplot(1, 2, 1)  # Primeiro gr�fico.
   nx.draw(G, pos, with_labels=True, labels={i: desig[i] for i in range(len(desig))},
          node_color='lightgray', node_size=500, font_size=10, font_color='black',
          edge_color='black', linewidths=1, edgecolors='black')  # Arestas e pesos em preto.
   nx.draw_networkx_nodes(G, pos, nodelist=[ini], node_color='lightgreen',
                         edgecolors='black', linewidths=0)  # Inicial em verde claro.
   nx.draw_networkx_nodes(G, pos, nodelist=[fin], node_color='lightsalmon',
                         edgecolors='black', linewidths=0)  # Final em laranja claro.
   nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d
                                                    in G.edges(data=True)}, font_color='black', rotate=False)
   plt.title("Grafo Original")  # T�tulo.

   # Plota o grafo resultante.
   plt.subplot(1, 2, 2)  # Segundo gr�fico.
   edge_colors = ['lightgray' if not (u in caminho and v in caminho and abs(
      caminho.index(u) - caminho.index(v)) == 1) else 'black' for u, v in
                 G_result.edges()]  # Arestas n�o pertencentes ao caminho em cinza claro.
   nx.draw(G_result, pos, with_labels=True, labels={i: desig[i] for i in range(
      len(desig))}, node_color='lightgray', node_size=500, font_size=10,
          font_color='black', edge_color=edge_colors, linewidths=1,
          edgecolors='black')  # Arestas configuradas.
   nx.draw_networkx_nodes(G_result, pos, nodelist=[ini], node_color='lightgreen',
                         edgecolors='black', linewidths=0)  # Inicial em verde claro.
   nx.draw_networkx_nodes(G_result, pos, nodelist=[fin], node_color='lightsalmon',
                         edgecolors='black', linewidths=0)  # Final em laranja claro.
   edge_labels_result = {(u, v): d['weight'] for u, v, d in G_result.edges(data=True)}
   # Exibe os r�tulos das arestas do grafo resultante com cor apropriada
   for (u, v) in edge_labels_result:
      color = 'black' if (u in caminho and v in caminho and abs(
         caminho.index(u) - caminho.index(v)) == 1) else 'lightgray'
      nx.draw_networkx_edge_labels(G_result, pos, edge_labels={(u, v): edge_labels_result[(u, v)]},
                                  font_color=color, rotate=False)

   plt.title("Grafo com Caminho M�nimo")  # T�tulo.
   plt.text(0.5, -0.1, f"Comprimento caminho: {Comp}", fontsize=10, ha='center',
           transform=plt.gca().transAxes)  # Exibe o comprimento total correto.

   plt.show()  # Exibe os dois gr�ficos.

# Fun��o principal para executar o programa.
# Cria as designa��es dos v�rtices e a matriz de adjac�ncias.
letra = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # Designa��es dos v�rtices.

# Define a matriz de adjac�ncias com os pesos das arestas.
MA = [
   [ 0,  5,  6, 10,  0, 0, 0],  # A
   [ 5,  0,  0,  0, 13, 0, 0],  # B
   [ 6,  0,  0,  3, 11, 6, 0],  # C
   [10,  0,  3,  0,  6, 4, 0],  # D
   [ 0, 13, 11,  6,  0, 0, 3],  # E
   [ 0,  0,  6,  4,  0, 0, 8],  # F
   [ 0,  0,  0,  0,  3, 8, 0]  # G
   ]  # Matriz de adjac�ncias que representa o grafo.

orig = 3  # Define o v�rtice inicial ('A').
destf = 1  # Define o v�rtice final ('G').

# Imprime informa��es sobre o v�rtice inicial e final.
print("\nVertice inicial.: " + letra[orig])  # Exibe o v�rtice inicial.
print("Vertice final...: " + letra[destf])  # Exibe o v�rtice final.

# Executa o algoritmo de Dijkstra e exibe o menor caminho e o seu custo.
caminho, Comp = dijkstra(orig, destf, MA)  # Executa Dijkstra.
print("Menor caminho de %s ateh %s: %-13s\nValor: %3d" %  # Exibe o resultado.
     (letra[orig], letra[destf], " > ".join(letra[v] for v in caminho), Comp))
CompTot = Comp

# Exibe outros caminhos para diferentes destinos a partir do v�rtice inicial.
print("\n--------------------------")
print("     Outros destinos")
print("--------------------------")
print("Dest.  Caminho       Custo")
print("--------------------------")

# La�o para encontrar e exibir o menor caminho para todos os v�rtices.
for dest in range(len(MA)):  # Percorre todos os destinos.
   if orig != dest and dest != destf:  # Exclui o v�rtice inicial e final.
      Path, Comp = dijkstra(orig, dest, MA)  # Calcula o caminho.
      print(" " + letra[dest], end="     ")
      print("%-13s %3d" % (" > ".join(letra[v] for v in Path), Comp))
      # Acima: exibe (associa letra ao �ndice).

# Plota os grafos original e resultante com o comprimento total.
plot_grafos(MA, caminho, orig, destf, letra, CompTot)  # Chama a fun��o para plotar.
