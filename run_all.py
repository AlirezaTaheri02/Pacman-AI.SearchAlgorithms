import subprocess
import tkinter as tk
from tkinter import messagebox

def ask(message):
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askquestion("Confirm to run?", message)
    root.destroy()
    return response

python = "python3" # Change this to {"python"} if required

# DFS
if ask("DFS: tinyMaze") == "yes":
    subprocess.run([python, "pacman.py", "-l", "tinyMaze", "-p", "SearchAgent"])
if ask("DFS: mediumMaze") == "yes":
    subprocess.run([python, "pacman.py", "-l", "mediumMaze", "-p", "SearchAgent"])
if ask("DFS: bigMaze") == "yes":
    subprocess.run([python, "pacman.py", "-l", "bigMaze", "-z", "0.5", "-p", "SearchAgent","--frameTime","0"])

# BFS
if ask("BFS: tinyMaze") == "yes":
    subprocess.run([python, "pacman.py", "-l", "tinyMaze", "-p", "SearchAgent","-a","fn=bfs"])
if ask("BFS: mediumMaze") == "yes":
    subprocess.run([python, "pacman.py", "-l", "mediumMaze", "-p", "SearchAgent","-a","fn=bfs"])
if ask("BFS: bigMaze") == "yes":
    subprocess.run([python, "pacman.py", "-l", "bigMaze", "-p", "SearchAgent","-a","fn=bfs","-z","0.5","--frameTime","0"])

# UCS
if ask("UCS: mediumMaze") == "yes":
    subprocess.run([python, "pacman.py", "-l", "mediumMaze", "-p", "SearchAgent","-a","fn=ucs"])
if ask("BFS: mediumDotMaze") == "yes":
    subprocess.run([python, "pacman.py", "-l", "mediumDottedMaze", "-p", "StayEastSearchAgent"])
if ask("BFS: mediumScaryMaze") == "yes":
    subprocess.run([python, "pacman.py", "-l", "mediumScaryMaze", "-p", "StayWestSearchAgent","--frameTime","0"])

# A*
if ask("A*: bigMaze") == "yes":
    subprocess.run([python, "pacman.py", "-l", "bigMaze","-z","0.5","-p", "SearchAgent","-a","fn=astar,heuristic=manhattanHeuristic","--frameTime","0"])
