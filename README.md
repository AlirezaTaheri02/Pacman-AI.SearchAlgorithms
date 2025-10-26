# 👾 Pacman Search Algorithms

This repository contains my implementation of classical search algorithms for the **Pacman AI Project**, developed as part of my *Artificial Intelligence course (Fall 2024)*.

##  Overview
Implemented algorithms:
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A\* Search

These algorithms enable Pacman agents to navigate different maze environments efficiently — including layouts with energy pellets and scenarios where Pacman is chased by ghosts.  
The project also includes a script that automatically runs all implemented algorithms and visualizes their execution in live simulations with a single command.

## 📷 Visual Demonstrations (images + tags)

Below are the screenshots I used in the README along with explicit tags and short captions for each image.  
Place the image files in the repository folder `assets/` and ensure the filenames match exactly.

| Image file (assets/) | Tags | Caption |
|---|---:|---|
| `DFS - Medium.png` | `DFS`, `mediumMaze`, `visualization`, `path-trace` | DFS exploring a medium maze — demonstrates deep-first path exploration and the expanded path trace. |
| `DFS - Big.png` | `DFS`, `bigMaze`, `visualization`, `path-trace` | DFS on a large maze — deep exploration can lead to long detours before reaching goal. |
| `BFS - big.png` | `BFS`, `bigMaze`, `shortest-path`, `visualization` | BFS in a large maze — level-order exploration finds the shortest-step path. |
| `UCS - Dotted.png` | `UCS`, `dottedMaze`, `costs`, `energy-pellets` | UCS on a dotted maze — demonstrates cost-aware expansion (useful with weighted steps or energy pellets). |
| `UCS - ScaryMaze.png` | `UCS`, `scaryMaze`, `costs`, `ghosts-scenario` | UCS in a 'scary' maze — cost-based planning in a complex environment (ghosts / dynamic threats). |

---

### Inline images with captions

### 🔍 Depth-First Search (DFS)
Explores the deepest available path first.

<figure>
  <img src="assets/DFS%20-%20Medium.png" alt="DFS - Medium maze (path trace)" />
  <figcaption><strong>DFS — Medium maze</strong> · Tags: <code>DFS</code>, <code>mediumMaze</code>, <code>visualization</code>, <code>path-trace</code></figcaption>
</figure>

<figure>
  <img src="assets/DFS%20-%20Big.png" alt="DFS - Big maze (deep exploration)" />
  <figcaption><strong>DFS — Big maze</strong> · Tags: <code>DFS</code>, <code>bigMaze</code>, <code>visualization</code>, <code>path-trace</code></figcaption>
</figure>

---

### 🕸️ Breadth-First Search (BFS)
Finds the shortest path (in number of steps) by exploring neighbors level-by-level.

<figure>
  <img src="assets/BFS%20-%20big.png" alt="BFS - Big maze (shortest path)" />
  <figcaption><strong>BFS — Big maze</strong> · Tags: <code>BFS</code>, <code>bigMaze</code>, <code>shortest-path</code>, <code>visualization</code></figcaption>
</figure>

---

### 💰 Uniform Cost Search (UCS)
Chooses the lowest cumulative-cost node to expand first — useful for weighted mazes.

<figure>
  <img src="assets/UCS%20-%20Dotted.png" alt="UCS - Dotted maze (cost-aware)" />
  <figcaption><strong>UCS — Dotted maze</strong> · Tags: <code>UCS</code>, <code>dottedMaze</code>, <code>costs</code>, <code>energy-pellets</code></figcaption>
</figure>

<figure>
  <img src="assets/UCS%20-%20ScaryMaze.png" alt="UCS - Scary maze (complex costs/ghosts)" />
  <figcaption><strong>UCS — Scary maze</strong> · Tags: <code>UCS</code>, <code>scaryMaze</code>, <code>costs</code>, <code>ghosts-scenario</code></figcaption>
</figure>






## ⚙️ How to Run
```bash
python3 run_all.py

