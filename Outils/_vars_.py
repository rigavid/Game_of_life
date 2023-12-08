try: from calculs import *
except: from Outils.calculs import *
haut = 1080
long = 1920
screen = [long, haut]
hg = [0, 0]
hd = [long, 0]
bg = [0, haut]
bd = [long, haut]
ct = [round(long/2), round(haut/2)]
p1 = [round((long-haut)/2), 0]
p2 = [round((long-haut)/2)+haut, 0]
p3 = [round((long-haut)/2), haut]
p4 = [round((long-haut)/2)+haut, haut]
cg = ct_sg(p1, p3)
cd = ct_sg(p2, p4)
ch = ct_sg(p1, p2)
cb = ct_sg(p3, p4)
if True: ## Format.vars ##
    new_line = '\n'
    espace = ' '
    BLACK        = "\033[30m"
    RED          = "\033[31m"
    GREEN        = "\033[32m"
    BROWN        = "\033[33m"
    BLUE         = "\033[34m"
    PURPLE       = "\033[35m"
    CYAN         = "\033[36m"
    LIGHT_GRAY   = "\033[37m"
    DARK_GRAY    = "\033[30m"
    LIGHT_RED    = "\033[31m"
    LIGHT_GREEN  = "\033[32m"
    YELLOW       = "\033[33m"
    LIGHT_BLUE   = "\033[34m"
    LIGHT_PURPLE = "\033[35m"
    LIGHT_CYAN   = "\033[36m"
    LIGHT_WHITE  = "\033[37m"
    BOLD         = '\033[1m'
    UNDERLINED   = '\033[4m'
    NORMAL       = '\033[00m' # @@ Always append to the end, else: terminal = BUG @@
    BOLD_RED     = f'{RED}{BOLD}'
    BOLD_GREEN   = f'{GREEN}{BOLD}'
    BOLD_BLUE    = f'{BLUE}{BOLD}'
if True: ## keys ##
    key_a = 97
    key_d = 100
    key_w = 119
    key_s = 115

    key_arr_l = 2424832
    key_arr_r = 2555904
    key_arr_u = 2490368
    key_arr_d = 2621440