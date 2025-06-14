# -- coding: latin-1 --

import sys  # Importa o m�dulo sys para controle do sistema.
import networkx as nx  # Importa a biblioteca networkx para manipula��o de grafos.
import matplotlib.pyplot as plt  # Importa o matplotlib para visualiza��o de grafos.

def dijkstra(ini, fin, grafo):
    # grafo: lista de adjacência, grafo[u] = [(v, peso), ...]
    if ini == fin:
        return [ini], 0

    n = len(grafo)
    resolvido = [False] * n
    distancia  = [sys.maxsize] * n
    anterior   = [-1] * n

    # vértice inicial
    distancia[ini] = 0
    resolvido[ini] = True

    while not resolvido[fin]:
        menorDistancia = sys.maxsize
        proximo = -1

        # detecta arestas
        for i in range(n):
          if resolvido[i]:
            for j, peso in grafo[i]:
                novaDistancia = distancia[i] + peso
                if novaDistancia < distancia[j]:
                    distancia[j] = novaDistancia
                    anterior[j] = i
                # escolha do próximo
                if not resolvido[j] and distancia[j] < menorDistancia:
                    menorDistancia = distancia[j]
                    proximo = j

        # caminho impossível
        if proximo == -1:
            return None, float('inf')

        resolvido[proximo] = True

    # reconstrução do caminho
    caminho = []
    vert = fin
    while vert != ini:
        caminho.insert(0, vert)
        vert = anterior[vert]
        if vert == -1:
            return None, float('inf')

    caminho.insert(0, ini)
    return caminho, distancia[fin]

# Fun��o para plotar os grafos original e resultante de Dijkstra.
# 'grafo' cont�m o grafo de adjac�ncias e 'caminho' cont�m o menor caminho.
# 'ini' e 'fin' s�o os v�rtices inicial e final respectivamente.
# 'desig' s�o as designa��es dos v�rtices (nomes).
def plot_grafos(grafo, caminho, ini, fin, desig, Comp):
   G = nx.Graph()  # Grafo original.
   G_result = nx.Graph()  # Grafo resultante.

   # Adiciona as arestas do grafo original.
   for i in range(len(grafo)):  # Percorre os v�rtices.
      for vizinho, peso in grafo[i]:  # Arestas e pesos.
         G.add_edge(i, vizinho, weight=peso)  # Aresta no grafo original.
         G_result.add_edge(i, vizinho, weight=peso)  # Aresta no grafo resultante.

   pos = nx.spring_layout(G, seed=24)  # Define a disposi��o dos n�s no gr�fico.

   # Plotando o grafo original.
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
# Cria as designa��es dos v�rtices e a lista de adjac�ncias.
letra = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # Designa��es dos v�rtices.

# Define a lista de adjac�ncias com os pesos das arestas.
LA = [
   [(1, 5), (2, 6), (3, 10)],  # A
   [(0, 5), (4, 13)],  # B
   [(0, 6), (3, 3), (4, 11), (5, 6)],  # C
   [(0, 10), (2, 3), (4, 6), (5, 4)],  # D
   [(1, 13), (2, 11), (3, 6), (6, 3)],  # E
   [(2, 6), (3, 4), (6, 8)],  # F
   [(4, 3), (5, 8)]  # G
   ]  # Lista de adjac�ncias que representa o grafo.

LA =[
     [(1, 5), (2, 6), (3, 10)],
     [(0, 5), (4, 13)],
     [(0, 6), (3, 3), (4, 11), (5, 6)],
     [(0, 10), (2, 3), (4, 6), (5, 4)],
     [(1, 13), (2, 11), (3, 6), (6, 3)],
     [(2, 6), (3, 4), (6, 8)],
     [(4, 3), (5, 8)],
   ]

orig = 3  # Define o v�rtice inicial ('A').
destf = 1  # Define o v�rtice final ('G').

# Imprime informa��es sobre o v�rtice inicial e final.
print("\nVertice inicial.: " + letra[orig])  # Exibe o v�rtice inicial.
print("Vertice final...: " + letra[destf])  # Exibe o v�rtice final.

# Executa o algoritmo de Dijkstra e exibe o menor caminho e o seu custo.
caminho, Comp = dijkstra(orig, destf, LA)  # Executa Dijkstra.
print("Menor caminho de %c ateh %c: %-13s\nValor: %3d" %  # Exibe o resultado.
     (letra[orig], letra[destf], " > ".join(letra[v] for v in caminho), Comp))
CompTot = Comp

# Exibe outros caminhos para diferentes destinos a partir do v�rtice inicial.
print("\n--------------------------")
print("     Outros destinos")
print("--------------------------")
print("Dest.  Caminho       Custo")
print("--------------------------")

# La�o para encontrar e exibir o menor caminho para todos os v�rtices.
for dest in range(len(LA)):  # Percorre todos os destinos.
   if orig != dest and dest != destf:  # Exclui o v�rtice inicial e final.
      Path, Comp = dijkstra(orig, dest, LA)  # Calcula o caminho.
      print(" " + letra[dest], end="     ")
      print("%-13s %3d" % (" > ".join(letra[v] for v in Path), Comp))
      # Acima: exibe (associa letra ao �ndice).

# Plota os grafos com o comprimento total.
plot_grafos(LA, caminho, orig, destf, letra, CompTot)  # Chama a fun��o para plotar.