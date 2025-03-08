from scipy.signal import fftconvolve
from tkinter import simpledialog
import matplotlib.pyplot as plt
from pyimager import *
import numpy as np
import time

def ask_num(int=True):
    n = simpledialog.askfloat("[Set size]", "Enter number: ")
    if int and n!=None: n=round(n)
    return n if n is not None else 0

def custom_convolve(m, kernel):
    pad_y, pad_x = kernel.shape[0]//2, kernel.shape[1]//2
    result = fftconvolve(np.pad(m, ((pad_y, pad_y), (pad_x, pad_x)), mode='wrap'), kernel, mode='same')
    return result[pad_y:pad_y + m.shape[1], pad_x:pad_x + m.shape[0]]

class glob:
    mu, sigma = 0.15, 0.015
    new, val = False, None
    mu_, sigma_ = 10, 100

def gauss(x, mu, sigma):
    return np.exp(-0.5 * ((x-mu)/sigma)**2)

def growth_function(x):
    return -1 + 2 * np.exp(-((x - glob.mu) ** 2) / (2 * glob.sigma ** 2))

def update_cells(m, kernel, dt=0.1, *args, **kwargs):
    conv = custom_convolve(m, kernel)/100
    return np.clip(m + dt * growth_function(conv), 0, 1)

def changeR(val):
    glob.new = "R"
    glob.val = val
def changeMu(val):
    glob.new = "M"
    glob.val = val/glob.mu_
def changeSigma(val):
    glob.new = "S"
    glob.val = val/glob.sigma_

