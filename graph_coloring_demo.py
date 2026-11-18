"""
Graph Coloring Demo: Exam Scheduling
Berdasarkan materi final project (Appendix A material.md)
"""

# ---------- Data: exams and their conflicts (shared students) ----------
exams = {
    "Calculus":    ["Physics", "Algebra", "Statistics"],
    "Physics":     ["Calculus", "Algebra", "Chemistry"],
    "Algebra":     ["Calculus", "Physics", "Programming"],
    "Statistics":  ["Calculus", "Chemistry"],
    "Chemistry":   ["Physics", "Statistics", "Programming"],
    "Programming": ["Algebra", "Chemistry"],
}
graph = {v: set(ns) for v, ns in exams.items()}


# ---------- 1. Simple greedy ----------
def greedy(graph, order=None):
    colors = {}
    for v in (order or list(graph)):
        used = {colors[u] for u in graph[v] if u in colors}
        c = 1
        while c in used:
            c += 1
        colors[v] = c
    return colors


# ---------- 2. Welsh-Powell ----------
def welsh_powell(graph):
    order = sorted(graph, key=lambda v: len(graph[v]), reverse=True)
    colors, c = {}, 0
    while len(colors) < len(graph):
        c += 1
        for v in order:
            if v not in colors and all(colors.get(u) != c for u in graph[v]):
                colors[v] = c
    return colors


# ---------- 3. DSATUR ----------
def dsatur(graph):
    colors = {}
    while len(colors) < len(graph):
        def key(v):
            sat = len({colors[u] for u in graph[v] if u in colors})
            return (sat, len(graph[v]))
        v = max((x for x in graph if x not in colors), key=key)
        used = {colors[u] for u in graph[v] if u in colors}
        c = 1
        while c in used:
            c += 1
        colors[v] = c
    return colors


# ---------- 4. Backtracking (exact, for a given k) ----------
def backtracking(graph, k):
    vertices = list(graph)
    colors = {}

    def solve(i):
        if i == len(vertices):
            return True
        v = vertices[i]
        for c in range(1, k + 1):
            if all(colors.get(u) != c for u in graph[v]):
                colors[v] = c
                if solve(i + 1):
                    return True
                del colors[v]
        return False

    return colors if solve(0) else None


def chromatic_number(graph):
    k = 1
    while backtracking(graph, k) is None:
        k += 1
    return k


# ---------- Validation ----------
def is_valid(graph, colors):
    return all(colors[u] != colors[v] for u in graph for v in graph[u])


# ---------- Run ----------
if __name__ == "__main__":
    print("=" * 60)
    print("  GRAPH COLORING BENCHMARK: EXAM SCHEDULING")
    print("=" * 60)
    for name, algo in [("Greedy", greedy), ("Welsh-Powell", welsh_powell), ("DSATUR", dsatur)]:
        result = algo(graph)
        print(f"{name:15} -> {max(result.values())} colors, valid={is_valid(graph, result)}")

    k = chromatic_number(graph)
    print(f"\nExact Chromatic Number χ(G) via Backtracking: {k}")

    best = backtracking(graph, k)
    print("\nOptimal Exam Schedule (Color = Time Slot):")
    print("-" * 45)
    for slot in range(1, k + 1):
        slot_exams = [v for v, c in best.items() if c == slot]
        print(f"  Slot {slot}: {', '.join(slot_exams)}")
    print("-" * 45)

    # Optional visualization
    try:
        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.Graph([(u, v) for u in graph for v in graph[u]])
        palette = ["#e74c3c", "#3498db", "#2ecc71", "#f1c40f", "#9b59b6", "#e67e22"]
        node_colors = [palette[best[n] - 1] for n in G.nodes]
        nx.draw(G, with_labels=True, node_color=node_colors, node_size=1800,
                font_size=9, font_weight="bold", edge_color="gray")
        plt.title("Exam conflict graph, colored by time slot")
        plt.savefig("coloring.png", dpi=150, bbox_inches="tight")
        print("Grafik tersimpan di 'coloring.png'")
    except ImportError:
        print("(Catatan: Install networkx dan matplotlib jika ingin menyimpan gambar grafik)")
