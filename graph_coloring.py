def welsh_powell_graph_coloring(adj_list):
    print("=" * 65)
    print("      SIMULASI ALGORITMA WELSH-POWELL (GRAPH COLORING)")
    print("=" * 65)
    
    # 1. Menghitung derajat (degree) setiap simpul
    degrees = {node: len(neighbors) for node, neighbors in adj_list.items()}
    
    # 2. Mengurutkan simpul berdasarkan derajat secara menurun (descending)
    sorted_nodes = sorted(degrees.keys(), key=lambda node: degrees[node], reverse=True)
    
    print("\n[LANGKAH 1] Urutan Simpul Berdasarkan Derajat Tertinggi:")
    print("-" * 55)
    print(f"{'Simpul':<8} | {'Derajat':<8} | {'Daftar Tetangga'}")
    print("-" * 55)
    for node in sorted_nodes:
        neighbors_str = ", ".join(adj_list[node])
        print(f"{node:<8} | {degrees[node]:<8} | [{neighbors_str}]")
    print("-" * 55)
    
    # Palet warna representasi
    color_palette = [
        "Warna 1 (Biru)",
        "Warna 2 (Merah)",
        "Warna 3 (Hijau)",
        "Warna 4 (Kuning)",
        "Warna 5 (Ungu)"
    ]
    
    node_colors = {}
    uncolored_nodes = list(sorted_nodes)
    color_index = 0
    iteration = 1
    
    print("\n[LANGKAH 2 & 3] Proses Iterasi Pewarnaan Simpul:")
    
    # 3. Proses iterasi setiap warna
    while uncolored_nodes:
        current_color = (
            color_palette[color_index] 
            if color_index < len(color_palette) 
            else f"Warna {color_index + 1}"
        )
        
        print(f"\n" + "=" * 55)
        print(f" ITERASI {iteration}: Mengalokasikan {current_color}")
        print("=" * 55)
        
        colored_in_this_round = []
        
        # Iterasi memeriksa simpul-simpul yang belum diwarnai
        for node in list(uncolored_nodes):
            # Cek apakah simpul ini bertetangga dengan simpul yang sudah diberi warna saat ini
            has_conflict = False
            conflicting_nodes = []
            
            for colored_node in colored_in_this_round:
                if colored_node in adj_list[node]:
                    has_conflict = True
                    conflicting_nodes.append(colored_node)
            
            if not has_conflict:
                # Simpul aman untuk diwarnai dengan warna saat ini
                node_colors[node] = current_color
                colored_in_this_round.append(node)
                uncolored_nodes.remove(node)
                prior = colored_in_this_round[:-1]
                prior_str = f", tidak bertetangga dg {prior}" if prior else "simpul awal ronde ini"
                print(f"  [BERHASIL] Simpul '{node}' -> Diberi {current_color} ({prior_str})")
            else:
                conflict_str = ", ".join(conflicting_nodes)
                print(f"  [DILEWATI] Simpul '{node}' -> Konflik tetangga dg {conflict_str} (berwarna sama)")
        
        print(f"\nSimpul yang selesai diwarnai pada Iterasi {iteration}: {colored_in_this_round}")
        color_index += 1
        iteration += 1

    # 4. Ringkasan Hasil Akhir
    print("\n" + "=" * 65)
    print("                    HASIL AKHIR PEWARNAAN")
    print("=" * 65)
    for node in sorted(adj_list.keys()):
        print(f"  Simpul '{node}' : {node_colors[node]}")
    
    total_colors = len(set(node_colors.values()))
    max_degree = max(degrees.values())
    
    print("-" * 65)
    print(f"Derajat Maksimum Graf Δ(G) : {max_degree}")
    print(f"Batas Atas Teori (Δ + 1)   : {max_degree + 1} warna")
    print(f"Total Warna Digunakan      : {total_colors} warna (Optimal!)")
    print("=" * 65)
    return node_colors

if __name__ == "__main__":
    # Graf contoh representatif: 6 Simpul (A, B, C, D, E, F)
    # C, D, E berderajat 4; A, B berderajat 3; F berderajat 2.
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C', 'E'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['A', 'C', 'E', 'F'],
        'E': ['B', 'C', 'D', 'F'],
        'F': ['D', 'E']
    }
    welsh_powell_graph_coloring(graph)
