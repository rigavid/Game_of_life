class col:
    noir=black=[0,0,0]
    blanc=white=[255,255,255]
    rouge=red=[255,0,0]
    bleu=blue=[0,0,255]
    vert=green=[0,255,0]
    cyan=[0,255,255]
    magenta=[255,0,255]
    jaune=yellow=[255,255,0]
    def new(hexadecimal='000000',tipe='bgr'):
        '''
            Couleur héxadécimale en BGR par défaut.
            Couleur héxadécimale en RGB si c'est spécifié sur le type.
            ---
            Retourne une couleur en BGR
        '''
        if type(hexadecimal) == int:
            hexadecimal = f'{hexadecimal:x}'
        hexadecimal.replace('#','')
        if tipe.lower()=='rgb':
            r, g, b = int(hexadecimal[0:2],base=16), int(hexadecimal[2:4],base=16), int(hexadecimal[4:6],base=16)
        else:
            b, g, r = int(hexadecimal[0:2],base=16), int(hexadecimal[2:4],base=16), int(hexadecimal[4:6],base=16)
        return[b,g,r]