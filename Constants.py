#Inherent Characteristics
WIDTH = 10
HEIGHT = 20
DROPSPEED = 2 #drops per second

#Drawing Characteristics
CELLDIM = 30
CELLMARGIN = CELLDIM//15
MARGINWIDTH = CELLDIM // 2 + 5
MARGINHEIGHT = CELLDIM // 2 + 5
CANVASWIDTH = CELLDIM*WIDTH+2*MARGINWIDTH
CANVASHEIGHT = CELLDIM*HEIGHT+2*MARGINHEIGHT

#Colors
BACKGROUND = (100, 100, 100)
GRIDBACKGROUND = (10, 10, 70)
COLOR_NONE = (50, 50, 100)
COLOR_I = (0, 255, 255) #Cyan
COLOR_O = (255, 255, 51) #Yellow
COLOR_T = (204, 0, 204) #Purple
COLOR_S = (0, 255, 0) #Green
COLOR_Z = (255, 0, 0) #Red
COLOR_J = (0, 0, 255) #Blue
COLOR_L = (255, 128, 0) #Orange
COLOR_I_GHOST = (0, 150, 150) #Cyan
COLOR_O_GHOST = (150, 150, 0) #Yellow
COLOR_T_GHOST = (120, 0, 120) #Purple
COLOR_S_GHOST = (0, 150, 0) #Green
COLOR_Z_GHOST = (150, 0, 0) #Red
COLOR_J_GHOST = (0, 0, 175) #Blue
COLOR_L_GHOST = (150, 50, 0) #Orange

COLOR_DICTIONARY = {None:COLOR_NONE,"I":COLOR_I,"O":COLOR_O,\
                    "T":COLOR_T,"S":COLOR_S,"Z":COLOR_Z,\
                    "J":COLOR_J,"L":COLOR_L}

COLOR_GHOST_DICTIONARY = {"I":COLOR_I_GHOST,"O":COLOR_O_GHOST,\
                          "T":COLOR_T_GHOST,"S":COLOR_S_GHOST,"Z":COLOR_Z_GHOST,\
                          "J":COLOR_J_GHOST,"L":COLOR_L_GHOST}

PIECES = ["I", "O", "T", "S", "Z", "J", "L"]

PIECEPOSITIONS = {"I":[[5,0],[5,1],[5,2],[5,3]],
                  "O":[[4,0],[4,1],[5,0],[5,1]],
                  "T":[[5,0],[4,1],[5,1],[6,1]],
                  "S":[[5,0],[6,0],[4,1],[5,1]],
                  "Z":[[4,0],[5,0],[5,1],[6,1]],
                  "J":[[4,0],[4,1],[5,1],[6,1]],
                  "L":[[6,0],[4,1],[5,1],[6,1]]}

PIECEORIGINS = {"I":[5,2],
                "O":[5,1],
                "T":[5,1],
                "S":[5,1],
                "Z":[5,1],
                "J":[5,1],
                "L":[5,1]}