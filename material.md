# Graph Coloring: Presentation Material

> Assignment requirements:
> 1. **REQUIRED:** Slides on the implementation / application of the topic
> 2. **BONUS:** Implementation demo
>
> Suggested length: **14 slides + live demo (about 15–20 minutes)**.
> Each slide below has: **Title → On-slide content → Speaker notes → Visual suggestion**.

---

## Slide 1: Title

**On slide**
- **Graph Coloring: Concepts, Algorithms, and Real-World Implementation**
- Presenter name(s) / Student ID
- Course name / Lecturer / Date

**Speaker notes**
Greet the audience and introduce the topic: "How can we assign 'colors' to things so that conflicting things never share the same color?"

**Visual:** A colorful graph (e.g., Petersen graph or a map) as the background.

---

## Slide 2: Agenda

**On slide**
1. What is Graph Coloring?
2. Key concepts and theorems
3. Algorithms
4. Step-by-step example
5. Applications / implementations (**main focus**)
6. Code implementation and demo
7. Conclusion

**Speaker notes**
Tell the audience that most of the time will be spent on real implementations, followed by a live demo.

---

## Slide 3: Motivation, a Real Problem

**On slide**
> *A university has 6 exams. Some students take multiple exams. Two exams with a shared student cannot be at the same time. What is the **minimum number of time slots** needed?*

- Exams = vertices
- Shared student = edge
- Time slot = color

**Speaker notes**
This is the classic motivating example. It shows that a scheduling problem is secretly a graph problem.

**Visual:** Left: a table of exams. Right: the same data drawn as a graph.

---

## Slide 4: What is Graph Coloring?

**On slide**
- **Graph G = (V, E)**: vertices V, edges E
- **Graph coloring**: assigning a color to each vertex so that **no two adjacent vertices share the same color**
- A coloring using *k* colors is called a **k-coloring**
- **Goal:** use as few colors as possible

**Speaker notes**
Emphasize the single rule: neighbors must differ. Mention that "colors" can be anything: integers, time slots, frequencies, registers.

**Visual:** A small graph with a valid coloring next to an invalid one (two adjacent vertices with the same color highlighted in red).

---

## Slide 5: Key Terminology

| Term | Meaning |
|---|---|
| **Proper coloring** | No adjacent vertices share a color |
| **Chromatic number χ(G)** | Minimum number of colors needed for G |
| **Clique** | Set of vertices that are all mutually adjacent |
| **Degree Δ(G)** | Maximum number of neighbors of any vertex |
| **Independent set** | Vertices with no edges between them (each color class is one) |

**Speaker notes**
Each color class forms an independent set, so graph coloring = partitioning the vertices into the fewest independent sets.

---

## Slide 6: Important Properties & Theorems

**On slide**
- **Lower bound:** χ(G) ≥ ω(G) (size of the largest clique)
- **Upper bound:** χ(G) ≤ Δ(G) + 1 (greedy guarantee)
- **Brooks' theorem:** χ(G) ≤ Δ(G) unless G is a complete graph or an odd cycle
- **Special graphs:**
  - Complete graph Kₙ → χ = n
  - Bipartite graph → χ ≤ 2
  - Even cycle → 2, odd cycle → 3
  - Tree → 2
- **Four Color Theorem:** every planar graph (e.g., a map) is 4-colorable (proved 1976, Appel & Haken)

**Speaker notes**
Don't prove anything; just state these as tools for estimating how many colors are needed.

**Visual:** Small diagrams of K₄, a cycle C₅, and a tree.

---

## Slide 7: Computational Complexity

**On slide**
- Deciding whether a graph is **2-colorable**: easy, O(V + E) (BFS/DFS)
- Deciding whether a graph is **k-colorable for k ≥ 3**: **NP-complete**
- Finding the exact χ(G) is **NP-hard**
- So in practice we use **heuristics** (fast, good but not always optimal) or **exact algorithms** (for small graphs)

**Speaker notes**
This explains why we study several algorithms instead of one perfect one.

---

## Slide 8: Algorithms Overview

