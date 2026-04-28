
import sys
from graph import Graph
from tree_isomorphism import check_isomorphism
 
# ──────────────────────────────────────────────────────────────────────
# Helpers de formatação
# ──────────────────────────────────────────────────────────────────────
 
SEP = "─" * 60
 
 
def print_sep(title: str = "") -> None:
    if title:
        pad = (58 - len(title)) // 2
        print(f"{'─' * pad} {title} {'─' * (58 - pad - len(title))}")
    else:
        print(SEP)
 
 
def print_adjacency(g: Graph, label: str) -> None:
    print_sep(f"Lista de adjacência — {label}")
    for v in range(g.v):
        neighbors = " → ".join(str(w) for w in g.adj(v))
        print(f"  {v:>4}: {neighbors if neighbors else '(sem vizinhos)'}")
    print(f"\n  Vértices : {g.v}")
    print(f"  Arestas  : {g.e}")
 
 
# ──────────────────────────────────────────────────────────────────────
# Programa principal
# ──────────────────────────────────────────────────────────────────────
 
def main() -> None:
    if len(sys.argv) != 3:
        print("Uso: python main.py arquivo1.txt arquivo2.txt")
        sys.exit(1)
 
    file1, file2 = sys.argv[1], sys.argv[2]
 
    # ── Leitura dos grafos ──────────────────────────────────────────
    print_sep()
    print("  ISOMORFISMO EM ÁRVORES — Codificação Canônica")
    print_sep()
 
    try:
        g1 = Graph.from_file(file1)
    except Exception as exc:
        print(f"\n[ERRO] Não foi possível ler '{file1}': {exc}")
        sys.exit(1)
 
    try:
        g2 = Graph.from_file(file2)
    except Exception as exc:
        print(f"\n[ERRO] Não foi possível ler '{file2}': {exc}")
        sys.exit(1)
 
    # ── Listas de adjacência ─────────────────────────────────────────
    print()
    print_adjacency(g1, f"Árvore 1  ({file1})")
    print()
    print_adjacency(g2, f"Árvore 2  ({file2})")
 
    # ── Análise de isomorfismo ────────────────────────────────────────
    print()
    print_sep("Validação e análise")
 
    result = check_isomorphism(g1, g2)
 
    # Validação — Árvore 1
    if result["valid1"]:
        print(f"\n  [Árvore 1]  É uma árvore válida.")
    else:
        print(f"\n  [Árvore 1]  NÃO é uma árvore válida.")
        print(f"             Motivo: {result['reason1']}")
 
    # Validação — Árvore 2
    if result["valid2"]:
        print(f"  [Árvore 2]  É uma árvore válida.")
    else:
        print(f"  [Árvore 2]  NÃO é uma árvore válida.")
        print(f"             Motivo: {result['reason2']}")
 
    # Se alguma entrada for inválida, encerra sem comparar
    if not result["valid1"] or not result["valid2"]:
        print()
        print_sep("Resultado")
        print("\n  Comparação não realizada: entrada(s) inválida(s).")
        print()
        print_sep()
        sys.exit(1)
 
    # Centros
    c1 = result["centers1"]
    c2 = result["centers2"]
    print(f"\n  [Árvore 1] Centro(s) encontrado(s): {c1}")
    print(f"  [Árvore 2] Centro(s) encontrado(s): {c2}")
 
    # Códigos canônicos
    print(f"\n  [Árvore 1] Codificação canônica:")
    print(f"             {result['code1']}")
    print(f"\n  [Árvore 2] Codificação canônica:")
    print(f"             {result['code2']}")
 
    # Veredito
    print()
    print_sep("Veredito final")
    if result["isomorphic"]:
        print("\n  ✔  As duas árvores SÃO ISOMORFAS.")
        print("     Ambas produziram a mesma codificação canônica.")
    else:
        print("\n  ✘  As duas árvores NÃO SÃO ISOMORFAS.")
        print("     As codificações canônicas são distintas.")
 
    print()
    print_sep()
 
 
if __name__ == "__main__":
    main()
	