# Required packages:
# >>> opencv-python
# >>> numpy
# >>> sty

import numpy as np, cv2, random as rd, copy, time, os
from sty import Style, RgbFg, fg
try: from path_functs import *
except: from Outils.path_functs import *
try: from terminal import *
except: from Outils.terminal import *
try: from couleurs import *
except: from Outils.couleurs import *
try: from calculs import *
except: from Outils.calculs import *
try: from _vars_ import *
except: from Outils._vars_ import *
def fusionImages(img, img_base, pos=[0, 0]):
    '''
    Prend:
    ------
    :img: ``np.array``\n
    :img_base: ``np.array``\n
    Renvoie:
    --------
    ``np.array``\nImage.
    '''
    pos = [round(v) for v in pos]
    x_offset, y_offset = pos
    try:
        img_base[y_offset:y_offset + img.shape[0], x_offset:x_offset + img.shape[1]] = img
        return img_base
    except (IndexError, ValueError):
        sz_x, sz_y = len(img[0]), len(img)
        for x_ in range(sz_x):
            x = pos[0]+x_
            if x<0 or x>=len(img_base[0]): continue
            for y_ in range(sz_y):
                y = pos[1]+y_
                if y<0 or y>=len(img_base): continue
                img_base[y,x] = img[y_,x_]
        return img_base
