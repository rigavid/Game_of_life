from Outils.cvt import *
from Outils.cvt2 import *
sz = [100, 100]

if sz[0]>sz[1]:
    max_x = 1000
    max_y = 1000/sz[0]*sz[1]
else:
    max_y = 1000
    max_x = 1000/sz[1]*sz[0]

class ps:
    clck = False
    time = time.time()
    pos = [0,0]

def souris(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        ps.clck = True
        pos = [x, y]
        if clicked_in(pos, [[(1920-max_x)/2, 40], [max_x+(1920-max_x)/2, max_y+40]]):
            ps.pos = [pos[n]-[(1920-max_x)/2, 40][n] for n in [0,1]]
    elif event == cv2.EVENT_MOUSEMOVE:
        if ps.clck and diff(ps.time, time.time()) > 0.1:
            pos = [x, y]
            if clicked_in(pos, [[(1920-max_x)/2, 40], [max_x+(1920-max_x)/2, max_y+40]]):
                ps.pos = [pos[n]-[(1920-max_x)/2, 40][n] for n in [0,1]]
    elif event == cv2.EVENT_LBUTTONUP:
        ps.clck = False

ly = layout(img=image.new_img(fond=col.new('404040')))
img_life = image(img=image.new_img(dimensions=[max_x, max_y], fond=col.blanc))
img_life_g = copy.deepcopy(img_life)
if sz[0] <= 350 or sz[1] <= 350:
    for x in range2(0, max_x, max_x/sz[0]):
        for y in range2(0, max_y, max_y/sz[1]):
            img_life_g.rectangle([x, y], [x+max_x/sz[0], y+max_y/sz[1]], col.new('202020'), 1)
jeu = ly.frame(img=copy.deepcopy(img_life), pos=[(1920-max_x)/2, 40])

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
img_g = True
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
            x = round((pos[0]-(max_x/sz[0])/2)/(max_x/sz[0]))
            y = round((pos[1]-(max_y/sz[1])/2)/(max_y/sz[1]))
            grille[x,y]=1 if grille[x,y]==0 else 0
        if img_g:
            img = copy.deepcopy(img_life_g)
        else:
            img = copy.deepcopy(img_life)
        for x in range2(0, max_x, max_x/sz[0]):
            for y in range2(0, max_y, max_y/sz[1]):
                try:
                    if grille[round(x/(max_x/sz[0])), round(y/(max_y/sz[1]))] == 1:
                        img.rectangle([x, y], [x+max_x/sz[0], y +
                                    max_y/sz[1]], col.black, 0)
                except:
                    pass
        jeu.img = img
        img = ly.montre(True, col_dbg=col.new('202020'), attente=0)
        wk = souris_sur_image(img.img, souris, attente=1, destroy=non)
        match wk:
            case 27: raise SystemExit
            case 13: pause = not pause
            case 8: grille = np.full(sz,0,np.int8)
            case 32: img_g = not img_g
            case 114: break
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