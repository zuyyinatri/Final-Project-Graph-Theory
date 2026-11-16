---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

  :root {
    --bg-light: #f7f7f5;
    --primary: #4c5b9e;
    --primary-light: #6473b7;
    --primary-dark: #374479;
    --card-bg: #f0efe9;
    --card-border: #e3e2dc;
    --text-dark: #1e2029;
    --text-muted: #5d6175;
    --white: #ffffff;
    --code-bg: #212534;
    --code-text: #e2e8f0;
  }

  section {
    background-color: var(--bg-light);
    color: var(--text-dark);
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    padding: 48px 64px;
    font-size: 20px;
    line-height: 1.5;
    letter-spacing: -0.01em;
  }

  /* Slash Prefix for Headings */
  h1, h2, h3 {
    color: var(--primary);
    font-weight: 700;
    margin: 0 0 20px 0;
    letter-spacing: -0.02em;
  }

  h1 { font-size: 46px; line-height: 1.15; }
  h2 { font-size: 38px; line-height: 1.2; }
  h3 { font-size: 24px; line-height: 1.25; }

  .slash {
    color: var(--primary);
    font-weight: 800;
    margin-right: 4px;
  }

  .header-tag {
    position: absolute;
    top: 40px;
    right: 64px;
    font-size: 16px;
    font-weight: 700;
    color: var(--primary);
    letter-spacing: 0.02em;
  }

  .footer-prepared {
    position: absolute;
    bottom: 40px;
    right: 64px;
    font-size: 15px;
    color: var(--text-dark);
    text-align: right;
  }
  .footer-prepared span.label {
    color: var(--primary);
    font-weight: 700;
    margin-right: 12px;
  }
  .footer-prepared span.names {
    font-weight: 500;
  }

  /* Slide Variations */
  section.dark {
    background-color: var(--primary);
    color: var(--white);
  }
  section.dark h1, section.dark h2, section.dark h3, section.dark .slash {
    color: var(--white);
  }
  section.dark .header-tag, section.dark .footer-prepared, section.dark .footer-prepared span.label {
    color: #d8def8;
  }

  /* Two Column Layouts */
  .columns-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    height: 80%;
    align-items: stretch;
  }

  .columns-split {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 36px;
    height: 82%;
    align-items: stretch;
  }

  /* Cards */
  .card {
    background-color: var(--card-bg);
    border-radius: 12px;
    padding: 24px 28px;
    box-sizing: border-box;
  }

  .card h3 {
    margin-top: 0;
    margin-bottom: 12px;
    color: var(--primary);
  }

  /* 4 Columns (Slide 6 style) */
  .grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    margin-top: 24px;
  }
  .card-col {
    background-color: var(--card-bg);
    padding: 24px 18px;
    border-radius: 10px;
    min-height: 380px;
    display: flex;
    flex-direction: column;
  }
  .card-col .step-num {
    font-size: 22px;
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 24px;
  }
  .card-col .step-title {
    font-size: 20px;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 12px;
  }
  .card-col p {
    font-size: 15px;
    color: var(--text-dark);
    line-height: 1.45;
    margin: 0;
  }

  /* 2x2 Grid (Slide 9 style) */
  .grid-2x2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 20px;
    margin-top: 24px;
    height: 75%;
  }
  .grid-2x2 .card {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    padding: 20px;
  }
  .grid-2x2 .card h3 {
    font-size: 22px;
    margin-bottom: 8px;
  }
  .grid-2x2 .card p {
    font-size: 16px;
    margin: 0;
    color: var(--text-dark);
  }

  /* Circle Badges Row (Slide 5 style) */
  .circles-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 30px;
    margin-top: 60px;
  }
  .circle-item {
    width: 220px;
    height: 220px;
    border-radius: 50%;
    background-color: var(--primary);
    color: var(--white);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
    font-weight: 700;
    font-size: 19px;
    line-height: 1.3;
    padding: 24px;
    box-sizing: border-box;
    box-shadow: 0 10px 24px rgba(76, 91, 158, 0.2);
  }
  .circle-divider {
    font-size: 38px;
    font-weight: 800;
    color: var(--primary);
  }

  /* Pill Tags (Slide 7 style) */
  .pill-group {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .pill-tag {
    background-color: var(--primary);
    color: var(--white);
    border-radius: 999px;
    padding: 12px 20px;
    text-align: center;
    font-weight: 600;
    font-size: 15px;
    letter-spacing: 0.01em;
  }

  /* Code Blocks */
  pre {
    background-color: var(--code-bg) !important;
    color: var(--code-text) !important;
    border-radius: 10px;
    padding: 16px 20px;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 13.5px;
    line-height: 1.45;
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
  }
  code {
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 0.9em;
  }

  /* Iteration Cards */
  .iter-box {
    background: #ffffff;
    border-left: 5px solid var(--primary);
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 14px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  }
  .iter-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 700;
    font-size: 17px;
    color: var(--primary);
    margin-bottom: 6px;
  }
  .iter-badge {
    background: var(--primary);
    color: white;
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 12px;
  }
  .iter-desc {
    font-size: 14px;
    color: var(--text-dark);
    line-height: 1.4;
  }
  /* Layout helpers (moved from inline styles so exports without --html still work) */
  .s1 { margin-top: 140px !important; }
  .s2 { font-size: 64px !important; line-height: 1.1 !important; margin-bottom: 12px !important; }
  .s3 { font-size: 22px !important; color: var(--text-muted) !important; font-weight: 500 !important; margin-top: 8px !important; }
  .s4 { margin-top: 20px !important; align-items: center !important; }
  .s5 { font-size: 52px !important; }
  .s6 { color: var(--text-muted) !important; font-size: 18px !important; max-width: 380px !important; }
  .s7 { display: flex !important; flex-direction: column !important; gap: 14px !important; padding-left: 40px !important; }
  .s8 { display: flex !important; gap: 20px !important; align-items: baseline !important; }
  .s9 { font-size: 24px !important; font-weight: 800 !important; color: var(--primary) !important; }
  .s10 { font-size: 21px !important; font-weight: 600 !important; }
  .s11 { margin-top: 15px !important; }
  .s12 { font-size: 18px !important; line-height: 1.6 !important; color: #eceffc !important; margin-top: 24px !important; max-width: 440px !important; }
  .s13 { padding-left: 20px !important; }
  .s14 { font-size: 22px !important; color: #ffffff !important; margin-bottom: 24px !important; }
  .s15 { display: flex !important; flex-direction: column !important; gap: 16px !important; }
  .s16 { font-size: 18px !important; font-weight: 700 !important; color: #ffffff !important; }
  .s17 { font-size: 14px !important; color: #d0d7fb !important; }
  .s18 { margin-top: 10px !important; }
  .s19 { font-size: 17px !important; line-height: 1.6 !important; color: var(--text-dark) !important; margin-top: 24px !important; padding-right: 20px !important; }
  .s20 { font-size: 16px !important; line-height: 1.6 !important; color: var(--text-muted) !important; margin-top: 14px !important; padding-right: 20px !important; }
  .s21 { display: flex !important; flex-direction: column !important; justify-content: center !important; gap: 16px !important; }
  .s22 { font-size: 20px !important; }
  .s23 { font-weight: 700 !important; font-size: 14px !important; color: var(--primary) !important; }
  .s24 { font-size: 15px !important; color: var(--text-dark) !important; }
  .s25 { color: var(--text-muted) !important; font-size: 17px !important; margin-top: -10px !important; }
  .s26 { font-size: 13px !important; font-weight: 400 !important; opacity: 0.9 !important; margin-top: 6px !important; display: block !important; }
  .s27 { display: grid !important; grid-template-columns: 1fr 1fr 1fr !important; gap: 30px !important; margin-top: 35px !important; }
  .s28 { text-align: center !important; font-size: 20px !important; }
  .s29 { margin-top: 20px !important; }
  .s30 { display: flex !important; flex-direction: column !important; justify-content: center !important; gap: 14px !important; }
  .s31 { font-size: 19px !important; }
  .s32 { font-size: 14px !important; margin: 0 !important; line-height: 1.5 !important; }
  .s33 { color: var(--text-muted) !important; font-size: 16px !important; margin-top: -10px !important; }
  .s34 { margin-top: 150px !important; }
  .s35 { font-size: 72px !important; line-height: 1.1 !important; margin-bottom: 12px !important; }
  .s36 { margin-bottom: 6px !important; }
  .s37 { font-size: 14px !important; color: var(--text-muted) !important; }
---

<!-- _paginate: false -->
<div class="header-tag">Teknik Informatika 2026</div>
<div class="s1">
  <h1 class="s2">
    <span class="slash">/</span> Final Project<br>Graph Theory
  </h1>
  <p class="s3">
    Optimasi Graph Coloring Menggunakan Algoritma Welsh-Powell
  </p>
</div>
<div class="footer-prepared">
  <span class="label">prepared by</span>
  <span class="names">Galuh &nbsp;|&nbsp; Zuyyin &nbsp;|&nbsp; Lina &nbsp;|&nbsp; Mai</span>
</div>

---

<div class="header-tag">Teknik Informatika 2026</div>
<div class="columns-2 s4">
  <div>
    <h2 class="s5"><span class="slash">/</span> Contents</h2>
    <p class="s6">
      Struktur pembahasan final project implementasi teori graf dan pewarnaan simpul (vertex coloring).
    </p>
  </div>
  <div class="s7">
    <div class="s8">
      <span class="s9">01</span>
      <span class="s10">About Us &amp; Team Roles</span>
    </div>
    <div class="s8">
      <span class="s9">02</span>
      <span class="s10">Problem Overview &amp; Complexity</span>
    </div>
    <div class="s8">
      <span class="s9">03</span>
      <span class="s10">Proposed Strategy (Welsh-Powell)</span>
    </div>
    <div class="s8">
      <span class="s9">04</span>
      <span class="s10">Python Implementation</span>
    </div>
    <div class="s8">
      <span class="s9">05</span>
      <span class="s10">Step-by-Step Iteration Process</span>
    </div>
    <div class="s8">
      <span class="s9">06</span>
      <span class="s10">Analysis &amp; Deliverables</span>
    </div>
  </div>
</div>

---

<!-- _class: dark -->
<div class="header-tag">Teknik Informatika 2026</div>
<div class="columns-split s11">
  <div>
    <h2><span class="slash">/</span> About Us</h2>
    <p class="s12">
      Kami adalah tim mahasiswa Teknik Informatika yang fokus mengeksplorasi optimasi graf diskret. Pada proyek ini, kami merancang dan membuktikan implementasi heuristik pewarnaan graf paling efisien untuk memecahkan konflik sumber daya komputasi.
    </p>
  </div>
  <div class="s13">
    <h3 class="s14"><span class="slash">/</span> Team Members</h3>
    <div class="s15">
      <div>
        <div class="s16">01 &nbsp; Galuh</div>
        <div class="s17">Problem Formulation &amp; Theoretical Foundations</div>
      </div>
      <div>
        <div class="s16">02 &nbsp; Zuyyin</div>
        <div class="s17">Algorithm Strategy &amp; Welsh-Powell Design</div>
      </div>
      <div>
        <div class="s16">03 &nbsp; Lina</div>
        <div class="s17">Python Core Engine &amp; Tracing Implementation</div>
      </div>
      <div>
        <div class="s16">04 &nbsp; Mai</div>
        <div class="s17">Complexity Analysis, Benchmarking &amp; Testing</div>
      </div>
    </div>
  </div>
</div>

---

<div class="header-tag">Teknik Informatika 2026</div>
<div class="columns-split s18">
  <div>
    <h2><span class="slash">/</span> Project<br>Overview</h2>
    <p class="s19">
      <strong>Vertex Coloring</strong> adalah penugasan warna/label pada setiap simpul graf <i>G</i> = (<i>V</i>, <i>E</i>) dengan aturan ketat: <em>tidak boleh ada dua simpul bertetangga (terhubung oleh sisi yang sama) yang memiliki warna serupa</em>.
    </p>
    <p class="s20">
      Tujuan utama adalah meminimalkan total warna yang digunakan, yang dikenal sebagai <strong>Bilangan Kromatik</strong> χ(<i>G</i>).
    </p>
  </div>
  <div class="card s21">
    <h3 class="s22"><span class="slash">/</span> Formal Definition</h3>
    <div>
      <div class="s23">MATHEMATICAL MODEL</div>
      <div class="s24"><i>c</i> : <i>V</i> → {1, 2, …, <i>k</i>} &emsp; s.t. &emsp; (<i>u</i>, <i>v</i>) ∈ <i>E</i> ⇒ <i>c</i>(<i>u</i>) ≠ <i>c</i>(<i>v</i>)</div>
    </div>
    <div>
      <div class="s23">OPTIMAL OBJECTIVE</div>
      <div class="s24">Cari <i>k</i><sub>min</sub> = χ(<i>G</i>) (Chromatic Number)</div>
    </div>
    <div>
      <div class="s23">COMPLEXITY CLASS</div>
      <div class="s24"><strong>NP-Hard</strong> (Pencarian eksak eksponensial O(<i>k</i><sup><i>V</i></sup>))</div>
    </div>
  </div>
</div>

---

<div class="header-tag">Teknik Informatika 2026</div>
<h2><span class="slash">/</span> Real-World Applications</h2>
<p class="s25">
  Mengapa Graph Coloring sangat krusial dalam pemecahan masalah komputasi dan teknik industri?
</p>
<div class="circles-row">
  <div class="circle-item">
    <div>Timetable &amp; Exam<br>Scheduling</div>
    <span class="s26">Mencegah jadwal ujian mahasiswa yang bentrok</span>
  </div>
  <div class="circle-divider">/</div>
  <div class="circle-item">
    <div>Frequency<br>Assignment</div>
    <span class="s26">Mencegah interferensi sinyal antar pemancar BTS</span>
  </div>
  <div class="circle-divider">/</div>
  <div class="circle-item">
    <div>Compiler Register<br>Allocation</div>
    <span class="s26">Optimasi alokasi variabel register CPU terbatas</span>
  </div>
</div>

---

<div class="header-tag">Teknik Informatika 2026</div>
<h2><span class="slash">/</span> Proposed Strategy</h2>
<p class="s25">
  Mengapa memilih <strong>Algoritma Welsh-Powell</strong> sebagai solusi paling efisien?
</p>
<div class="grid-4">
  <div class="card-col">
    <div class="step-num">01</div>
    <div class="step-title">The NP-Hard Challenge</div>
    <p>Pencarian brute-force memerlukan O(<i>k</i><sup><i>V</i></sup>) kombinasi. Tidak layak secara komputasi untuk graf dengan puluhan hingga ratusan simpul.</p>
  </div>
  <div class="card-col">
    <div class="step-num">02</div>
    <div class="step-title">Greedy Heuristic</div>
    <p>Pendekatan Greedy membuat keputusan lokal optimal di tiap langkah tanpa backtracking, menghasilkan eksekusi yang luar biasa cepat.</p>
  </div>
  <div class="card-col">
    <div class="step-num">03</div>
    <div class="step-title">Welsh-Powell Power</div>
    <p>Mengurutkan simpul berdasarkan derajat (degree) menurun. Simpul tersulit (derajat tertinggi) diwarnai lebih awal untuk meminimalkan konflik.</p>
  </div>
  <div class="card-col">
    <div class="step-num">04</div>
    <div class="step-title">Guaranteed Bound</div>
    <p>Kompleksitas O(<i>V</i> log <i>V</i> + <i>V</i> + <i>E</i>). Memberikan jaminan batas atas χ(<i>G</i>) ≤ Δ(<i>G</i>) + 1, di mana Δ adalah derajat maksimum.</p>
  </div>
</div>

---

<div class="header-tag">Teknik Informatika 2026</div>
<h2><span class="slash">/</span> Scope of Work</h2>
<p class="s25">
  Tiga pilar alur kerja sistem pewarnaan graf Welsh-Powell
</p>
<div class="s27">
  <div>
    <h3 class="s28"><span class="slash">/</span> 01 Pre-Processing</h3>
    <div class="pill-group s29">
      <div class="pill-tag">Adjacency List Modeling</div>
      <div class="pill-tag">Degree Count: deg(v) = |N(v)|</div>
      <div class="pill-tag">Descending Sort by Degree</div>
    </div>
  </div>
  <div>
    <h3 class="s28"><span class="slash">/</span> 02 Coloring Core</h3>
    <div class="pill-group s29">
      <div class="pill-tag">Color Palette Initialization</div>
      <div class="pill-tag">Iterative Round Assignment</div>
      <div class="pill-tag">Adjacency Conflict Checker</div>
    </div>
  </div>
  <div>
    <h3 class="s28"><span class="slash">/</span> 03 Output &amp; Analysis</h3>
    <div class="pill-group s29">
      <div class="pill-tag">Iteration Process Tracing</div>
      <div class="pill-tag">Chromatic Upper Bound Verify</div>
      <div class="pill-tag">Conflict-Free Final Output</div>
    </div>
  </div>
</div>

---

<div class="header-tag">Teknik Informatika 2026</div>
<h2><span class="slash">/</span> Python Implementation</h2>
<div class="columns-split s18">
  <div>
    <pre><code class="language-python">def welsh_powell(graph):
    # 1. Hitung derajat &amp; urutkan descending
    degrees = {u: len(adj) for u, adj in graph.items()}
    nodes = sorted(graph, key=lambda u: degrees[u], reverse=True)
&nbsp;
    colors = {}
    color_id = 1
    uncolored = list(nodes)
&nbsp;
    # 2. Iterasi pewarnaan per ronde
    while uncolored:
        colored_this_round = []
        for u in list(uncolored):
            # Cek konflik tetangga dengan warna saat ini
            if not any(v in graph[u] for v in colored_this_round):
                colors[u] = f"Warna_{color_id}"
                colored_this_round.append(u)
                uncolored.remove(u)
        color_id += 1
&nbsp;
    return colors
</code></pre>
  </div>
  <div class="card s30">
    <h3 class="s31"><span class="slash">/</span> Key Algorithmic Steps</h3>
    <p class="s32">
      <strong>1. Adjacency List:</strong> Graf disimpan dalam <code>dict</code> Python untuk akses tetangga simpul dalam O(1) amortized.
    </p>
    <p class="s32">
      <strong>2. Sort Derajat (O(<i>V</i> log <i>V</i>)):</strong> Mengurutkan simpul secara menurun menjamin simpul dengan potensi bentrok terbesar diwarnai lebih dahulu.
    </p>
    <p class="s32">
      <strong>3. Independent Set Search:</strong> Pada setiap iterasi, simpul-simpul yang tidak saling berhubungan diberi warna yang sama secara maksimal.
    </p>
  </div>
</div>

---

<div class="header-tag">Teknik Informatika 2026</div>
<h2><span class="slash">/</span> Step-by-Step Iteration Process</h2>
<p class="s33">
  Graf Uji 6 Simpul: <strong>C(4), D(4), E(4), A(3), B(3), F(2)</strong> &mdash; Urutan Prioritas Derajat
</p>
<div class="s11">
  <div class="iter-box">
    <div class="iter-header">
      <span>Iterasi 1: Alokasi Warna 1 (Biru)</span>
      <span class="iter-badge">Selesai: { C, F }</span>
    </div>
    <div class="iter-desc">
      &bull; <strong>C</strong> (derajat 4) diwarnai pertama kali.<br>
      &bull; Simpul <strong>D, E, A, B</strong> dilewati karena bertetangga langsung dengan C.<br>
      &bull; Simpul <strong>F</strong> tidak bertetangga dengan C &rarr; Diberi <strong>Warna 1 (Biru)</strong>.
    </div>
  </div>
  <div class="iter-box">
    <div class="iter-header">
      <span>Iterasi 2: Alokasi Warna 2 (Merah)</span>
      <span class="iter-badge">Selesai: { D, B }</span>
    </div>
    <div class="iter-desc">
      &bull; <strong>D</strong> (belum berwarna, derajat tertinggi) diberi Warna 2.<br>
      &bull; Simpul <strong>E, A</strong> dilewati karena bertetangga dengan D.<br>
      &bull; Simpul <strong>B</strong> tidak bertetangga dengan D &rarr; Diberi <strong>Warna 2 (Merah)</strong>.
    </div>
  </div>
  <div class="iter-box">
    <div class="iter-header">
      <span>Iterasi 3: Alokasi Warna 3 (Hijau)</span>
      <span class="iter-badge">Selesai: { E, A }</span>
    </div>
    <div class="iter-desc">
      &bull; <strong>E</strong> diberi Warna 3.<br>
      &bull; Simpul <strong>A</strong> tersisa dan tidak bertetangga dengan E &rarr; Diberi <strong>Warna 3 (Hijau)</strong>. Semua simpul terwarnai!
    </div>
  </div>
</div>

---

<div class="header-tag">Teknik Informatika 2026</div>
<h2><span class="slash">/</span> Deliverables &amp; Results</h2>
<p class="s25">
  Ringkasan evaluasi output algoritma pada kasus uji representatif
</p>
<div class="grid-2x2">
  <div class="card">
    <h3>Optimal Chromatic Number</h3>
    <p>Hanya membutuhkan <strong>3 Warna</strong> (Biru, Merah, Hijau) dari batas atas teoritis (Δ + 1 = 5).</p>
  </div>
  <div class="card">
    <h3>Zero Conflict Guarantee</h3>
    <p>100% validitas terbukti: Tidak ada dua simpul bertetangga yang berbagi warna yang sama.</p>
  </div>
  <div class="card">
    <h3>Time Complexity</h3>
    <p>Eksekusi instan O(<i>V</i> log <i>V</i> + <i>V</i> + <i>E</i>). Sangat efisien dibandingkan pencarian eksak yang eksponensial.</p>
  </div>
  <div class="card">
    <h3>Space Complexity</h3>
    <p>Penggunaan memori linear O(<i>V</i> + <i>E</i>) dengan representasi Adjacency List yang ringan.</p>
  </div>
</div>

---

<!-- _paginate: false -->
<div class="header-tag">Teknik Informatika 2026</div>
<div class="s34">
  <h1 class="s35">
    <span class="slash">/</span> Thank<br>You
  </h1>
  <p class="s3">
    Ada pertanyaan seputar Graph Coloring &amp; Welsh-Powell?
  </p>
</div>
<div class="footer-prepared">
  <div class="s36">
    <span class="label">prepared by</span>
    <span class="names">Galuh &nbsp;|&nbsp; Zuyyin &nbsp;|&nbsp; Lina &nbsp;|&nbsp; Mai</span>
  </div>
  <div class="s37">
    Teknik Informatika &bull; Final Project Teori Graf 2026
  </div>
</div>