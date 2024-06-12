from Outils.cvt2 import *
from Outils.cvt import montre


if True: ## Conway's game of life ##
    fenetre = layout(img=image.new_img(dimensions=[1920,1080,3]))
    matrix = np.full([1080,1080,3], col.black, np.uint8)
    jeu = fenetre.frame(pos=[(1920-1080)//2, 0], img=matrix, name='matrix')
    fenetre.montre(except_frames=[jeu])