class Lenia:
    def generate_kernel(self):
        y, x = np.ogrid[-self.R:self.R, -self.R:self.R]
        distance = np.sqrt(x**2 + y**2) / self.R * len(self.rings)
        K_multiring = np.zeros_like(distance)
        for i in range(len(self.rings)):
            K_multiring += (distance.astype(int) == i) * self.rings[i] * gauss(distance%1, self.mu, self.sigma)
        return K_multiring

    def get_rd_m(self):
        return np.random.rand(self.size, self.size)

    def __init__(self, size):
        self.min_size = 100
        self.max_size = RES.resolution[1]
        self.size = min(max(size, self.min_size), self.max_size)
        self.m = self.get_rd_m()
        self.cells, self.img = new_img((self.size, self.size)), new_img(name="Lenia")
        self.last, self.gen, self.first, self.pause = 0, 0, time.time(), False
        self.R, self.mu, self.sigma, self.dt = 13, 0.5, 0.15, 0.1
        self.rings = [1]
        self.kernel = self.generate_kernel()

    def image(self):
        self.cells.img = np.stack([self.m * 255] * 3, axis=-1)
        s1, s2 = self.img.size(), self.cells.size()
        x, y = (s1[0]-s2[0])//2, (s1[1]-s2[1])//2
        ## Clear infos ##
        self.img.rectangle([0, 0], RES.resolution, COL.white, 0)
        ## Vars for infos ##
        alive = np.sum(self.m > 0.1)
        dead = np.sum(self.m <= 0.1)
        t = time.time()-self.first if not self.pause else self.paused_time-self.first
        fps = 1 / (time.time() - self.last) if self.last else 0
        ## Write infos ##
        prsT, prs = (COL.black, 3, 6, 0, 2, True), (COL.black, 2, 4, 0, 2, False)
        self.img.text(f"^UL^Stats^UL^", [x/2, 50], *prsT)
        start = 100
        texts = [
            f"  Gen. : {self.gen:,}",
            f"  Time : {t:.2f}s",
            f"  Size : {self.m.shape[0]} cases",
            "",
            f"En vie : {alive:,}",
            f"Mortes : {dead:,}",
            f" Ratio : {alive/self.m.size*100:0>5.2f}% Viv.",
            f" Ratio : {dead/self.m.size*100:0>5.2f}% Mor.",
            f" Total : {self.m.size:,}",
            "",
            f"  MGPS : {self.gen/t:.2f}",
            f"   FPS : {fps:.2f}",
            f" Calcs : {self.m.size*self.kernel.size:,}",
            f"C/S : {int(self.m.size*fps*self.kernel.size):,}",
        ]
        for t in texts:
            self.img.text(t, [x/2-200, start], *prs)
            start += 50
        ## Write help ##
        self.img.text(f"^UL^Commands^UL^", [RES.resolution[0]-x/2, 50], *prsT)
        start = 150
        texts = [
            f"R to start randomly",
            f"P to pause simul.",
            f"S to set grid size",
            f"I to show kernel",
            f"K to modify kernel",
        ]
        for t in texts:
            self.img.text(t, [RES.resolution[0]-x/2-180, start], *prs)
            start += 50
        ## Write behaviour info ##
        self.img.text(f"^UL^Behaviour^UL^", [x/2, RES.resolution[1]/2+350], *prsT)
        start = RES.resolution[1]/2+400
        texts = [
            f" ^B87^ : {glob.sigma}",
            f" ^B81^ : {glob.mu}",
        ]
        for t in texts:
            self.img.text(t, [x/2-200, start], *prs)
            start += 50
        ## Write kernel info ##
        self.img.text(f"^UL^Kernel^UL^", [RES.resolution[0]-x/2, RES.resolution[1]/2+150], *prsT)
        start = RES.resolution[1]/2+200
        texts = [
            f" R : {self.R}",
            f" X : ",
            f" Y : ",
            f" ^B87^ : {self.sigma}",
            f" ^B81^ : {self.mu}",
        ]
        for t in texts:
            self.img.text(t, [RES.resolution[0]-x/2-180, start], *prs)
            start += 50
        ## Updates game ##
        th = 3
        self.img.rectangle([x-1-th, y-1-th], [x+s2[0]+th, y+s2[1]+th], COL.red, 0)
        self.img.img[y:y+s2[1], x:x+s2[0]] = self.cells.img
        self.last = time.time()

    def resize(self, size):
        if self.max_size >= size >= self.min_size:
            self.size = size
            self.m = np.random.rand(self.size, self.size)
            self.first = time.time()
            if self.pause: self.paused_time = self.first
            self.gen = 0

    def update(self):
        self.m = update_cells(self.m, self.kernel, self.dt, mu=self.mu, sigma=self.sigma)
        self.gen += 1
        self.image()

    def kernel_img(self):
        mult = 5
        img = new_img((self.kernel.shape[0]*mult, self.kernel.shape[1]*mult), COL.black)
        for x in range(self.kernel.shape[0]):
            for y in range(self.kernel.shape[1]):
                img.img[x*mult:x*mult+mult, y*mult:y*mult+mult] = np.full((mult, mult, 3), [self.kernel[x, y]*255 for _ in "..."])
        return img.img

    def start(self):
        self.image()
        self.img.build()
        while self.img.is_opened():
            wk = self.img.show()
            match wk:
                case 114:# R (reset)
                    self.m = self.get_rd_m()
                    self.gen, self.first = 0, time.time()
                    self.image()
                case 115:# S (set size)
                    self.resize(ask_num())
                case 112:# P (pause)
                    if not self.pause: self.paused_time = time.time()
                    else: self.first += time.time() - self.paused_time
                    self.pause = not self.pause
                case 105:# I (info)
                    print(f"Final Kernel: min={self.kernel.min()}, max={self.kernel.max()}")
                    plt.subplot(121)
                    plt.imshow(game.kernel, interpolation='none', cmap='gray')
                    plt.title('Convolution filter')
                    plt.subplot(122)
                    a = np.arange(0, 0.4, 0.001)
                    plt.plot(a, growth_function(a))
                    plt.axhline(0, linestyle='--', color='red')
                    plt.colorbar()
                    plt.show()
                case 107:# K (kernel)
                    ki = new_img(self.kernel.shape, background=COL.black, name="[Kernel editor]")
                    ki.build()
                    max_ = 100
                    cv2.createTrackbar("R", ki.name, self.R, max_, changeR)
                    cv2.createTrackbar("Mu", ki.name, round(self.mu*glob.mu_), 25*max_//100, changeMu)
                    cv2.createTrackbar("Sigma", ki.name, round(self.sigma*glob.sigma_), max_, changeSigma)
                    cv2.setTrackbarMin("R", ki.name, 5)
                    cv2.setTrackbarMin("Mu", ki.name, 1)
                    cv2.setTrackbarMin("Sigma", ki.name, 15)
                    ki.img = self.kernel_img()
                    while ki.is_opened():
                        wk = ki.show()
                        if glob.new:
                            match glob.new:
                                case "R": self.R = glob.val
                                case "M": self.mu = glob.val
                                case "S": self.sigma = glob.val
                            glob.new = False
                            glob.val = None
                            self.kernel = self.generate_kernel()
                            ki.img = self.kernel_img()
                        elif wk == 114: ## R
                            n = ask_num()
                            if n>0 and n<5 and n!=None:
                                r = []
                                for i in range(n):
                                    n2 = ask_num(False)
                                    if 1>=(n2)>0 and n2!=None:
                                        r.append(n2)
                                self.rings = r
                                self.kernel = self.generate_kernel()
                                ki.img = self.kernel_img()
                    cv2.destroyWindow(ki.name)
            if self.pause:
                self.image()
                continue
            self.update()

if __name__ == "__main__":
    game = Lenia(RES.resolution[1])
    game.start()
    # print(game.kernel)