class image:
    class boutton:
        def __init__(self, nom='-', coos=[[0, 0], []]) -> None:
            self.nom = nom
            return None
    def new_img(self=None, dimensions=screen, fond=[256 for _ in range(3)]) -> np.array:
        return(np.full([round(v) for v in dimensions[::-1]]+[3], fond[::-1], np.uint8))
    def __init__(self, nom='image_python', img=None) -> None:
        self.nom = nom
        if type(img) == type(None):
            img = self.new_img()
        elif type(img) == image:
            img = img.img
        self.img = np.array(img)
        return None
    def agrandis_img(self, cmb=2):
        img = np.array([[[0,0,0] for x in range(len(self.img[0])*cmb)] for y in range(len(self.img)*cmb)])
        for y in range(len(img)):
            for x in range(len(img[0])):
                img[y,x] = self.img[y//cmb,x//cmb]
        self.img = img
        return(None)
    def __str__(self, ordre=True) -> str:
        img_str = ''
        n = 0
        cmb = len(self.img)*len(self.img[0])
        if ordre:
            mn_x, mx_x, st_x = 0, len(self.img), 1
            mn_y, mx_y, st_y = 0, len(self.img[0]), 1
        else:
            mn_x, mx_x, st_x = len(self.img)-1, -1, -1
            mn_y, mx_y, st_y = len(self.img[0])-1, -1, -1
        for x in range(mn_x, mx_x, st_x):
            for y in range(mn_y, mx_y, st_y):
                b, g, r = self.img[x, y]
                fg.custom = Style(RgbFg(r, g, b))
                img_str += f'{fg.custom}██'
                n += 1
            print(f'{len(self.img)}, {len(self.img[0])} - {n/cmb*100:4f}%', end='\r')
            img_str += '\n'
        img_str += fg.custom+fg.rs
        print(' '*20, end='\r')
        return(img_str)
    def montre(self, attente=0, destroy=False, fullscreen=False) -> int:
        '''
        In:
        ---
        :attente: ``int`` miliseconds\n
        :destroy: ``bool``\n
        :relocalisage_de_l_img: ``list | tuple `` of ``int`` [x, y]\n
        Out:
        ----
        ``None``
        '''
        if fullscreen:
            cv2.namedWindow(self.nom, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(self.nom, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(self.nom, np.array(self.img, np.uint8))
        wk = cv2.waitKeyEx(attente)
        if destroy == True: cv2.destroyWindow(self.nom)
        return(wk)
    def imprime(self, ordre=True) -> None:
        print(self.__str__(ordre), end='')
        return None
    def ligne(self, p1, p2, col=col.noir, ep=1, lineType=0) -> None:
        p1, p2 = [round(p) for p in p1], [round(p) for p in p2]
        cv2.line(self.img, p1, p2, col[::-1], ep, [cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA][lineType%3])
        return None
    def rectangle(self, p1, p2, col=col.noir, ep=1, lineType=0) -> None:
        p1, p2 = [round(p) for p in p1], [round(p) for p in p2]
        cv2.rectangle(self.img, p1, p2, col[::-1], ep if ep != 0 else -1, [cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA][lineType%3])
        return None
    def triangle(self, p1=ct_sg(p3, ct), p2=ct_sg(p4, ct), p3=ct_sg(ct, ch), couleur=col.noir, epaisseur=1, lineType=0):
        lineType = [cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA][lineType%3]
        couleur = couleur[::-1]
        img = self.img
        p1 = [round(i) for i in p1]
        p2 = [round(i) for i in p2]
        p3 = [round(i) for i in p3]
        epaisseur = int(epaisseur)
        if epaisseur <= 0:
            if epaisseur == 0:
                epaisseur = 1
            else:
                epaisseur = abs(epaisseur)
            points = points_segment(p2, p3)
            for i in points:
                cv2.line(img, p1, i, couleur, epaisseur)
        cv2.line(img, p1, p2, couleur, epaisseur, lineType)
        cv2.line(img, p2, p3, couleur, epaisseur, lineType)
        cv2.line(img, p3, p1, couleur, epaisseur, lineType)
        self.img = img
        return None
    def cercle(self, ct, rayon=10, col=col.noir, ep=1, lineType=0) -> None:
        ct = [round(p) for p in ct]; ep = round(ep)
        cv2.circle(self.img, ct, rayon, col[::-1], ep if ep != 0 else -1, [cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA][lineType%3])
        return None
    def ellipse(self, ct, rayons=[10, 10], col=col.noir, ep=1, lineType=0) -> None:
        ct = [round(p) for p in ct]; ep = round(ep)
        cv2.ellipse(self.img, ct, rayons, 0, 360, 0, col[::-1], ep if ep != 0 else -1, [cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA][lineType%3])
        return None
    def sauve_image(self, path='', nom_fichier=None) -> None:
        if nom_fichier == None: nom_fichier = self.nom
        if path != '':
            r = os.getcwd()
            os.chdir(path)
        print(nom_fichier)
        cv2.imwrite(nom_fichier, self.img)
        if path != '': os.chdir(r)
        return None
    def ouvre_image(self, chemin) -> None:
        stream = open(f'{chemin}', "rb")
        bytes = bytearray(stream.read())
        numpyarray = np.asarray(bytes, dtype=np.uint8)
        self.img = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
        return None
    def set_img(self, img) -> None:
        self.img = np.array(img, np.uint8)
        return None
    def ecris(self, texte, ct, couleur=col.red, epaisseur=1, taille=1, police=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, lineType=0) -> None:
        if True: ## Vars ##
            x1, y1 = ct
            x2, y2 = ct
            epaisseur = round(epaisseur)
            textes = list(enumerate(str(texte).split('\n')))
            valdef = cv2.getTextSize('Agd', police, taille, epaisseur)
            xxx = (x1+x2)/2
            yyy = (y1+y2)/2
            yyy -= round(valdef[0][1]*(len(textes)-1))
        for i, line in textes:
            tailles = cv2.getTextSize(line, police, taille, epaisseur)
            x = round(xxx-tailles[0][0]/2)
            y = round(yyy+tailles[1]/2)
            yy = y + i*tailles[0][1]*2
            cv2.putText(self.img, line, (x, yy), police, taille, couleur, epaisseur, [cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA][lineType%3])
        return None

class layout:
    class frame_:
        def __init__(self, img=image.new_img(fond=col.white), pos=[0,0], name='frame0') -> None:
            self.name = name
            self.img = image(img=copy.deepcopy(img))
            self.pos = pos
        def __str__(self) -> str:
            return self.name
    def __init__(self, img=image.new_img(), frames=[]) -> None:
        self.img = image(img=copy.deepcopy(img))
        self.frames = frames
    def frame(self, img=image.new_img(fond=col.white, dimensions=[100, 100]), pos=[0,0], name=None):
        if name == None:
            name = 'frame' + str(len(self.frames))
        while name in self.frames: name += '_2'
        fenetre = self.frame_(img=img, pos=pos, name=name)
        self.frames.append(fenetre)
        return fenetre
    def montre(self, debug=False, frames=None, except_frames=[], col_dbg=col.red, attente=1):
        img = image(img=copy.deepcopy(self.img.img))
        if frames == None: frames = copy.deepcopy(self.frames)
        for frm in except_frames:
            ind = [i.name for i in frames].index(frm.name)
            if ind != -1: frames.pop(ind)
        for frame in frames:
            img.img = fusionImages(frame.img.img, img.img, frame.pos)
            if debug:
                img.rectangle(frame.pos, [frame.pos[0]+len(frame.img.img[0]), frame.pos[1]+len(frame.img.img)], col_dbg, 3)
        if attente < 0:
            return img.montre(attente, fullscreen=True)
        else: return copy.deepcopy(img)
    

if __name__ == '__main__':
    img = image('Test')
    pt = pt_sg([0, 0], screen)
    img.ellipse(pt, [500, 100], col.magenta, 10)
    img.ligne([0, 0], screen, col.white, 10)
    img.cercle([0, 0], 100, col.red, 0)
    img.cercle(screen, 1000, col.red, 0)
    img.montre(fullscreen=True)