| Algorithm | Type | Idea | Complexity |
|---|---|---|---|
| **Greedy** | Heuristic | Color vertices in a given order, pick the smallest free color | O(V + E) |
| **Welsh–Powell** | Heuristic | Greedy, but vertices sorted by **degree (descending)** | O(V²) |
| **DSATUR** | Heuristic | Always color the vertex with the **most distinct neighbor colors** (highest saturation) | O(V²) |
| **Backtracking** | Exact | Try colors, undo when a conflict occurs | Exponential |

**Speaker notes**
Greedy is simplest but depends on vertex order. Welsh–Powell and DSATUR improve the order. Backtracking guarantees a correct answer for a given k but is slow.

---

## Slide 9: Welsh–Powell Algorithm

**On slide (pseudocode)**
```
1. Sort vertices by degree, highest first
2. color = 1
3. While uncolored vertices remain:
     a. Give `color` to the first uncolored vertex
     b. Walk down the list: give `color` to every uncolored
        vertex NOT adjacent to any vertex already given `color`
     c. color = color + 1
```

**Speaker notes**
Explain intuition: high-degree vertices are the most constrained, so color them first.

---

## Slide 10: Worked Example (Welsh–Powell)

**Graph:** vertices A–F, edges:
`A-B, A-C, A-D, B-C, B-E, C-F, D-E, E-F`

| Vertex | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Degree | 3 | 3 | 3 | 2 | 3 | 2 |

Sorted order: **A, B, C, E, D, F**

| Step | Action | Result |
|---|---|---|
| Color 1 | A ✓; B ✗ (adj A); C ✗; E ✓; D ✗ (adj A); F ✗ (adj E) | {A, E} |
| Color 2 | B ✓; C ✗ (adj B); D ✓; F ✓ | {B, D, F} |
| Color 3 | C ✓ | {C} |

**Final: 3 colors → χ(G) = 3** (A-B-C is a triangle, so 3 is also the lower bound, therefore optimal).

**Speaker notes**
Walk through the table slowly. Point out the triangle A-B-C proves we can't do better than 3.

**Visual:** Draw the graph; animate the coloring step by step (Red → Blue → Green).

---

## Slide 11: Application 1, Scheduling (Exam / Class Timetabling)

**On slide**
- Vertex = exam/course; Edge = shared students or shared lecturer/room
- Color = time slot
- Minimum colors = **minimum number of time slots**
- Used by universities worldwide for timetabling

**Speaker notes**
Link back to the motivating example in Slide 3. The same model works for meeting schedules, shift planning, and sports fixtures.

---

## Slide 12: Application 2, Other Real-World Uses

**On slide**

| Domain | Vertices | Edge means | Color = |
|---|---|---|---|
| **Map coloring** | Countries/provinces | Share a border | Map color |
| **Register allocation (compilers)** | Variables | Alive at the same time | CPU register |
| **Frequency / channel assignment** | Radio towers / Wi-Fi routers | Within interference range | Frequency channel |
| **Sudoku** | 81 cells | Same row/column/box | Digit 1–9 |
| **Traffic lights** | Road movements | Would collide | Signal phase |
| **Chemical storage** | Chemicals | Dangerous if stored together | Storage room |

**Speaker notes**
Pick 2–3 to explain in more detail depending on audience interest. Compilers and Wi-Fi channels are great for informatics students.

**Visual:** An icon for each domain.

---

## Slide 13: Implementation (Python)

**On slide:** a short code excerpt (full code in the Demo section below)

```python
def welsh_powell(graph):
    order = sorted(graph, key=lambda v: len(graph[v]), reverse=True)
    colors, c = {}, 0
    while len(colors) < len(graph):
        c += 1
        for v in order:
            if v not in colors and all(colors.get(u) != c for u in graph[v]):
                colors[v] = c
    return colors
```

**Speaker notes**
Explain that the graph is stored as an adjacency list (dictionary of sets) and the code mirrors the pseudocode on Slide 9.

---

## Slide 14: Demo

**On slide**
- **Live demo:** Exam scheduling with Graph Coloring
- Input: list of exams + conflicts
- Output: time slot per exam + graph visualization

