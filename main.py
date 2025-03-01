from tkinter import simpledialog
from pyimager import *
from numba import njit
import tkinter as tk
import numpy as np
import datetime
import time

def ask_num():
    root = tk.Tk()
    root.withdraw()
    n = simpledialog.askinteger("[Set size]", "Enter number: ")
    return n if n is not None else 0

@njit
def get_voisins(m):
    rows, cols = m.shape
    voisins = np.zeros_like(m)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            voisins[i, j] = (m[i-1, j-1] + m[i-1, j] + m[i-1, j+1] + m[i, j-1] + m[i, j+1] + m[i+1, j-1] + m[i+1, j] + m[i+1, j+1])
    return voisins

@njit
def update_cells(m):
    voisins = get_voisins(m)
    return np.where((m == 1) & ((voisins < 2) | (voisins > 3)), 0, m) | np.where((m == 0) & (voisins == 3), 1, 0)

def format_time(s):
    h, m, s = int(s // 3600), int((s % 3600) // 60), int(s % 60)
    ts = ""
    if h > 0: ts += f"{h}h"
    if m > 0 or h > 0: ts += f"{m}m"
    ts += f"{s}s"
    return ts


class GameOfLife:
    def __init__(self, size):
        self.min_size = 100
        self.max_size = RES.resolution[1]
        self.size = min(max(size, self.min_size), self.max_size)
        self.m = np.random.randint(0, 2, (self.size, self.size), dtype=np.int8)
        self.cells = new_img((self.size, self.size))
        self.img = new_img(name="Game of Life")
        self.last = 0

    def image(self):
        self.cells.img = np.stack([self.m * 255] * 3, axis=-1)
        s1, s2 = self.img.size(), self.cells.size()
        x, y = (s1[0]-s2[0])//2, (s1[1]-s2[1])//2
        ## Clear infos ##
        self.img.rectangle([0, 0], RES.resolution, COL.white, 0)
        ## Vars for infos ##
        alive, dead, t = np.sum(self.m == 1), np.sum(self.m == 0), np.sum(self.m != 2)
        prsT, prs = (COL.black, 3, 6, 0, 2, True), (COL.black, 2, 4, 0, 2, False)
        self.img.text(f"^UL^Stats^UL^", [x/2, 100], *prsT)
        start = 200
        ## Write infos ##
        texts = [
            f"  Gen. : {self.gen:,}",
            f"  Time : {format_time(time.time()-self.first)}",
            f"En vie : {alive:,}",
            f"Mortes : {dead:,}",
            f" Total : {t:,}",
            f" Ratio : {alive/t*100:0>5.2f}% Viv.",
            f" Ratio : {dead /t*100:0>5.2f}% Mor.",
            f"  Size : {self.m.shape[0]} cases",
            f"  Size : {self.cells.size()[0]} px",
            f"   FPS : {1/(time.time()-self.last):.2f}",
        ]
        for t in texts:
            self.img.text(t, [x/2-200, start], *prs)
            start += 50
        ## Write help ##
        self.img.text(f"^UL^Commands^UL^", [RES.resolution[0]-x/2, 100], *prsT)
        start = 200
        texts = [
            f"R to start randomly",
            f"P to pause simul.",
            f"S to set grid size",
            f"+ to increase size",
            f"- to decrease size",
        ]
        for t in texts:
            self.img.text(t, [RES.resolution[0]-x/2-180, start], *prs)
            start += 50
        ## Updates game ##
        th = 3
        self.img.rectangle([x-1-th, y-1-th], [x+s2[0]+th, y+s2[1]+th], COL.red, 0)
        self.img.img[y:y+s2[1], x:x+s2[0]] = self.cells.img
        self.last = time.time()

    def update(self):
        self.m = update_cells(self.m)
        self.gen += 1
        self.image()

    def start(self):
        self.gen, self.first = 0, time.time()
        self.image()
        self.img.build()
        pause = False
        while self.img.is_opened():
            wk = self.img.show()
            match wk:
                case 114:## R ##
                    self.m = np.random.randint(0, 2, (self.m.shape), dtype=np.int8)
                    self.gen, self.first = 0, time.time()
                    self.image()
                    self.img.show()
                case 45: ## - ##
                    if self.m.shape[0]>self.min_size and self.m.shape[1]>self.min_size:
                        self.m = self.m[0:-1, 0:-1]
                        if pause:
                            self.image()
                            self.img.show()
                case 43: ## + ##
                    if self.m.shape[0]<self.max_size and self.m.shape[1]<self.max_size:
                        self.m = np.hstack([self.m, np.zeros((self.m.shape[0], 1), dtype=self.m.dtype)])
                        self.m = np.vstack([self.m, np.zeros((1, self.m.shape[1]), dtype=self.m.dtype)])
                        if pause:
                            self.image()
                            self.img.show()
                case 112:## P ##
                    if not pause: self.paused_time = time.time()
                    else: self.first += time.time() - self.paused_time
                    pause = not pause
                case 115:## S ##
                    s = ask_num()
                    if s>=self.min_size and s<=self.max_size:
                        if s<=self.m.shape[0]: self.m = self.m[0:s, 0:s]
                        else:
                            while self.m.shape[0]<s:
                                self.m = np.hstack([self.m, np.zeros((self.m.shape[0], 1), dtype=self.m.dtype)])
                                self.m = np.vstack([self.m, np.zeros((1, self.m.shape[1]), dtype=self.m.dtype)])
            if pause: continue
            self.update()

if __name__ == "__main__":
    game = GameOfLife(RES.resolution[1])
    game.start()