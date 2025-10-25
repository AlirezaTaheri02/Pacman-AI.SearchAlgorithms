# Pacman Search Algorithms 🧩

This repository contains my implementation of classic search algorithms for the Pacman AI project, developed as part of my **Artificial Intelligence course (Fall 2024)**.

## 🚀 Overview
Implemented algorithms:
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A\* Search
- Custom heuristics (Manhattan, Corners, etc.)

These agents navigate the Pacman environment to find optimal paths in various mazes.

## 🧠 How to Run
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
