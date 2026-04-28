from __future__ import annotations
from collections import deque
from typing import List, Optional, Tuple
 
from graph import Graph
 
 
# ======================================================================
# 1. Validação
# ======================================================================
 
def is_tree(g: Graph) -> Tuple[bool, str]:
    
    if g.v == 0:
        return False, "O grafo não possui vértices."
 
    # Condição necessária: |E| == |V| - 1
    if g.e != g.v - 1:
        return False, (
            f"Número de arestas ({g.e}) ≠ número de vértices - 1 ({g.v - 1}). "
            "Um grafo com ciclo ou desconexo não é uma árvore."
        )
 
    # Verificação de conectividade via BFS
    visited = [False] * g.v
    queue = deque([0])
    visited[0] = True
    count = 1
 
    while queue:
        u = queue.popleft()
        for w in g.adj(u):
            if not visited[w]:
                visited[w] = True
                count += 1
                queue.append(w)
 
    if count != g.v:
        return False, (
            f"O grafo não é conexo: apenas {count} de {g.v} vértices são alcançáveis "
            "a partir do vértice 0."
        )
 
    return True, ""
 
 
# ======================================================================
# 2. Centros
# ======================================================================
 
def find_centers(g: Graph) -> List[int]:
    
    if g.v == 1:
        return [0]
 
    degree = [g.degree(v) for v in range(g.v)]
 
    # Folhas iniciais: grau 0 ou 1
    leaves: List[int] = [v for v in range(g.v) if degree[v] <= 1]
    processed = len(leaves)
 
    while processed < g.v:
        new_leaves: List[int] = []
        for u in leaves:
            for w in g.adj(u):
                degree[w] -= 1
                if degree[w] == 1:
                    new_leaves.append(w)
        processed += len(new_leaves)
        leaves = new_leaves
 
    return leaves
 
 
# ======================================================================
# 3. Codificação canônica
# ======================================================================
 
def canonical_code(g: Graph, root: int) -> str:
    
    parent = [-1] * g.v
    order: List[int] = []
    visited = [False] * g.v
 
    queue = deque([root])
    visited[root] = True
 
    while queue:
        u = queue.popleft()
        order.append(u)
        for w in g.adj(u):
            if not visited[w]:
                visited[w] = True
                parent[w] = u
                queue.append(w)
 
    # Calcula os códigos de baixo para cima
    code: List[Optional[str]] = [None] * g.v
 
    for u in reversed(order):
        child_codes = []
        for w in g.adj(u):
            if parent[w] == u:          # w é filho de u
                child_codes.append(code[w])
        child_codes.sort()              # ordenação lexicográfica obrigatória
        code[u] = "(" + "".join(child_codes) + ")"
 
    return code[root]
 
 
def tree_canonical(g: Graph) -> Tuple[str, List[int]]:
   
    centers = find_centers(g)
 
    if len(centers) == 1:
        return canonical_code(g, centers[0]), centers
 
    # Dois centros: escolhe a representação menor lexicograficamente
    c1, c2 = centers[0], centers[1]
    code1 = canonical_code(g, c1)
    code2 = canonical_code(g, c2)
 
    # A codificação canônica final é a menor das duas
    final_code = min(code1, code2)
    return final_code, centers
 
 
# ======================================================================
# 4. Interface principal
# ======================================================================
 
def check_isomorphism(g1: Graph, g2: Graph) -> dict:
    
    result: dict = {}
 
    ok1, reason1 = is_tree(g1)
    ok2, reason2 = is_tree(g2)
 
    result["valid1"] = ok1
    result["valid2"] = ok2
    result["reason1"] = reason1
    result["reason2"] = reason2
 
    if not ok1 or not ok2:
        result["centers1"] = None
        result["centers2"] = None
        result["code1"] = None
        result["code2"] = None
        result["isomorphic"] = None
        return result
 
    code1, centers1 = tree_canonical(g1)
    code2, centers2 = tree_canonical(g2)
 
    result["centers1"] = centers1
    result["centers2"] = centers2
    result["code1"] = code1
    result["code2"] = code2
    result["isomorphic"] = code1 == code2
 
    return result