**Speaker notes**
Switch to the terminal / notebook. See "Demo Script" below.

---

## Slide 15: Conclusion

**On slide**
- Graph coloring turns **conflict problems** into a clean graph model
- Finding the optimal coloring is **NP-hard**, but heuristics (Welsh–Powell, DSATUR) work well in practice
- Real applications: **scheduling, compilers, wireless networks, maps, Sudoku**
- Key takeaway: *"If things conflict, think graph coloring."*

---

## Slide 16: References

- West, D. B. (2001). *Introduction to Graph Theory* (2nd ed.). Prentice Hall.
- Rosen, K. H. *Discrete Mathematics and Its Applications*. McGraw-Hill.
- Welsh, D. J. A., & Powell, M. B. (1967). An upper bound for the chromatic number of a graph and its application to timetabling problems. *The Computer Journal*, 10(1).
- Brélaz, D. (1979). New methods to color the vertices of a graph. *Communications of the ACM*, 22(4).
- Appel, K., & Haken, W. (1977). Every planar map is four colorable. *Illinois Journal of Mathematics*.
- Chaitin, G. J. et al. (1981). Register allocation via coloring. *Computer Languages*, 6(1).

*(Verify the citation details against your own library/course format before submitting.)*

---

# Appendix A: Full Demo Code

Save as `graph_coloring_demo.py`. Requires Python 3.8+. The visualization part needs `pip install networkx matplotlib` (optional; the text output works without it).

```python
"""Graph Coloring demo: exam scheduling."""

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
    for name, algo in [("Greedy", greedy), ("Welsh-Powell", welsh_powell), ("DSATUR", dsatur)]:
        result = algo(graph)
        print(f"{name:13} -> {max(result.values())} colors, valid={is_valid(graph, result)}")

    k = chromatic_number(graph)
    print(f"\nExact chromatic number (backtracking): {k}")

    best = backtracking(graph, k)
    print("\nExam schedule (color = time slot):")
    for slot in range(1, k + 1):
        print(f"  Slot {slot}: {', '.join(v for v, c in best.items() if c == slot)}")

    # ---------- Optional visualization ----------
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
        plt.show()
    except ImportError:
        print("\n(Install networkx and matplotlib to see the graph drawing.)")
```

---

# Appendix B: Demo Script (what to say / do)

1. **Show the data** (30 s): "Six exams, edges mean a student takes both."
2. **Run the script** (1 min): point out that Greedy, Welsh–Powell, and DSATUR each report a number of colors, all validated.
3. **Show the exact answer** (30 s): backtracking gives the true minimum.
4. **Show the schedule** (30 s): "Exams in the same slot never share a student."
5. **Show the picture** (30 s): open `coloring.png`.
6. **Interactive moment** (optional): add a new conflict edge, re-run, and see if the number of slots changes.

**Backup plan:** take a screenshot or record a short screen capture of the output beforehand in case the live demo fails.

---

# Appendix C: Possible Q&A

| Question | Short answer |
|---|---|
| Why not always use backtracking? | Exponential time; infeasible for large graphs. |
| Is greedy ever optimal? | Sometimes, but the result depends on vertex order; a bad order can use many more colors than needed. |
| What is the difference between Welsh–Powell and DSATUR? | Welsh–Powell fixes the order once by degree; DSATUR chooses dynamically based on how many different colors neighbors already use. |
| Is χ(G) always equal to the biggest clique? | No. It's only a lower bound (e.g., the 5-cycle has clique size 2 but needs 3 colors). |
| Why does the Four Color Theorem matter? | It guarantees any map needs at most 4 colors; it was the first major theorem proven with computer assistance. |

---

# Appendix D: Design Suggestions for the Slides

- **Palette:** use 4–5 strong, distinct colors (red, blue, green, yellow, purple), since the topic is literally about color.
- **Fonts:** one sans-serif font; code in a monospace font.
- **Per slide:** at most 5 bullets, one visual.
- **Animations:** animate only the coloring steps (Slides 4 and 10).
- **Tools for diagrams:** draw.io, PowerPoint shapes, or generate pictures with the networkx code above.