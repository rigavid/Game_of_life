from Outils.cvt import *
from Outils.cvt2 import *

class ps:
    clck = False
    time = time.time()
    pos = [0,0]

def souris(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        ps.clck = True
        pos = [x, y]
        if clicked_in(pos, [[(1920-1000)/2, 40], [1000+(1920-1000)/2, 1040]]):
            ps.pos = [pos[n]-[(1920-1000)/2, 40][n] for n in [0,1]]
    elif event == cv2.EVENT_MOUSEMOVE:
        if ps.clck and diff(ps.time, time.time()) > 0.1:
            pos = [x, y]
            if clicked_in(pos, [[(1920-1000)/2, 40], [1000+(1920-1000)/2, 1040]]):
                ps.pos = [pos[n]-[(1920-1000)/2, 40][n] for n in [0,1]]
    elif event == cv2.EVENT_LBUTTONUP:
        ps.clck = False

sz = [100, 100]
ly = layout(img=image.new_img(fond=col.new('404040')))
img_life = image(img=image.new_img(dimensions=[1000, 1000], fond=col.blanc))
if sz[0] <= 350 or sz[1] <= 350:
    for x in range(0, 1000, 1000//sz[0]):
        for y in range(0, 1000, 1000//sz[1]):
            img_life.rectangle([x, y], [x+1000//sz[0], y+1000//sz[1]], col.new('202020'), 1)
jeu = ly.frame(img=copy.deepcopy(img_life), pos=[(1920-1000)/2, 40])

voisins = [[-1, -1], [0, -1], [1, -1],
           [-1, 0], [1, 0],
           [-1, 1], [0, 1], [1, 1]]

def count_vsns(grille, pos) -> int:
    x, y = pos
    vsns = 0
    for v in voisins:
        x_, y_ = [[x, y][n]+v[n] for n in [0, 1]]
        if x_ < 0 or y_ < 0:
            continue
        elif x_ >= len(grille) or y_ >= len(grille[0]):
            continue
        if grille[x_, y_] != 0:
            vsns += 1
    return vsns
pause = False
while True:
    grille = np.full(sz, 0, np.int8)
    positions = []
    for _ in range(rd.randint(0, sz[0]*sz[1]-1)):
        positions.append([rd.randint(0,sz[0]-1),rd.randint(0,sz[1]-1)])
    for p in positions:
        grille[p[0], p[1]] = 1
    while True:
        if ps.pos != [0,0]:
            pos = ps.pos; ps.pos=[0,0]
            x = round(pos[0]//(1000//sz[0]))
            y = round(pos[1]//(1000//sz[1]))
            grille[x,y]=1 if grille[x,y]==0 else 0
        img = copy.deepcopy(img_life)
        for x in range(0, 1000, 1000//sz[0]):
            for y in range(0, 1000, 1000//sz[1]):
                try:
                    if grille[x//(1000//sz[0]), y//(1000//sz[1])] == 1:
                        img.rectangle([x, y], [x+1000//sz[0], y +
                                    1000//sz[1]], col.black, 0)
                except:
                    pass
        jeu.img = img
        img = ly.montre(True, col_dbg=col.new('202020'), attente=0)
        wk = souris_sur_image(img.img, souris, attente=1, destroy=non)
        match wk:
            case 32: break
            case 27: raise SystemExit
            case 13: pause = not pause
            case 8: grille = np.full(sz,0,np.int8)
            case -1: pass
            case _: print(wk)
        if not pause:
            grille2 = np.full(sz, 0, np.int8)
            for x in range(sz[0]):
                for y in range(sz[1]):
                    p = grille[x, y] == 1
                    n = count_vsns(grille, [x, y])
                    if p:
                        if n in [2, 3]:
                            grille2[x, y] = 1
                    else:
                        if n == 3:
                            grille2[x, y] = 1
            grille = copy.deepcopy(grille2)