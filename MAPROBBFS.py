# -*- coding: latin-1 -*-

import matplotlib.pyplot as plt
import networkx as nx

def recomendar_amigos_matriz(matriz_adj, usuario_id):
   """
   Esta fun��o gera recomenda��es de amizade para um usu�rio espec�fico em
   um grafo representado por uma matriz de adjac�ncia passada como par�metro
   (matriz_adj): as conex�es n�o valoradas e n�o direcionadas representam
   uma amizade.
   
   A fun��o segue o conceito de "amigos de amigos" para gerar recomenda��es.
   Ela recomenda apenas amigos de amigos que ainda n�o sejam amigos diretos
   do usu�rio selecionado. 
   
   Para isso, a fun��o faz o seguinte:

   1. Inicializa duas estruturas de dados tipo conjunto: 'amigos_diretos' para
   armazenar os amigos diretos do usu�rio e 'recomendacoes' para armazenar as
   recomenda��es de amizade. Conjuntos s�o utilizados porque eles automaticamente
   evitam duplicatas e t�m opera��es r�pidas de adi��o e verifica��o de
   elementos (exemplo de cria��o de conjunto: recomendacoes = set() )

   2. Itera sobre todos os v�rtices (usu�rios) no grafo para identificar amigos
   diretos do usu�rio selecionado (usuario_id). Se uma entrada 
   matriz_adj[usuario_id][i] for 1, isso significa que o usu�rio i � um amigo
   direto e � adicionado ao conjunto 'amigos_diretos'.

   3. Para cada amigo direto identificado, a fun��o itera novamente por todos os
   v�rtices para encontrar amigos de amigos. Se matriz_adj[amigo][i] for 1 e i
   n�o for o usu�rio selecionado nem um amigo direto, i � adicionado ao conjunto
   'recomendacoes'.

   4. Finalmente, a fun��o retorna a lista de recomenda��es, convertendo o
   conjunto 'recomendacoes' em uma lista (list(recomendacoes)) para o resultado
   final.
   """
      
   """
   COMPLETAR COMPLETAR COMPLETAR 
   """ 
   
def recomendar_amigos_matriz(matriz_adj, usuario_id):
   """
   Gera recomenda��es de amizade para um usu�rio em um grafo representado
   por uma matriz de adjac�ncia. A recomenda��o � de amigos de amigos
   que ainda n�o sejam amigos diretos do usu�rio.
   """
   num_vertices = len(matriz_adj)  # N�mero de v�rtices no grafo.
   amigos_diretos = set()  # Conjunto para armazenar amigos diretos do usu�rio.
   recomendacoes = set()   # Conjunto para armazenar as recomenda��es de amizade.

   # Utiliza-se conjuntos ("set()") para armazenar amigos diretos e recomenda��es
   # porque conjuntos evitam automaticamente elementos duplicados. Isso � �til
   # porque se quer garantir que cada amigo ou recomenda��o apare�a apenas uma vez,
   # mesmo que m�ltiplos caminhos no grafo levem ao mesmo amigo ou recomenda��o.
   # Al�m disso, opera��es como adicionar elementos a um conjunto e verificar
   # a exist�ncia de um elemento em um conjunto s�o muito r�pidas, o que torna
   # o uso de conjuntos eficiente para este prop�sito.

   # Itera sobre todos os v�rtices para identificar amigos diretos do usu�rio.
   for i in range(num_vertices):
      if matriz_adj[usuario_id][i] == 1:  # Verifica se existe uma liga��o direta.
         amigos_diretos.add(i)  # Adiciona o v�rtice ao conjunto de amigos diretos.

   # Itera sobre cada amigo direto para encontrar amigos de amigos.
   for amigo in amigos_diretos:
      for i in range(num_vertices):
         # Verifica se h� uma conex�o do amigo para um novo n�,
         # que n�o seja o usu�rio nem um amigo direto.
         if matriz_adj[amigo][i] == 1 and i != usuario_id and i not in amigos_diretos:
            recomendacoes.add(i)  # Adiciona ao conjunto de recomenda��es.

   return list(recomendacoes)  # Retorna a lista de recomenda��es.

