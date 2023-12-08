######################################
### Auteur : Tim Tamet -- Martínez ###
### Nom pr : cvt.py ##################

## *_* TODO *_* ##
## TODO Passer tout le programme en POO dans cvt2.py ##
## TODO Quand ce sera fait, supprimer ce programme et renommer cvt2.py en cvt.py ##

## ***TODO*** Faire l'horloge sybyllienne ##

######################################
### À régler : ###########################################
### Il faut remonter les majuscules pour que le bas ######
### soit le même pour les minuscules et les majuscules ###
##########################################################
### TODO :####################################################################
### - class image (comme ça, touts les dessins suporteront le canal alpha) ###
### - ♮ ######################################################################
### - ℗ ##################################################
### - Il faut rajouter tous les idéogrammes (du Tim) ##### ## Il faut d'abord les mettre dans la table du cahier (ou plus d'ailleurs) ##
##########################################################

## To get pip installed packages : `pip freeze`

oui = True
non = False
pas = False
aucun = aucune = 0
wk = 0
if oui: ## Tout ##
    if oui: ## En developpement ##
        pass
    if oui: ## À classer ##
        def ellipsed(ct, rayons, angle):
            b, a = rayons
            p1, p2 = coosCercle(ct, min(a, b), angle), coosCercle(ct, max(a, b), angle)
            x, y = p1[0] - p2[0], p1[1] - p2[1]
            p3 = (p1[0] - x, p1[1])
            p4 = (p1[0], p1[1] - y)
            if a < b:
                return(p3)
            else:
                return(p4)
    if oui: ########################### Classes ###
        class save_pos:
            d = ''
        class iterateur:
            def __init__(self, texte):
                self._texte = texte
                self._index = 0
            def __next__(self):
                if self._index < len(self._texte):
                    out = self._texte[self._index]
                    self._index += 1
                    return(out)
                raise StopIteration
        class chaine:
            if oui: ## Alphabets ##
                latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÇÑabcdefghijklmnopqrstuvwxyzçñ'
                grec = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩƩαβγδεζηθικλμνξοπρσςτυφχψωʃ'
                russe = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            index = 0
            texte = ''
            chars = {
                '#':'hashtag',
                #############################################################################################################################################################################################
                ## Latin : ##################################################################################################################################################################################
                ### Nombres : ###############################################################################################################################################################################
                'full':'a1',' ':'b1','0':'c1','1':'d1', '2':'e1', '3':'f1', '4':'g1', '5':'h1', '6':'i1', '7':'j1', '8':'k1', '9':'l1', '+':'m1', '-':'n1', '±':'o1', '÷':'p1', '×':'q1', ## Nombres, cæt. ##
                ### Maj : ###################################################################################################################################################################################
                '¿':'a2', '?':'b2', 'A':'c2', 'B':'d2', 'C':'e2', 'D':'f2', 'E':'g2', 'F':'h2', 'G':'i2', 'H':'j2', 'I':'k2', 'J':'l2', 'K':'m2', 'L':'n2', 'M':'o2', 'N':'p2', 'O':'q2', ## Latin maj 1/2 ##
                '¡':'a3', '!':'b3', 'P':'c3', 'Q':'d3', 'R':'e3', 'S':'f3', 'T':'g3', 'U':'h3', 'V':'i3', 'W':'j3', 'X':'k3', 'Y':'l3', 'Z':'m3', 'Æ':'n3', 'Œ':'o3', 'Ç':'p3', 'Ñ':'q3', ## Latin maj 2/2 ##
                ### Min : ###################################################################################################################################################################################
                ' ':'a4', '‽':'b4', 'a':'c4', 'b':'d4', 'c':'e4', 'd':'f4', 'e':'g4', 'f':'h4', 'g':'i4', 'h':'j4', 'i':'k4', 'j':'l4', 'k':'m4', 'l':'n4', 'm':'o4', 'n':'p4', 'o':'q4', ## Latin min 1/2 ##
                '(':'a5', ')':'b5', 'p':'c5', 'q':'d5', 'r':'e5', 's':'f5', 't':'g5', 'u':'h5', 'v':'i5', 'w':'j5', 'x':'k5', 'y':'l5', 'z':'m5', 'æ':'n5', 'œ':'o5', 'ç':'p5', 'ñ':'q5', ## Latin min 2/2 ##
                ### Aide : ##################################################################################################################################################################################
                '[latin]interogation_inverse':'a2', '[latin]exclamation_inverse':'a3', '[latin]point_exclarrogatif_inverse':'a4', '[latin]point_exclarrogatif':'b4', ################## Aide Latin 1/3 ######
                '[latin]ae_maj':'n3', '[latin]oe_maj':'o3', '[latin]c_cedille_maj':'p3', '[latin]n_tilde_maj':'q3', '[latin]ae_min':'n5', '[latin]oe_min':'o5', ####################### Aide Latin 2/3 ######
                '[latin]c_cedille_min':'p5', '[latin]n_tilde_min':'q5', '[math]plus_minus':'o1', '[math]division':'p1', '[math]multiplication':'q1', ################################## Aide Latin 3/3 ######
                ## Grec : ###################################################################################################################################################################################
                ### Γρεκ : ##################################################################################################################################################################################
                #### Maj : ##################################################################################################################################################################################
                '[':'a6', ']':'b6', 'Α':'c6', 'Β':'d6', 'Γ':'e6', 'Δ':'f6', 'Ε':'g6', 'Ζ':'h6', 'Η':'i6', 'Θ':'j6', 'Ι':'k6', 'Κ':'l6', 'Λ':'m6', 'Μ':'n6', 'Ν':'o6', 'Ξ':'p6', 'Ο':'q6', ## Grec maj 1/2 ###
                '{':'a7', '}':'b7', 'Π':'c7', 'Ρ':'d7', 'Σ':'e7', 'Σ':'f7', 'Τ':'g7', 'Υ':'h7', 'Φ':'i7', 'Χ':'j7', 'Ψ':'k7', 'Ω':'l7', 'Ʃ':'m7', ########################################## Grec maj 1/2 ###
                #### Min : ##################################################################################################################################################################################
                '<':'a8', '>':'b8', 'α':'c8', 'β':'d8', 'γ':'e8', 'δ':'f8', 'ε':'g8', 'ζ':'h8', 'η':'i8', 'ϑ':'j8', 'ι':'k8', 'κ':'l8', 'λ':'m8', 'μ':'n8', 'ν':'o8', 'ξ':'p8', 'ο':'q8', ## Grec maj 1/2 ###
                '`':'a9', '´':'b9', 'π':'c9', 'ρ':'d9', 'σ':'e9', 'ς':'f9', 'τ':'g9', 'υ':'h9', 'ϕ':'i9', 'χ':'j9', 'ψ':'k9', 'ω':'l9', 'ʃ':'m9', ########################################## Grec maj 1/2 ###
                'φ':'i9', '᾿':'n7', '῾':'n7', 'ͺ':'o7', '῀':'o9', ################################################################################################################ Suplément Grec ###########
                ### Aide : ##################################################################################################################################################################################
                #### Maj : ##################################################################################################################################################################################
                '[grec]alpha_maj':'c6', '[grec]beta_maj':'d6', '[grec]gamma_maj':'e6', '[grec]delta_maj':'f6', '[grec]epsilon_maj':'g6', '[grec]zita_maj':'h6', '[grec]eta_maj':'i6', # Aide Grec maj 1/4 ###
                '[grec]theta_maj':'j6', '[grec]iota_maj':'k6', '[grec]kappa_maj':'l6', '[grec]lambda_maj':'m6', '[grec]mi_maj':'n6', '[grec]ni_maj':'o6', '[grec]ksi_maj':'p6', ####### Aide Grec maj 2/4 ###
                '[grec]omicron_maj':'q6', '[grec]pi_maj':'c7', '[grec]ro_maj':'d7', '[grec]sigma_maj':'e7', '[grec]sigma_maj':'f7', '[grec]tau_maj':'g7', '[grec]upsilon_maj':'h7', ### Aide Grec maj 3/4 ###
                '[grec]phi_maj':'i7', '[grec]khi_maj':'j7', '[grec]psi_maj':'k7', '[grec]omega_maj':'l7', '[grec]esh_maj':'m7', ####################################################### Aide Grec maj 4/4 ###
                #### Min : ##################################################################################################################################################################################
                '[grec]alpha_min':'c8', '[grec]beta_min':'d8', '[grec]gamma_min':'e8', '[grec]delta_min':'f8', '[grec]epsilon_min':'g8', '[grec]zita_min':'h8','[grec]eta_min':'i8', ## Aide Grec min 1/4 ###
                '[grec]theta_min':'j8', '[grec]iota_min':'k8', '[grec]kappa_min':'l8', '[grec]lambda_min':'m8', '[grec]mi_min':'n8', '[grec]ni_min':'o8', '[grec]ksi_min':'p8', ####### Aide Grec min 2/4 ###
                '[grec]omicron_min':'q8', '[grec]pi_min':'c9', '[grec]ro_min':'d9', '[grec]sigma_min':'e9', '[grec]sigma_min':'f9', '[grec]tau_min':'g9', '[grec]upsilon_min':'h9', ### Aide Grec min 3/4 ###
                '[grec]phi_min':'i9', '[grec]khi_min':'j9', '[grec]psi_min':'k9', '[grec]omega_min':'l9', '[grec]esh_min':'m9', ####################################################### Aide Grec min 4/4 ###
                '[grec]esprit_doux':'n7', '[grec]esprit_rude':'n7', '[grec]iota_subscrit':'o7', '[grec]tilde':'o9', '[grec]esprit_doux_tilde':'n9', ######################### Aide Suplément Grec 1/2 #######
                '[grec]esprit_rude_tilde':'n9', ############################################################################################################################# Aide Suplément Grec 2/2 #######
                ## Spécial : ################################################################################################################################################################################
                ### Symboles : ################################################################################################################################################################################################
                '^':'a10', 'ˇ':'b10', '-':'c10', '–':'d10', '—':'e10', '_':'f10', '‾':'g10', '/':'h10', '\\':'i10', '|':'j10', '¦':'k10', '†':'l10', '‡':'m10', '=':'n10', '≠':'o10', '~':'p10', '*':'q10', ## Spécial 1/4 ####
                '̏' :'a11', '˝':'b11', '@':'c11', '&':'d11', '$':'e11', '€':'f11', '¥':'g11', '£':'h11', '\'':'i11', '"':'j11', '¬':'k11', '«':'l11', '»':'m11', '™':'n11', '®':'o11', '©':'p11', ' ':'q11', ## Spécial 2/4 ####
                '¨':'a12', '˙':'b12', '.':'c12', ',':'d12', ' ':'e12', ':':'f12', ';':'g12', '°':'h12', 'º':'i12', 'ª':'j12', '·':'k12', '%':'l12', '‰':'m12', '§':'n12', '¶':'o12', '♯':'p12', '♭':'q12', ### Spécial 3/4 ####
                ' ':'a13', '˜':'b13', 'ſ':'c13', 'ẞ':'d13', 'þ':'e13', 'Þ':'f13', 'ð':'g13', 'Ð':'h13', 'ŋ':'i13', 'Ŋ':'j13', 'ʒ':'k13', 'Ʒ':'l13', ' ':'m13', ' ':'n13', ' ':'o13', ' ':'p13', '�':'q13', ## Spécial 4/4 ####
                'ß':'', ############################################################################################################################################################################ Suplément Spécial 1/1 ####
                ### Noms : ####################################################################################################################################################################################################
                '[latin]accent_circomflexe':'a10', '[latin]accent_antiflexe':'b10', '[latin]tiret':'c10', '[latin]tiret_moyen':'d10', '[latin]tiret_long':'e10', '[latin]endscore':'f10', #################### Spécial 1/12 ###
                '[latin]topscore':'g10', '[latin]slash':'h10', '[latin]backslash':'i10', '[latin]barre':'j10', '[latin]broken_bar':'k10', '[latin]croix':'l10', '[latin]double_croix':'m10', ################# Spécial 2/12 ###
                '[latin]egal':'n10', '[latin]pas_egal':'o10', '[latin]approx':'p10', '[latin]asterisque':'q10', '[latin]accent_double_grave':'a11', '[latin]accent_double_aigu':'b11', ####################### Spécial 3/12 ###
                '[latin]arrobas':'c11', '[latin]esperluette':'d11', '[latin]dollar':'e11', '[latin]euro':'f11', '[latin]yen':'g11', '[latin]livre':'h11', '[latin]apostrophe':'i11', ######################### Spécial 4/12 ###
                '[latin]guillemets':'j11', '[latin]non':'k11', '[latin]guillemets_ouvrants':'l11', '[latin]guillemets_fermants':'m11', '[latin]tm':'n11', '[latin]registered_mark':'o11', #################### Spécial 5/12 ###
                '[latin]copyright':'p11', '[latin]copyleft':'q11', '[latin]trema':'a12', '[latin]point_suscrit':'b12', '[latin]point':'c12', '[latin]virgule':'d12', '[latin]virgule_retourne':'e12', ######## Spécial 6/12 ###
                '[latin]deux_points':'f12', '[latin]point_virgule':'g12', '[latin]degres':'h12', '[latin]o_':'i12', '[latin]a_':'j12', '[latin]point_median':'k12', '[latin]pour_cent':'l12', ################ Spécial 7/12 ###
                '[latin]pour_mille':'m12', '[latin]paragraphe':'n12', '[latin]capitulum':'o12', '[latin]chapitre':'o12', '[musique]diese':'p12', '[musique]bemol':'q12', ##################################### Spécial 8/12 ###
                '[latin]accent_rond_en_chef':'a13', '[latin]accent_tilde':'b13', '[latin]s_long':'c13', '[latin]eszett_maj':'d13', '[latin]thorn_min':'e13', '[latin]thorn_maj':'f13', ####################### Spécial 9/12 ###
                '[latin]eth_min':'g13', '[latin]eth_maj':'h13', '[latin]eng_min':'i13', '[latin]eng_maj':'j13', '[latin]ej_min':'k13', '[latin]ej_maj':'l13', '[programmation]cs':'m13', ##################### Spécial 10/12 ##
                '[programmation]csharp':'m13', '[programmation]c#':'m13', '[programmation]cpp':'n13', '[programmation]c_plus_plus':'n13',  '[programmation]py':'o13', '[programmation]python':'o13', ######### Spécial 11/12 ##
                '[programmation]html':'p13', '[latin]unicode_error':'q13', '[latin]eszet_min':'a18', '[latin]winn_maj':'a19', '[latin]winn_min':'a20', '[latin]yogh_maj':'a21', '[latin]yogh_min':'a22', ##### Spécial 12/12 ##
                ## Russe : ####################################################################################################################################################################################################
                ### Русский : #################################################################################################################################################################################################
                #### Maj : ####################################################################################################################################################################################################
                'А':'a14', 'Б':'b14', 'В':'c14', 'Г':'d14', 'Д':'e14', 'Е':'f14', 'Ё':'g14', 'Ж':'h14', 'З':'i14', 'И':'j14', 'Й':'k14', 'К':'l14', 'Л':'m14', 'М':'n14', 'Н':'o14', 'О':'p14', 'П':'q14', ## Russe maj 1/2 ###
                'Р':'a15', 'С':'b15', 'Т':'c15', 'У':'d15', 'Ф':'e15', 'Х':'f15', 'Ц':'g15', 'Ч':'h15', 'Ш':'i15', 'Щ':'j15', 'Ъ':'k15', 'Ы':'l15', 'Ь':'m15', 'Э':'n15', 'Ю':'o15', 'Я':'p15', ' ':'q15', ## Russe maj 2/2 ###
                #### Min : ####################################################################################################################################################################################################
                'а':'a16', 'б':'b16', 'в':'c16', 'г':'d16', 'д':'e16', 'е':'f16', 'ё':'g16', 'ж':'h16', 'з':'i16', 'и':'j16', 'й':'k16', 'к':'l16', 'л':'m16', 'м':'n16', 'н':'o16', 'о':'p16', 'п':'q16', ## Russe min 1/2 ###
                'р':'a17', 'с':'b17', 'т':'c17', 'у':'d17', 'ф':'e17', 'х':'f17', 'ц':'g17', 'ч':'h17', 'ш':'i17', 'щ':'j17', 'ъ':'k17', 'ы':'l17', 'ь':'m17', 'э':'n17', 'ю':'o17', 'я':'p17', ' ':'q17', ## Russe min 2/2 ###
                ### Russe : ###################################################################################################################################################################################################
                #### Maj : ####################################################################################################################################################################################################
                '[russe]a_maj':'a14', '[russe]b_maj':'b14', '[russe]v_maj':'c14', '[russe]g_maj':'d14', '[russe]d_maj':'e14', '[russe]ye_maj':'f14', '[russe]yo_maj':'g14', '[russe]j_maj':'h14', ########### Russe maj 1/5 ###
                '[russe]z_maj':'i14', '[russe]i_maj':'j14', '[russe]y_maj':'k14', '[russe]k_maj':'l14', '[russe]l_maj':'m14', '[russe]m_maj':'n14', '[russe]h_maj':'o14', '[russe]o_maj':'p14', ############# Russe maj 2/5 ###
                '[russe]p_maj':'q14', '[russe]r_maj':'a15', '[russe]c_maj':'b15', '[russe]t_maj':'c15', '[russe]u_maj':'d15', '[russe]f_maj':'e15', '[russe]x_maj':'f15', '[russe]ts_maj':'g15', ############ Russe maj 3/5 ###
                '[russe]tch_maj':'h15', '[russe]sh_maj':'i15', '[russe]sch_maj':'j15', '[russe]tvyordi_snak_maj':'k15', '[russe]wi_maj':'l15', '[russe]myejki_snak_maj':'m15', '[russe]e_maj':'n15', ######## Russe maj 4/5 ###
                '[russe]yu_maj':'o15', '[russe]yu_maj':'p15', ' ':'q15', #################################################################################################################################### Russe maj 5/5 ###
                #### Min : ####################################################################################################################################################################################################
                '[russe]a_min':'a16', '[russe]b_min':'b16', '[russe]v_min':'c16', '[russe]g_min':'d16', '[russe]d_min':'e16', '[russe]ye_min':'f16', '[russe]yo_min':'g16', '[russe]j_min':'h16', ########### Russe min 1/5 ###
                '[russe]z_min':'i16', '[russe]i_min':'j16', '[russe]y_min':'k16', '[russe]k_min':'l16', '[russe]l_min':'m16', '[russe]m_min':'n16', '[russe]h_min':'o16', '[russe]o_min':'p16', ############# Russe min 2/5 ###
                '[russe]p_min':'q16', '[russe]r_min':'a17', '[russe]c_min':'b17', '[russe]t_min':'c17', '[russe]u_min':'d17', '[russe]f_min':'e17', '[russe]x_min':'f17', '[russe]ts_min':'g17', ############ Russe min 3/5 ###
                '[russe]tch_min':'h17', '[russe]sh_min':'i17', '[russe]sch_min':'j17', '[russe]tvyordi_snak_min':'k17', '[russe]wi_min':'l17', '[russe]myejki_snak_min':'m17', '[russe]e_min':'n17', ######## Russe min 4/5 ###
                '[russe]yu_min':'o17', '[russe]yu_min':'p17', ' ':'q17',##################################################################################################################################### Russe min 2/2 ###
                ### Symboles : ################################################################################################################################################################################################
                'coeur_n':'a18', 'trefle_n':'b18', 'carreau_n':'c18', 'pique_n':'d18', 'pion_b':'e18', 'fou_b':'f18', 'cavalier_b':'g18', 'dame_b':'h18', 'roi_b':'i18', 'python_p':'j18', ################### Symboles 1/2 ###
                'cœur_n':'a18', 'coeurs_n':'a18', 'cœurs_n':'a18', 'trefles_n':'b18', 'carreaux_n':'c18', 'piques_n':'d18', ################################################################################## Symboles 2/2 ###
                ### Accents : #################################################################################################################################################################################################
                'à':'a9\\c4', 'á':'b9\\c4', 'â':'a10\\c4', 'ä':'b10\\c4', 'è':'a9\\g4', 'é':'b9\\g4', 'ê':'a1\\g40', 'ë':'b1\\g40', 'ì':'a9\\k4', 'í':'b9\\k4', 'î':'a1\\k40', 'ï':'b1\\k40', 'ò':'a9\\q4', ### Accents 1/4 ###
                'ó':'b9\\q4', 'ô':'a10\\q4', 'ö':'b10\\q4', 'ù':'a9\\h5', 'ú':'b9\\h5', 'û':'a10\\h5', 'ü':'b10\\h5', 'À':'a9\\c2', 'Á':'b9\\c2', 'Â':'a10\\c2', 'Ä':'b10\\c2', 'È':'a9\\g2', 'É':'b9\\g2', ### Accents 2/4 ###
                'Ê':'a10\\g2', 'Ë':'b10\\g2', 'Ì':'a9\\k2', 'Í':'b9\\k2', 'Î':'a10\\k2', 'Ï':'b10\\k2', 'Ò':'a9\\q2', 'Ó':'b9\\q2', 'Ô':'a10\\q2', 'Ö':'b10\\q2', 'Ù':'a9\\h3', 'Ú':'b9\\h3', 'Û':'a10\\h3', ## Accents 3/4 ###
                'Ü':'b10\\h3', ################################################################################################################################################################################ Accents 4/4 ###
                ###############################################################################################################################################################################################################
                '\n':'n', '\b':'v', '\t':'t', '\f':'f', '\v':'v', '\r':'r', '\a':'a', ' ':'b1' ## Charactères de format #######################################################################################################
                ###############################################################################################################################################################################################################
            }
            def texted(texte):
                try:
                    if texte[0] == '\b':
                        return(texte[1:len(texte)])
                except:
                    pass
                bsl = '\\'
                out = '\\'
                char = '\a' ## Le caractère qui précède le nom complet d'un caractère, c'est le même pour fermer ##
                ind = 0
                while ind < len(texte):
                    i = texte[ind]
                    if i == char:
                        char_name, ind = suivant(char, texte, ind)
                        out += f'{char_name}{bsl}'
                    else:
                        try:
                            out += f'{chaine.chars[i]}\\' ## Si reconnu ##
                        except:
                            out += 'q13\\' ## Si non : char non reconnu ##
                    ind += 1
                return(out)
            def __init__(self, texte, index=0):
                self.texte = chaine.texted(texte)
                self.index = index
            def __str__(self):
                return(self.texte)
            def __iter__(self):
                return(iterateur(self.texte))
            def suivant(self, jusque=1, out=False):
                if type(jusque) == float:
                    jusque = round(jusque, 0)
                if type(jusque) == int:
                    if jusque + self.index < len(self.texte):
                        self.index += jusque
                elif type(jusque) == str:
                    indexy = self.index + 1
                    out = ''
                    while self.texte[indexy] != jusque:
                        out += self.texte[indexy]
                        indexy += 1
                    self.index = indexy
                if out:
                    return(out)
            def va(self, ou, occurrence=0):
                if type(ou) == float:
                    ou = round(ou, 0)
                if type(ou) == int:
                    if ou >= 0 and ou < len(self.texte):
                        self.index = ou
                elif type(ou) == str:
                    choses = []
                    truc = 0
                    for i in self.texte:
                        if i == ou:
                            choses.append(truc)
                        truc += 1
                    if len(choses) == 0:
                        return(None)
                    elif len(choses) == 1:
                        return(choses[0])
                    else:
                        try:
                            return(choses[occurrence])
                        except:
                            return(choses[-1])
            def islower(self, quoi=[0, -1]):
                if self.texte[quoi[0] : quoi[1]].islower():
                    return(True)
                return(False)
            def isupper(self, quoi=[0, -1]):
                if self.texte[quoi[0] : quoi[1]].isupper():
                    return(True)
                return(False)
            def upper(self):
                self.texte = self.texte.upper()
            def lower(self):
                self.texte = self.texte.lower()
            def upper_char(self):
                if self.index == 0:
                    self.texte = f'{self.texte[0].upper()}{self.texte[1 : len(self.texte)]}'
                elif self.index == len(self.text) - 1:
                    self.texte = f'{self.texte[0 : len(self.texte) - 1]}{self.texte[-1].upper()}'
                else:
                    self.texte = f'{self.texte[0 : self.index]}{self.texte[self.index].upper()}{self.texte[self.index + 1 : len(self.texte)]}'
            def lower_char(self):
                if self.index == 0:
                    self.texte = f'{self.texte[0].lower()}{self.texte[1 : len(self.texte)]}'
                elif self.index == len(self.text) - 1:
                    self.texte = f'{self.texte[0 : len(self.texte) - 1]}{self.texte[-1].lower()}'
                else:
                    self.texte = f'{self.texte[0 : self.index]}{self.texte[self.index].lower()}{self.texte[self.index + 1 : len(self.texte)]}'
        class souris:
            x = 0
            y = 0
        class pt_img_cartee:
            pt = (960, 540)
    if oui: ########################### Imports ### ## Licences ######
        import cv2 ## Dessins, affichage... ####### ## Apache 2.0 ####
        import numpy as np ######### Arrays ####### ## BSD-3-Clause ##
        import math ######### Mathématiques ####### ## Builded-in ####
        import random as rd ### Aleatoireté ####### ## Builded-in ####
        import time ## Chronos, heure etc... ###### ## Builded-in ####
        from datetime import date, datetime ####### ## Builded-in ####
        import os ## Outils systeme ############### ## Builded-in ####
        import copy ## Duplie les [] et les {} #### ## Builded-in ####
    if oui: ############################ Format ###
        def suivant(ou, texte, ind=0):
            if type(ou) == int:
                out = ''
                while ind < ou:
                    out += texte[ind]
                    ind += 1
                return(out, ind)
            elif type(ou) == str:
                out = ''
                ind += 1
                while ind < len(texte):
                    if texte[ind] == ou:
                        break
                    out += texte[ind]
                    ind += 1
                return(out, ind)
        def majuscule(texte, quoi=0):
            if quoi == 0:
                texte = texte[0].upper() + texte[1 : len(texte)]
            elif quoi == len(texte) - 1:
                texte = texte[0 : 1] + texte[-1].upper()
            elif type(quoi) == str:
                out = ''
                for i in texte:
                    if i == quoi:
                        i = i.upper()
                    out += i
                return(out)
            elif type(quoi) == list or type(quoi) == tuple:
                texte = texte[0 : quoi[0]] + texte[quoi[0] : quoi[1]].upper() + texte[quoi[1] : len(texte)]
            else:
                try:
                    texte = texte[0 : quoi] + texte[quoi].upper() + texte[quoi + 1 : len(texte)]
                except:
                    return(texte)
            return(texte)
        def minuscule(texte, quoi=0):
            if quoi == 0:
                texte = texte[0].lower() + texte[1 : len(texte)]
            elif quoi == len(texte) - 1:
                texte = texte[0 : 1] + texte[-1].lower()
            elif type(quoi) == str:
                out = ''
                for i in texte:
                    if i == quoi:
                        i = i.lower()
                    out += i
                return(out)
            elif type(quoi) == list or type(quoi) == tuple:
                texte = texte[0 : quoi[0]] + texte[quoi[0] : quoi[1]].lower() + texte[quoi[1] : len(texte)]
            else:
                try:
                    texte = texte[0 : quoi] + texte[quoi].lower() + texte[quoi + 1 : len(texte)]
                except:
                    return(texte)
            return(texte)
        def ordre_alphabetique(texte):
            return(''.join(i for i in list(texte).sort))
    if oui: ####################### Temporalité ###
        def jour_semaine(jour):
            '''Transforme un nombre entre 0 et 6 en jour de\nla semaine et traduit les anglais en français.'''
            jour = jour.lower()
            if jour == 'monday':
                return('lundi')
            elif jour == 'tuesday':
                return('mardi')
            elif jour == 'wednesday':
                return('mercredi')
            elif jour == 'thursday':
                return('jeudi')
            elif jour == 'friday':
                return('vendredi')
            elif jour == 'saturday':
                return('samedi')
            elif jour == 'sunday':
                return('dimanche')
            elif jour == 0:
                return('lundi')
            elif jour == 1:
                return('mardi')
            elif jour == 2:
                return('mercredi')
            elif jour == 3:
                return('jeudi')
            elif jour == 4:
                return('vendredi')
            elif jour == 5:
                return('samedi')
            elif jour == 6:
                return('dimanche')
            else:
                return('fête')
        def mois(mois):
            mois = mois.lower()
            if mois == 'january':
                return('janvier')
            elif mois == 'february':
                return('février')
            elif mois == 'march':
                return('mars')
            elif mois == 'april':
                return('avril')
            elif mois == 'may':
                return('mai')
            elif mois == 'june':
                return('juin')
            elif mois == 'july':
                return('juillet')
            elif mois == 'august':
                return('août')
            elif mois == 'september':
                return('septembre')
            elif mois == 'october':
                return('octobre')
            elif mois == 'november':
                return('novembre')
            elif mois == 'december':
                return('décembre')
            else:
                return('\\mois\\')
        def aujourdhui(format='normal'):
            out = date.today()
            if format == 'court':
                out = out.strftime('%d/%m/%y')
            elif format == 'normal':
                out = out.strftime('%d/%m/%Y')
            elif format == 'long':
                out = out.strftime('%d %B %Y')
            elif format == 'complet':
                out = majuscule(jour_semaine(datetime.now().strftime('%A'))),  out.strftime('%d'),  mois(out.strftime('%B')),  out.strftime('%Y')
            return(out)
        def heure(format='%H:%M:%S'):
            return(datetime.now().strftime(format))
        def maintenant(formatDeLHeure='%H:%M:%S', formatDuJour='normal', link=' '):
            return(f'{heure(formatDeLHeure)}{link}{aujourdhui(formatDuJour)}')
    if oui: ############## Fonctions de calculs ###
        def coosEllipse(pt, rayons, an, angleEllipse=0):
            b, a = rayons
            a, b = abs(round(a)), abs(round(b))
            if a == b:
                return(coosCercle(pt, a, an))
            x, y = pt
            f1 = (x + racine_carree(pow(b, 2) - pow(a, 2)), y) if b > a else (x, y + racine_carree(pow(a, 2) - pow(b, 2)))
            f2 = (x - racine_carree(pow(b, 2) - pow(a, 2)), y) if b > a else (x, y - racine_carree(pow(a, 2) - pow(b, 2)))
            p = ellipsed(pt, rayons, an)
            angl = angleEntrePoints(pt, p)
            p = coosCercle(pt, dist(p, pt), angl + angleEllipse)
            return(p)
        def diff(a, b):
            return(abs(a - b))
        def nouvelle_couleur(hexadecimal, type='bgr'):
            match type:
                case 'rbg': r, b, g = int(hexadecimal[0:2], base=16), int(hexadecimal[2:4], base=16), int(hexadecimal[4:6], base=16)
                case 'rgb': r, g, b = int(hexadecimal[0:2], base=16), int(hexadecimal[2:4], base=16), int(hexadecimal[4:6], base=16)
                case 'grb': g, r, b = int(hexadecimal[0:2], base=16), int(hexadecimal[2:4], base=16), int(hexadecimal[4:6], base=16)
                case 'gbr': g, b, r = int(hexadecimal[0:2], base=16), int(hexadecimal[2:4], base=16), int(hexadecimal[4:6], base=16)
                case 'brg': b, r, g = int(hexadecimal[0:2], base=16), int(hexadecimal[2:4], base=16), int(hexadecimal[4:6], base=16)
                case 'bgr': b, g, r = int(hexadecimal[0:2], base=16), int(hexadecimal[2:4], base=16), int(hexadecimal[4:6], base=16)
                case _: raise ValueError('Unknown type of colour!')
            return([b, g, r])
        def ct_sg(pt1, pt2):
            '''
            Prend:
            ------
            :pt1: ``tuple (x, y)``\n
            :pt2: ``tuple (x, y)``\n
            Renvoie:
            --------
            ``ct``: ``tuple (x, y)``
            '''
            ct = (int((pt1[0] + pt2[0]) / 2), int((pt1[1] + pt2[1]) / 2))
            return(ct)
        def ct_cr(p1, p2, p3, p4):
            return(ct_sg(ct_sg(p1, p2), ct_sg(p3, p4)))
        def pt_sg(pt1, pt2, mult1=1, mult2=1):
            '''
            Prend:
            ------
            :pt1: ``tuple (x, y)``\n
            :pt2: ``tuple (x, y)``\n
            :mult1: ``float`` or ``int``\n
            :mult2: ``float`` or ``int``\n
            Renvoie:
            --------
            ``ct``: ``tuple (x, y)``
            '''
            total = mult1 + mult2
            if total == 0:
                return((0, 0))
            pt = (int((pt1[0] * mult1 + pt2[0] * mult2) / total), int((pt1[1] * mult1 + pt2[1] * mult2) / total))
            return(pt)
        def str_long_de(num: int):
            '''
            Prend:
            ------
            :num: ``int``\n
            Renvoie:
            --------
            ``str`` de len() spécifiée
            '''
            if num > 0:
                out = 'a'*round(num)
            else:
                out = ''
            return(out)
        def points_segment(p1, p2):
            '''
            Prend:
            ------
            :p1: ``tuple`` ou ``list`` (x, y)\n
            :p2: ``tuple``  ou ``list`` (x, y)\n
            Renvoie:
            --------
            ``list`` de ``tuple`` (x, y)
            '''
            xa, ya = p1
            xb, yb = p2
            '''xa, ya = int(xa), int(ya)
            xb, yb = int(xb), int(yb)'''
            if xa == xb:
                dif = ya - yb
                numbs = range(abs(dif))
                out = []
                if dif < 0:
                    for i in numbs:
                        out.append([xa, yb - i])
                else:
                    for i in numbs:
                        out.append([xa, yb + i])
            else:
                xc = np.linspace(xa, xb, max(abs(xa - xb), abs(ya - yb)))
                yc = (yb - ya) / (xb - xa) * (xc - xa) + ya
                yc = [round(c) for c in yc]
                pos = 0
                out = []
                for i in xc:
                    out.append([int(xc[pos]), int(yc[pos])])
                    pos += 1
            return(out)
        def decoupe(string):
            '''
            Prend:
            ------
            :nombre: ``complex`` ou ``str(complex)``\n
            Renvoie:
            --------
            ``float``
            '''
            out = ''
            string = str(string)
            for i in string:
                if  i == '(':
                    pass
                elif i == ')':
                    pass
                elif i == 'j':
                    break
                else:
                    out += i
            return(float(out))
        def dist(p1, p2):
            a, b = p1
            c, d = p2
            diffX = abs(a - c)
            diffY = abs(b - d)
            dist = math.sqrt((diffX * diffX) + (diffY * diffY))
            dist = float(decoupe(dist))
            return(dist)
        def angleEntrePoints(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            diffX = x1 - x2
            diffY = y1 - y2
            rotation = math.degrees(math.atan2(diffY, diffX))
            return(rotation+180)
        def coosCercle(ct, rayon, angle):
            '''
            Prend:
            ------
            :ct: ``tuple (x, y)``\n
            :rayon: ``int``\n
            :angle: ``int``\n\tInclinaison du cercle par rapport à son centre.\n
            Renvoie:
            --------
            ``tuple (x, y)``\n\tPosition du cercle à l\'angle précisé.
            '''
            angle = math.radians(angle)
            cos = float(decoupe(str(math.cos(angle))))
            sin = float(decoupe(str(math.sin(angle))))
            return([int(ct[0] + cos * rayon), int(ct[1] + sin * rayon)])
        def moyenne(elementA, elementB, mult_elementA=1, mult_elementB=1, return_type='int'):
            '''
            Fait la moyennes entre les elements
            Prend:
            ------
            :elementA: ``float`` / ``int``
            :elementB: ``float`` / ``int``
            :return_type: ``str``\n
            :mult_elementA: ``float`` / ``int``
            :mult_elementB: ``float`` / ``int``
            Renvoie:
            --------
            ``float``
            '''
            total_elements = mult_elementA + mult_elementB
            moyenne = ((elementA * mult_elementA) + (elementB * mult_elementB)) / total_elements
            if return_type != 'float':
                moyenne = int(moyenne)
            return(moyenne)
        def point_x_parabole(a, b, c, p, x):
            sd_x = x
            b = 0-b
            pt = pt_img_cartee.pt
            xct = round(pt[0])
            x = -xct - 10
            yct = round(pt[1])
            save = []
            while x <= xct:
                save.append([x + xct, yct - (a * (x ** p) + b * x + c)])
                if save[-1][0] == sd_x:
                    return(save[-1])
                x += 1
            print(f'The <x> parameter :{x}: never crosses the parabola:\n\ty = {a}·{x}^2 + {b}·{x} + {c}')
            raise ValueError
        def racine_carree(n):
            return(float(decoupe(math.sqrt(n))))
        def equation_2eme_degre(a, b, c):
            try:
                y1 = (-b + racine_carree(b**2 - 4*a*c)) / (2*a)
            except:
                y1 = 'r'
            try:
                y2 = (-b - racine_carree(b**2 - 4*a*c)) / (2*a)
            except:
                y2 = 'r'
            if y1 == 'r' and y2 == 'r':
                return(None)
            elif y1 == 'r':
                return(y2)
            elif y2 == 'r':
                return(y1)
            else:
                return(y1, y2)
        def oppose(n):
            return(0 - n)
    if oui: ### Fonctions de valeurs par défaut ###
        def chars(tailleChar=1):
            longChar = int(75 * tailleChar)
            hautChar = int(longChar / 3 * 4.5)
            return(longChar, hautChar)
        def coos(haut_image=1080, long_image=1920):
            haut = haut_image
            long = long_image
            dd = (0, haut)
            deb = (int((long - haut) / 2), 0)
            fin = (deb[0] + haut, haut)
            ff = (long, 0)
            x = int(long / 2)
            y = int(haut / 2)
            ct = (x, y)
            p1 = deb
            p2 = (fin[0], p1[1])
            p3 = (p1[0], fin[1])
            p4 = fin
            ch = ct_sg(p1, p2)
            cb = ct_sg(p3, p4)
            cg = ct_sg(p1, p3)
            cd = ct_sg(p2, p4)
            c1 = ct_sg(p1, ct)
            c2 = ct_sg(p2, ct)
            c3 = ct_sg(p3, ct)
            c4 = ct_sg(p4, ct)
            cth = ct_sg(ct, ch)
            ctb = ct_sg(ct, cb)
            ctg = ct_sg(ct, cg)
            ctd = ct_sg(ct, cd)
            ct1 = ct_sg(ct, p1)
            ct2 = ct_sg(ct, p2)
            ct3 = ct_sg(ct, p3)
            ct4 = ct_sg(ct, p4)
            return(haut, long, dd, deb, fin, ff, x, y, ct, p1, p2, p3, p4, ch, cb, cg, cd, c1, c2, c3, c4, cth, ctb, ctg, ctd, ct1, ct2, ct3, ct4)
        def par_defaut(couleur=(0, 0, 0), epaisseur=9, rayon=300, sagitta=25):
            plein = -1
            rotation = 0
            return(couleur, epaisseur, rayon, plein, rotation, sagitta)
        def proprietes_fenetre():
            return(cv2.WND_PROP_FULLSCREEN)
        def valeurs_fenetre():
            return(cv2.WINDOW_FULLSCREEN)
        def coos_a(p1, p2, p3, p4):
            ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
            ch = ct_sg(p1, p2)
            cb = ct_sg(p3, p4)
            cg = ct_sg(p1, p3)
            cd = ct_sg(p2, p4)
            c1 = ct_sg(p1, ct)
            c2 = ct_sg(p2, ct)
            c3 = ct_sg(p3, ct)
            c4 = ct_sg(p4, ct)
            cth = ct_sg(ct, ch)
            ctb = ct_sg(ct, cb)
            ctg = ct_sg(ct, cg)
            ctd = ct_sg(ct, cd)
            ct1 = ct_sg(ct, p1)
            ct2 = ct_sg(ct, p2)
            ct3 = ct_sg(ct, p3)
            ct4 = ct_sg(ct, p4)
            return(haut, long, dd, deb, fin, ff, x, y, ct, p1, p2, p3, p4, ch, cb, cg, cd, c1, c2, c3, c4, cth, ctb, ctg, ctd, ct1, ct2, ct3, ct4)
    if oui: ############## Variables par défaut ###
        if oui: ## Couleurs ##
            ## Blanc et noir ##
            noir = (0, 0, 0)
            blanc = (255, 255, 255)
            ## Couleurs primaires ##
            rouge = (0, 0, 255)
            bleu = (255, 0, 0)
            vert = (0, 255, 0)
            ## Couleurs secondaires ##
            jaune = (0, 255, 255)
            cyan = (255, 255, 0)
            magenta = (255, 0, 255)
            ## Autres couleurs ##
            turquoise = (255//2, 255//2, 0)
            bois = (80, 150, 190)
        if oui: ## Noms des touches ##
            tabulationKey, newLineKey, returnLineKey, spaceBarKey, exclamationMarkKey, doubleQuotesKey = '\t', '\n', '\r', ' ', '!', '"'
            hashTagKey, dollarSignKey, perCentKey, esperluetteKey, singleQuoteKey, openingParentesisKey = '#', '$', '%', '&', "'", '('
            ClosingParentesisKey, asteriskKey, plusSignKey, comaKey, minusSignKey, dotKey, slashKey, zeroKey = ')', '*', '+', ',', '-', '.', '/', '0'
            oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, colonKey = '1', '2', '3', '4', '5', '6', '7', '8', '9', ':'
            semiColonKey, lessThanSignKey, equalSignKey, GreaterSignKey, interrogationMarkKey, atSignKey = ';', '<', '=', '>', '?', '@'
            openingBracketsKey, backSlashKey, closingBracketsKey, circumflexKey, underScoreKey, graveAccentKey = '[', '\\', ']', '^', '_', '`'
            aKey, bKey, cKey, dKey, eKey, fKey, gKey, hKey, iKey, jKey, kKey, lKey, mKey, nKey = 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
            oKey, pKey, qKey, rKey, sKey, tKey, uKey, vKey, wKey, xKey, yKey, zKey, openingBracesKey = 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{'
            verticalBarKey, closingBracesKey, medianTildeKey, acceptKey, addKey, altKey, lefAltKey, rightAltCase = '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright'
            appsKey, backSpaceKey, broserBackKey, browserFavoritesKey, browserForwardKey = 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward'
            browserHomeKey, browserRefreshKey, browserSearchKey, brouserStopKey, capsLockKey = 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock'
            clearKey, convertKey, ctrlKey, leftCtrlKey, rightCtrlKey, decimalKey, delKey = 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del'
            deleteKey, divideKey, downKey, endKey, enterKey, escKey, escapeKey, executeKey, f1Key = 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1'
            f10Key, f11Key, f12Key, f13Key, f14Key, f15Key, f16Key, f17Key, f18Key, f19Key, f2Key = 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2'
            f20Key, f21Key, f22Key, f23Key, f24Key, f3Key, f4Key, f5Key, f6Key, f7Key, f8Key, f9Key = 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9'
            finalKey, fnKey, hanguelKey, hangulKey, hanjaKey, helpKey, homeKey, insertKey = 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert'
            junjaKey, kanaKey, kanjiKey, launchApp1Key, launchApp2Key, launchMailKey = 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail'
            launchMediadiaSelectKey, leftKey, changeModeKey, multiplyKey, nextTrackKey = 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 
            nonConvertKey, num0Key, num1Key, num2Key, num3Key, num4Key, num5Key, num6Key, num7Key = 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7'
            num8Key, num9Key, numLockKey, pageDownKey, pageUpKey, pauseKey, pgdnKey, pgupKey = 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup'
            playPauseKey, previousTrackKey, printKey, printScreenKey, prntscrnKey, prtscKey = 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc'
            prtscrKey, returnKey, rightKey, lockScrollKey, selectKey, separatorKey, shiftKey = 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift'
            leftShiftKey, rightShiftKey, sleepKey, spaceKey, stopKey, subtractKey, tabKey, upKey = 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up'
            volumeDownKey, molumeMuteKey, volumeUpKey, winKey, leftWinKey, rightWinKey, yenKey = 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen'
            commandKey, optionKey, leftOptionKey, rightOptionKey = 'command', 'option', 'optionleft', 'optionright'
        if oui: ## Coos et valeurs par défaut ##
            longChar, hautChar = chars(1)
            haut, long, dd, deb, fin, ff, x, y, ct, p1, p2, p3, p4, ch, cb, cg, cd, c1, c2, c3, c4, cth, ctb, ctg, ctd, ct1, ct2, ct3, ct4 = coos()
            pt_img_cartee.pt = (long//2, haut//2)
            cth = ct_sg(ct, ch)
            ctb = ct_sg(ct, cb)
            couleur, epaisseur, rayon, plein, rotation, sagitta = par_defaut()
            prop_plein_ecran = proprietes_fenetre()
            vale_plein_ecran = valeurs_fenetre()
            taille, espacement = 1, 1
            souligne, surligne, combine = 'None', 'None', False
            police = 'basique'
            help = False
            hg = (0, 0)
            hd = (long, 0)
            bg = (0, haut)
            bd = (long, haut)
    if oui: ######################## Ordinateur ###
        def relocate_img():
            return([0, 0])
            Get_ecrans.reconnais_ecrans()
            pas_bougee = [0, 0]
            with open('./dependances/ecrans_reconnus.txt', 'r') as file:
                txt = file.read()
            ecrans = txt.split('\n')
            if len(ecrans) <= 1: return(pas_bougee)
            for i in ecrans:
                if i == 'ThinkVision T22v-20':
                    return(pas_bougee) #([0, -1080])
            return(pas_bougee)
        relocaliser_l_image = relocate_img()
    if oui: ############################ Formes ###
        def lune(img, pt=ct, taille=1, couleur=[0, 200, 255], couleur2=[0, 128, 255], rot=0):
            for i in range(1, int(taille*40)):
                ellipse(img, pt, i, [200, 200, 200], 2, 90-i, 270+i)
            return(img)
        def soleil(img, pt=ct, taille=1, couleur=[0, 200, 255], couleur2=[0, 128, 255], rot=0):
            cercle(img, pt, 50*taille, couleur, 0)
            for i in range(0, 360, 36):
                i += rot
                a, b = coosCercle(pt, 75, i), coosCercle(pt, 150, i)
                ligne(img, a, b, couleur2, epaisseur*taille)
            return(img)
        def nuage(img, pto=cth, taille=1, couleur=blanc, bord=3, couleur2=[30, 30, 30]):
            pt = pto
            a = 200*taille+bord
            ellipse(img, pt, (taille*a, taille*a/2.4), couleur2, 0)
            for i in [0, 0, 160, 170, 190, 210, -20, -10, 10, 30]:
                pt = coosCercle(pt, taille*100, i)
                a = 120*taille+bord
                ellipse(img, pt, (taille*a, taille*a/2.4), couleur2, 0)
            pt = pto
            a = 200*taille
            ellipse(img, pt, (taille*a, taille*a/2.4), couleur, 0)
            for i in [0, 0, 160, 170, 190, 210, -20, -10, 10, 30]:
                pt = coosCercle(pt, taille*100, i)
                a = 120*taille
                ellipse(img, pt, (taille*a, taille*a/2.4), couleur, 0)
            return(img)
        def montagnette(img, ct=ct, t=1, o=0):
            o -= 90
            triangle(img, coosCercle(ct, 60*t, 0+o), coosCercle(ct, 50*t, 120+o), coosCercle(ct, 50*t, 240+o), nouvelle_couleur('809d9d'), 0)
            triangle(img, coosCercle(ct, 60*t, 0+o), coosCercle(ct, 50*t, 120+o), coosCercle(ct, 50*t, 240+o), noir, 3)
            return(img)
        def maison(img, ct=ct, t=1, o=0, cl=nouvelle_couleur('506d6d'), cl2=nouvelle_couleur('405050'), clp=bois):
            o -= 90
            phd = coosCercle(ct, 50*t, o+45)
            phg = coosCercle(ct, 50*t, o-45)
            pbd = coosCercle(ct, 50*t, o+135)
            pbg = coosCercle(ct, 50*t, o+225)
            pbcg = pt_sg(pbg, pbd, 7, 4)
            rectangle(img, phg, pbd, cl, 0)
            rectangle(img, phg, pbd, noir, 3)
            triangle(img, phg, phd, coosCercle(ct_sg(phg, phd), 60*t, o), cl2, 0)
            triangle(img, phg, phd, coosCercle(ct_sg(phg, phd), 60*t, o), noir, 3)
            rectangle(img, pbcg, pt_sg(pbg, phd, 4, 7), clp, 0)
            rectangle(img, pbcg, pt_sg(pbg, phd, 4, 7), noir, 3)
            return(img)
        def perso(img, ctt=ct, t=1, o=0, clt=blanc, clv=blanc):
            h, w = 20*t, 10*t
            ct = coosCercle(ctt, 25*t, 90+o)
            pttb = coosCercle(ctt, round(w/3), 90)
            cg, cd = coosCercle(ct, w, 180+0), coosCercle(ct, w, 0+o)
            ellipse(img, ct, (w, h), clv, 0, 180, angle=o)
            ellipse(img, ct, (w, h), noir, 2, 180, angle=o)
            ligne(img, coosCercle(ct, w, 180+o), coosCercle(ct, w, 0+o), noir, 2)
            triangle(img, cg, ct, coosCercle(ct_sg(cg, ct), h, 90+o), clv, 0)
            triangle(img, cg, ct, coosCercle(ct_sg(cg, ct), h, 90+o), noir, 2)
            triangle(img, cd, ct, coosCercle(ct_sg(cd, ct), h, 90+o), clv, 0)
            triangle(img, cd, ct, coosCercle(ct_sg(cd, ct), h, 90+o), noir, 2)
            cercle(img, coosCercle(ct_sg(cd, ct), h, 90+o), 3*t, noir, 0, 180)
            cercle(img, coosCercle(ct_sg(cg, ct), h, 90+o), 3*t, noir, 0, 180)
            cercle(img, ctt, round(w/4*3), clt, 0)
            cercle(img, ctt, round(w/4*3), noir, 2)
            cercle(img, coosCercle(ctt, round(w/3), -30), t, noir, 0)
            cercle(img, coosCercle(ctt, round(w/3), -150), t, noir, 0)
            arc(img, coosCercle(pttb, t*3, 0), coosCercle(pttb, t*3, 180), t, noir, 1)
            return(img)
        def polygone_regulier(img, ct=ct, n_cotes=5, rayon_vertex=rayon, couleur=noir, epaisseur=epaisseur, rotation=0):
            '''
            Dessin d'un polygone regulier avec autant de vertex que ``n_cotes``.\n
            Prend:
            ------
            :img: ``np.array``\n
            :ct: ``tuple (x, y)``\n
            :n_cotes: ``int``\n
            :rayon_vertex: ``int``\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            :rotation: ``int``\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            n_cotes, rayon_vertex, epaisseur = int(n_cotes), int(rayon_vertex), int(epaisseur)
            save, ct = ct, []
            for i in save:
                ct.append(int(i))
            rotation += 360 / (n_cotes * 2)
            if n_cotes > 100:
                n_cotes = 100
            points = []
            for i in range(n_cotes):
                rot = (360 / n_cotes) * i + rotation
                points.append(coosCercle(ct, rayon_vertex, rot))
            if epaisseur < 0:
                epaisseur = abs(epaisseur)
                plein = True
            elif epaisseur == 0:
                epaisseur = 10
                plein = True
            else:
                plein = False
            a = points[0]
            points.append(a)
            for i in points:
                ligne(img, a, i, couleur, epaisseur)
                a = i
            if plein:
                pts = []
                a = points[0]
                for i in points:
                    pts.append(points_segment(a, i))
                    a = i
                truc = 0
                for i in pts:
                    for j in i:
                        cv2.line(img, ct, j, couleur, epaisseur)
                        truc += 1
            return(img)
        def cercle(img, ct=ct, rayon=rayon, couleur=noir, epaisseur=epaisseur, angleDebut=0, angleFin=360, angle=0):
            '''
            Cercle dont le centre et ``ct``, et le rayon est de la longueur``rayon``\n\n
            Prend:
            ------
            :img: ``np.array``\n
            :ct: ``tuple (x, y)``\n
            :rayon: ``int``\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            :angleDebut: ``int``\n\tOù comence le cercle\n\t90º c'est vers le haut.\n
            :angleFin: ``int``\nOù se termine le cercle.\n
            :angle: ``int``\n\tInclinaison du cercle par rapport à son centre.\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            save, ct = ct, []
            for i in save:
                ct.append(int(i))
            rayon, epaisseur = abs(int(rayon)), int(epaisseur)
            if epaisseur <= 0:
                try:
                    cv2.ellipse(img, ct, (rayon, rayon), angle, angleDebut, angleFin, couleur, abs(epaisseur))
                except:
                    pass
                epaisseur = -1
            cv2.ellipse(img, ct, (rayon, rayon), angle, angleDebut, angleFin, couleur, epaisseur)
            return(img)
        def ellipse(img, ct=ct, rayons=(rayon, rayon//2), couleur=noir, epaisseur=epaisseur, angleDebut=0, angleFin=360, angle=0):
            '''
            Fait une ellipse.
            Prend:
            ------
            :img: ``np.array``\n
            :ct: ``tuple (x, y)``\n
            :rayons: ``tuple (int)``\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            :angleDebut: ``int``\n\tOù comence l\'ellipse\n\t90º c'est vers le haut.\n
            :angleFin: ``int``\nOù se termine l\'ellipse.\n
            :angle: ``int``\n\tInclinaison du cercle par rapport à son centre.\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            if type(rayons) == int:
                rayons = [rayons, rayons]
            save, ct = ct, []
            for i in save:
                ct.append(int(i))
            rayons, a = [], rayons
            for i in a:
                rayons.append(int(i))
            epaisseur = int(epaisseur)
            if epaisseur <= 0:
                try:
                    cv2.ellipse(img, ct, rayons, angle, angleDebut, angleFin, couleur, abs(epaisseur))
                except:
                    pass
                epaisseur = -1
            cv2.ellipse(img, ct, rayons, angle, angleDebut, angleFin, couleur, epaisseur)
            return(img)
        def ellipse_points(img, p1=p1, p2=p2, rayon=25, couleur=noir, epaisseur=epaisseur, angleDebut=0, angleFin=180):
            '''
            Prend:
            ------
            :img: ``np.array``\n
            :p1: ``tuple (x, y)``\n
            :p2: ``tuple (x, y)``\n
            :rayon: ``int``\n\tSéparation de la ligne au segment p1-p2.\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            :angleDebut: ``int``\n\tOù comence l\'ellipse\n\t90º c'est vers le haut.\n
            :angleFin: ``int``\nOù se termine l\'ellipse.\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            rayon, epaisseur = int(rayon), int(epaisseur)
            rotation = angleEntrePoints(p1, p2)
            if rayon < 0:
                rayon = abs(rayon)
            elif rayon == 0:
                if epaisseur == 0:
                    epaisseur = -1
                else:
                    abs(epaisseur)
                cv2.line(img, p1, p2, couleur, epaisseur)
                return(img)
            if epaisseur <= 0:
                try:
                    cv2.ellipse(img, ct_sg(p1, p2), (dist(p1, p2) // 2, rayon), int(rotation), angleDebut, angleFin, couleur, abs(epaisseur))
                except:
                    pass
                epaisseur = -1
            cv2.ellipse(img, ct_sg(p1, p2), (dist(p1, p2) // 2, rayon), int(rotation), angleDebut, angleFin, couleur, epaisseur)
            return(img)
        def cercle_point(img, ct=ct, p1=p1, couleur=noir, epaisseur=epaisseur, angleDebut=0, angleFin=360, angle=0):
            '''
            Cercle dont le centre et ``ct``, et le contour passe par ``p1``\n\n
            Prend:
            ------
            :img: ``np.array``\n
            :ct: ``tuple (x, y)``\n
            :p1: ``tuple (x, y)``\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            :angleDebut: ``int``\n\tOù comence le cercle\n\t90º c'est vers le haut.\n
            :angleFin: ``int``\nOù se termine le cercle.\n
            :angle: ``int``\n\tInclinaison du cercle par rapport à son centre.\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            save, ct = ct, []
            for i in save:
                ct.append(abs(int(i)))
            save, p1 = p1, []
            for i in save:
                p1.append(abs(int(i)))
            rayon = dist(p1, ct)
            rayon, epaisseur = int(rayon), int(epaisseur)
            if epaisseur <= 0:
                try:
                    cv2.ellipse(img, ct, (rayon, rayon), angle-90, angleDebut, angleFin, couleur, abs(epaisseur))
                except:
                    pass
                epaisseur = -1
            cv2.ellipse(img, ct, (rayon, rayon), angle-90, angleDebut, angleFin, couleur, epaisseur)
            return(img)
        def cercle_points(img, p1=p1, p2=p2, couleur=noir, epaisseur=epaisseur, angleDebut=0, angleFin=360, angle=0):
            '''
            Fait un cercle qui est de la longueur pile du ``p1`` au ``p2``.\n
            Prend:
            ------
            :img: ``np.array``\n
            :p1: ``tuple (x, y)``\n
            :p2: ``tuple (x, y)``\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            :angleDebut: ``int``\n\tOù comence le cercle\n\t90º c'est vers le haut.\n
            :angleFin: ``int``\nOù se termine le cercle.\n
            :angle: ``int``\n\tInclinaison du cercle par rapport à son centre.\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            ct = (abs(int(moyenne(p1[0], p2[0]))), abs(int(moyenne(p1[1], p2[1]))))
            rayon = int(dist(p1, p2) / 2)
            rayon, epaisseur = int(rayon), int(epaisseur)
            if epaisseur <= 0:
                try:
                    cv2.ellipse(img, ct, (rayon, rayon), angle-90, angleDebut, angleFin, couleur, abs(epaisseur))
                except:
                    pass
                epaisseur = -1
            cv2.ellipse(img, ct, (rayon, rayon), angle-90, angleDebut, angleFin, couleur, epaisseur)
            return(img)
        def cercle_points_dist(img, pts, rayon=rayon, couleur=noir, epaisseur=epaisseur, angleDebut=0, angleFin=360, angle=0):
            '''
            Se au centre des points de ``pts`` et dessine un cercle de rayon ``rayon``.\n
            Prend:
            ------
            :img: ``np.array``\n
            :ct: ``tuple (x, y)``\n
            :pts: ``tuple`` / ``list`` de coos -> ``((x, y), (x, y), ···)``\n
            :rayon: ``int``\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            :angleDebut: ``int``\n\tOù comence le cercle\n\t90º c'est vers le haut.\n
            :angleFin: ``int``\nOù se termine le cercle.\n
            :angle: ``int``\n\tInclinaison du cercle par rapport à son centre.\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            rayon, epaisseur = int(rayon), int(epaisseur)
            n_coos = 0
            xy = 0
            yy = 0
            for i in pts:
                xy += i[0]
                yy += i[1]
                n_coos += 1
            ct = (int(xy / n_coos), int(yy / n_coos))
            cercle(img, ct, rayon, couleur, epaisseur, angleDebut, angleFin, angle)
            return(img)
        def arc(img, p1=p1, p2=p2, sagitta=25, couleur=noir, epaisseur=epaisseur):
            '''
            Prend:
            ------
            :img: ``np.array``\n
            :p1: ``tuple (x, y)``\n
            :p2: ``tuple (x, y)``\n
            :sagitta: ``int``\n\tSéparation de la ligne au segment p1-p2.\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            sagitta, epaisseur = round(sagitta), round(epaisseur)
            if epaisseur == 0:
                epaisseur = -1
            rotation = angleEntrePoints(p1, p2)
            if sagitta < 0:
                sagitta = abs(sagitta)
            elif sagitta == 0:
                abs(epaisseur)
                cv2.line(img, p1, p2, couleur, epaisseur)
                return(img)
            if epaisseur < 0:
                try:
                    cv2.ellipse(img, ct_sg(p1, p2), (round(dist(p1, p2)/2), sagitta), rotation, 180, 360, couleur, abs(epaisseur))
                except:
                    pass
                epaisseur = -1
            cv2.ellipse(img, ct_sg(p1, p2), (round(dist(p1, p2)/2), sagitta), rotation, 180, 360, couleur, epaisseur)
            return(img)
        def arc_dist(img, p1=ct, dist=25, sagitta=25, couleur=noir, epaisseur=epaisseur):
            '''
            Prend:
            ------
            :img: ``np.array``\n
            :p1: ``tuple (x, y)``\n
            :dist: ``tuple (+x, +y)``\n
            :sagitta: ``int``\n\tSéparation de la ligne au segment p1-p2.\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            sagitta, epaisseur = int(sagitta), int(epaisseur)
            p2 = (p1[0] + dist, p1[1] + dist)
            arc(img, p1, p2, sagitta, couleur, epaisseur)
            return(img)
        def arc_dists(img, p1=ct, dists=[25, 25], sagitta=25, couleur=noir, epaisseur=epaisseur):
            '''
            Prend:
            ------
            :img: ``np.array``\n
            :p1: ``tuple (x, y)``\n
            :dist: ``tuple (+x, +y)``\n
            :sagitta: ``int``\n\tSéparation de la ligne au segment p1-p2.\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            sagitta, epaisseur = int(sagitta), int(epaisseur)
            p2 = (p1[0] + dists[0], p1[1] + dists[1])
            arc(img, p1, p2, sagitta, couleur, epaisseur)
            return(img)
        def ligne(img, p1=p1, p2=p2, couleur=noir, epaisseur=epaisseur):
            '''
            Prend:
            ------
            :img: ``liste``\n
            :p1: ``tuple (x, y)``\n
            :p2: ``tuple (x, y)``\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            save, save2, p1, p2 = p1, p2, [], []
            for i in save:
                p1.append(int(i))
            for i in save2:
                p2.append(int(i))
            epaisseur = int(epaisseur)
            if epaisseur <= 0:
                epaisseur = 1
            cv2.line(img, p1, p2, couleur, epaisseur)
            return(img)
        def ligne_dist(img, p1=ct, dist=rayon, couleur=noir, epaisseur=epaisseur, rotation=0):
            '''
            Prend:
            ------
            :img: ``liste``\n
            :p1: ``tuple (x, y)``\n
            :dist: ``tuple`` (+x, +y)\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            dist, epaisseur = int(dist), abs(int(epaisseur))
            p2 = coosCercle(p1, dist, rotation)
            save, save2, p1, p2 = p1, p2, [], []
            for i in save:
                p1.append(int(i))
            for i in save2:
                p2.append(int(i))
            epaisseur = int(epaisseur)
            if epaisseur <= 0:
                epaisseur = 1
            cv2.line(img, p1, p2, couleur, epaisseur)
            return(img)
        def rectangle(img, pt1=c1, pt2=c2, couleur=noir, epaisseur=epaisseur, rotation=0, help=False):
            '''
            Prend:
            ------
            :img: ``np.array``\n
            :p1: ``tuple (x, y)``\n
            :p2: ``tuple (x, y)``\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            :rotation: ``int``\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            save, save2, pt1, pt2 = pt1, pt2, [], []
            for i in save: pt1.append(int(i))
            for i in save2: pt2.append(int(i))
            epaisseur = int(epaisseur)
            if rotation == 0:
                if epaisseur < 0:
                    cv2.rectangle(img, pt1, pt2, couleur, abs(epaisseur))
                    epaisseur = -1
                elif epaisseur == 0:
                    epaisseur = -1
                cv2.rectangle(img, pt1, pt2, couleur, epaisseur)
                return(img)
            if epaisseur < 0:
                epaisseur = abs(epaisseur)
                plein = True
            elif epaisseur == 0:
                epaisseur = 10
                plein = True
            else:
                plein = False
            if oui: ## Coos ##
                x = pt2[0] - pt1[0]
                y = pt2[1] - pt1[1]
                p1 = pt1
                p2 = coosCercle(p1, y, rotation)
                p3 = coosCercle(p1, x, rotation + 90)
                p4 = coosCercle(p3, y, rotation)
            if oui: ## Côtés ##
                cv2.line(img, p1, p2, couleur, epaisseur)
                cv2.line(img, p1, p3, couleur, epaisseur)
                cv2.line(img, p2, p4, couleur, epaisseur)
                cv2.line(img, p3, p4, couleur, epaisseur)
            if plein:
                ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
                points = [points_segment(p1, p2), points_segment(p1, p3), points_segment(p2, p4), points_segment(p3, p4)]
                for i in points:
                    for j in i:
                        cv2.line(img, j, ct, couleur, epaisseur + 2)
            if help:
                cercle(img, pt1, 10, turquoise, 0)
                cercle(img, pt2, 10, turquoise, 0)
            return(img)
        def carreau(img, p1=ct_sg(ct, ch), dists=(100, 200), couleur=vert, epaisseur=epaisseur, rotation=0, help=False):
            '''
            Dessin d'un rectangle à partir d'un point et une distance.\n
            Prend:
            ------
            :img: ``np.array``\n
            :p1: ``tuple (x, y)``\n
            :dist: ``tuple`` (+x, +y)\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            :rotation: ``int``\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            save, p1 = p1, []
            for i in save:
                p1.append(int(i))
            epaisseur = int(epaisseur)
            dists, a = [], dists
            for i in a:
                dists.append(int(i))
            epaisseur = int(epaisseur)
            rotation += 180
            if epaisseur < 0:
                epaisseur = abs(epaisseur)
                plein = True
            elif epaisseur == 0:
                epaisseur = 10
                plein = True
            else:
                plein = False
            if oui: ## Coos ##
                p2 = coosCercle(p1, dists[0], rotation + 180)
                ct = ct_sg(p1, p2)
                p3 = coosCercle(ct, dists[1] // 2, rotation + 90)
                p4 = coosCercle(ct, dists[1] // 2, rotation - 90)
            if plein:
                ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
                pts = [points_segment(p1, p3), points_segment(p1, p4), points_segment(p2, p3), points_segment(p2, p4)]
                for i in pts:
                    for j in i:
                        cv2.line(img, ct, j, couleur, 10)
            if oui: ## Côtés ##
                cv2.line(img, p1, p3, couleur, epaisseur)
                cv2.line(img, p1, p4, couleur, epaisseur)
                cv2.line(img, p2, p3, couleur, epaisseur)
                cv2.line(img, p2, p4, couleur, epaisseur)
            if help:
                cercle(img, p1, 10, bleu, 0)
                cercle(img, p2, 10, rouge, 0)
                cercle(img, ct, 20, turquoise, 0)
                cercle(img, p3, 10, vert, 0)
                cercle(img, p4, 10, jaune, 0)
            return(img)
        def triangle(img, p1=ct_sg(p3, ct), p2=ct_sg(p4, ct), p3=ct_sg(ct, ch), couleur=noir, epaisseur=epaisseur):
            '''
            Dessin d'un triangle.\n
            Prend:
            ------
            :img: ``np.array``\n
            :p1: ``tuple (x, y)``\n
            :p2: ``tuple (x, y)``\n
            :p3: ``tuple (x, y)``\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            p1 = [round(i) for i in p1]
            p2 = [round(i) for i in p2]
            p3 = [round(i) for i in p3]

            epaisseur = int(epaisseur)
            if epaisseur <= 0:
                if epaisseur == 0:
                    epaisseur = 2
                else:
                    epaisseur = abs(epaisseur)
                    if epaisseur <=1:
                        epaisseur = 2
                points = points_segment(p2, p3)
                for i in points:
                    cv2.line(img, p1, i, couleur, epaisseur)
            if oui: ## Côtés ##
                cv2.line(img, p1, p2, couleur, epaisseur)
                cv2.line(img, p2, p3, couleur, epaisseur)
                cv2.line(img, p3, p1, couleur, epaisseur)
            return(img)
        def triangle_(img, p1=ct_sg(p3, ct), p2=ct_sg(p4, ct), p3=ct_sg(ct, ch), couleur=noir, epaisseur=epaisseur):
            '''
            Dessin d'un triangle.\n
            Prend:
            ------
            :img: ``np.array``\n
            :p1: ``tuple (x, y)``\n
            :p2: ``tuple (x, y)``\n
            :p3: ``tuple (x, y)``\n
            :couleur: ``tuple`` (b, g, r)\n
            :epaisseur: ``int``\n\tSi l'épaisseur est <= 0, alors le rectangle se remplit.\n
            Renvoie:
            --------
            ``img`` ou ``rien``\n
            Soit: ``img = rectangle(···)``\n
            Soit: ``rectangle(···)``
            '''
            epaisseur = int(epaisseur)
            if epaisseur <= 0:
                if epaisseur == 0:
                    epaisseur = 1
                else:
                    epaisseur = abs(epaisseur)
                    if epaisseur < 1:
                        epaisseur = 1
                points = points_segment(p2, p3)
                for i in points:
                    cv2.line(img, p1, i, couleur, epaisseur)
            if oui: ## Côtés ##
                cv2.line(img, p1, p2, couleur, epaisseur)
                cv2.line(img, p2, p3, couleur, epaisseur)
                cv2.line(img, p3, p1, couleur, epaisseur)
            return(img)
        def spirale(img, ct=ct, rayon=rayon, t_dist='lineere', couleur='random', epaisseur=epaisseur, c_ep=0, rotation=0, tours=1):
            '''
            :img: ``np.array``\n
            :ct: ``tuple``\n
            :dist: rayon ``int``\n
            :t_dist: ``int`` or ``'lineere'``\n
            :couleur: ``'random'`` or ``tuple``\n
            :epaisseur: ``int``\n
            :c_ep: ``int`` changement d'épaisseur\n
            :rotation: ``int``\n
            :tours: ``float`` or ``int``\n
            :step: ``int``
            '''
            rayon, epaisseur = int(rayon), int(epaisseur)
            a = 1
            for i in range(tours):
                a /= 2
            step = 1 + a
            color = couleur
            mult = 1
            while rayon > 0 and step != 0 and step != 0.0:
                if couleur == 'random':
                    color = (rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
                cercle(img, ct, int(rayon), color, int(epaisseur), 0, tours, rotation)
                rotation += tours
                if t_dist == 'lineere':
                    rayon -= step
                else:
                    rayon -= step * mult
                epaisseur += c_ep
                mult += 1
            return(img)
        def vortex(img, ct=ct, rayon=rayon, t_dist='lineere', couleur='random', epaisseur=epaisseur, c_ep=0, nºbras=4, rotation=0, angle=1, step=1):
            for i in range(nºbras):
                spirale(img, ct, rayon, t_dist, couleur, epaisseur, c_ep, 360 / nºbras * i + rotation, angle, step)
            return(img)
        def vortex_vortex(img, cto=ct, dists=[0], angles=[0, 90, 180, 270], couleur='random', taille_spirale=25, rotation_spirales=0, rotation=0, c_ep=0, bras=4, tours=1, step=1):
            for i in dists:
                for j in angles:
                    ct = coosCercle(cto, i, j + rotation)
                    vortex(img, ct, taille_spirale, 'lineere', couleur, plein, c_ep, bras, rotation_spirales, tours, step)
            return(img)
        def grille(img, epaisseur1=5, epaisseur2=2, pto=pt_img_cartee.pt, couleur=noir, d=[haut, long]):
            x, y = pto
            ligne(img, [x, 0], [x, d[0]], couleur, epaisseur1)
            ligne(img, [0, y], [d[1], y], couleur, epaisseur1)
            for i in range(x, 0, -50):
                ligne(img, [i, 0], [i, d[0]], couleur, epaisseur2)
            for i in range(x, d[1], 50):
                ligne(img, [i, 0], [i, d[0]], couleur, epaisseur2)
            for i in range(y, 0, -50):
                ligne(img, [0, i], [d[1], i], couleur, epaisseur2)
            for i in range(y, d[0], 50):
                ligne(img, [0, i], [d[1], i], couleur, epaisseur2)
            return(img)
        def parabole(img, a=1, b=0, c=0, puissance=2, couleur=bleu, epaisseur=10):
            p = puissance
            b = 0 - b
            pt = pt_img_cartee.pt
            xct = round(pt[0])
            x = -xct - 10
            yct = round(pt[1])
            save = []
            while x <= xct:
                save.append([x + xct, yct - (a * (x ** p) + b * x + c)])
                if len(save) > 2:
                    try:
                        ligne(img, save[-2], save[-1], couleur, epaisseur)
                    except:
                        pass
                x += 1
            return(img)
        def bande(img, pt=ct, haut=75, long=300, couleur=bois, rot=0):
            abg = coosCercle(pt, long/2, 180 + rot)
            ahg = coosCercle(abg, haut, 270 + rot)
            bg = coosCercle(abg, haut/5, 90 + rot)
            abd = coosCercle(pt, long/2, 0 + rot)
            ahd = coosCercle(abd, haut, 270 + rot)
            bd = coosCercle(abd, haut/5, 90 + rot)
            hg = coosCercle(bg, haut, 270 + rot)
            hd = coosCercle(bd, haut, 270 + rot)
            bd = coosCercle(bd, long/5, 0 + rot)
            bg = coosCercle(bg, long/5, 180 + rot)
            hd = coosCercle(hd, long/5, 0 + rot)
            hg = coosCercle(hg, long/5, 180 + rot)
            c = coosCercle(pt, haut, 270 + rot)
            triangle(img, bg, ahg, abg, couleur, 0)
            triangle(img, hg, abg, ahg, couleur, 0)
            triangle(img, bd, ahd, abd, couleur, 0)
            triangle(img, hd, abd, ahd, couleur, 0)
            for i in points_segment(pt, c):
                ellipse(img, i, [long/2, long/10], couleur, 2, 0, 180, 180 + rot)
            a = 10
            bois2 = [bois[0]-a, bois[1]-a, bois[2]-a]
            ligne(img, ahg, abg, bois2, 2)
            ligne(img, ahd, abd, bois2, 2)
            return(img, c)
        def etoile(img, ct=ct, rayon=100, couleur=turquoise, epaisseur=0, n_bras=5, rot=0, help=False):
            if n_bras >= 100:
                n_bras = 99
            ptsl = []
            ptsp = []
            angle = 360/n_bras
            rot -= 90
            for i in range(n_bras):
                ptsl.append(coosCercle(ct, rayon, angle*i + rot))
            for i in range(n_bras*2):
                ptsp.append(coosCercle(ct, rayon/2.61096605744125, angle*i + angle/2 + rot))
            for i in range(n_bras):
                triangle(img, ptsl[i], ptsp[i-1], ptsp[i+1], couleur, epaisseur)
            if rayon >= 17:
                polygone_regulier(img, ct, n_bras, rayon/4, couleur, epaisseur, 180 + rot)
            if help:
                for i in ptsl:
                    cercle(img, i, 1, turquoise, 0)
                for i in ptsp:
                    cercle(img, i, 1, vert, 0)
            return(img)
        def montagne(img, ct=ct, dist=75, couleur1=noir, couleur2=blanc, rot=0):
            ud = dist
            p4 = coosCercle(ct, ud, 45)
            ph = coosCercle(ct, ud*1.1, -90)
            p1 = coosCercle(ct, ud, 45+180)
            p2 = coosCercle(ct, ud, 45+270)
            picg = coosCercle(p1, ud/3, -45)
            picd = coosCercle(p2, ud/3, -90-45)
            valg = coosCercle(picg, ud/3, 45)
            vald = coosCercle(picd, ud/3, 90+45)
            triangle(img, p1, picg, valg, couleur2, 0)
            triangle(img, p2, picd, vald, couleur2, 0)
            triangle(img, ph, valg, vald, couleur2, 0)
            rectangle(img, p1, p4, couleur1, -2.5, rot)
            return(img)
        def ars(img, secteurs, forme=0, saute=1):
            cercle(img, ct, rayon, couleur, epaisseur / 5)
            cercle(img, ct, rayon + 50, couleur, epaisseur / 5)
            cercle(img, ct, rayon + 150, couleur, epaisseur / 5)
            points = []
            points2 = []
            for i in range(secteurs):
                points.append(coosCercle(ct, rayon, 360 / secteurs * i))
            for i in range(secteurs):
                points2.append(coosCercle(ct, rayon + 150, 360 / secteurs * i))
            ctrl = 0
            for i in points:
                ligne(img, i, points2[ctrl], couleur, epaisseur / 5)
                ctrl += 1
            if forme == 0:
                for i in points:
                    for j in points:
                        ligne(img, i, j, couleur, epaisseur / secteurs)
            elif forme == 1:
                ctrl = 0
                for i in range(saute):
                    points.append(points[i])
                for i in points:
                    try:
                        ligne(img, i, points[ctrl + saute], couleur, epaisseur / num)
                    except:
                        pass
                    ctrl += 1
            return(img)
        def cadre(img, pt1, pt2, cl=blanc, cl2=noir, ep_b=3, rot=0):
            rectangle(img, pt1, pt2, cl, 0, rot)
            rectangle(img, pt1, pt2, cl2, ep_b, rot)
            return(img)
        def point(img, pt, cl=rouge):
            cercle(img, pt, 10, cl, 0)
            return(img)
    if oui: ############################ Images ###
        def image(dimensions=(haut, long, 3), remplissage=blanc):
            '''
            Prend:
            ------
            :dimensions: ``tuple`` ``(x, y, z)``\n
            Si z est 3 C'est les couleur BGR (et pas RGB)
            Si z est 4 Alors c'est BGRA, où A est le canal alpha
            :remplissage1: ``int``\n
            Renvoie:
            --------
            ``img`` (``np.array``)
            '''
            img = np.full(dimensions, remplissage, np.uint8)
            return(img)
        def image_cartesienne(dimensions=(haut, long, 3), remplissage=blanc, couleur_lignes=noir, point_debut=(0, 0)):
            '''
            Prend:
            ------
            :dimensions: ``tuple`` ``(x, y, z)``\n
            Si z est 3 C'est les couleur BGR (et pas RGB)
            Si z est 4 Alors c'est BGRA, où A est le canal alpha
            :remplissage1: ``int``\n
            :couleur_lignes: ``int``n
            Renvoie:
            --------
            ``img`` (``np.array``)
            '''
            img = image(dimensions, remplissage)
            grille(img, pto=point_debut, couleur=couleur_lignes, d=dimensions[0:2])
            return(img)
        def image_cadre(dimensions=(haut, long, 3), remplissage=blanc, couleur_cadre=noir):
            '''
            Prend:
            ------
            :dimensions: ``tuple`` ``(x, y, z)``\n
            Si z est 3 C'est les couleur BGR (et pas RGB)\n
            Si z est 4 Alors c'est BGRA, où A est le canal alpha\n\n
            :remplissage: ``tuple rgb``\n
            :couleur_cadre: ``tuple rgb``\n
            Renvoie:
            --------
            ``img`` (``np.array``)
            '''
            img = np.full(dimensions, remplissage, np.uint8)
            cv2.rectangle(img, dd, deb, couleur_cadre, plein)
            cv2.rectangle(img, ff, fin, couleur_cadre, plein)
            return(img)
        def image_cartesienne_cadre(dimensions=(haut, long, 3), remplissage=blanc, couleur_cadre=bleu, couleur_lignes=noir):
            '''
            Prend:
            ------
            :dimensions: ``tuple`` ``(x, y, z)``\n
            Si z est 3 C'est les couleur BGR (et pas RGB)\n
            Si z est 4 Alors c'est BGRA, où A est le canal alpha\n\n
            :remplissage: ``tuple rgb``\n
            :couleur_cadre: ``tuple rgb``\n
            Renvoie:
            --------
            ``img`` (``np.array``)
            '''
            img = image(dimensions, remplissage)
            cv2.rectangle(img, dd, deb, couleur_cadre, plein)
            cv2.rectangle(img, ff, fin, couleur_cadre, plein)
            grille(img, couleur_lignes, p1, p4, 25, 5)
            return(img)
        def image_cercle(dimensions=(haut, long, 3), remplissage=blanc):
            '''
            Prend:
            ------
            :dimensions: ``tuple`` ``(x, y, z)``\n
            Si z est 3 C'est les couleur BGR (et pas RGB)
            Si z est 4 Alors c'est BGRA, où A est le canal alpha
            :remplissage1: ``[B G R]``\n
            Renvoie:
            --------
            ``img`` (``np.array``)
            '''
            img = image(dimensions, remplissage)
            cv2.circle(img, ct, x // 2, blanc, -1)
            return(img)
        def ouvre_image(chemin):
            '''
            Prend:
            ------
            :chemin: ``str`` vers le fichier\n(il faut séparer avec deux '\\'\nPcq sinon il considère la lettre suivante comme un caractère spécial)\n
            Renvoie:
            --------
            ``img`` (``np.array``)
            '''
            img = cv2.imread(chemin)
            return(img)
        def sauve_image(nom_fichier, img, path=''):
            if path != '':
                r = os.getcwd()
                os.chdir(path)
            cv2.imwrite(nom_fichier, img)
            if path != '':
                os.chdir(r)
    if oui: ########## Fonctions sur les images ###
        def zoom_at(img, zoom=1, angle=0, coord=None):
            cy, cx = [ i/2 for i in img.shape[:-1] ] if coord is None else coord[::-1]
            rot_mat = cv2.getRotationMatrix2D((cx,cy), angle, zoom)
            result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
            return(result)
        def fusionImages(petite_img, grande_img):
            '''
            Prend:
            ------
            :petite_img: ``np.array``\n
            :grande_img: ``np.array``\n
            Renvoie:
            --------
            ``np.array``\nImage.
            '''
            s_img = petite_img
            img = grande_img
            x_offset = 50
            y_offset = 50
            img[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img
            return(img)
        def montre(img, nomFenetre='img', attente=0, destroy=True, dists=relocate_img()):
            '''
            Prend:
            ------
            :nomFenetre: ``str``\n
            :img: ``np.array``\n
            :attente: ``int``\n
            Renvoie:
            --------
            ``None``
            '''
            cv2.namedWindow(nomFenetre, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(nomFenetre, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.moveWindow(nomFenetre, dists[0], dists[1])
            cv2.imshow(nomFenetre, img)
            wk = cv2.waitKeyEx(attente)
            if destroy == True:
                cv2.destroyWindow(nomFenetre)
            return(wk)
        def montre_part(img, pto=[0, 0], t=[long-1, haut-1], nomFenetre='img', attente=0, destroy=True, dists=relocate_img()):
            im = img[pto[1]:pto[1]+t[1], pto[0]:pto[0]+t[0]]
            return(montre(im, nomFenetre, attente, destroy, dists))
        def img_part(img, pto=[0, 0], t=[long-1, haut-1]):
            return(np.array(img[pto[1]:pto[1]+t[1], pto[0]:pto[0]+t[0]]))
        def attend_touche(attente):
            if attente >= 0:
                quoi = cv2.waitKeyEx(attente)
                return(quoi)
        def souris_sur_image(img, fonction, nomFenetre='img', attente=0, destroy=True, param=None):
            '''
            Prend:
            ------
            :nomFenetre: ``str``\n
            :fonction: ``function``\nSeulement le nom de la fonction, sans les parenthèses.\n
            :img: ``np.array``\n
            :attente: ``int``\n
            Renvoie:
            --------
            ``None``
            '''
            cv2.namedWindow(nomFenetre, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(nomFenetre, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow(nomFenetre, img)
            cv2.setMouseCallback(nomFenetre, fonction, param)
            wk = cv2.waitKeyEx(attente)
            if destroy == True:
                cv2.destroyWindow(nomFenetre)
            return(wk)
        def ferme(nomFenetre):
            '''
            Ferme la fenêtre (python) qui correspond avec le nom introduit.
            '''
            try:
                cv2.destroyWindow(nomFenetre)
            except:
                print(f'None window named {nomFenetre}.')
        def ferme_all():
            '''
            Ferme toutes les fenêtres ouvertes (par python).
            '''
            cv2.destroyAllWindows()
        def fenetre(nomFenetre, propriete):
            cv2.namedWindow(nomFenetre, propriete)
        def def_propriete_fenetre(nomFenetre, propriete, valeur):
            cv2.setWindowProperty(nomFenetre, propriete, valeur)
        def img_plein_ecran(nomFenetre='img'):
            cv2.namedWindow(nomFenetre, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(nomFenetre, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        def montre_img(img, nomFenetre='img'):
            cv2.namedWindow(nomFenetre, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(nomFenetre, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow(nomFenetre, img)
        def clicked_in(pos, boutton): ## Is pos between boutton[0] (haut gauche) and boutton[1] (bas droite) ##
            a_l_interieur = pos[0] >= boutton[0][0] and pos[0] <= boutton[1][0] and pos[1] >= boutton[0][1] and pos[1] <= boutton[1][1]
            return(a_l_interieur)
        def visual_input(img, text='', placeholder='', end='', nomFenetre='img', pt1=p1, pt2=p4, taille=4, couleur=noir, epaisseur=epaisseur, police=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, chars=None, help=False):
            out = placeholder if type(placeholder) == str else ''
            if chars == None: chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;_ 0123456789-+*!?#@|$%&/()[]{}=\'\"\\'#ñcÑÇ
            while True:
                imag = ecris(copy.deepcopy(img), text + out + end, pt1, pt2, taille, couleur, epaisseur, police, help)
                montre_img(imag, nomFenetre)
                wk = attend_touche(0)
                char = chr(wk)
                try:
                    chars.index(char)
                    out += char
                except:
                    if wk == 8:
                        try:
                            out = out[0:len(out)-1]
                        except:
                            continue
                    elif wk == 13:
                        break
                    elif wk == 27:
                        return(0)
                    else:
                        print(wk)
            return(out)
    if oui: ############ Miscellanous functions ###
        def execute(path):
            os.startfile(path)
    if oui: ### CV2.puttext()
        def ecris(img, texte, pt1, pt2, taille=1, couleur=noir, epaisseur=epaisseur, police=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, help=False):
            if help:
                for i in [pt1, pt2]:
                    point(img, i)
            if oui: ## Vars ##
                x1, y1 = pt1
                x2, y2 = pt2
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
                cv2.putText(img, line, (x, yy), police, taille, couleur, epaisseur)
            return(img)
        def visual_input(img, text='', placeholder='', end='', nomFenetre='img', pt1=p1, pt2=p4, taille=4, couleur=noir, epaisseur=epaisseur, police=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, chars=None, help=False):
            out = placeholder if type(placeholder) == str else ''
            if chars == None: chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. 0123456789'#ñcÑÇ
            while True:
                imag = ecris(copy.deepcopy(img), text + out + end, pt1, pt2, taille, couleur, epaisseur, police, help)
                montre_img(imag, nomFenetre)
                wk = attend_touche(0)
                char = chr(wk)
                try:
                    chars.index(char)
                    out += char
                except:
                    if wk == 8:
                        try:
                            out = out[0:len(out)-1]
                        except:
                            continue
                    elif wk == 13:
                        break
                    elif wk == 27:
                        return(0)
                    else:
                        print(wk)
            return(out)
    if oui: ######## scripte et ses dépandances ###
        def scripte_format(img, p1, p2, p3, p4, souligne, surligne, epaisseur):
            if surligne != 'None':
                if oui: ## Coos ##
                    ligne(img, p1, p3, surligne, 1)
                    ligne(img, p1, p2, surligne, 1)
                    ligne(img, p2, p4, surligne, 1)
                    ligne(img, p3, p4, surligne, 1)
                    ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
                for i in points_segment(p1, p3):
                    ligne(img, i, ct, surligne, 2)
                for i in points_segment(p1, p2):
                    ligne(img, i, ct, surligne, 2)
                for i in points_segment(p2, p4):
                    ligne(img, i, ct, surligne, 2)
                for i in points_segment(p3, p4):
                    ligne(img, i, ct, surligne, 2)
            if souligne != 'None':
                if save_pos.d == '':
                    g = pt_sg(p1, p3, 1, 15)
                else:
                    g = save_pos.d
                d = pt_sg(p2, p4, 1, 15)
                ligne(img, g, d, souligne, int(epaisseur / 5 * 4))
                save_pos.d = ct_sg(g, d)
            return(img)
        def num(img, cotes, p1, p2, p3, p4, couleur=noir, epaisseur=epaisseur):
            if oui: ## Coos ##
                ch = ct_sg(p1, p2)
                cb = ct_sg(p3, p4)
                cg = ct_sg(p1, p3)
                cd = ct_sg(p2, p4)
                ct = ct_sg(p1, p4)
            for i in cotes:
                if i == 'a':
                    ligne(img, ct_sg(p1, ch), ct_sg(p2, ch), couleur, epaisseur)
                elif i == 'b':
                    ligne(img, ct_sg(p1, ch), ct_sg(cg, ct), couleur, epaisseur)
                elif i == 'c':
                    ligne(img, ct_sg(p2, ch), ct_sg(cd, ct), couleur, epaisseur)
                elif i == 'd':
                    ligne(img, ct_sg(cg, ct), ct_sg(cd, ct), couleur, epaisseur)
                elif i == 'e':
                    ligne(img, ct_sg(p3, cb), ct_sg(cg, ct), couleur, epaisseur)
                elif i == 'f':
                    ligne(img, ct_sg(p4, cb), ct_sg(cd, ct), couleur, epaisseur)
                elif i == 'g':
                    ligne(img, ct_sg(p3, cb), ct_sg(p4, cb), couleur, epaisseur)
            return(img)
        def minCoos(p1, p2, p3, p4, rot=0):
            hg = p1
            hd = p2
            bg = p3
            bd = p4
            ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
            p1 = pt_sg(p1, ct, 7, 2)
            p2 = pt_sg(p2, ct, 7, 2)
            p3 = pt_sg(p3, ct, 7, 2)
            p4 = pt_sg(p4, ct, 7, 2)
            ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
            p1h = pt_sg(hg, ct, 5, 2)
            p2h = pt_sg(hd, ct, 5, 2)
            p3b = pt_sg(bg, ct, 5, 2)
            p4b = pt_sg(bd, ct, 5, 2)
            ch = ct_sg(p1, p2)
            cb = ct_sg(p3, p4)
            cg = ct_sg(p1, p3)
            cd = ct_sg(p2, p4)
            a, b = 2, 1
            c1 = ct_sg(p1, cg)
            c2 = ct_sg(p2, cd)
            c3 = ct_sg(p3, cg)
            c4 = ct_sg(p4, cd)
            return(p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b)
        def coos2(p1, p2, p3, p4):
            ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
            p1 = (pt_sg(p1, ct, 7, 2))
            p2 = (pt_sg(p2, ct, 7, 2))
            p3 = (pt_sg(p3, ct, 7, 2))
            p4 = (pt_sg(p4, ct, 7, 2))
            ct = ct_sg(p1, p4)
            ch = ct_sg(p1, p2)
            cb = ct_sg(p3, p4)
            cg = ct_sg(p1, p3)
            cd = ct_sg(p2, p4)
            c1 = coosCercle(p1, dist(p1, ct) // 3, 0)
            c2 = coosCercle(p2, dist(p2, ct) // 3, 0)
            c3 = coosCercle(p3, dist(p3, ct) // 3, 180)
            c4 = coosCercle(p4, dist(p4, ct) // 3, 180)
            return(p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4)
        def chars(img, char, p1, p2, p3, p4, couleur=noir, epaisseur=epaisseur, police='basic', rotation=0, taille=1, pos=0, combine=False):
            save_pos = pos
            if oui: ## Ajuste les points nécessaires pour dessiner les chars ##
                a, b = 3, 1
                ep = epaisseur
                hg = p1
                hd = p2
                bg = p3
                bd = p4
                cg = ct_sg(p1, p3)
                cd = ct_sg(p2, p4)
                ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
                p1h = pt_sg(p1, cg, 5, 2)
                p2h = pt_sg(p2, cd, 5, 2)
                p3b = pt_sg(p3, cg, 5, 2)
                p4b = pt_sg(p4, cd, 5, 2)
                p1 = pt_sg(p1, ct, 7, 2)
                p2 = pt_sg(p2, ct, 7, 2)
                p3 = pt_sg(p3, ct, 7, 2)
                p4 = pt_sg(p4, ct, 7, 2)
                ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
                e1 = pt_sg(hg, p1, 4, 15)
                e2 = pt_sg(hd, p2, 4, 15)
                e3 = pt_sg(bg, p3, 4, 15)
                e4 = pt_sg(bd, p4, 4, 15)
                ch = ct_sg(p1, p2)
                cb = ct_sg(p3, p4)
                cg = ct_sg(p1, p3)
                cd = ct_sg(p2, p4)
                c1 = ct_sg(p1, cg)
                c2 = ct_sg(p2, cd)
                c3 = ct_sg(p3, cg)
                c4 = ct_sg(p4, cd)
                ct1 = ct_sg(p1, ct)
                ct2 = ct_sg(p2, ct)
                ct3 = ct_sg(p3, ct)
                ct4 = ct_sg(p4, ct)
                ctg = ct_sg(cg, ct)
                ctd = ct_sg(cd, ct)
                cth = ct_sg(ch, ct)
                ctb = ct_sg(cb, ct)
            if police == 'basic' or police == 'basique' or police == 'simple' or police == 'simplex':
                if char == 'a1': ## Rmplit tt ## ## Full square ##
                    rectangle(img, p1, p4, couleur, plein)
                    pos -= 1
                elif char == 'b1': ## Ecrit :   ## ## Espace #######
                    pass
                elif char == 'c1': ## Ecrit : 0 ## ## 0 num ########
                    num(img, 'abcefg', p1, p2, p3, p4, couleur, epaisseur)
                elif char == 'd1': ## Ecrit : 1 ## ## 1 num ########
                    num(img, 'cf', p1, p2, p3, p4, couleur, epaisseur)
                elif char == 'e1': ## Ecrit : 2 ## ## 2 num ########
                    num(img, 'acdeg', p1, p2, p3, p4, couleur, epaisseur)
                elif char == 'f1': ## Ecrit : 3 ## ## 3 num ########
                    num(img, 'acdfg', p1, p2, p3, p4, couleur, epaisseur)
                elif char == 'g1': ## Ecrit : 4 ## ## 4 num ########
                    num(img, 'bcdf', p1, p2, p3, p4, couleur, epaisseur)
                elif char == 'h1': ## Ecrit : 5 ## ## 5 num ########
                    num(img, 'abdfg', p1, p2, p3, p4, couleur, epaisseur)
                elif char == 'i1': ## Ecrit : 6 ## ## 6 num ########
                    num(img, 'abdefg', p1, p2, p3, p4, couleur, epaisseur)
                elif char == 'j1': ## Ecrit : 7 ## ## 7 num ########
                    num(img, 'acf', p1, p2, p3, p4, couleur, epaisseur)
                elif char == 'k1': ## Ecrit : 8 ## ## 8 num ########
                    num(img, 'abcdefg', p1, p2, p3, p4, couleur, epaisseur)
                elif char == 'l1': ## Ecrit : 9 ## ## 9 num ########
                    num(img, 'abcdfg', p1, p2, p3, p4, couleur, epaisseur)
                elif char == 'm1': ## Ecrit : + ## ## Signe Plus ###
                    ligne(img, ctg, ctd, couleur, epaisseur)
                    ligne(img, cth, ctb, couleur, epaisseur)
                elif char == 'n1': ## Ecrit : - ## ## Signe Moins ##
                    ligne(img, ctg, ctd, couleur, epaisseur)
                elif char == 'o1': ## Ecrit : ± ## ## Plus Minus ###
                    ligne(img, ct_sg(ct_sg(cd, ct), ct_sg(ch, p2)), ct_sg(ct_sg(cg, ct), ct_sg(p1, ch)), couleur, epaisseur)
                    ligne(img, pt_sg(ch, ct, 4, 1), pt_sg(ch, ct, 1, 4), couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(cg, ct), ct_sg(p3, cb)), ct_sg(ct_sg(cd, ct), ct_sg(cb, p4)), couleur, epaisseur)
                elif char == 'p1': ## Ecrit : ÷ ## ## Diviser ######
                    ligne(img, ctg, ctd, couleur, epaisseur)
                    cercle(img, pt_sg(ch, ct, 2, 3), epaisseur // 3 * 2, couleur, plein)
                    cercle(img, pt_sg(cb, ct, 2, 3), epaisseur // 3 * 2, couleur, plein)
                elif char == 'q1': ## Ecrit : × ## ## Multiplier ###
                    ligne(img, ct1, ct4, couleur, epaisseur)
                    ligne(img, ct2, ct3, couleur, epaisseur)
                elif char == 'a2': ## Ecrit : ¿ ## ##Interrogeant1##
                    ellipse(img, pt_sg(ct, cb, 3, 5), [dist(cg, cd) / 3, dist(cg, cd) / 3], couleur, epaisseur, -130, 90, 180 + rotation)
                    ligne(img, pt_sg(ct, cb, 5), ct_sg(ch, ct), couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch, 1, 5), epaisseur / 3 * 2, couleur, plein)
                elif char == 'b2': ## Ecrit : ? ## ##Interrogeant2##
                    ellipse(img, pt_sg(ct, ch, 3, 5), [dist(cg, cd) / 3, dist(cg, cd) / 3], couleur, epaisseur, -130, 90, rotation)
                    ligne(img, pt_sg(ct, ch, 5), ct_sg(cb, ct), couleur, epaisseur)
                    cercle(img, pt_sg(ct, cb, 1, 5), epaisseur / 3 * 2, couleur, plein)
                elif char == 'c2': ## Ecrit : A ## ## A maj ########
                    ligne(img, ch, p3, couleur, epaisseur)
                    ligne(img, ch, p4, couleur, epaisseur)
                    ligne(img, pt_sg(ch, p3, 2, 3), pt_sg(ch, p4, 2, 3), couleur, epaisseur)
                elif char == 'd2': ## Ecrit : B ## ## B maj ########
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    ligne(img, p3, cb, couleur, epaisseur)
                    cercle(img, ct_sg(ct, ch), dist(ct, ch) / 2, couleur, epaisseur, -90, 90, rotation)
                    cercle(img, ct_sg(ct, cb), dist(ct, cb) / 2, couleur, epaisseur, -90, 90, rotation)
                elif char == 'e2': ## Ecrit : C ## ## C maj ########
                    ellipse(img, pt_sg(ct, cd, 8, 5), [dist(p2, cd), dist(ct, cd)], couleur, epaisseur, -20, 200, 90 + rotation)
                elif char == 'f2': ## Ecrit : D ## ## D maj ########
                    sagitta = abs(pt_sg(cg, ct, 3)[0] - ct_sg(p2, p4)[0])
                    ellipse(img, ct, [dist(ct, cd), dist(ch, ct)], couleur, epaisseur, -90, 90, rotation)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, p3, cb, couleur, epaisseur)
                elif char == 'g2': ## Ecrit : E ## ## E maj ########
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, cg, pt_sg(ct, cd, 3, 1), couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'h2': ## Ecrit : F ## ## F maj ########
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ct_sg(ch, p2), couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                elif char == 'i2': ## Ecrit : G ## ## G maj ########
                    ellipse(img, pt_sg(ct, cd, 8, 5), [dist(p2, cd), dist(ct, cd)], couleur, epaisseur, -25, 200, 90 + rotation)
                    ligne(img, p4, cd, couleur, epaisseur)
                    ligne(img, ct_sg(ct, cd), cd, couleur, epaisseur)
                elif char == 'j2': ## Ecrit : H ## ## H maj ########
                    ligne(img, pt_sg(p1, ch, 3, 1), pt_sg(p3, cb, 3, 1), couleur, epaisseur)
                    ligne(img, pt_sg(p2, ch, 3, 1), pt_sg(p4, cb, 3, 1), couleur, epaisseur)
                    ligne(img, pt_sg(cg, ct, 3, 1), pt_sg(cd, ct, 3, 1), couleur, epaisseur)
                elif char == 'k2': ## Ecrit : I ## ## I maj ########
                    ligne(img, ct_sg(p1, ch), ct_sg(p2, ch), couleur, epaisseur)
                    ligne(img, ct_sg(p3, cb), ct_sg(p4, cb), couleur, epaisseur)
                    ligne(img, ch, cb, couleur, epaisseur)
                elif char == 'l2': ## Ecrit : J ## ## J maj ########
                    sagitta = int(abs(ct[1] - cb[1]) / 6 * 5)
                    ligne(img, ct_sg(p1, ch), p2, couleur, epaisseur)
                    h, b = 4, 1
                    ptt2 = pt_sg(cd, p4, h, b)
                    ligne(img, p2, ptt2, couleur, epaisseur)
                    cnt = pt_sg(ct, cb, h, b)
                    ellipse(img, cnt, (dist(cnt, ptt2), dist(cnt, cb)), couleur, epaisseur, 0, 180, rotation)
                elif char == 'm2': ## Ecrit : K ## ## K maj ########
                    ligne(img, ct_sg(p1, ch), ct_sg(p3, cb), couleur, epaisseur)
                    ligne(img, ct_sg(ct, cg), p2, couleur, epaisseur)
                    ligne(img, pt_sg(ct_sg(ct, cg), pt_sg(ct_sg(ct, cg), p2), 3, 2), p4, couleur, epaisseur)
                elif char == 'n2': ## Ecrit : L ## ## L maj ########
                    ligne(img, ct_sg(p1, ch), ct_sg(p3, cb), couleur, epaisseur)
                    ligne(img, ct_sg(p3, cb), pt_sg(p4, cb, 5, 2), couleur, epaisseur)
                elif char == 'o2': ## Ecrit : M ## ## M maj ########
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p2, ct, couleur, epaisseur)
                elif char == 'p2': ## Ecrit : N ## ## N maj ########
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p1, p4, couleur, epaisseur)
                elif char == 'q2': ## Ecrit : O ## ## O maj ########
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cg)), couleur, epaisseur, 0, 360, 90 + rotation)
                elif char == 'a3': ## Ecrit : ¡ ## ## Exclamation1##
                    ligne(img, cb, ct_sg(ch, ct), couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch, 1, 5), epaisseur / 3 * 2, couleur, plein)
                elif char == 'b3': ## Ecrit : ! ## ## Exclamation2##
                    ligne(img, ch, ct_sg(cb, ct), couleur, epaisseur)
                    cercle(img, pt_sg(ct, cb, 1, 5), epaisseur / 3 * 2, couleur, plein)
                elif char == 'c3': ## Ecrit : P ## ## P maj ########
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch), dist(pt_sg(ct, ch), ch), couleur, epaisseur, -90, 90, rotation)
                elif char == 'd3': ## Ecrit : Q ## ## Q maj ########
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cg)), couleur, epaisseur, angle=90+rotation)
                    ligne(img, p4, ct_sg(ct, cb), couleur, epaisseur)
                elif char == 'e3': ## Ecrit : R ## ## R maj ########
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    ligne(img, p4, ct, couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch), dist(pt_sg(ct, ch), ch), couleur, epaisseur, -90, 90, rotation)
                elif char == 'f3': ## Ecrit : S ## ## S maj ########
                    tour = 225
                    cercle(img, ct_sg(cg, p2), dist(ct_sg(cg, p2), ct), couleur, epaisseur, 0, tour, 90 + rotation)
                    cercle(img, ct_sg(cg, p4), dist(ct_sg(cg, p4), ct), couleur, epaisseur, 0, tour, -90 + rotation)
                elif char == 'g3': ## Ecrit : T ## ## T maj ########
                    ligne(img, pt_sg(p1, ch, 4, 1), pt_sg(p2, ch, 4, 1), couleur, epaisseur)
                    ligne(img, ch, cb, couleur, epaisseur)
                elif char == 'h3': ## Ecrit : U ## ## U maj ########
                    h, b = 4, 1
                    ptt1 = pt_sg(cg, p3, h, b)
                    ptt2 = pt_sg(cd, p4, h, b)
                    ligne(img, p1, ptt1, couleur, epaisseur)
                    ligne(img, p2, ptt2, couleur, epaisseur)
                    cnt = pt_sg(ct, cb, h, b)
                    ellipse(img, cnt, (dist(cnt, ptt2), dist(cnt, cb)), couleur, epaisseur, 0, 180, rotation)
                elif char == 'i3': ## Ecrit : V ## ## V maj ########
                    ligne(img, p1, cb, couleur, epaisseur)
                    ligne(img, p2, cb, couleur, epaisseur)
                elif char == 'j3': ## Ecrit : W ## ## W maj ########
                    ligne(img, p1, ct_sg(cb, p3), couleur, epaisseur)
                    ligne(img, p2, ct_sg(cb, p4), couleur, epaisseur)
                    ligne(img, ct, ct_sg(cb, p3), couleur, epaisseur)
                    ligne(img, ct, ct_sg(cb, p4), couleur, epaisseur)
                elif char == 'k3': ## Ecrit : X ## ## X maj ########
                    ligne(img, p1, p4, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                elif char == 'l3': ## Ecrit : Y ## ## Y maj ########
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p2, ct, couleur, epaisseur)
                    ligne(img, ct, cb, couleur, epaisseur)
                elif char == 'm3': ## Ecrit : Z ## ## Z maj ########
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                    ligne(img, pt_sg(cg, ct, 3, 1), pt_sg(cd, ct, 3, 1), couleur, epaisseur)
                elif char == 'n3': ## Ecrit : Æ ## ## Æ maj ########
                    ligne(img, ch, p3, couleur, epaisseur)
                    ligne(img, ch, cb, couleur, epaisseur)
                    ligne(img, pt_sg(p3, ch, 3, 2), pt_sg(ch, cb, 2, 3), couleur, epaisseur)
                    ligne(img, cb, p4, couleur, epaisseur)
                    ligne(img, ch, p2, couleur, epaisseur)
                    ligne(img, ct, cd, couleur, epaisseur)
                elif char == 'o3': ## Ecrit : Œ ## ## Œ maj ########
                    ellipse(img, ct_sg(cg, ct), (dist(ct, ch), dist(ct, cg) / 2), couleur, epaisseur, 0, 360, 90 + rotation)
                    ligne(img, ct_sg(cb, p3), p4, couleur, epaisseur)
                    ligne(img, ct_sg(ch, p1), p2, couleur, epaisseur)
                    ligne(img, ct, cd, couleur, epaisseur)
                elif char == 'p3': ## Ecrit : Ç ## ## Ç maj ########
                    ellipse(img, pt_sg(ct, cd, 8, 5), [dist(p2, cd), dist(ct, cd)], couleur, epaisseur, -20, 200, 90 + rotation)
                    ligne(img, ctb, p3, couleur, epaisseur)
                elif char == 'q3': ## Ecrit : Ñ ## ## Ñ maj ########
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p1, p4, couleur, epaisseur)
                    accent(img, 'tilde', hg, hd, bg, bd, couleur, epaisseur, rotation)
                elif char == 'a4': ## Ecrit : ¡¿## #Exclarrogeant1##
                    ellipse(img, pt_sg(ct, cb, 3, 5), [dist(cg, cd) // 3, dist(cg, cd) // 3], couleur, epaisseur, -40, 180, 90 + rotation)
                    ligne(img, cb, ct_sg(ch, ct), couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch, 1, 5), epaisseur // 3 * 2, couleur, plein)
                elif char == 'b4': ## Ecrit : !?## #Exclarrogeant2##
                    ellipse(img, pt_sg(ct, ch, 3, 5), [dist(cg, cd) // 3, dist(cg, cd) // 3], couleur, epaisseur, -40, 180, 270 + rotation)
                    ligne(img, ch, ct_sg(cb, ct), couleur, epaisseur)
                    cercle(img, pt_sg(ct, cb, 1, 5), epaisseur // 3 * 2, couleur, plein)
                elif char == 'c4': ## Ecrit : a ## ## A min ########
                    p3, p4 = pt_sg(p3, p4, a, b), pt_sg(p3, p4, b, a)
                    ligne(img, ct, p3, couleur, ep)
                    ligne(img, ct, p4, couleur, ep)
                    ligne(img, pt_sg(ct, p3, 2, 5), pt_sg(ct, p4, 2, 5), couleur, ep)
                elif char == 'd4': ## Ecrit : b ## ## B min ########
                    g = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b))
                    ligne(img, pt_sg(p3, p4, a, b), ct_sg(pt_sg(p1, p2, a, b), pt_sg(cg, cd, a, b)), couleur, ep)
                    ligne(img, pt_sg(p3, p4, a, b), cb, couleur, ep)
                    ligne(img, ct, pt_sg(cg, cd, a, b), couleur, ep)
                    ellipse(img, ct_sg(ct, cb), (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, -90, 90, rotation)
                elif char == 'e4': ## Ecrit : c ## ## C min ########
                    ellipse(img, ct_sg(ct, cb), (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, 45, 360-45, rotation)
                elif char == 'f4': ## Ecrit : d ## ## D min ########
                    g = ct_sg(pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a))
                    ligne(img, pt_sg(p3, p4, b, a), ct_sg(pt_sg(p1, p2, b, a), pt_sg(cg, cd, b, a)), couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), cb, couleur, ep)
                    ligne(img, ct, pt_sg(cg, cd, b, a), couleur, ep)
                    ellipse(img, ct_sg(ct, cb), (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, 90, 270, rotation)
                elif char == 'g4': ## Ecrit : e ## ## E min ########
                    ellipse(img, ct_sg(ct, cb), (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, 45, 360, rotation)
                    d = dist(ct, ctb)
                    g, d = coosCercle(ct_sg(ct, cb), d, 180 + rotation), coosCercle(ct_sg(ct, cb), d, 0 + rotation)
                    ligne(img, g, d, couleur, ep)
                elif char == 'h4': ## Ecrit : f ## ## F min ########
                    a, b = 15, 4
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                    g, d = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b)), ct_sg(pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a))
                    ligne(img, g, ctb, couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(p3, p4, a, b), couleur, ep)
                elif char == 'i4': ## Ecrit : g ## ## G min ########
                    a, b = 15, 4
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                    g, d = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b)), ct_sg(pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a))
                    ligne(img, ct_sg(ctb, d), d, couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), d, couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), pt_sg(p3, p4, a, b), couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(p3, p4, a, b), couleur, ep)
                elif char == 'j4': ## Ecrit : h ## ## H min ########
                    g = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b))
                    ligne(img, pt_sg(p3, p4, a, b), ct_sg(pt_sg(p1, p2, a, b), pt_sg(cg, cd, a, b)), couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a), couleur, ep)
                elif char == 'k4': ## Ecrit : i ## ## I min ########
                    ligne(img, cb, ct, couleur, ep)
                    cercle(img, cth, ep//2, couleur, 0)
                elif char == 'l4': ## Ecrit : j ## ## J min ########
                    ligne(img, ctb, ct, couleur, ep)
                    cercle(img, cth, ep//2, couleur, 0)
                    ptt = ct_sg(ct_sg(cg, ct), ct_sg(p3, cb))
                    ellipse(img, ptt, [dist(ptt, ctb), dist(ctb, cb)], couleur, ep, 0, 90)
                elif char == 'm4': ## Ecrit : k ## ## K min ########
                    g = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b))
                    ct = ct_sg(pt_sg(ct, cb), g)
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, ct, g, couleur, ep)
                    ligne(img, ct, pt_sg(cg, cd, b, a), couleur, ep)
                    ligne(img, ct, pt_sg(p3, p4, b, a), couleur, ep)
                elif char == 'n4': ## Ecrit : l ## ## L min ########
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, pt_sg(p3, p4, a, b), cb, couleur, ep)
                elif char == 'o4': ## Ecrit : m ## ## M min ########
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a), couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), ctb, couleur, ep)
                    ligne(img, pt_sg(cg, cd, b, a), ctb, couleur, ep)
                elif char == 'p4': ## Ecrit : n ## ## N min ########
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a), couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(p3, p4, b, a), couleur, ep)
                elif char == 'q4': ## Ecrit : o ## ## O min ########
                    ellipse(img, ctb, (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, angle=rotation)
                elif char == 'a5': ## Ecrit : ( ## ## Parentesis1 ##
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cg) / 3 * 2), couleur, epaisseur, 0, 180, 90 + rotation)
                elif char == 'b5': ## Ecrit : ) ## ## Parentesis2 ##
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cg) / 3 * 2), couleur, epaisseur, 0, 180, rotation - 90)
                elif char == 'c5': ## Ecrit : p ## ## P min ##
######
                    a, b = 15, 4
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                    g, d = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b)), ct_sg(pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a))
                    ligne(img, g, d, couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(p3, p4, a, b), couleur, ep)
                    ligne(img, pt_sg(cg, cd, b, a), d, couleur, ep)
                elif char == 'd5': ## Ecrit : q ## ## Q min ########
                    ellipse(img, ct_sg(ct, cb), (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, angle=rotation)
                    a, b = 15, 4
                    ligne(img, pt_sg(p3, p4, b, a), ct_sg(cb, ctb), couleur, ep)
                elif char == 'e5': ## Ecrit : r ## ## R min ########
                    a, b = 15, 4
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                    g, d = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b)), ct_sg(pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a))
                    ligne(img, g, d, couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(p3, p4, a, b), couleur, ep)
                    ligne(img, pt_sg(cg, cd, b, a), d, couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), ctb, couleur, ep)
                elif char == 'f5': ## Ecrit : s ## ## S min ########
                    a, b = 15, 4
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(p3, p4, b, a), couleur, ep)
                    g, d = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b)), ct_sg(pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a))
                    ligne(img, g, d, couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), g, couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), d, couleur, ep)
                elif char == 'g5': ## Ecrit : t ## ## T min ########
                    ligne(img, cb, ct, couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                elif char == 'h5': ## Ecrit : u ## ## U min ########
                    a, b = 15, 4
                    g = ct_sg(p3, cg)
                    d = ct_sg(p4, cd)
                    ellipse(img, ctb, (dist(ctb, g)*0.575, dist(ctb, g)*0.75), couleur, ep, 0, 180, rotation)
                    ligne(img, pt_sg(g, d, a, b), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, pt_sg(d, g, a, b), pt_sg(cd, cg, a, b), couleur, ep)
                elif char == 'i5': ## Ecrit : v ## ## V min ########
                    a, b = 15, 4
                    ligne(img, cb, pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, cb, pt_sg(cd, cg, a, b), couleur, ep)
                elif char == 'j5': ## Ecrit : w ## ## W min ########
                    a, b = 15, 4
                    ligne(img, pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a), couleur, ep)
                    a, b = 12, 4
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), ctb, couleur, ep)
                    ligne(img, pt_sg(p3, p4, a, b), ctb, couleur, ep)
                elif char == 'k5': ## Ecrit : x ## ## X min ########
                    a, b = 15, 4
                    ligne(img, pt_sg(p3, p4, b, a), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                elif char == 'l5': ## Ecrit : y ## ## Y min ########
                    a, b = 15, 4
                    ligne(img, ctb, pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                elif char == 'm5': ## Ecrit : z ## ## Z min ########
                    a, b = 15, 4
                    g, d = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b)), ct_sg(pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a))
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(p3, p4, b, a), couleur, ep)
                    ligne(img, g, d, couleur, ep)
                elif char == 'n5': ## Ecrit : æ ## ## Æ min ########
                    a, b = 15, 4
                    ligne(img, ct, cb, couleur, ep)
                    ligne(img, ct, pt_sg(p3, p4, a, b), couleur, ep)
                    ligne(img, cb, pt_sg(p3, p4, b, a), couleur, ep)
                    ligne(img, ct, pt_sg(cg, cd, b, a), couleur, ep)
                    ctd = ct_sg(pt_sg(cg, cd, b, a), pt_sg(p3, p4, b, a))
                    ctg3 = ct_sg(ct, pt_sg(p3, p4, a, b))
                    ligne(img, ctg3, ctd, couleur, ep)
                elif char == 'o5': ## Ecrit : œ ## ## Œ min ########
                    a, b = 15, 4
                    ligne(img, ct, cb, couleur, ep)
                    ellipse(img, ct_sg(ct, cb), (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, 90, 270, rotation)
                    ligne(img, cb, pt_sg(p3, p4, b, a), couleur, ep)
                    ligne(img, ct, pt_sg(cg, cd, b, a), couleur, ep)
                    ctd = ct_sg(pt_sg(cg, cd, b, a), pt_sg(p3, p4, b, a))
                    ctg3 = ct_sg(ct, cb)
                    ligne(img, ctg3, ctd, couleur, ep)
                elif char == 'p5': ## Ecrit : ç ## ## Ç min ########
                    ellipse(img, ct_sg(ct, cb), (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, 45, 360-45, rotation)
                    a, b = 15, 4
                    ligne(img, pt_sg(p3, p4, a, b), ct_sg(cb, ctb), couleur, ep)
                elif char == 'q5': ## Ecrit : ñ ## ## Ñ min ########
                    accent(img, 'tilde', c1, c2, p3, p4, couleur, epaisseur, rotation)
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a), couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(p3, p4, b, a), couleur, ep)
                elif char == 'a6': ## Ecrit : [ ## ## Brackets 1 ###
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, p3, cb, couleur, epaisseur)
                elif char == 'b6': ## Ecrit : ] ## ## Brackets 2 ###
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p2, ch, couleur, epaisseur)
                    ligne(img, p4, cb, couleur, epaisseur)
                elif char == 'c6': ## Ecrit : Α ## ## Alpha maj ####
                    ligne(img, ch, p3, couleur, epaisseur)
                    ligne(img, ch, p4, couleur, epaisseur)
                    ligne(img, pt_sg(ch, p3, 2, 3), pt_sg(ch, p4, 2, 3), couleur, epaisseur)
                elif char == 'd6': ## Ecrit : Β ## ## Beta maj #####
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    ligne(img, p3, cb, couleur, epaisseur)
                    cercle(img, ct_sg(ct, ch), dist(ct, ch) / 2, couleur, epaisseur, -90, 90, rotation)
                    cercle(img, ct_sg(ct, cb), dist(ct, cb) / 2, couleur, epaisseur, -90, 90, rotation)
                elif char == 'e6': ## Ecrit : Γ ## ## Gamma maj ####
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ct_sg(ch, p2), couleur, epaisseur)
                elif char == 'f6': ## Ecrit : Δ ## ## Delsta maj ###
                    ligne(img, p3, p4, couleur, epaisseur)
                    ligne(img, p3, ch, couleur, epaisseur)
                    ligne(img, p4, ch, couleur, epaisseur)
                elif char == 'g6': ## Ecrit : Ε ## ## Epsilon maj ##
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, cg, pt_sg(ct, cd, 3, 1), couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'h6': ## Ecrit : Ζ ## ## Zita maj #####
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'i6': ## Ecrit : Η ## ## Ita maj ######
                    ligne(img, pt_sg(p1, ch, 3, 1), pt_sg(p3, cb, 3, 1), couleur, epaisseur)
                    ligne(img, pt_sg(p2, ch, 3, 1), pt_sg(p4, cb, 3, 1), couleur, epaisseur)
                    ligne(img, pt_sg(cg, ct, 3, 1), pt_sg(cd, ct, 3, 1), couleur, epaisseur)
                elif char == 'j6': ## Ecrit : Θ ## ## Theta maj ####
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cg)), couleur, epaisseur, 0, 360, 90 + rotation)
                    ligne(img, cg, cd, couleur, epaisseur)
                elif char == 'k6': ## Ecrit : Ι ## ## Iota maj #####
                    ligne(img, ct_sg(p1, ch), ct_sg(p2, ch), couleur, epaisseur)
                    ligne(img, ct_sg(p3, cb), ct_sg(p4, cb), couleur, epaisseur)
                    ligne(img, ch, cb, couleur, epaisseur)
                elif char == 'l6': ## Ecrit : Κ ## ## Kappa maj ####
                    ligne(img, ct_sg(p1, ch), ct_sg(p3, cb), couleur, epaisseur)
                    ligne(img, ct_sg(ct, cg), p2, couleur, epaisseur)
                    ligne(img, pt_sg(ct_sg(ct, cg), pt_sg(ct_sg(ct, cg), p2), 3, 2), p4, couleur, epaisseur)
                elif char == 'm6': ## Ecrit : Λ ## ## Lambda maj ###
                    ligne(img, p3, ch, couleur, epaisseur)
                    ligne(img, p4, ch, couleur, epaisseur)
                elif char == 'n6': ## Ecrit : Μ ## ## Mi maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p2, ct, couleur, epaisseur)
                elif char == 'o6': ## Ecrit : Ν ## ## Ni maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p1, p4, couleur, epaisseur)
                elif char == 'p6': ## Ecrit : Ξ ## ## Ksi maj ######
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                    ligne(img, ct_sg(cg, ct), ct_sg(cd, ct), couleur, epaisseur)
                elif char == 'q6': ## Ecrit : Ο ## ## Omicron maj ##
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cg)), couleur, epaisseur, 0, 360, 90 + rotation)
                elif char == 'a7': ## Ecrit : { ## ## Braces 1 #####
                    ellipse(img, ct_sg(ct, cd), (dist(ct, ch), dist(ct, pt_sg(ct, cd, 1, 5))), couleur, epaisseur, 0, 70, 90 + rotation)
                    ellipse(img, ct_sg(ct, cd), (dist(ct, ch), dist(ct, pt_sg(ct, cd, 1, 5))), couleur, epaisseur, 110, 180, 90 + rotation)
                    ellipse(img, p3, (dist(cg, p3), dist(p3, cb)), couleur, epaisseur, 0, 42, rotation - 90)
                    ellipse(img, p1, (dist(cg, p1), dist(p1, ch)), couleur, epaisseur, 0, -42, 90 + rotation)
                elif char == 'b7': ## Ecrit : } ## ## Braces 2 #####
                    ellipse(img, ct_sg(ct, cg), (dist(ct, ch), dist(ct, pt_sg(ct, cd, 1, 5))), couleur, epaisseur, 0, 70, rotation - 90)
                    ellipse(img, ct_sg(ct, cg), (dist(ct, ch), dist(ct, pt_sg(ct, cd, 1, 5))), couleur, epaisseur, 110, 180, rotation - 90)
                    ellipse(img, p4, (dist(cd, p4), dist(p4, cb)), couleur, epaisseur, 0, -42, rotation - 90)
                    ellipse(img, p2, (dist(cd, p2), dist(p2, ch)), couleur, epaisseur, 0, 42, 90 + rotation)
                elif char == 'c7': ## Ecrit : Π ## ## Pi maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                elif char == 'd7': ## Ecrit : Ρ ## ## Ro maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch), dist(pt_sg(ct, ch), ch), couleur, epaisseur, 0, 180, rotation - 90)
                elif char == 'e7': ## Ecrit : Σ ## ## Sigma maj ####
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p3, ct, couleur, epaisseur)
                    ligne(img, p3, p4)
                elif char == 'f7': ## Ecrit : Σ ## ## Sigma maj 2 ##
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p3, ct, couleur, epaisseur)
                    ligne(img, p3, p4)
                elif char == 'g7': ## Ecrit : Τ ## ## Tau maj ######
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, ch, cb, couleur, epaisseur)
                elif char == 'h7': ## Ecrit : Υ ## ## Upsilon maj ##
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p2, ct, couleur, epaisseur)
                    ligne(img, ct, cb, couleur, epaisseur)
                elif char == 'i7': ## Ecrit : Φ ## ## Phi maj ######
                    ligne(img, ch, cb, couleur, epaisseur)
                    ellipse(img, ct, (dist(pt_sg(ch, ct, 8, 2), ct), dist(pt_sg(cd, ct, 8, 2), ct)), couleur, epaisseur)
                elif char == 'j7': ## Ecrit : Χ ## ## Khi maj ######
                    ligne(img, p1, p4, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                elif char == 'k7': ## Ecrit : Ψ ## ## Psi maj ######
                    ligne(img, ch, cb, couleur, epaisseur)
                    ellipse(img, ch, (dist(ch, ct), dist(ch, ct) - 20), couleur, epaisseur, -90, 90, 90 + rotation)
                elif char == 'l7': ## Ecrit : Ω ## ## Oméga maj ####
                    ellipse(img, pt_sg(ct, cb, 5, 1), (dist(ct, cb), dist(ct, cd)), couleur, epaisseur, -150, 150, -90 + rotation)
                    ligne(img, p3, ct_sg(p3, cb), couleur, epaisseur)
                    ligne(img, p4, ct_sg(p4, cb), couleur, epaisseur)
                elif char == 'm7': ## Ecrit : Σ ## ## Esh maj ######
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p3, ct, couleur, epaisseur)
                    ligne(img, p3, p4)
                elif char == 'n7': ## Rmplit tt ## ## Full square ##
                    rectangle(img, p1, p4, turquoise, plein)
                    pos -= 1
                elif char == 'o7': ## Rmplit tt ## ## Full square ##
                    rectangle(img, p1, p4, rouge, plein)
                    pos -= 1
                elif char == 'p7': ## Rmplit tt ## ## Full square ##
                    rectangle(img, p1, p4, vert, plein)
                    pos -= 1
                elif char == 'q7': ## Rmplit tt ## ## Full square ##
                    rectangle(img, p1, p4, bleu, plein)
                    pos -= 1
                elif char == 'a8': ## Ecrit : < ## ## Plus petit ###
                    ligne(img, pt_sg(p2, cg, 5, 3), ct_sg(cg, ct), couleur, epaisseur)
                    ligne(img, pt_sg(p4, cg, 5, 3), ct_sg(cg, ct), couleur, epaisseur)
                elif char == 'b8': ## Ecrit : > ## ## Plus gramd ###
                    ligne(img, pt_sg(p1, cd, 5, 3), ct_sg(cd, ct), couleur, epaisseur)
                    ligne(img, pt_sg(p3, cd, 5, 3), ct_sg(cd, ct), couleur, epaisseur)
                elif char == 'c8': ## Ecrit : α ## ## Alpha min ####
                    ellipse(img, ct_sg(ctb, ct_sg(cg, p3)), (dist(ct, ctb)/2, dist(ct, cb)/2), couleur, ep, angle=rotation)
                    ellipse(img, ct_sg(ctb, ct_sg(cd, p4)), (dist(ct, ctb)/2, dist(ct, cb)/2), couleur, ep, 90, 270, rotation)
                elif char == 'd8': ## Ecrit : β ## ## Beta min #####
                    a, b = 15, 4
                    g, d = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b)), ct_sg(pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a))
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(pt_sg(p1, p2, a, b), pt_sg(cg, cd, a, b), 20, 19), couleur, ep)
                    ctbb = ct_sg(ct_sg(ctb, cb), ctb)
                    ctbb = coosCercle(ctbb, ep/5, -90+rotation)
                    ellipse(img, ctbb, (dist(ct, cd)/2, dist(ctbb, cb)), couleur, ep, -90, 90, rotation)
                    cthh = ct_sg(cth, ct)
                    cthh = coosCercle(cthh, ep, 180+rotation)
                    ellipse(img, cthh, (dist(ct, cd)/2, dist(ctbb, cb)), couleur, ep, -125, 60, rotation)
                elif char == 'e8': ## Ecrit : γ ## ## Gamma min ####
                    a, b = 15, 4
                    ligne(img, cb, pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, cb, pt_sg(cd, cg, a, b), couleur, ep)
                    ellipse(img, ct_sg(bg, bd), [ep/2, ep], couleur, ep, angle=rotation)
                elif char == 'f8': ## Ecrit : δ ## ## Delta min ####
                    a, b = 15, 4
                    g, d = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b)), ct_sg(pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a))
                    ligne(img, cth, ct_sg(pt_sg(ct, cd, 7, 8), pt_sg(cb, p4, 3, 4)), couleur, ep)
                    ligne(img, cth, ct_sg(pt_sg(p1, p2, b, a), pt_sg(cg, cd, b, a)))
                    ellipse(img, ctb, (dist(ct, cd)/2, dist(ctb, cb)), couleur, ep, angle=rotation)
                elif char == 'g8': ## Ecrit : ε ## ## Epsilon min ## ζθξτφχψωʃ
                    ellipse(img, ct_sg(ctb, ct), (dist(ct, cb)/2, dist(ct, ctb)/2), couleur, ep, 70, 315, angle=rotation)
                    ellipse(img, ct_sg(ctb, cb), (dist(ct, cb)/2, dist(ct, ctb)/2), couleur, ep, 45, 290, rotation)
                elif char == 'h8': ## Ecrit : ζ ## ## Zita min #####
                    pass
                elif char == 'i8': ## Ecrit : η ## ## Ita min ######
                    ptd = ct_sg(pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a))
                    ligne(img, pt_sg(cg, cd, b, a), coosCercle(ptd, dist(ctb, ct)*1.5, 90), couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b), couleur, ep)
                elif char == 'j8': ## Ecrit : θ ## ## Theta min ####
                    pass
                elif char == 'k8': ## Ecrit : ι ## ## Iota min #####
                    ligne(img, ctb, ct, couleur, ep)
                    ptt = ct_sg(ct_sg(cd, ct), ct_sg(p4, cb))
                    ellipse(img, ptt, [dist(ptt, ctb), dist(ctb, cb)], couleur, ep, 90, 180)
                elif char == 'l8': ## Ecrit : κ ## ## Kappa min ####
                    g = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b))
                    ct = ct_sg(pt_sg(ct, cb), g)
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, ct, g, couleur, ep)
                    ligne(img, ct, pt_sg(cg, cd, b, a), couleur, ep)
                    ligne(img, ct, pt_sg(p3, p4, b, a), couleur, ep)
                elif char == 'm8': ## Ecrit : λ ## ## Lambda min ###
                    a, b = 15, 4
                    ligne(img, ct, pt_sg(p3, p4, a, b), couleur, ep)
                    ligne(img, pt_sg(p1, p2, a, b), pt_sg(p4, p3, a, b), couleur, ep)
                elif char == 'n8': ## Ecrit : μ ## ## Mi min #######
                    ptg = ct_sg(pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b))
                    ligne(img, pt_sg(cg, cd, a, b), coosCercle(ptg, dist(ctb, ct)*1.5, 90), couleur, ep)
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(p3, p4, b, a), couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a), couleur, ep)
                elif char == 'o8': ## Ecrit : ν ## ## Ni min #######
                    a, b = 15, 4
                    ligne(img, cb, pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, cb, pt_sg(cd, cg, a, b), couleur, ep)
                elif char == 'p8': ## Ecrit : ξ ## ## Ksi min ######
                    pass
                elif char == 'q8': ## Ecrit : ο ## ## Omicron min ##
                    ellipse(img, ctb, (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, angle=rotation)
                elif char == 'a9': ## Ecrit : ` ## ## Ouvert #######
                    accent(img, 'ouvert', p1, p2, c1, c2, couleur, epaisseur)
                    pos -= 1
                elif char == 'b9': ## Ecrit : ´ ## ## Fermé ########
                    accent(img, 'ferme', p1, p2, c1, c2, couleur, epaisseur)
                    pos -= 1
                elif char == 'c9': ## Ecrit : π ## ## Pi min #######
                    ligne(img, pt_sg(p3, p4, a, b), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, pt_sg(p3, p4, b, a), pt_sg(cg, cd, b, a), couleur, ep)
                    ligne(img, pt_sg(cg, cd, a, b), pt_sg(cg, cd, b, a), couleur, ep)
                elif char == 'd9': ## Ecrit : ρ ## ## Ro min #######
                    ellipse(img, ctb, (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, angle=rotation)
                    ptg = coosCercle(ctb, dist(ctb, ct), 180)
                    ligne(img, ptg, coosCercle(ptg, dist(ctb, ct)*1.5, 90), couleur, ep)
                elif char == 'e9': ## Ecrit : σ ## ## Sigma min ####
                    ellipse(img, ctb, (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, angle=rotation)
                    ligne(img, ct, coosCercle(ct, dist(ctb, ct)*1.5, 0), couleur, ep)
                elif char == 'f9': ## Ecrit : ς ## ## Sigma 2 min ##
                    ellipse(img, ctb, (dist(ct, ctb), dist(ct, cb)/2), couleur, ep, 60, 300, angle=rotation)
                    ptg = coosCercle(ctb, dist(ctb, ct), 180)
                    ellipse(img, ptg, (dist(ct, ctb)*2, dist(ct, cb)*0.9), couleur, ep, 30, 80, angle=rotation)
                elif char == 'g9': ## Ecrit : τ ## ## Tau  min #####
                    pass
                elif char == 'h9': ## Ecrit : υ ## ## Upsilon min ##
                    a, b = 15, 4
                    g = ct_sg(p3, cg)
                    d = ct_sg(p4, cd)
                    ellipse(img, ctb, (dist(ctb, g)*0.575, dist(ctb, g)*0.75), couleur, ep, 0, 180, rotation)
                    ligne(img, ct_sg(g, cg), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, pt_sg(g, d, a, b), pt_sg(cg, cd, a, b), couleur, ep)
                    ligne(img, pt_sg(d, g, a, b), pt_sg(cd, cg, a, b), couleur, ep)
                elif char == 'i9': ## Ecrit : φ ## ## phi min ######
                    pass
                elif char == 'j9': ## Ecrit : χ ## ## Khi min ######
                    pass
                elif char == 'k9': ## Ecrit : ψ ## ## Psi min ######
                    pass
                elif char == 'l9': ## Ecrit : ω ## ## Omega min ####
                    pass
                elif char == 'm9': ## Ecrit : ʃ ## ## Esh min ######
                    pass
                elif char == 'n9': ## Rmplit tt ## ## Full square ##
                    rectangle(img, p1, p4, turquoise, epaisseur)
                    pos -= 1
                elif char == 'o9': ## Rmplit tt ## ## Full square ##
                    rectangle(img, p1, p4, rouge, epaisseur)
                    pos -= 1
                elif char == 'p9': ## Rmplit tt ## ## Full square ##
                    rectangle(img, p1, p4, vert, epaisseur)
                    pos -= 1
                elif char == 'q9': ## Rmplit tt ## ## Full square ##
                    rectangle(img, p1, p4, bleu, epaisseur)
                    pos -= 1
                elif char == 'a10': ## Ecrit : ^ ## ## Circonflexe##
                    ligne(img, c1, ch, couleur, epaisseur)
                    ligne(img, c2, ch, couleur, epaisseur)
                    pos -= 1
                elif char == 'b10': ## Ecrit : ˇ ## ## Caron #######
                    ligne(img, p1, ct_sg(c1, c2), couleur, epaisseur)
                    ligne(img, p2, ct_sg(c1, c2), couleur, epaisseur)
                    pos -= 1
                elif char == 'c10': ## Ecrit : - ## ## Tiret court##
                    ligne(img, ct_sg(cg, ct), ct_sg(cd, ct), couleur, epaisseur)
                elif char == 'd10': ## Ecrit : - ## ## tiret moyen##
                    ligne(img, pt_sg(cg, ct, 2, 1), pt_sg(cd, ct, 2, 1), couleur, epaisseur)
                elif char == 'e10': ## Ecrit : - ## ## Tiret long ##
                    ligne(img, cg, cd, couleur, epaisseur)
                elif char == 'f10': ## Ecrit : _ ## ## Underscore ##
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'g10': ## Ecrit : _ ## ## Topscore ####
                    ligne(img, p1, p2, couleur, epaisseur)
                elif char == 'h10': ## Ecrit : / ## ## Slash #######
                    ligne(img, ct_sg(p2, ch), ct_sg(p3, cb), couleur, epaisseur)
                elif char == 'i10': ## Ecrit : \ ## ## Backslash ###
                    ligne(img, ct_sg(p1, ch), ct_sg(p4, cb), couleur, epaisseur)
                elif char == 'j10': ## Ecrit : | ## ## Bar #########
                    ligne(img, ch, cb, couleur, epaisseur)
                elif char == 'k10': ## Ecrit : ¦ ## ## Broken bar ##
                    ligne(img, ch, pt_sg(ch, ct, 4, 13), couleur, epaisseur)
                    ligne(img, cb, pt_sg(cb, ct, 4, 13), couleur, epaisseur)
                elif char == 'l10': ## Ecrit : † ## ## Croix #######
                    ligne(img, ch, cb, couleur, epaisseur)
                    ligne(img, ct1, ct2, couleur, epaisseur)
                elif char == 'm10': ## Ecrit : ‡ ## ## DoubleCroix##
                    ligne(img, ch, cb, couleur, epaisseur)
                    ligne(img, ct1, ct2, couleur, epaisseur)
                    ligne(img, ct3, ct4, couleur, epaisseur)
                elif char == 'n10': ## Ecrit : = ## ## Égal ########
                    ligne(img, ct1, ct2, couleur, epaisseur)
                    ligne(img, ct3, ct4, couleur, epaisseur)
                elif char == 'o10': ## Ecrit : = ## ## Pas égal ####
                    poin1, poin2 = ct_sg(p2, ch), ct_sg(p3, cb)
                    aa, bb = 1, 7
                    ligne(img, pt_sg(poin1, poin2, aa, bb), pt_sg(poin1, poin2, bb, aa), couleur, epaisseur)
                    ligne(img, ct1, ct2, couleur, epaisseur)
                    ligne(img, ct3, ct4, couleur, epaisseur)
                elif char == 'p10': ## Ecrit : ~ ## ## Aprox #######
                    accent(img, 'tilde', cg, cd, p3, p4, couleur, epaisseur, rotation)
                elif char == 'q10': ## Ecrit : * ## ## Astérisque ##
                    p1 = pt_sg(ch, p1, 3, 4)
                    p2 = pt_sg(ch, p2, 3, 4)
                    p3 = pt_sg(ct, cg, 3, 4)
                    p4 = pt_sg(ct, cd, 3, 4)
                    ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
                    ch = ct_sg(p1, p2)
                    cg = ct_sg(p1, p3)
                    cd = ct_sg(p2, p4)
                    cb = ct_sg(p3, p4)
                    div = 2.5
                    ligne(img, ct_sg(ch, ct), ct_sg(cb, ct), couleur, epaisseur / div)
                    ligne(img, ct_sg(ct_sg(p1, ct), ct_sg(cg, ct)), ct_sg(ct_sg(p4, ct), ct_sg(cd, ct)), couleur, epaisseur / div)
                    ligne(img, ct_sg(ct_sg(p2, ct), ct_sg(cd, ct)), ct_sg(ct_sg(p3, ct), ct_sg(cg, ct)), couleur, epaisseur / div)
                elif char == 'a11': ## Ecrit : ˝ ## ## DeuxAccents##
                    ligne(img, c1, ch, couleur, epaisseur)
                    ligne(img, ct_sg(c1, c2), p2, couleur, epaisseur)
                    pos -= 1
                elif char == 'b11': ## Ecrit : ̏  ## ## DeuxAccents##
                    ligne(img, c2, ch, couleur, epaisseur)
                    ligne(img, ct_sg(c1, c2), p1, couleur, epaisseur)
                    pos -= 1
                elif char == 'c11': ## Ecrit : @ ## ## Arrobas ##### ## À refaire ##
                    pass
                elif char == 'd11': ## Ecrit : & ## ## Esperluette## ## À refaire ##
                    pass
                elif char == 'e11': ## Ecrit : $ ## ## Dollar ######
                    tour = 225
                    cercle(img, ct_sg(cg, p2), dist(ct_sg(cg, p2), ct), couleur, epaisseur, 0, tour, 90 + rotation)
                    cercle(img, ct_sg(cg, p4), dist(ct_sg(cg, p4), ct), couleur, epaisseur, 0, tour, -90 + rotation)
                    ligne(img, pt_sg(p2, ch, 3, 8), pt_sg(p3, cb, 3, 8), couleur, epaisseur)
                elif char == 'f11': ## Ecrit : € ## ## Euro ########
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cd)), couleur, epaisseur, -45, 225, 90 + rotation)
                    ligne(img, pt_sg(p1, p3, 8, 5), pt_sg(pt_sg(ch, p2, 3, 1), pt_sg(cb, p4, 3, 1), 8, 5), couleur, epaisseur)
                    ligne(img, pt_sg(p1, p3, 5, 8), pt_sg(pt_sg(ch, p2, 3, 1), pt_sg(cb, p4, 3, 1), 5, 8), couleur, epaisseur)
                elif char == 'g11': ## Ecrit : ¥ ## ## Yens ########
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p2, ct, couleur, epaisseur)
                    ligne(img, ct, cb, couleur, epaisseur)
                    ligne(img, cg, cd, couleur, epaisseur)
                    ligne(img, ct_sg(p3, cg), ct_sg(p4, cd), couleur, epaisseur)
                elif char == 'h11': ## Ecrit : £ ## ## Livre #######
                    ellipse(img, pt_sg(ct_sg(ct, ch), ct_sg(p2, cd), 2, 1), (dist(pt_sg(ct_sg(ct, ch), ct_sg(p2, cd), 2, 1), ct_sg(p1, ct)), dist(ct_sg(ct, ch), ch)), couleur, epaisseur, 0, 180, 180 + rotation)
                    ligne(img, ct_sg(p1, ct), ct_sg(p3, cb), couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                elif char == 'i11': ## Ecrit : ' ## ## Apostrophe ##
                    ligne(img, ch, ct_sg(ch, ct), couleur, epaisseur)
                elif char == 'j11': ## Ecrit : " ## ## GuillemetsH##
                    ligne(img, pt_sg(p1, p2, 7, 4), pt_sg(ct_sg(p1, cg), ct_sg(p2, cd), 7, 4), couleur, epaisseur)
                    ligne(img, pt_sg(p1, p2, 4, 7), pt_sg(ct_sg(p1, cg), ct_sg(p2, cd), 4, 7), couleur, epaisseur)
                elif char == 'k11': ## Ecrit : ¬ ## ## Pas [qqc] ###
                    ligne(img, ct1, ct2, couleur, epaisseur)
                    ligne(img, ct2, ct_sg(ctd, ct2), couleur, epaisseur)
                elif char == 'l11': ## Ecrit : » ## ## GuillemetsO##
                    ligne(img, c1, ct, couleur, epaisseur)
                    ligne(img, c3, ct, couleur, epaisseur)
                    ligne(img, ct_sg(c1, c2), cd, couleur, epaisseur)
                    ligne(img, ct_sg(c3, c4), cd, couleur, epaisseur)
                elif char == 'm11': ## Ecrit : « ## ## GuillemetsF##
                    ligne(img, c2, ct, couleur, epaisseur)
                    ligne(img, c4, ct, couleur, epaisseur)
                    ligne(img, ct_sg(c1, c2), cg, couleur, epaisseur)
                    ligne(img, ct_sg(c3, c4), cg, couleur, epaisseur)
                elif char == 'n11': ## Ecrit : ™ ## ## Trade Mark ##
                    c1, c2 = p1, p2
                    c3, c4 = cg, cd
                    ct = ct_sg(ct_sg(c1, c4), ct_sg(c2, c3))
                    ligne(img, ct_sg(c1, c2), ct_sg(ct, cd), couleur, epaisseur)
                    ligne(img, c2, ct_sg(ct, cd), couleur, epaisseur)
                    ligne(img, ct_sg(c1, c2), c1, couleur, epaisseur)
                    ligne(img, ct_sg(c1, c2), ct_sg(c3, c4), couleur, epaisseur)
                    ligne(img, c2, c4, couleur, epaisseur)
                    ligne(img, ct_sg(c1, ct_sg(c1, c2)), ct_sg(c3, ct_sg(c3, c4)), couleur, epaisseur)
                elif char == 'o11': ## Ecrit : ® ## ## Registered ##
                    c1, c2 = p1, p2
                    c3, c4 = cg, cd
                    ch = ct_sg(c1, c2)
                    cb = ct_sg(c3, c4)
                    cg = ct_sg(c1, c3)
                    cd = ct_sg(c2, c4)
                    ct = ct_sg(ct_sg(c1, c4), ct_sg(c2, c3))
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cd)), couleur, epaisseur)
                    c1 = ct_sg(c1, ct)
                    c2 = ct_sg(c2, ct)
                    c3 = ct_sg(c3, ct)
                    c4 = ct_sg(c4, ct)
                    ch = ct_sg(c1, c2)
                    cb = ct_sg(c3, c4)
                    cg = ct_sg(c1, c3)
                    cd = ct_sg(c2, c4)
                    ligne(img, c1, c3, couleur, epaisseur / 2)
                    ligne(img, c1, ch, couleur, epaisseur / 2)
                    ligne(img, cg, ct, couleur, epaisseur / 2)
                    ligne(img, c4, ct, couleur, epaisseur / 2)
                    cercle(img, pt_sg(ct, ch), dist(pt_sg(ct, ch), ch), couleur, epaisseur / 2, 0, 180, -90 + rotation)
                elif char == 'p11': ## Ecrit : © ## ## Copyright ###
                    c1, c2 = p1, p2
                    c3, c4 = cg, cd
                    ch = ct_sg(c1, c2)
                    cb = ct_sg(c3, c4)
                    cg = ct_sg(c1, c3)
                    cd = ct_sg(c2, c4)
                    ct = ct_sg(ct_sg(c1, c4), ct_sg(c2, c3))
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cd)), couleur, epaisseur)
                    c1 = ct_sg(c1, ct)
                    c2 = ct_sg(c2, ct)
                    c3 = ct_sg(c3, ct)
                    c4 = ct_sg(c4, ct)
                    ch = ct_sg(c1, c2)
                    cb = ct_sg(c3, c4)
                    cg = ct_sg(c1, c3)
                    cd = ct_sg(c2, c4)
                    ellipse(img, pt_sg(cg, cd, 7, 6), [dist(c2, cd), dist(ct, cd)], couleur, epaisseur / 2, -20, 200, 90 + rotation)
                elif char == 'q11': ## Ecrit : 🄯 ## ## Copyleft ####
                    c1, c2 = p1, p2
                    c3, c4 = cg, cd
                    ch = ct_sg(c1, c2)
                    cb = ct_sg(c3, c4)
                    cg = ct_sg(c1, c3)
                    cd = ct_sg(c2, c4)
                    ct = ct_sg(ct_sg(c1, c4), ct_sg(c2, c3))
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cd)), couleur, epaisseur)
                    c1 = ct_sg(c1, ct)
                    c2 = ct_sg(c2, ct)
                    c3 = ct_sg(c3, ct)
                    c4 = ct_sg(c4, ct)
                    ch = ct_sg(c1, c2)
                    cb = ct_sg(c3, c4)
                    cg = ct_sg(c1, c3)
                    cd = ct_sg(c2, c4)
                    ellipse(img, pt_sg(cg, cd, 6, 7), [dist(c2, cd), dist(ct, cd)], couleur, epaisseur / 2, -20, 200, -90 + rotation)
                elif char == 'a12': ## Ecrit : ¨ ## ## Diæresis ####
                    cercle(img, ct_sg(cg, ch), int(epaisseur*0.675), couleur, plein)
                    cercle(img, ct_sg(cd, ch), int(epaisseur*0.675), couleur, plein)
                    pos -= 1
                elif char == 'b12': ## Ecrit : ¨ ## ## Dot above ###
                    cercle(img, ct_sg(ct, ch), epaisseur / 2, couleur, plein)
                    pos -= 1
                elif char == 'c12': ## Ecrit : . ## ## Point #######
                    cercle(img, cb, int(epaisseur*0.675), couleur, plein)
                elif char == 'd12': ## Ecrit : , ## ## Virgule #####
                    ligne(img, cb, pt_sg(cb, cd, 11, 2), couleur, epaisseur)
                elif char == 'e12': ## Ecrit : , ## ## A-Virgule ###
                    ligne(img, cb, pt_sg(cb, cg, 11, 2), couleur, epaisseur)
                elif char == 'f12': ## Ecrit : : ## ## DeuxPoints ##
                    cercle(img, cth, int(epaisseur*0.675), couleur, plein)
                    cercle(img, ctb, int(epaisseur*0.675), couleur, plein)
                elif char == 'g12': ## Ecrit : ; ## ##PointVirgule##
                    cercle(img, ct, int(epaisseur*0.675), couleur, plein)
                    ligne(img, cb, pt_sg(cb, cd, 11, 2), couleur, epaisseur)
                elif char == 'h12': ## Ecrit : º ## ## Degres ######
                    cercle(img, ct_sg(ct, ch), epaisseur, couleur, epaisseur / 1.25)
                elif char == 'i12': ## Ecrit : º ## ## Masculin ####
                    cercle(img, ct_sg(ct, ch), epaisseur * 0.8, couleur, epaisseur / 1.25)
                    ligne(img, ct_sg(p3, ch), ct_sg(p4, ch), couleur, epaisseur)
                elif char == 'j12': ## Ecrit : ª ## ## Féminin #####
                    rectangle(img, coosCercle(ct_sg(ct, ch), epaisseur, rotation - 45), coosCercle(ct_sg(ct, ch), epaisseur, rotation - 45 + 180), couleur, epaisseur * 0.8)
                    ligne(img, ct_sg(p3, ch), ct_sg(p4, ch), couleur, epaisseur)
                elif char == 'k12': ## Ecrit : · ## ## PointMédian##
                    cercle(img, ct, int(epaisseur*0.675), couleur, plein)
                elif char == 'l12': ## Ecrit : % ## ## Pourcent ####
                    cercle(img, ct_sg(ct, p1), epaisseur, couleur, epaisseur / 1.25)
                    cercle(img, ct_sg(ct, p4), epaisseur, couleur, epaisseur / 1.25)
                    ligne(img, ct_sg(ct, p2), ct_sg(ct, p3), couleur, epaisseur)
                elif char == 'm12': ## Ecrit : % ## ## Pourmille ###
                    cercle(img, ct_sg(ct, p1), epaisseur, couleur, epaisseur / 1.25)
                    cercle(img, ct_sg(ct_sg(ct, cb), ct_sg(p4, ct)), epaisseur, couleur, epaisseur / 1.25)
                    cercle(img, ct_sg(cd, p4), epaisseur, couleur, epaisseur / 1.25)
                    ligne(img, ct_sg(ct, p2), ct_sg(ct, p3), couleur, epaisseur)
                elif char == 'n12': ## Ecrit : § ## ## Paragraphe ##
                    cercle(img, ct, dist(ct, ct_sg(ct, cd)), couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch, 1, 2), dist(ct, ct_sg(ct, cd)), couleur, epaisseur, 0, 250, 90 + rotation)
                    cercle(img, pt_sg(ct, cb, 1, 2), dist(ct, ct_sg(ct, cd)), couleur, epaisseur, 0, 250, -90 + rotation)
                elif char == 'o12': ## Ecrit : ¶ ## ## Capitulum ###
                    ligne(img, pt_sg(p1, p2, 2, 1), pt_sg(p3, p4, 2, 1), couleur, epaisseur)
                    ligne(img, pt_sg(p1, p2, 1, 2), pt_sg(p3, p4, 1, 2), couleur, epaisseur)
                    ligne(img, pt_sg(p1, p2, 1, 2), pt_sg(p1, p2, 2, 1), couleur, epaisseur)
                    cercle(img, ct_sg(pt_sg(p1, p2, 2, 1), pt_sg(cg, cd, 2, 1)), dist(pt_sg(p1, p2, 2, 1), ct_sg(pt_sg(p1, p2, 2, 1), pt_sg(cg, cd, 2, 1))), couleur, -epaisseur, 0, 180, 90 + rotation)
                elif char == 'p12': ## Ecrit : ♯ ## ## Dièse #######
                    ligne(img, ct_sg(ch, c1), ct_sg(p3, cb), couleur, epaisseur)
                    ligne(img, ct_sg(ch, p2), ct_sg(c4, cb), couleur, epaisseur)
                    ligne(img, ct_sg(c1, cg), ct_sg(c2, p2), couleur, epaisseur)
                    ligne(img, ct_sg(c3, p3), ct_sg(c4, cd), couleur, epaisseur)
                elif char == 'q12': ## Ecrit : ♭ ## ## Bémol #######
                    ligne(img, ct_sg(ch, c1), ct_sg(p3, cb), couleur, epaisseur)
                    cercle(img, pt_sg(ct_sg(ch, c1), ct_sg(p3, cb), 1, 3), dist(pt_sg(ct_sg(ch, c1), ct_sg(p3, cb), 1, 3), ct_sg(p3, cb)), couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'a13': ## Ecrit : ſ ## ## S long min ##
                    ligne(img, cg, ct_sg(cg, ct), couleur, epaisseur)
                    ligne(img, ct_sg(ch, cg), ct_sg(p3, cb), couleur, epaisseur)
                    ellipse(img, ct_sg(ch, ct), (dist(ct_sg(ch, ct), ct_sg(ch, cg)), dist(ct_sg(ch, ct), ch)), couleur, epaisseur, 0, 180, 180 + rotation)
                elif char == 'b13': ## Ecrit : ~ ## ## Tilde #######
                    accent(img, 'tilde', p1, p2, cg, cd, couleur, epaisseur, rotation)
                elif char == 'c13': ## Ecrit : ß ## ## Eszett min ##
                    ligne(img, ct_sg(ch, cg), ct_sg(p3, cb), couleur, epaisseur)
                    ellipse(img, ct_sg(ct, cb), (dist(ct, cb) / 2, dist(ct, cd) / 2), couleur, epaisseur, 0, 180, -90 + rotation)
                    ellipse(img, ct_sg(ch, ct), (dist(ct_sg(ch, ct), ct_sg(ch, cg)), dist(ct_sg(ch, ct), ch)), couleur, epaisseur, 0, 270, 180 + rotation)
                elif char == 'd13': ## Ecrit : ẞ ## ## Eszett maj ##
                    ligne(img, ct_sg(ch, cg), ct_sg(p3, cb), couleur, epaisseur)
                    ellipse(img, ct_sg(ct, cb), (dist(ct, cb) / 2, dist(ct, cd) / 1.5), couleur, epaisseur, 0, 180, -90 + rotation)
                    ellipse(img, ct_sg(ch, ct), (dist(ct_sg(ch, ct), ct_sg(ch, cg)), dist(ct_sg(ch, ct), ch)), couleur, epaisseur, 0, 270, 180 + rotation)
                elif char == 'e13': ## Ecrit : þ ## ## Thorn min ###
                    ligne(img, ct_sg(p1, ch), ct_sg(p3, cb), couleur, epaisseur)
                    cercle(img, ct_sg(ct_sg(p1, ch), ct_sg(p3, cb)), dist(ct_sg(ct_sg(p1, ch), ct_sg(p3, cb)), ct) * 1.25, couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'f13': ## Ecrit : Þ ## ## Thorn maj ###
                    ligne(img, ct_sg(p1, ch), ct_sg(p3, cb), couleur, epaisseur)
                    cercle(img, ct_sg(ct_sg(p1, ch), ct_sg(p3, cb)), dist(ct_sg(ct_sg(p1, ch), ct_sg(p3, cb)), ct) * 1.75, couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'g13': ## Ecrit : ð ## ## Eth min #####
                    pass
                elif char == 'h13': ## Ecrit : Ð ## ## Eth maj #####
                    ellipse(img, pt_sg(ct, cg, 8, 5), [dist(p2, cd), dist(ct, cd)], couleur, epaisseur, 0, 180, -90 + rotation)
                    ligne(img, pt_sg(p1, ch, 3, 4), pt_sg(p3, cb, 3, 4), couleur, epaisseur)
                    ligne(img, cd, ct, couleur, epaisseur)
                elif char == 'i13': ## Ecrit : ŋ ## ## Eng min #####
                    pass
                elif char == 'j13': ## Ecrit : Ŋ ## ## Eng maj #####
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p1, p4, couleur, epaisseur)
                    arc(img, p4, ct_sg(ct_sg(ct_sg(bg, bd), cb), p4), 5, couleur, epaisseur)
                elif char == 'k13': ## Ecrit : ʒ ## ## Ej min ######
                    ligne(img, c1, c2, couleur, epaisseur)
                    ligne(img, c2, ct, couleur, epaisseur)
                    ellipse(img, ct_sg(ct, cb), (dist(p3, ct_sg(cg, p3)), dist(ct_sg(cg, p3), ct_sg(ct, cb))), couleur, epaisseur, 0, 270, -90 + rotation)
                elif char == 'l13': ## Ecrit : Ʒ ## ## Ej maj ######
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, p2, ct, couleur, epaisseur)
                    ellipse(img, ct_sg(ct, cb), (dist(p3, ct_sg(cg, p3)), dist(ct_sg(cg, p3), ct_sg(ct, cb))), couleur, epaisseur, 0, 270, -90 + rotation)
                elif char == 'm13': ## Ecrit : C ## ## C sharp #####
                    ellipse(img, pt_sg(ct, cd, 8, 5), [dist(p2, cd), dist(ct, cd)], couleur, epaisseur, -20, 200, 90 + rotation)
                    p1 = ct_sg(ch, ct)
                    p3 = ct_sg(cb, ct)
                    p2 = ct_sg(p2, ct)
                    p4 = ct_sg(p4, ct)
                    ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
                    c1 = ct_sg(c1, ct)
                    c2 = ct_sg(c2, ct)
                    c3 = ct_sg(c3, ct)
                    c4 = ct_sg(c4, ct)
                    ch = ct_sg(p1, p2)
                    cb = ct_sg(p3, p4)
                    epaisseur /= 2
                    ligne(img, c1, c2, couleur, epaisseur)
                    ligne(img, c3, c4, couleur, epaisseur)
                    ligne(img, pt_sg(p1, ch, 8, 1), pt_sg(p3, cb, 10, 1), couleur, epaisseur)
                    ligne(img, pt_sg(p2, ch, 2, 1), pt_sg(p4, cb, 1, 2), couleur, epaisseur)
                elif char == 'n13': ## Ecrit : C ## ## C plus plus##
                    ellipse(img, pt_sg(ct, cd, 8, 5), [dist(p2, cd), dist(ct, cd)], couleur, epaisseur, -20, 200, 90 + rotation)
                    epaisseur /= 2
                    ligne(img, pt_sg(ct, ch, 4, 2), pt_sg(ct, cb, 4, 2), couleur, epaisseur)
                    ligne(img, pt_sg(cd, cg, 1, 2), cd, couleur, epaisseur)
                    ligne(img, pt_sg(pt_sg(ch, ct, 2, 4), pt_sg(p2, cd, 2, 4), 2, 4), pt_sg(pt_sg(cb, ct, 2, 4), pt_sg(p4, cd, 2, 4), 2, 4), couleur, epaisseur)
                elif char == 'o13': ## Ecrit : P ## ## Python ######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch), dist(pt_sg(ct, ch), ch), couleur, epaisseur, 0, 180, -90 + rotation)
                    pass
                elif char == 'p13': ## Ecrit : H ## ## Html ########
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, ct_sg(ch, p1), ct_sg(p3, cb), couleur, epaisseur)
                    ligne(img, cg, ct_sg(cg, ct), couleur, epaisseur)
                    ligne(img, ch, p2, couleur, epaisseur)
                    ligne(img, ct_sg(p4, cb), p4, couleur, epaisseur)
                    ligne(img, ct_sg(p4, cb), ct_sg(ct_sg(p4, cb), ct_sg(ct, cd)), couleur, epaisseur)
                    ligne(img, ct_sg(ch, p2), ct_sg(ct_sg(ch, p2), ct_sg(ct, cd)), couleur, epaisseur)
                    ligne(img, ct_sg(cd, ct), ct_sg(cd, p2), couleur, epaisseur)
                    ligne(img, ct_sg(cd, ct), ct_sg(ch, ct), couleur, epaisseur)
                    ligne(img, ct_sg(cd, p2), ct_sg(cd, p4), couleur, epaisseur)
                    ligne(img, ct_sg(ch, ct), ct_sg(ct, cb), couleur, epaisseur)
                elif char == 'q13': ## Ecrit : ? ## ## UnicodeErr ##
                    carreau(img, ch, [dist(cb, ch), dist(cg, cd)], couleur, plein, rotation + 90)
                    cercle(img, pt_sg(ct, cb, 2, 7), 3, blanc, 0)
                    ligne(img, ct_sg(ct, cb), pt_sg(ct, cb, 7, 2), blanc, 5)
                    ellipse(img, pt_sg(ch, cb, 13, 9), [dist(cg, cd) // 10 * 3, dist(cg, cd) // 4], blanc, 5, -30, 180, -90 + rotation)
                elif char == 'a14': ## Ecrit : А ## ## А maj #######
                    ligne(img, ch, p3, couleur, epaisseur)
                    ligne(img, ch, p4, couleur, epaisseur)
                    ligne(img, pt_sg(ch, p3, 2, 3), pt_sg(ch, p4, 2, 3), couleur, epaisseur)
                elif char == 'b14': ## Ecrit : Б ## ## Б maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, pt_sg(ch, p2, 1, 2), couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    ligne(img, p3, cb, couleur, epaisseur)
                    cercle(img, ct_sg(ct, cb), dist(ct, cb) / 2, couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'c14': ## Ecrit : В ## ## В maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    ligne(img, p3, cb, couleur, epaisseur)
                    cercle(img, ct_sg(ct, ch), dist(ct, ch) / 2, couleur, epaisseur, 0, 180, -90 + rotation)
                    cercle(img, ct_sg(ct, cb), dist(ct, cb) / 2, couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'd14': ## Ecrit : Г ## ## Г maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, pt_sg(ch, p2, 1, 2), couleur, epaisseur)
                elif char == 'e14': ## Ecrit : Д ## ## Д maj #######
                    ligne(img, c3, c4, couleur, epaisseur)
                    ligne(img, c3, p3, couleur, epaisseur)
                    ligne(img, c4, p4, couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(c3, c4), c3), ct_sg(p1, ch), couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(c4, c3), c4), ct_sg(p2, ch), couleur, epaisseur)
                    ligne(img, ct_sg(p1, ch), ct_sg(p2, ch), couleur, epaisseur)
                elif char == 'f14': ## Ecrit : Е ## ## Е maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, cg, pt_sg(ct, cd, 3, 1), couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'g14': ## Ecrit : Ё ## ## Ё maj #######
                    cercle(img, ct_sg(hg, ct_sg(hg, hd)), epaisseur / 2, couleur, plein)
                    cercle(img, ct_sg(hd, ct_sg(hg, hd)), epaisseur / 2, couleur, plein)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, cg, pt_sg(ct, cd, 3, 1), couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'h14': ## Ecrit : Ж ## ## Ж maj #######
                    ctpg = ct_sg(ct_sg(ct, cg), ct)
                    ctpd = ct_sg(ct_sg(ct, cd), ct)
                    ligne(img, p1, ctpg, couleur, epaisseur)
                    ligne(img, p3, ctpg, couleur, epaisseur)
                    ligne(img, p2, ctpd, couleur, epaisseur)
                    ligne(img, p4, ctpd, couleur, epaisseur)
                    ligne(img, ctpg, ctpd, couleur, epaisseur)
                    ligne(img, ch, cb, couleur, epaisseur)
                elif char == 'i14': ## Ecrit : З ## ## З maj #######
                    cercle(img, ct_sg(ct, ch), dist(ct, ch) / 2, couleur, epaisseur, -40, 200, -90 + rotation)
                    cercle(img, ct_sg(ct, cb), dist(ct, cb) / 2, couleur, epaisseur, -20, 220, -90 + rotation)
                elif char == 'j14': ## Ecrit : И ## ## И maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                elif char == 'k14': ## Ecrit : Й ## ## Й maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                    accent(img, 'breve', hg, hd, p1, p2, couleur, epaisseur, rotation)
                elif char == 'l14': ## Ecrit : К ## ## К maj #######
                    ligne(img, ct_sg(p1, ch), ct_sg(p3, cb), couleur, epaisseur)
                    ligne(img, ct_sg(ct, cg), p2, couleur, epaisseur)
                    ligne(img, pt_sg(ct_sg(ct, cg), pt_sg(ct_sg(ct, cg), p2), 3, 2), p4, couleur, epaisseur)
                elif char == 'm14': ## Ecrit : Л ## ## Л maj #######
                    ligne(img, ct_sg(p1, ch), p2, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ellipse(img, p1, (dist(p1, p3), dist(ct_sg(p1, ch), ch)), couleur, epaisseur, 90, 180, -90 + rotation)
                elif char == 'n14': ## Ecrit : М ## ## М maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p2, ct, couleur, epaisseur)
                elif char == 'o14': ## Ecrit : Н ## ## Н maj #######
                    ligne(img, pt_sg(p1, ch, 3, 1), pt_sg(p3, cb, 3, 1), couleur, epaisseur)
                    ligne(img, pt_sg(p2, ch, 3, 1), pt_sg(p4, cb, 3, 1), couleur, epaisseur)
                    ligne(img, pt_sg(cg, ct, 3, 1), pt_sg(cd, ct, 3, 1), couleur, epaisseur)
                elif char == 'p14': ## Ecrit : О ## ## О maj #######
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cg)), couleur, epaisseur, 0, 360, -90 + rotation)
                elif char == 'q14': ## Ecrit : П ## ## П maj #######
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p3, p1, couleur, epaisseur)
                elif char == 'a15': ## Ecrit : Р ## ## Р maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch), dist(pt_sg(ct, ch), ch), couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'b15': ## Ecrit : С ## ## С maj #######
                    ellipse(img, pt_sg(ct, cd, 8, 5), [dist(p2, cd), dist(ct, cd)], couleur, epaisseur, -20, 200, 90 + rotation)
                elif char == 'c15': ## Ecrit : Т ## ## Т maj #######
                    ligne(img, pt_sg(p1, ch, 4, 1), pt_sg(p2, ch, 4, 1), couleur, epaisseur)
                    ligne(img, ch, cb, couleur, epaisseur)
                elif char == 'd15': ## Ecrit : У ## ## У maj #######
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                elif char == 'e15': ## Ecrit : Ф ## ## Ф maj #######
                    ligne(img, ch, cb, couleur, epaisseur)
                    ellipse(img, ct, (dist(pt_sg(ch, ct, 8, 2), ct), dist(pt_sg(cd, ct, 8, 2), ct)), couleur, epaisseur)
                elif char == 'f15': ## Ecrit : Х ## ## Х maj #######
                    ligne(img, p1, p4, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                elif char == 'g15': ## Ecrit : Ц ## ## Ц maj #######
                    ligne(img, p3, p4, couleur, epaisseur)
                    ligne(img, ct_sg(p2, ch), ct_sg(p4, cb), couleur, epaisseur)
                    ligne(img, p3, p1, couleur, epaisseur)
                    ligne(img, p4, pt_sg(ct_sg(bd, bg), bd, 2, 7), couleur, epaisseur)
                elif char == 'h15': ## Ecrit : Ч ## ## Ч maj #######
                    ligne(img, ct_sg(ct_sg(p2, ch), ct_sg(p4, cb)), ct_sg(ct_sg(p1, ch), ct_sg(p3, cb)), couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(p1, ch), ct_sg(p3, cb)), ct_sg(p1, ch), couleur, epaisseur)
                    ligne(img, ct_sg(p2, ch), ct_sg(p4, cb), couleur, epaisseur)
                elif char == 'i15': ## Ecrit : Ш ## ## Ш maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                    ligne(img, ch, cb, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                elif char == 'j15': ## Ecrit : Щ ## ## Щ maj #######
                    ligne(img, p3, p4, couleur, epaisseur)
                    ligne(img, ct_sg(p2, ch), ct_sg(p4, cb), couleur, epaisseur)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, ct_sg(p1, ct_sg(p2, ch)), ct_sg(p3, ct_sg(p4, cb)), couleur, epaisseur)
                    ligne(img, p4, pt_sg(ct_sg(bd, bg), bd, 2, 7), couleur, epaisseur)
                elif char == 'k15': ## Ecrit : Ъ ## ## Ъ maj #######
                    ligne(img, ct_sg(p1, ch), ct_sg(p3, cb), couleur, epaisseur)
                    ligne(img, ct_sg(p1, ch), p1, couleur, epaisseur)
                    ligne(img, ct_sg(p3, cb), cb, couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(p1, ch), ct_sg(p3, cb)), ct, couleur, epaisseur)
                    cercle(img, ct_sg(ct, cb), dist(ct_sg(ct, ch), ch), couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'l15': ## Ecrit : Ы ## ## Ы maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p3, pt_sg(p3, cb, 2, 5), couleur, epaisseur)
                    ligne(img, cg, pt_sg(cg, ct, 2, 5), couleur, epaisseur)
                    cercle(img, pt_sg(ct_sg(cg, p3), ct_sg(ct, cb), 2, 5), dist(ct_sg(ct, ch), ch), couleur, epaisseur, 0, 180, -90 +  rotation)
                elif char == 'm15': ## Ecrit : Ь ## ## Ь maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p3, cb, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    cercle(img, ct_sg(ct, cb), dist(ct_sg(ct, ch), ch), couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'n15': ## Ecrit : Э ## ## Э maj #######
                    ligne(img, ct, cd, couleur, epaisseur)
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cd)), couleur, epaisseur, -40, 220, -90 + rotation)
                elif char == 'o15': ## Ecrit : Ю ## ## Ю maj #######
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    ellipse(img, ct_sg(ct, cd), (dist(ct, ch), dist(ct_sg(ct, cd), cd)), couleur, epaisseur, 0, 360, -90 + rotation)
                elif char == 'p15': ## Ecrit : Я ## ## Я maj #######
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p2, ch, couleur, epaisseur)
                    ligne(img, cd, ct, couleur, epaisseur)
                    ligne(img, p3, ct, couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch), dist(pt_sg(ct, ch), ch), couleur, epaisseur, 0, 180, 90 + rotation)
                elif char == 'q15': ## Rmplit tt ## ## Square##
                    for i, j in [(p1, p3), (p1, p2), (p2, p4), (p3, p4)]:
                        ligne(img, i, j, noir, epaisseur)
                    pos -= 1
                elif char == 'a16': ## Ecrit : а ## ## А min #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, ch, p3, couleur, epaisseur)
                    ligne(img, ch, p4, couleur, epaisseur)
                    ligne(img, pt_sg(ch, p3, 2, 3), pt_sg(ch, p4, 2, 3), couleur, epaisseur)
                elif char == 'b16': ## Ecrit : б ## ## Б maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, pt_sg(ch, p2, 1, 2), couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    ligne(img, p3, cb, couleur, epaisseur)
                    cercle(img, ct_sg(ct, cb), dist(ct, cb) / 2, couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'c16': ## Ecrit : в ## ## В maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    ligne(img, p3, cb, couleur, epaisseur)
                    cercle(img, ct_sg(ct, ch), dist(ct, ch) / 2, couleur, epaisseur, 0, 180, -90 + rotation)
                    cercle(img, ct_sg(ct, cb), dist(ct, cb) / 2, couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'd16': ## Ecrit : г ## ## Г maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, pt_sg(ch, p2, 1, 2), couleur, epaisseur)
                elif char == 'e16': ## Ecrit : д ## ## Д maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, c3, c4, couleur, epaisseur)
                    ligne(img, c3, p3, couleur, epaisseur)
                    ligne(img, c4, p4, couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(c3, c4), c3), ct_sg(p1, ch), couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(c4, c3), c4), ct_sg(p2, ch), couleur, epaisseur)
                    ligne(img, ct_sg(p1, ch), ct_sg(p2, ch), couleur, epaisseur)
                elif char == 'f16': ## Ecrit : е ## ## Е maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, cg, pt_sg(ct, cd, 3, 1), couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'g16': ## Ecrit : ё ## ## Ё maj #######
                    cercle(img, ct_sg(pt_sg(hg, cg, 2), ct_sg(hg, hd)), epaisseur / 2, couleur, plein)
                    cercle(img, ct_sg(pt_sg(hd, cd, 2), ct_sg(hg, hd)), epaisseur / 2, couleur, plein)
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, cg, pt_sg(ct, cd, 3, 1), couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'h16': ## Ecrit : ж ## ## Ж maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ctpg = ct_sg(ct_sg(ct, cg), ct)
                    ctpd = ct_sg(ct_sg(ct, cd), ct)
                    ligne(img, p1, ctpg, couleur, epaisseur)
                    ligne(img, p3, ctpg, couleur, epaisseur)
                    ligne(img, p2, ctpd, couleur, epaisseur)
                    ligne(img, p4, ctpd, couleur, epaisseur)
                    ligne(img, ctpg, ctpd, couleur, epaisseur)
                    ligne(img, ch, cb, couleur, epaisseur)
                elif char == 'i16': ## Ecrit : з ## ## З maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    cercle(img, ct_sg(ct, ch), dist(ct, ch) / 2, couleur, epaisseur, -40, 200, -90 + rotation)
                    cercle(img, ct_sg(ct, cb), dist(ct, cb) / 2, couleur, epaisseur, -20, 220, -90 + rotation)
                elif char == 'j16': ## Ecrit : и ## ## И maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                elif char == 'k16': ## Ecrit : й ## ## Й maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                    accent(img, 'breve', hg, hd, p1, p2, couleur, epaisseur, rotation)
                elif char == 'l16': ## Ecrit : к ## ## К maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, ct_sg(p1, ch), ct_sg(p3, cb), couleur, epaisseur)
                    ligne(img, ct_sg(ct, cg), p2, couleur, epaisseur)
                    ligne(img, pt_sg(ct_sg(ct, cg), pt_sg(ct_sg(ct, cg), p2), 3, 2), p4, couleur, epaisseur)
                elif char == 'm16': ## Ecrit : л ## ## Л maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, ct_sg(p1, ch), p2, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ellipse(img, p1, (dist(p1, p3), dist(ct_sg(p1, ch), ch)), couleur, epaisseur, 90, 180, -90 + rotation)
                elif char == 'n16': ## Ecrit : м ## ## М maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p2, ct, couleur, epaisseur)
                elif char == 'o16': ## Ecrit : н ## ## Н maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, pt_sg(p1, ch, 3, 1), pt_sg(p3, cb, 3, 1), couleur, epaisseur)
                    ligne(img, pt_sg(p2, ch, 3, 1), pt_sg(p4, cb, 3, 1), couleur, epaisseur)
                    ligne(img, pt_sg(cg, ct, 3, 1), pt_sg(cd, ct, 3, 1), couleur, epaisseur)
                elif char == 'p16': ## Ecrit : о ## ## О maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cg)), couleur, epaisseur, 0, 360, -90 + rotation)
                elif char == 'q16': ## Ecrit : п ## ## П maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p2, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p3, p1, couleur, epaisseur)
                elif char == 'a17': ## Ecrit : р ## ## Р maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch), dist(pt_sg(ct, ch), ch), couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'b17': ## Ecrit : с ## ## С maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ellipse(img, pt_sg(ct, cd, 8, 5), [dist(p2, cd), dist(ct, cd)], couleur, epaisseur, -20, 200, 90 + rotation)
                elif char == 'c17': ## Ecrit : т ## ## Т maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, pt_sg(p1, ch, 4, 1), pt_sg(p2, ch, 4, 1), couleur, epaisseur)
                    ligne(img, ch, cb, couleur, epaisseur)
                elif char == 'd17': ## Ecrit : у ## ## У maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, ct, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                elif char == 'e17': ## Ecrit : ф ## ## Ф maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, ch, cb, couleur, epaisseur)
                    ellipse(img, ct, (dist(pt_sg(ch, ct, 8, 2), ct), dist(pt_sg(cd, ct, 8, 2), ct)), couleur, epaisseur)
                elif char == 'f17': ## Ecrit : х ## ## Х maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p4, couleur, epaisseur)
                    ligne(img, p2, p3, couleur, epaisseur)
                elif char == 'g17': ## Ecrit : ц ## ## Ц maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4, rotation)
                    ligne(img, p3, p4, couleur, epaisseur)
                    ligne(img, ct_sg(p2, ch), ct_sg(p4, cb), couleur, epaisseur)
                    ligne(img, p3, p1, couleur, epaisseur)
                    ligne(img, p4, pt_sg(ct_sg(bd, bg), bd, 2, 7), couleur, epaisseur)
                elif char == 'h17': ## Ecrit : ч ## ## Ч maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, ct_sg(ct_sg(p2, ch), ct_sg(p4, cb)), ct_sg(ct_sg(p1, ch), ct_sg(p3, cb)), couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(p1, ch), ct_sg(p3, cb)), ct_sg(p1, ch), couleur, epaisseur)
                    ligne(img, ct_sg(p2, ch), ct_sg(p4, cb), couleur, epaisseur)
                elif char == 'i17': ## Ecrit : ш ## ## Ш maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                    ligne(img, ch, cb, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                elif char == 'j17': ## Ecrit : щ ## ## Щ maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4, rotation)
                    ligne(img, p3, p4, couleur, epaisseur)
                    ligne(img, ct_sg(p2, ch), ct_sg(p4, cb), couleur, epaisseur)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, ct_sg(p1, ct_sg(p2, ch)), ct_sg(p3, ct_sg(p4, cb)), couleur, epaisseur)
                    ligne(img, p4, pt_sg(ct_sg(bd, bg), bd, 2, 7), couleur, epaisseur)
                elif char == 'k17': ## Ecrit : ъ ## ## Ъ maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, ct_sg(p1, ch), ct_sg(p3, cb), couleur, epaisseur)
                    ligne(img, ct_sg(p1, ch), p1, couleur, epaisseur)
                    ligne(img, ct_sg(p3, cb), cb, couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(p1, ch), ct_sg(p3, cb)), ct, couleur, epaisseur)
                    cercle(img, ct_sg(ct, cb), dist(ct_sg(ct, ch), ch), couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'l17': ## Ecrit : ы ## ## Ы maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p3, pt_sg(p3, cb, 2, 5), couleur, epaisseur)
                    ligne(img, cg, pt_sg(cg, ct, 2, 5), couleur, epaisseur)
                    cercle(img, pt_sg(ct_sg(cg, p3), ct_sg(ct, cb), 2, 5), dist(ct_sg(ct, ch), ch), couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'm17': ## Ecrit : ь ## ## Ь maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, p3, cb, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    cercle(img, ct_sg(ct, cb), dist(ct_sg(ct, ch), ch), couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'n17': ## Ecrit : э ## ## Э maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, ct, cd, couleur, epaisseur)
                    ellipse(img, ct, (dist(ct, ch), dist(ct, cd)), couleur, epaisseur, -40, 220, -90 + rotation)
                elif char == 'o17': ## Ecrit : ю ## ## Ю maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, cg, ct, couleur, epaisseur)
                    ellipse(img, ct_sg(ct, cd), (dist(ct, ch), dist(ct_sg(ct, cd), cd)), couleur, epaisseur, 0, 360, -90 + rotation)
                elif char == 'p17': ## Ecrit : я ## ## Я maj #######
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4, hg, hd, bd, bg, p1h, p2h, p3b, p4b = minCoos(p1, p2, p3, p4)
                    ligne(img, p2, p4, couleur, epaisseur)
                    ligne(img, p2, ch, couleur, epaisseur)
                    ligne(img, cd, ct, couleur, epaisseur)
                    ligne(img, p3, ct, couleur, epaisseur)
                    cercle(img, pt_sg(ct, ch), dist(pt_sg(ct, ch), ch), couleur, epaisseur, 0, 180, 90 + rotation)
                elif char == 'q17': ## Rmplit tt ## ## Full square##
                    rectangle(img, p1, p4, noir, plein)
                    pos -= 1
                elif char == 'a18': ## Ecrit : ♥ ## ## Cœur ########
                    triangle(img, pt_sg(cg, p1, 3, 1), pt_sg(cd, p2, 3, 1), cb, couleur, plein)
                    cercle(img, ct_sg(cg, ch), dist(cg, ct) / 1.6, couleur, plein)
                    cercle(img, ct_sg(cd, ch), dist(cg, ct) / 1.6, couleur, plein)
                elif char == 'b18': ## Ecrit : ♣ ## ## Trèfle ######
                    cercle(img, ct_sg(ct, ch), dist(ct, cg) / 2, couleur, plein)
                    cercle(img, ct_sg(ct, cg), dist(ct, cg) / 2, couleur, plein)
                    cercle(img, ct_sg(ct, cd), dist(ct, cd) / 2, couleur, plein)
                    triangle(img, ct_sg(ct, ch), pt_sg(cb, p3, 3), pt_sg(cb, p4, 3), couleur, plein)
                elif char == 'c18': ## Ecrit : ♦ ## ## Carreau #####
                    triangle(img, cg, cd, cb, couleur, plein)
                    triangle(img, cg, cd, ch, couleur, plein)
                elif char == 'd18': ## Ecrit : ♠ ## ## Piques ######
                    triangle(img, pt_sg(cg, p3, 3, 1), pt_sg(cd, p4, 3, 1), ch, couleur, plein)
                    cercle(img, ct_sg(cg, cb), dist(cg, ct) / 1.6, couleur, plein)
                    cercle(img, ct_sg(cd, cb), dist(cg, ct) / 1.6, couleur, plein)
                    triangle(img, ct, pt_sg(cb, p3, 3), pt_sg(cb, p4, 3), couleur, plein)
                elif char == 'e18': ## Ecrit : · ## ## Pion blanc ## ## À refaire ##
                    cercle(img, ct, dist(ct_sg(ct, ch), ct), couleur, epaisseur)
                    ellipse(img, ct_sg(cg, p3), (dist(ct_sg(cg, p3), p3), dist(cg, ct_sg(cg, ct))), couleur, epaisseur, 90, 180, -90 + rotation)
                    ellipse(img, ct_sg(cd, p4), (dist(ct_sg(cg, p3), p3), dist(cg, ct_sg(cg, ct))), couleur, epaisseur, 180, 270, -90 + rotation)
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'f18': ## Ecrit : · ## ## Fou blanc ### ## À refaire ##
                    cercle(img, ct_sg(ct, ch), dist(ct_sg(ct, ch), ct), couleur, epaisseur)
                    ellipse(img, cg, (dist(cg, p3), dist(cg, ct_sg(cg, ct))), couleur, epaisseur, 90, 180, -90 + rotation)
                    ellipse(img, cd, (dist(cg, p3), dist(cg, ct_sg(cg, ct))), couleur, epaisseur, 180, 270, -90 + rotation)
                    ligne(img, pt_sg(ct_sg(ct, ch), ct_sg(p1, cg), 3), pt_sg(ct_sg(ct, ch), ct_sg(p2, cd), 3), couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'g18': ## Ecrit : · ## #Cavalier blanc# ## À refaire ##
                    ellipse(img, ct_sg(ct, ch), (dist(ct_sg(ct, ch), ct), dist(p2, ch)), couleur, epaisseur, -145, 90, -90 + rotation)
                    ellipse(img, ct_sg(ct, ch), (dist(ct_sg(ct, ch), ct), dist(p2, ch) + epaisseur), couleur, epaisseur, 0, 125, -90 + rotation)
                    ligne(img, ct_sg(ct, cg), ct, couleur, epaisseur)
                    ligne(img, ct, p3, couleur, epaisseur)
                    ligne(img, p3, p4, couleur, epaisseur)
                    ligne(img, ct_sg(cd, p2), p4, couleur, epaisseur)
                    cercle(img, ct_sg(ct_sg(cg, ch), ct_sg(ct, ch)), epaisseur / 2, couleur, plein)
                elif char == 'h18': ## Ecrit : · ## ##Dame blanche## ## À refaire ##
                    points = [ch, cg, cd, ct_sg(ct_sg(cg, ch), p1), ct_sg(ct_sg(cd, ch), p2)]
                    for i in points:
                        cercle(img, i, epaisseur, couleur, plein)
                        triangle(img, i, pt_sg(pt_sg(ct, cb, 3), p3, 9), pt_sg(pt_sg(ct, cb, 3), p4, 9), couleur, plein)
                    ellipse(img, cb, (dist(cb, ct_sg(pt_sg(pt_sg(ct, cb, 3), p3, 9), pt_sg(pt_sg(ct, cb, 3), p4, 9))), dist(cb, p4)), couleur, epaisseur, -90, 90, -90 + rotation)
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'i18': ## Ecrit : · ## ## Roi blanc ### ## À refaire ##
                    ligne(img, ch, cb, couleur, epaisseur)
                    ligne(img, pt_sg(ct_sg(ct, ch), ct_sg(p1, cg)), pt_sg(ct_sg(ct, ch), ct_sg(p2, cd)), couleur, epaisseur)
                    ellipse(img, cb, (dist(cb, ct_sg(pt_sg(pt_sg(ct, cb, 3), p3, 9), pt_sg(pt_sg(ct, cb, 3), p4, 9))), dist(cb, p4)), couleur, epaisseur, -90, 90, -90 + rotation)
                    ligne(img, p3, p4, couleur, epaisseur)
                elif char == 'j18': ## Ecrit : · ## ## Python logo## ## À refaire ##
                    epaisseur /= 4
                    rectangle(img, p1, p4, couleur, plein)
                    cercle(img, pt_sg(p1, ct, 3), epaisseur, (255 - couleur[0], 255 - couleur[1], 255 - couleur[2]), plein)
                    cercle(img, pt_sg(p4, ct, 3), epaisseur, (255 - couleur[0], 255 - couleur[1], 255 - couleur[2]), plein)
                    ligne(img, ct_sg(p1, cg), pt_sg(ct_sg(p1, cg), ct_sg(ct, ch), 1, 2), (255 - couleur[0], 255 - couleur[1], 255 - couleur[2]), epaisseur)
                    ligne(img, ct_sg(p4, cd), pt_sg(ct_sg(p4, cd), ct_sg(ct, cb), 1, 2), (255 - couleur[0], 255 - couleur[1], 255 - couleur[2]), epaisseur)
                    ligne(img, pt_sg(cg, ct, 1, 2), pt_sg(cd, ct, 1, 2), (255 - couleur[0], 255 - couleur[1], 255 - couleur[2]), epaisseur)
                    ligne(img, pt_sg(p2, ch, 1, 2), pt_sg(cd, ct, 1, 2), (255 - couleur[0], 255 - couleur[1], 255 - couleur[2]), epaisseur)
                    ligne(img, pt_sg(p3, cb, 1, 2), pt_sg(cg, ct, 1, 2), (255 - couleur[0], 255 - couleur[1], 255 - couleur[2]), epaisseur)
                elif char == 'k18': ## Ecrit : | ## ##Note blanche##
                    ligne(img, ct_sg(p1, ch), ct_sg(p3, cb), couleur, epaisseur)
                    ctr = ct_sg(ct_sg(cg, ct), ct_sg(p3, cb))
                    ellipse(img, ctr, (dist(ctr, ct_sg(cg, ct)), dist(ctr, ct_sg(ct, p4))), couleur, epaisseur, 0, 180, -90 + rotation)
                elif char == 'l18': ## Ecrit : | ## ## Note noire ##
                    ligne(img, ct_sg(p1, ch), ct_sg(p3, cb), couleur, epaisseur)
                    ctr = ct_sg(ct_sg(cg, ct), ct_sg(p3, cb))
                    ellipse(img, ctr, (dist(ctr, ct_sg(cg, ct)), dist(ctr, ct_sg(ct, p4))), couleur, -epaisseur, 0, 180, -90 + rotation)
                elif char == 'm18': ## Ecrit : / ## ## Éclair ######
                    ligne(img, ct_sg(p2, ch), pt_sg(cg, ct, 1, 2), couleur, epaisseur)
                    ligne(img, pt_sg(cg, ct, 1, 2), pt_sg(cd, ct, 1, 2), couleur, epaisseur)
                    ligne(img, pt_sg(cd, ct, 1, 2), ct_sg(p3, cb), couleur, epaisseur)
                elif char == 'n18': ## Ecrit : C ## ## Chapeau #####
                    ligne(img, cg, cd, couleur, epaisseur)
                    rectangle(img, ct_sg(p1, ct), ct_sg(ct, cd), couleur, plein, 0, False)
                elif char == 'o18': ## Ecrit : R ## ## Rond ########
                    ellipse(img, ct, (dist(ct, ct_sg(ct, ch)), dist(ct, ct_sg(ct, cd))), couleur, epaisseur, 0, 360, rotation)
                elif char == 'p18': ## Ecrit : G ## ## Clé de sol ## ## À faire ##
                    pass
                elif char == 'q18': ## Ecrit : A ## ## Clé de la ### ## À faire ##
                    pass
                elif char == 'r1': ## Ecrit : J ## ## JavaScript ###
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, ch, ct_sg(ct, cb), couleur, epaisseur)
                    ellipse(img, ct_sg(p3, ct), [dist(ct_sg(p3, ct), ct_sg(p3, cb)), dist(ct_sg(p3, ct), ct_sg(ct, cb))], couleur, epaisseur, 90, 270, -90 + rotation)
                    tour = 225
                    p1, p2, p3, p4, ch, cb, cg, cd, ct, c1, c2, c3, c4 = coos2(ct, cd, cb, p4)
                    cercle(img, ct_sg(cg, p2), dist(ct_sg(cg, p2), ct), couleur, epaisseur, 0, tour, 90 + rotation)
                    cercle(img, ct_sg(cg, p4), dist(ct_sg(cg, p4), ct), couleur, epaisseur, 0, tour, -90 + rotation)
                elif char == 's1': ## Ecrit : J ## ## JavaCupTea ### ## À faire ##
                    pass
                elif char == 't1': ## Ecrit : F ## ## F sharp ######
                    ligne(img, p1, ch, couleur, epaisseur)
                    ligne(img, p1, p3, couleur, epaisseur)
                    ligne(img, cg, pt_sg(ct, cg, 3), couleur, epaisseur)
                    p1 = ct_sg(ch, ct)
                    p3 = ct_sg(cb, ct)
                    p2 = ct_sg(p2, ct)
                    p4 = ct_sg(p4, ct)
                    ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
                    c1 = ct_sg(c1, ct)
                    c2 = ct_sg(c2, ct)
                    c3 = ct_sg(c3, ct)
                    c4 = ct_sg(c4, ct)
                    ch = ct_sg(p1, p2)
                    cb = ct_sg(p3, p4)
                    epaisseur /= 2
                    ligne(img, c1, c2, couleur, epaisseur)
                    ligne(img, c3, c4, couleur, epaisseur)
                    ligne(img, pt_sg(p1, ch, 8, 1), pt_sg(p3, cb, 10, 1), couleur, epaisseur)
                    ligne(img, pt_sg(p2, ch, 2, 1), pt_sg(p4, cb, 1, 2), couleur, epaisseur)
                elif char == 'u1': ## Ecrit : \ ## ## <\> ##########
                    ligne(img, ct_sg(ct_sg(p1, ch), ch), ct_sg(ct_sg(p4, cb), cb), couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(p1, cg), ct_sg(cg, ch)), cg, couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(p3, cg), ct_sg(cg, cb)), cg, couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(p2, cd), ct_sg(cd, ch)), cd, couleur, epaisseur)
                    ligne(img, ct_sg(ct_sg(p4, cd), ct_sg(cd, cb)), cd, couleur, epaisseur)
                elif char == 'v1': ## Ecrit : . ## ## Point jap ####
                    cercle(img, ct_sg(ct, cb), dist(ct_sg(ct, cb), cb) / 2, couleur, epaisseur, 0, 360, 0)
                elif char == 'w1': ## Ecrit : , ## ## Virgule jap ##
                    ligne(img, ct_sg(p3, ct), ct_sg(cb, p4), couleur, epaisseur)
                ## Il manque les chars de r1 à dk18 ##
                elif char == 'hashtag': ## Y faut lui assigner un code ##
                    ligne(img, c1, c2, couleur, epaisseur)
                    ligne(img, c3, c4, couleur, epaisseur)
                    ligne(img, pt_sg(p1, ch, 1, 2), pt_sg(p3, cb, 2, 1), couleur, epaisseur)
                    ligne(img, pt_sg(p2, ch, 2, 1), pt_sg(p4, cb, 1, 2), couleur, epaisseur)
                else: ######## Si char pas identifié correctement ##
                    pos = char_inconnu(img, hg, hd, bg, bd, noir, police, rotation, taille, pos)
            elif police == 'complex': ## À faire ##
                if char == 'c1':
                    ellipse(img, ct, (abs(ct[1] - ch[1]), int(abs(ct[0] - cd[0]) / 5 * 4)), couleur, epaisseur)
                    ligne(img, ct_sg(ch, (ct[0] + int(abs(ct[0] - cd[0]) / 5 * 4), ct[1])), ct_sg(cb, (ct[0] - int(abs(ct[0] - cd[0]) / 5 * 4), ct[1])), couleur, epaisseur)
                elif char == 'd1':
                    ligne(img, ch, cb, couleur, epaisseur)
                    ligne(img, ct_sg(cb, p3), ct_sg(cb, p4), couleur, epaisseur)
                    ligne(img, ch, ct_sg(cg, ch), couleur, epaisseur)
                else: ######## Si char pas identifié correctement ##
                    pos = char_inconnu(img, hg, hd, bg, bd, noir, police, rotation, taille, pos)
            if combine:
                return(img, pos)
            else:
                return(img, save_pos)
        def char_inconnu(img, hg, hd, bg, bd, noir, police, rotation, taille, pos):
            img, r = chars(img, 'q15', hg, hd, bg, bd, noir, 10 * taille, police, rotation, taille, pos, True)
            img, r = chars(img, 'q13', hg, hd, bg, bd, noir, 10 * taille, police, rotation, taille, pos)
            return(img, pos)
        def accent(img, accent, p1, p2, p3, p4, couleur=noir, epaisseur=epaisseur, rotation=0):
            if oui: #################################################### Coos secondaires ####
                ch = ct_sg(p1, p2)
                cb = ct_sg(p3, p4)
                cg = ct_sg(p1, p3)
                cd = ct_sg(p2, p4)
                ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
                accent = accent.lower()
                mult_brev = 1.5
                mult_tild = 0.645
                taille_tilde = 5
            if   accent == 'ouvert' or accent == 'grave': ############## Écrit l'accent '`' ##
                ligne(img, pt_sg(cb, p4, 2, 1), pt_sg(ch, p1, 2, 1), couleur, epaisseur)
            elif accent == 'ferme' or accent == 'aigu': ################ Écrit l'accent '´' ##
                p1, p2 = p2, p1
                p3, p4 = p4, p3
                cg = cd
                ligne(img, pt_sg(cb, p4, 2, 1), pt_sg(ch, p1, 2, 1), couleur, epaisseur)
            elif accent == 'circonflexe' or accent == 'circomflexe': ### Écrit l'accent '^' ##
                ligne(img, pt_sg(cb, p2, 2, 1), ch, couleur, epaisseur)
                ligne(img, pt_sg(cb, p1, 2, 1), ch, couleur, epaisseur)
            elif accent == 'trema' or accent == 'tremat': ############## Écrit l'accent '¨' ##
                cercle(img, pt_sg(ct, cd, 2, 1), 1, couleur, epaisseur)
                cercle(img, pt_sg(ct, cg, 2, 1), 1, couleur, epaisseur)
            elif accent == 'point': #################################### Écrit l'accent '˙' ##
                cercle(img, ct, 1, couleur, epaisseur)
            elif accent == 'caron'or accent == 'antiflexe': ############ Écrit l'accent 'ˇ' ##
                ligne(img, pt_sg(ch, p4, 2, 1), cb, couleur, epaisseur)
                ligne(img, pt_sg(ch, p3, 2, 1), cb, couleur, epaisseur)
            elif accent == 'breve': #################################### Écrit l'accent '˘' ##
                cercle(img, ct, dist(ct, ch) * mult_brev, couleur, epaisseur, 0, 180, rotation)
            elif accent == 'antibreve' or accent == 'breve retourne': ## Écrit:˘ à l'envers ##
                cercle(img, ct, dist(ct, ch) * mult_brev, couleur, epaisseur, 180, 360, rotation)
            elif accent == 'macron': ################################### Écrit l'accent 'ˉ' ##
                ligne(img, ct_sg(cg, ct), ct_sg(cd, ct), couleur, epaisseur)
            elif accent == 'tilde': #################################### Écrit l'accent '˜' ##
                ellipse(img, pt_sg(ch, p1, 2), (dist(ct_sg(p1, ch), ch) * mult_tild, taille_tilde), couleur, epaisseur, 0, 180, 180 + rotation)
                ellipse(img, pt_sg(ch, p2, 2), (dist(ct_sg(p2, ch), ch) * mult_tild, taille_tilde), couleur, epaisseur, 0, 180, rotation)
            elif accent == 'rond' or accent == 'rond en chef': ######### Écrit l'accent '°' ##
                cercle(img, ct_sg(ct, cb), epaisseur, couleur, epaisseur)
            elif accent == 'dferme': ################################### Écrit l'accent '˝' ##
                ligne(img, ct_sg(cb, p3), ch, couleur, epaisseur)
                ligne(img, cb, ct_sg(ch, p2), couleur, epaisseur)
            elif accent == 'douvert': ################################## Écrit l'accent '˵' ##
                ligne(img, ct_sg(cb, p4), cb, couleur, epaisseur)
                ligne(img, ch, ct_sg(cb, p1), couleur, epaisseur)   
            elif accent == 'cedille': ################################## Écrit l'accent '¸' ##
                if oui: ## Coos ##
                    ct = ct_sg(ct_sg(p1, p4), ct_sg(p2, p3))
                    p1 = (pt_sg(p1, ct, 5, 1))
                    p2 = (pt_sg(p2, ct, 5, 1))
                    p3 = (pt_sg(p3, ct, 5, 1))
                    p4 = (pt_sg(p4, ct, 5, 1))
                    ch = ct_sg(p1, p2)
                    cb = ct_sg(p3, p4)
                    cg = ct_sg(p1, p3)
                    cd = ct_sg(p2, p4)
                    ct = ct_sg(p1, p4)
                ligne(img, ct_sg(cb, cd), pt_sg(p4, p3, 1, 2), couleur, epaisseur)
            return(img)
        def scripte(img, pto, texte, taille=1, espacement=1, couleur=noir, epaisseur=epaisseur, police='basic', rotation=0, help=False, souligne='None', surligne='None', combine=False, rot_par_char=0):
            '''
            Prend:
            ------
            :img: ``np.array``\n
            :pto: ``tuple (x, y)``\n
            :texte: ``ctr``\n
            :taille: ``int/float``\n
            :espacement: ``int/float``\n
            :couleur: ``tuple (B, G, R)``\n
            :epaisseur: ``int``\n
            :police: ``str``\n
            :rotation: ``int`` Pas terminée du tout !\n
            Renvoie:
            --------
            ``img``: ``np.array``
            '''
            rote = 0
            if oui: #################### Coos et formatage du texte ##
                hc = longChar / 3 * 4.5
                hc *= espacement
                hc *= taille
                hc = round(hc)
                pos = 0
                lignes = 0
                pt = pto
                texte = chaine(texte)
            while True: ## Lecture du texte et impression des chars ##
                if oui: ## Coos du char ##
                    pto = coosCercle(pt, hc * lignes * taille, rotation + 90)
                    p1 = coosCercle(pto, longChar * pos * taille * espacement, rotation)
                    p2 = coosCercle(p1, longChar * taille * espacement, rotation + rot_par_char * rote)
                    p3 = coosCercle(p1, hautChar * taille, rotation + 90 + rot_par_char * rote)
                    p4 = coosCercle(p2, hautChar * taille, rotation + 90 + rot_par_char * rote)
                char = texte.suivant('\\')
                if char == ' ':
                    scripte_format(img, p1, p2, p3, p4, souligne, surligne, epaisseur)
                    pos += 1
                elif char == 'n':
                    save_pos.d = ''
                    lignes += 1
                    pos = 0
                elif char == 'r':
                    save_pos.d = ''
                    lignes -= 1
                    pos = 0
                elif char == 'v':
                    save_pos.d = ''
                    lignes == 0
                    pos = 0
                elif char == 'f':
                    save_pos.d = ''
                    pos -= 4
                elif char == 't':
                    save_pos.d = ''
                    pos += 4
                elif char == 'a':
                    save_pos.d = ''
                else:
                    scripte_format(img, p1, p2, p3, p4, souligne, surligne, epaisseur)
                    try:
                        img, pos = chars(img, char, p1, p2, p3, p4, couleur, epaisseur, police, rotation + rot_par_char * rote, taille, pos, combine)
                        if type(pos) != int: pos = pos[-1]
                    except Exception as i:
                        print(i)
                        img, pos = char_inconnu(img, p1, p2, p3, p4, noir, police, rotation + rot_par_char * rote, taille, pos)
                    pos += 1
                    rotation += rot_par_char
                    rote += 1
                if help:
                        cercle(img, pto, 20, turquoise, plein)
                        cercle(img, p1, 15, bleu, plein)
                        cercle(img, p2, 15, vert, plein)
                        cercle(img, p3, 15, rouge, plein)
                        cercle(img, p4, 15, noir, plein)
                if texte.index == len(texte.texte) - 1:
                    break
            return(img)
    if oui: ######################## Animations ###
        def defilement(img=image(), texte='Texte d\'essai.', wk=27, help=False):
            sens = True
            a = '                          '
            if sens:
                texte += a
            else:
                texte = a + texte
            wtk = 0
            while wtk != wk:
                wtk = montre(scripte(copy.deepcopy(img), (0, 0), texte, combine=True, help=help), 'img', 300, False)
                if sens:
                    texte = texte[1:len(texte)] + texte[0]
                else:
                    texte = texte[-1] + texte[0:len(texte) - 1]
        def horloge(img=image(), couleur=turquoise, sep1='h', sep2=':', wk=27, help=False):
            wtk = 0
            format = f'%H{sep1}%M{sep2}%S'
            while wtk != wk:
                wtk = montre(scripte(copy.deepcopy(img), ct, f'\r\f{heure(format)}\n\f\f   {aujourdhui()}', combine=True, couleur=couleur, help=help), 'img', 300, False)
        def syb_time(heure):
            h, m, s, f = heure.split(':')
            temps = [int(i) for i in (h, m, s)]
            while len(f) < 6: f = f'0{f}'
            t = float(f'0.{f}')
            types = [3600, 60, 1]
            for type_, valeur in enumerate(temps):
                t += types[type_]*valeur
            t = round(t/(60*60*24)*(10*100*100))
            t = str('0'*6)[:6-len(str(t)):]+str(t)
            t = f'{t[:2]}:{t[2:4]}:{t[4:6]}'
            return(t)
        def horloge_sybylline(img=image(), couleur=turquoise, wk=27, help=False):
            wtk = 0; frmt = '%H:%M:%S:%f'
            while wtk != wk: wtk = montre(scripte(copy.deepcopy(img), ct, f'\r\f{syb_time(datetime.now().strftime(frmt))}\n\f\f   {aujourdhui()}', combine=True, couleur=couleur, help=help), 'img', 1, False)
        def coos_de_la_souris(event, x, y, flags, params):
            souris.x, souris.y = x, y
        def coos_souris(img=image(), couleur=turquoise, wk=27):
            wtk = 0
            nomFenetre = 'img'
            while wtk != wk:
                pos = f'({souris.x}, {souris.y})'
                img = scripte(image(), ct, f'\r\f\f   {pos:^12}', couleur=couleur)
                cv2.namedWindow(nomFenetre, cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty(nomFenetre, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow(nomFenetre, img)
                cv2.setMouseCallback(nomFenetre, coos_de_la_souris)
                wtk = cv2.waitKey(1)
    if oui: ############################# Demos ###
        def demo(help=True, polise='simplex'):
            txt = []
            st = '\b\\b1\\b1\\b1\\b1\\b1\\b1'
            n = 0; l = 0
            t = st
            ind = 0
            lts = 'abcdefghijklmnopqrstuvwxyz'
            lst_lts = []
            w = 0
            for lpp in [17, 17, 17, 16, 16, 16, 16]:
                lst_lts.append('')
                for i in range(lpp):
                    if ind < len(lts): lst_lts[w] += lts[ind]+':'
                    else: lst_lts[w] += lts[ind//len(lts)-1]+lts[ind%len(lts)]+':'
                    ind += 1
                lst_lts[w] = lst_lts[w][:len(lst_lts[w])-1:]
                w+=1
            print(lst_lts)
            for lets in lst_lts:
                for i in range(18):
                    for j in lets.split(':'):
                        t += f'\\{j}{i+1}'
                        n += 1
                        if n%17 == 0:
                            if not (l+1)%9 == 0: t += f'\\n\\{st[2::]}'; l+= 1
                            else: l+=1
                            if l%9 == 0: txt.append(t); t = st
            if t != st: txt.append(t)
            i = 0; r=0
            while True:
                texte = txt[i]
                print(texte)
                #img = scripte(scripte(image(remplissage=turquoise), hg, texte+'\\', 1, combine=non), hg, f'{i+1:2d}/{len(txt):2d}', surligne=vert, souligne=rouge, couleur=bleu)
                r+=1
                img = scripte(scripte(image(remplissage=turquoise), ct, texte+'\\', 1, combine=non, rotation=r), hg, f'{i+1:2d}/{len(txt):2d}', surligne=vert, souligne=rouge, couleur=bleu)
                wk = montre(img, 'demo', 1, non)
                match wk:
                    case 27: break
                    case 32: i += 1; i=i%len(txt)
                    case  8: i -= 1; i=(i+len(txt))%len(txt)
            ferme_all()
        def dessin():
            class clrsdessn:
                r = 0
                g = 0
                b = 0
            def get_clrs_r(val):
                clrsdessn.r = val
            def get_clrs_g(val):
                clrsdessn.g = val
            def get_clrs_b(val):
                clrsdessn.b = val
            class ep:
                ep = epaisseur
            def get_ep(val):
                ep.ep = val
            img = image()
            wk = 0
            nf = 'img'
            coos_s = None
            montre_img(img, nf)
            cv2.createTrackbar('epaisseur', nf, 0, 255, get_ep)
            cv2.createTrackbar('r', nf, 0, 255, get_clrs_r)
            cv2.createTrackbar('g', nf, 0, 255, get_clrs_g)
            cv2.createTrackbar('b', nf, 0, 255, get_clrs_b)
            draw = False
            while wk != 27:
                montre_img(img, nf)
                couleur = [clrsdessn.b, clrsdessn.g, clrsdessn.r]
                cv2.setMouseCallback(nf, coos_de_la_souris)
                if coos_s != None and draw:
                    ligne(img, coos_s, [souris.x, souris.y], couleur, ep.ep)
                coos_s = [souris.x, souris.y]
                wk = cv2.waitKey(1)
                if wk == 32:
                    draw = not draw
                elif wk == 8:
                    draw = not draw
        def dessin_alea_infini(pl='p'):
            img = image(remplissage=[rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)])
            wk = 0
            min_c = 0
            max_c = 255
            min_l = 0
            max_l = long
            min_h = 0
            max_h = haut
            min_e = 0
            max_e = 30
            while wk != 27:
                a, b = rd.randint(0, 1000000), rd.randint(0, 1000000)
                if a == b:
                    img = image(remplissage=[rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)])
                couleur = [rd.randint(min_c, max_c), rd.randint(min_c, max_c), rd.randint(min_c, max_c)]
                p1 = [rd.randint(min_l, max_l), rd.randint(min_h, max_h)]
                p2 = [rd.randint(min_l, max_l), rd.randint(min_h, max_h)]
                ep = rd.randint(min_e, max_e)
                if pl == 'p':
                    ligne(img, p1, p1, couleur, ep)
                    ligne(img, p2, p2, couleur, ep)
                else:
                    ligne(img, p1, p2, couleur, ep)
                wk = montre(img, attente=1, destroy=False)
        def soizik(img, p1=(0, 0), p2=(long, 0), p3=(0, haut), p4=(long, haut)):
            h = 'a0'
            b = '40'
            vert = nouvelle_couleur(f'{b}{h}{b}')
            bleu = nouvelle_couleur(f'{h}{b}{b}')
            rouge = nouvelle_couleur(f'{b}{b}{h}')
            b, a = 4, 7
            c, d = 2, 1
            chg = pt_sg(p1, p2, a, b)
            cgh = pt_sg(p1, p3, c, d)
            cdh = pt_sg(p2, p4, c, d)
            cdb = pt_sg(p2, p4, d, c)
            rectangle(img, chg, cgh, noir, plein)
            rectangle(img, chg, cdh, bleu, plein)
            rectangle(img, cgh, p4, rouge, plein)
            rectangle(img, cgh, cdb, vert, plein)
            etoile(img, ct_sg(chg, cgh), dist(chg, cgh)/4.75, blanc, 0, 5, 0, False)
            return(img)
        def blason(img=image(), pt=ct, ud = 75, rotation=0, cri='TAMET', texte1='LA BEAUTÉ EST DANS LES YEUX', texte2 = 'DE CELUI QUI LA REGARDE'):
            ct = pt
            ep = ud/15
            aurum = [5, 207, 242] ###### En choisir un mieux ###
            rubis = [20, 50, 255] ###### En choisir un mieux ###
            pourpre = [100, 30, 100] ### En choisir un mieux ###
            noir = [0, 0, 0] ########### En choisir un mieux ###
            bleu = [255, 20, 20] ####### En choisir un mieux ###
            rouge = [20, 20, 255] ###### En choisir un mieux ###
            vert = [20, 255, 20] ####### En choisir un mieux ###
            gris = [50, 50, 50] ######## En choisir un mieux ###
            blanc = [215, 215, 215] #### En choisir un mieux ###
            opale = [100, 50, 50] ###### En choisir un mieux ###
            emeraude = [50, 100, 20] ### En choisir un mieux ###
            #### Coos ####
            ura = 5
            pol = 'basic'
            pth = coosCercle(ct, ud*3.6, 270)
            ptdp = coosCercle(pth, ud*5.4, 0)
            ptgp = coosCercle(pth, ud*5.4, 180)
            ptgh = coosCercle(ptgp, ud, 45)
            ptgb = coosCercle(ptgh, ud, 90)
            ptdh = coosCercle(ptdp, ud, 90+45)
            ptdb = coosCercle(ptdh, ud, 90)
            pthg = coosCercle(pth, ud, 135)
            pthd = coosCercle(pth, ud, 45)
            ptch = pt_sg(pth, ct_sg(pthg, pthd), 1, 6)
            pbx = dist(ptgb, ptdb)/10 * 3
            pby = dist(ptgb, ptdb)/10 * 3
            gby = dist(ptgb, ptdb)/10 * 4
            ptbg = coosCercle(ptgb, pby, 90)
            ptbd = coosCercle(ptdb, pby, 90)
            ptgb1 = coosCercle(ptgb, pbx, 0)
            ptgb2 = coosCercle(ptdb, pbx, 180)
            ptbgd = coosCercle(ptgb1, pby, 90)
            ptbdg = coosCercle(ptgb2, pby, 90)
            ptgb3 = coosCercle(ptgb1, gby, 90)
            ptgb4 = coosCercle(ptgb2, gby, 90)
            ptbgb = coosCercle(ptgb, gby, 90)
            ptbdb = coosCercle(ptdb, gby, 90)
            cthpbg = [ptgb[0] + pbx/2, ptgb[1] + (pby/2)*4/3.5]
            cthpbd = [ptdb[0] - pbx/2, ptdb[1] + (pby/2)*4/3.5]
            cg = ct_sg(ptgh, ptgb)
            cd = ct_sg(ptdh, ptdb)
            pt = ct_sg(cg, cd)
            ptg = ct_sg(pt, cg)
            ptgd = ct_sg(ptg, pt)
            ptgg = pt_sg(ptg, cg, 2, 5)
            ptd = ct_sg(pt, cd)
            ptdg = ct_sg(ptd, pt)
            ptdd = pt_sg(ptd, cd, 2, 5)
            t = 0.2
            pegd = coosCercle(ptg, ud*t, 0)
            pedg = coosCercle(ptd, ud*t, 180)
            t = 1
            pegg = coosCercle(pegd, ud*t, 180)
            pedd = coosCercle(pedg, ud*t, 0)
            d = 0.2
            pegdh = coosCercle(pegd, ud*d, 225)
            pegdb = coosCercle(pegd, ud*d, 135)
            peggh = coosCercle(pegg, ud*d, 315)
            peggb = coosCercle(pegg, ud*d, 45)
            pedgh = coosCercle(pedg, ud*d, 315)
            pedgb = coosCercle(pedg, ud*d, 45)
            peddh = coosCercle(pedd, ud*d, 225)
            peddb = coosCercle(pedd, ud*d, 135)
            pextg = coosCercle(ct_sg(ptbg, ptbd), dist([ct_sg(ptbg, ptbd)[0], 0], [ct_sg(ptbg, ptbgd)[0], 0])*2, 180)
            pextd = coosCercle(ct_sg(ptbg, ptbd), dist([ct_sg(ptbg, ptbd)[0], 0], [ct_sg(ptbg, ptbgd)[0], 0])*2, 0)
            ptb = pt_sg(ct, coosCercle(ct, ud*7, 90), 6, 13)
            ### Grand écu ###
            b = 1
            ellipse(img, ct_sg(ptbg, ptbd), [dist(ptbg, ptbd)/2, dist(ptgb1, ptgb3)*b], gris, 0, 0, 180)
            ellipse(img, ct_sg(ptbg, ptbd), [dist(ptbg, ptbd)/2, dist(ptgb1, ptgb3)*b], vert, 0, 135, 180)
            ellipse(img, ct_sg(ptbg, ptbd), [dist(ptbg, ptbd)/2, dist(ptgb1, ptgb3)*b], vert, 0, 0, 45)
            cte = ct_sg(ptbg, ptbd)
            xe, ye = cte
            ae = dist(ptbg, ptbd)/2
            be = dist(ptgb1, ptgb3)*b
            q1 = ct_sg(ptgb, ptgb1)[0]
            q2 = ct_sg(ptdb, ptgb2)[0]
            pointeeg = q1, round(max(equation_2eme_degre(1, -2 * ye, ye ** 2 - ((be ** 2) * (1 - ((q1 - xe) ** 2) / (ae ** 2))))))
            pointeed = q2, round(max(equation_2eme_degre(1, -2 * ye, ye ** 2 - ((be ** 2) * (1 - ((q2 - xe) ** 2) / (ae ** 2))))))
            triangle(img, pointeeg, pth, pointeed, gris, 0)
            ellipse(img, [ct_sg(ptbg, ptbd)[0], ct_sg(ptbg, ptbd)[1]-ud*1.5], [dist(ptgb1, ptgb3)*b, (dist(cthpbg, cthpbd)+ud)/2], blanc, 0, 0, 180)
            ctged = coosCercle(ct_sg(ptgb3, ptgb4), dist(ptgb1, ptgb), 0)
            ctgeg = coosCercle(ct_sg(ptgb3, ptgb4), dist(ptgb1, ptgb), 180)
            ctged = coosCercle(ctged, dist(ptgb3, ptbgd)/3*2, 270)
            ctgeg = coosCercle(ctgeg, dist(ptgb3, ptbgd)/3*2, 270)
            for i in points_segment(pextg, coosCercle(pextg, ud, 270)):
                ellipse(img, i, [dist(ptbg, ptbd)/2, dist(ptgb1, ptgb3)*b], vert, 3, 0, 45)
            for i in points_segment(pextd, coosCercle(pextd, ud, 270)):
                ellipse(img, i, [dist(ptbg, ptbd)/2, dist(ptgb1, ptgb3)*b], vert, 3, 180, 135)
            for i in points_segment(ct_sg(pextg, pextd), coosCercle(ct_sg(pextg, pextd), 1, 270)):
                ellipse(img, i, [dist(ptbg, ptbd)/2, dist(ptgb1, ptgb3)*b], vert, 4, 3.5, 45)
            for i in points_segment(ct_sg(pextg, pextd), coosCercle(ct_sg(pextg, pextd), 1, 270)):
                ellipse(img, i, [dist(ptbg, ptbd)/2, dist(ptgb1, ptgb3)*b], vert, 4, 175, 135)
            ### Couronne ###
            triangle(img, ptgp, ptgh, ptgb, aurum, 0)
            triangle(img, ptdp, ptdh, ptdb, aurum, 0)
            triangle(img, pth, pthd, pthg, aurum, 0)
            rectangle(img, ptgh, ptdb, aurum, 0)
            carreau(img, ptch, [ud*0.75, ud*0.5], rubis, 0, 90)
            triangle(img, pt_sg(ptgp, ptgb, 7, 4), pt_sg(ptgp, ptgb, 2, 7), ct_sg(pt_sg(ptgp, ptgb, 1, 2), ptgh), rubis, 0)
            triangle(img, pt_sg(ptdp, ptdb, 7, 4), pt_sg(ptdp, ptdb, 2, 7), ct_sg(pt_sg(ptdp, ptdb, 1, 2), ptdh), rubis, 0)
            triangle(img, pegg, peggh, peggb, emeraude, 0)
            triangle(img, pegd, pegdh, pegdb, emeraude, 0)
            triangle(img, pedg, pedgh, pedgb, emeraude, 0)
            triangle(img, pedd, peddh, peddb, emeraude, 0)
            rectangle(img, peggh, pegdb, emeraude, 0)
            rectangle(img, peddh, pedgb, emeraude, 0)
            cercle(img, ptgd, ep*2, opale, 0)
            cercle(img, ptdg, ep*2, opale, 0)
            cercle(img, ptgg, ep*2, opale, 0)
            cercle(img, ptdd, ep*2, opale, 0)
            ### Écu gauche ###
            triangle(img, pt_sg(ptbg, ptbgb, 2), pt_sg(ptbgd, ptgb3, 2), pointeeg, vert, 0)
            rectangle(img, ptgb, pt_sg(ptbgd, ptgb3, 2), rouge, 0)
            rectangle(img, ptgb, cthpbg, noir, 0)
            rectangle(img, ptgb1, cthpbg, bleu, 0)
            etoile(img, ct_sg(ptgb, cthpbg), dist(ptgb2, cthpbd)/3.325, blanc)
            ### Écu droit ###
            triangle(img, pt_sg(ptbd, ptbdb, 2), pt_sg(ptbdg, ptgb4, 2), pointeed, vert, 0)
            rectangle(img, ptdb, pt_sg(ptbdg, ptgb4, 2), rouge, 0)
            rectangle(img, ptdb, cthpbd, noir, 0)
            rectangle(img, ptgb2, cthpbd, bleu, 0)
            etoile(img, ct_sg(ptdb, cthpbd), dist(ptgb2, cthpbd)/3.325, blanc)
            ### Écu central ###
            for i in points_segment(ctgeg, coosCercle(ctgeg, ud*3, 270)):
                ellipse(img, i, [dist(ptbg, ptbd)/2, dist(ptgb1, ptgb3)*b], pourpre, 3, 0, 53)
            for i in points_segment(ctged, coosCercle(ctged, ud*3, 270)):
                ellipse(img, i, [dist(ptbg, ptbd)/2, dist(ptgb1, ptgb3)*b], pourpre, 3, 180, 127)
            rectangle(img, ptbgd, ptgb2, pourpre, 0)
            montagne(img, pt_sg(ct, ptb, 5), dist(ptgb3, ptgb4)/4.)
            etoile(img, ct_sg(ct, ptb), dist(ptgb3, ptgb4)/4.5)
            ### Bande supérieure ###
            img, ptculm = bande(img, pth, ud, ud*4)
            mt = 0.5/75*ud
            cbt = 10/75*ud
            ou = coosCercle(ptculm, longChar*mt/2 + longChar*mt*2, 180)
            scripte(img, coosCercle(ou, hautChar*mt/4, 270), cri, mt, 1, noir, ep*(mt*(1 + mt)), pol, -cbt, rot_par_char=cbt/5, combine=True)
            ### Bande inférieure ###
            img, ptterr = bande(img, ptb, ud*1.5, ud*4.5, rot=180)
            mt /= 2
            ep = 2/75*ud
            sep1 = 0.6
            sep2 = 0.7
            roty = 0.7
            ptterr = coosCercle(ptterr, hautChar*mt/2*(1-roty), 90)
            if len(texte1) % 2 == 0:
                a1 = longChar*mt/2
            else:
                a1 = 0
            if len(texte2) % 2 == 0:
                a2 = longChar*mt/2
            else:
                a2 = 0
            ou1 = coosCercle(coosCercle(ptterr, a1 + longChar*mt*(len(texte1)/2*sep1), 180 + rotation), hautChar*mt/2*6, 270 + rotation)
            ou2 = coosCercle(coosCercle(ptterr, a2 + longChar*mt*(len(texte2)/2*sep2), 180 + rotation), hautChar*mt/2*3, 270 + rotation)
            scripte(img, ou1, texte1, mt, sep1, noir, ep, pol, rot_par_char=-roty, rotation=len(texte1)*roty, combine=True)
            scripte(img, ou2, texte2, mt, sep2, noir, ep, pol, rot_par_char=-roty, rotation=len(texte2)*roty, combine=True)
            ## Points de repère ##
            pts = []
            for i in pts:
                cercle(img, i, ura, rubis, 0)
            return(img)
    if oui: ############################## Main ###
        def main(exec=False, help=True):
            if exec:
                demo(help)
if oui: ## Main ##
    #main(exec=non, help=False)
    #horloge(help=oui)
    pass