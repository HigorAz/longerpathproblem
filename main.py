"""
Caminho mais longo.
Leitura de arquivo de entrada com:
  # Numero de vertices
  5

  # Matriz de adjacencia, onde 0 significa ausencia de aresta
  0 1 2 0 0
  0 0 3 5 0
  0 0 0 1 2
  0 0 0 0 6
  0 0 0 0 0

  # Origem e destino (indices comecando em 0)
  0 4

Execucao:
  Comando padrao (Executa entrada.txt):
  python main.py
  Ou, caso queria personalizado:
  python main.py entrada1.txt
"""

from typing import List, Tuple, Optional
import sys

def parse_input_file(path: str) -> Tuple[int, List[List[int]], int, int]:
    # Le o arquivo de entrada ignorando linhas em branco e comentarios que comecam com '#'.
    # Retorna: (n, matriz, origem, destino)
    
    with open(path, 'r', encoding='utf-8') as f:
        raw = [line.strip() for line in f.readlines()]

    # remove comentarios e linhas vazias
    lines = []
    for line in raw:
        if not line:
            continue
        if line.strip().startswith('#'):
            continue
        lines.append(line)

    if not lines:
        raise ValueError("Arquivo de entrda vazio.")

    # primeira linha: numero de vertices
    n = int(lines[0])
    if n <= 0:
        raise ValueError("Numero de vertices deve ser positivo.")

    # próximas n linhas: matriz de adjacencia
    if len(lines) < 1 + n + 1:
        raise ValueError("Arquivo de entrada incompleto: matriz ou origem/destino ausentes.")

    matriz: List[List[int]] = []
    for i in range(1, 1 + n):
        row_str = lines[i].split()
        if len(row_str) != n:
            raise ValueError(f"Linha {i+1} da matriz deve ter {n} inteiros.")
        row = [int(x) for x in row_str]
        matriz.append(row)

    # ultima linha util: origem e destino
    origem_dest = lines[1 + n].split()
    if len(origem_dest) != 2:
        raise ValueError("Linha de origem e destino deve conter exatamente dois inteiros.")
    origem, destino = map(int, origem_dest)

    if not (0 <= origem < n and 0 <= destino < n):
        raise ValueError("Origem/destino fora do intervalo [0, n-1].")

    return n, matriz, origem, destino


def topo_sort_from_adj_matrix(n: int, adj: List[List[int]]) -> List[int]:

    # Lanca ValueError se detectar ciclo (i.e., se nao for DAG).
    indeg = [0] * n
    for u in range(n):
        for v in range(n):
            if adj[u][v] != 0:  # 0 = ausencia de aresta (atencao: nao suportamos aresta com peso 0)
                indeg[v] += 1

    # fila de graus de entrda zero
    queue = [i for i in range(n) if indeg[i] == 0]
    order: List[int] = []

    idx = 0
    while idx < len(queue):
        u = queue[idx]
        idx += 1
        order.append(u)
        # "remove" as arestas de u
        for v in range(n):
            if adj[u][v] != 0:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)

    if len(order) != n:
        raise ValueError("O grafo nao e aciclico (ciclo detectado).")
    return order


def longest_path_dag(
    n: int, adj: List[List[int]], s: int, t: int
) -> Tuple[Optional[List[int]], Optional[int]]:
    # Programacao dinamica em ordem topológica para DAG.
    # Distancas iniciam em -inf; dist[s] = 0.
    # Relaxa u->v em ordem topológica maximizando dist[v].

    # Retorna (caminho, peso_total) ou (None, None) se nao ha caminho s->t.
    order = topo_sort_from_adj_matrix(n, adj)

    # dist[v] = melhor peso acumulado de s ate v
    NEG_INF = -10**18  # suficiente para int; evita usar -math.inf para somas com inteiros
    dist = [NEG_INF] * n
    parent = [-1] * n
    dist[s] = 0

    # percorre vertices conforme topológica
    for u in order:
        if dist[u] == NEG_INF:
            # u nao e alcancavel a partir de s; pode pular relaxacoes
            continue
        for v in range(n):
            w = adj[u][v]
            if w != 0:  # existe aresta u->v
                cand = dist[u] + w
                if cand > dist[v]:
                    dist[v] = cand
                    parent[v] = u

    if dist[t] == NEG_INF:
        return None, None

    # reconstoi caminho de t voltando por 'parent'
    path = []
    cur = t
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path, dist[t]


def main():
    path = "entrada.txt"
    if len(sys.argv) >= 2:
        path = sys.argv[1]

    try:
        n, matriz, origem, destino = parse_input_file(path)
    except Exception as e:
        print(f"Erro ao ler '{path}': {e}")
        sys.exit(1)

    try:
        caminho, peso = longest_path_dag(n, matriz, origem, destino)
    except Exception as e:
        print(f"Erro ao processar o grafo: {e}")
        sys.exit(1)

    if caminho is None:
        print(f"Nao existe caminho de {origem} ate {destino}.")
    else:
        print(f"Caminho maximo: {caminho}")
        print(f"Peso total: {peso}")


if __name__ == "__main__":
    main()