def desenhar_recomendacoes_matriz(matriz_adj, usuario_id, recomendacoes, nomes_usuarios):
   """
   Desenha o grafo com o usu�rio selecionado e suas recomenda��es de amizade.
   Utiliza a biblioteca NetworkX para cria��o do grafo e Matplotlib para desenhar.
   """
   G = nx.Graph()    # Cria um grafo n�o direcionado.
   cores_nomes = {}  # Dicion�rio para armazenar as cores dos n�s (nomes dos usu�rios).
   
   # Adiciona arestas ao grafo usando os nomes dos usu�rios.
   for i in range(len(matriz_adj)):
      for j in range(i, len(matriz_adj)):  # Itera apenas uma vez por par (i, j).
         if matriz_adj[i][j] == 1:  # Verifica a exist�ncia de uma aresta.
            G.add_edge(nomes_usuarios[i], nomes_usuarios[j])  # Adiciona aresta.
   
   # Define as cores dos n�s baseando-se em nomes de usu�rios e recomenda��es.
   for i in range(len(matriz_adj)):
      if i == usuario_id:
         cores_nomes[nomes_usuarios[i]] = 'green'  # Cor do usu�rio selecionado.
      elif i in recomendacoes:
         cores_nomes[nomes_usuarios[i]] = 'red'    # Cor para recomenda��es.
      else:
         cores_nomes[nomes_usuarios[i]] = 'black'  # Cor para os outros n�s.
   
   # Calcula a posi��o dos n�s para o layout do grafo.
   pos = nx.spring_layout(G)   # Usa o layout de mola para distribuir os n�s.
   plt.figure(figsize=(6, 4))  # Define o tamanho da figura.
   
   # Define o t�tulo do grafo.  
   nomes_recomendados = [nomes_usuarios[i] for i in recomendacoes]
   Tit = f"Recomenda��es de amizade para {nomes_usuarios[usuario_id]}:\n"
   Tit += ", ".join(nomes_recomendados) +"."
   plt.title(Tit)  

   # Desenha o grafo com cores dos v�rtices em branco e peso de fonte em negrito.
   nx.draw(G, pos, with_labels=False, node_color='white', font_weight='bold')
   
   # Itera sobre cada item no dicion�rio "pos", que cont�m as posi��es
   # dos n�s do grafo. Cada item � uma chave-valor, onde a chave "node" 
   # � o nome do n� (por exemplo, 'Ana', 'Bruno') e o valor "(x, y)" 
   # � uma tupla contendo as coordenadas de posi��o do n� no plano 2D.
   for node, (x, y) in pos.items():
      
      # Verifica se o n� atual � o usu�rio selecionado.
      if node == nomes_usuarios[usuario_id]:
         facecolor = '#FFD700'  # Define a cor de fundo como amarelo um pouco mais escuro.    
      
      # Se o n� n�o for o usu�rio selecionado, verifica se ele est� na lista de recomenda��es.
      elif node in [nomes_usuarios[i] for i in recomendacoes]:
         facecolor = '#ADD8E6'  # Define a cor de fundo como azul claro para recomenda��es.    
      
      # Se o n� n�o for o usu�rio nem uma recomenda��o, define a cor de fundo como branca.
      else:
         facecolor = 'white' 
      
      # Desenha o texto do nome do n� no grafo com as configura��es de cor de fundo e texto.
      plt.text(x, y, node, fontsize=10, ha='center', va='center', 
              bbox=dict(facecolor=facecolor, edgecolor='black', boxstyle='round,pad=0.2'), 
              color=cores_nomes[node])
   
   # Exibe a figura.
   plt.show()  # Mostra o grafo na tela.

def criar_grafo_exemplo_matriz():
   """
   Cria um grafo exemplo com 10 v�rtices e uma densidade moderada
   para testar a recomenda��o de amizade.
   """
   # Matriz de adjac�ncia representando as conex�es de amizade.
   matriz_adj = [
      [0, 1, 1, 0, 0, 1, 0, 0, 0, 0],  # Ana -> Bruno, Carla, Fabio.
      [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],  # Bruno -> Ana, Daniel, Gabriela.
      [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # Carla -> Ana, Daniel, Eduarda.
      [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],  # Daniel -> Bruno, Carla, Henrique.
      [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],  # Eduarda -> Carla, Fabio, Isabela.
      [1, 0, 0, 0, 1, 0, 1, 0, 0, 0],  # Fabio -> Ana, Eduarda, Gabriela.
      [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],  # Gabriela -> Bruno, Fabio, Henrique.
      [0, 0, 0, 1, 0, 0, 1, 0, 1, 1],  # Henrique -> Daniel, Gabriela, Isabela, Jo�o.
      [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],  # Isabela -> Eduarda, Henrique, Jo�o.
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]   # Jo�o -> Henrique, Isabela.
      ]
   return matriz_adj  # Retorna a matriz de adjac�ncia.

# Execu��o do exemplo de uso.
nomes_usuarios = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", 
                 "Fabio", "Gabriela", "Henrique", "Isabela", "Jo�o"]
matriz_adj = criar_grafo_exemplo_matriz()  # Cria o grafo exemplo.

# Solicita ao usu�rio para escolher um nome da lista.
print("Usu�rios dispon�veis:", ", ".join(nomes_usuarios))
nome_usuario = input("Digite o nome do usu�rio para ver as recomenda��es: ")
usuario_id = nomes_usuarios.index(nome_usuario)  # Obt�m o �ndice do usu�rio selecionado.

# Gera e exibe as recomenda��es de amizade.
recomendacoes = recomendar_amigos_matriz(matriz_adj, usuario_id)
nomes_recomendados = [nomes_usuarios[i] for i in recomendacoes]
print("Recomenda��es de amizade para {}: {}".format(nome_usuario, ", ".join(nomes_recomendados)))

# Desenha o grafo com as recomenda��es.
desenhar_recomendacoes_matriz(matriz_adj, usuario_id, recomendacoes, nomes_usuarios)
