# -*- coding: latin-1 -*-

import matplotlib.pyplot as plt
import networkx as nx

def recomendar_amigos_lista(lista_adj, usuario_id):
   """
   Esta fun��o gera recomenda��es de amizade para um usu�rio espec�fico em
   um grafo representado por uma lista de adjac�ncia passada como par�metro
   (lista_adj): as conex�es n�o valoradas e n�o direcionadas representam
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

   2. Identifica os amigos diretos do usu�rio selecionado acessando a lista
   de adjac�ncia na posi��o do usu�rio. Todos os amigos diretos s�o adicionados
   ao conjunto 'amigos_diretos'..

   3. Para cada amigo direto identificado, a fun��o itera sobre a lista de
   adjac�ncia desses amigos para encontrar amigos de amigos. Se o amigo de um
   amigo n�o for o usu�rio selecionado e n�o for um amigo direto, ele � adicionado
   ao conjunto 'recomendacoes'.

   4. Finalmente, a fun��o retorna a lista de recomenda��es, convertendo o
   conjunto 'recomendacoes' em uma lista (list(recomendacoes)) para o resultado
   final.
   """
   recomendacoes = set()
   amigos_diretos = set()
   for amigo in lista_adj[usuario_id]:
      amigos_diretos.add(amigo)
   for amigo in amigos_diretos:
    for i in lista_adj[amigo]:
      if i != usuario_id and i not in amigos_diretos:
        recomendacoes.add(i)
   return list(recomendacoes)
   """
   COMPLETAR COMPLETAR COMPLETAR
   """

def desenhar_recomendacoes_lista(lista_adj, usuario_id, recomendacoes, nomes_usuarios):
   """
   Desenha o grafo com o usu�rio selecionado e suas recomenda��es de amizade.
   Utiliza a biblioteca NetworkX para cria��o do grafo e Matplotlib para desenhar.
   """
   G = nx.Graph()    # Cria um grafo n�o direcionado.
   cores_nomes = {}  # Dicion�rio para armazenar as cores dos n�s (nomes dos usu�rios).

   # Adiciona arestas ao grafo usando os nomes dos usu�rios.
   for i in range(len(lista_adj)):
      for j in lista_adj[i]:  # Itera sobre cada amigo na lista de adjac�ncia.
         if i < j:  # Adiciona arestas apenas uma vez para evitar duplica��o.
            G.add_edge(nomes_usuarios[i], nomes_usuarios[j])  # Adiciona aresta.

   # Define as cores dos n�s baseando-se em nomes de usu�rios e recomenda��es.
   for i in range(len(lista_adj)):
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
   Tit += ", ".join(nomes_recomendados) + "."
   plt.title(Tit)

   # Desenha o grafo com cores dos v�rtices em branco e peso de fonte em negrito.
   nx.draw(G, pos, with_labels=True, node_color='white', font_weight='bold')

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
      plt.text(x, y, node, fontsize=12, ha='center', va='center',
              bbox=dict(facecolor=facecolor, edgecolor='black', boxstyle='round,pad=0.2'),
              color=cores_nomes[node])

   # Exibe a figura.
   plt.show()  # Mostra o grafo na tela.

def criar_grafo_exemplo_lista():
   """
   Cria um grafo exemplo com 10 v�rtices e uma densidade moderada
   para testar a recomenda��o de amizade.
   """
   # Lista de adjac�ncia representando as conex�es de amizade.
   lista_adj = [
      [1, 2, 5],       # Ana -> Bruno, Carla, Fabio.
      [0, 3, 6],       # Bruno -> Ana, Daniel, Gabriela.
      [0, 3, 4],       # Carla -> Ana, Daniel, Eduarda.
      [1, 2, 7],       # Daniel -> Bruno, Carla, Henrique.
      [2, 5, 8],       # Eduarda -> Carla, Fabio, Isabela.
      [0, 4, 6],       # Fabio -> Ana, Eduarda, Gabriela.
      [1, 5, 7],       # Gabriela -> Bruno, Fabio, Henrique.
      [3, 6, 8, 9],    # Henrique -> Daniel, Gabriela, Isabela, Jo�o.
      [4, 7, 9],       # Isabela -> Eduarda, Henrique, Jo�o.
      [7, 8]           # Jo�o -> Henrique, Isabela.
   ]
   return lista_adj  # Retorna a lista de adjac�ncia.

# Execu��o do exemplo de uso.
nomes_usuarios = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda",
                 "Fabio", "Gabriela", "Henrique", "Isabela", "Jo�o"]
lista_adj = criar_grafo_exemplo_lista()  # Cria o grafo exemplo.

# Solicita ao usu�rio para escolher um nome da lista.
print("Usu�rios dispon�veis:", ", ".join(nomes_usuarios))
nome_usuario = input("Digite o nome do usu�rio para ver as recomenda��es: ")
usuario_id = nomes_usuarios.index(nome_usuario)  # Obt�m o �ndice do usu�rio selecionado.

# Gera e exibe as recomenda��es de amizade.
recomendacoes = recomendar_amigos_lista(lista_adj, usuario_id)
nomes_recomendados = [nomes_usuarios[i] for i in recomendacoes]
print("Recomenda��es de amizade para {}: {}".format(nome_usuario, ", ".join(nomes_recomendados)))

# Desenha o grafo com as recomenda��es.
desenhar_recomendacoes_lista(lista_adj, usuario_id, recomendacoes, nomes_usuarios)

