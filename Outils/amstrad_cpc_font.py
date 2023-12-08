from cvt2 import *

if is_file('cvt2.py'):
    rel_path = './'
elif is_file('cvt2.py', 'Outils'):
    rel_path = './Outils'


img = image()
img.ouvre_image(rel_path+'/Amstrad_CPC_Full_AMSDOS_Character_Set.png')

img.montre(fullscreen=True)

pw = 2

xc, yc = 8*pw, 8*pw

coul = col.black
c = 0
remove_dir('imgs_cpc_font', rel_path)
if create_dir_if_unexisting('imgs_cpc_font', rel_path):
    print('\nExecuting\n')
    for y in range(16):
        for x in range(16):
            im = img.img[(y*yc):(y*yc)+yc, (x*xc):(x*xc)+xc]
            im = [[col.black if sum(i2)<256*3/2 else col.white for i2 in im[i]] for i in range(len(im))]
            img_char = image()
            img_char.set_img(im)
            img_char.imprime()
            img_char.sauve_image(rel_path+'/imgs_cpc_font/', f'CPC_char_n_{c}.jpg'); c+=1