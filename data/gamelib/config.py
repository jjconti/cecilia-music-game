import os
import data

WHITE = (255,255,255)
BLACK = (0,0,0)

WINDOW_TITLE = "Cecilia Music Game"
WINDOW = 640,480

INTRO = data.filepath('main.jpg')
HELP = data.filepath('help.jpg')
FINAL = data.filepath('fin.jpg')
FINAL2 = data.filepath('finalfinal.jpg')
FONDO = data.filepath('guita1.jpg')
#PORTA = data.filepath('portacuerdas.jpg')
#PLAYBG = data.filepath('play.jpg')

C = 5

CUERDAS = [0, 5, 10, 15, 30, 50, 65]

# Sounds

G1 = data.filepath(os.path.join('sounds', '1ra-e.wav'))
G2 = data.filepath(os.path.join('sounds', '2da-B.wav'))
G3 = data.filepath(os.path.join('sounds', '3ra-G.wav'))
G4 = data.filepath(os.path.join('sounds', '4ta-D.wav'))
G5 = data.filepath(os.path.join('sounds', '5ta-A.wav'))
G6 = data.filepath(os.path.join('sounds', '6ta-E.wav'))
GALL = data.filepath(os.path.join('sounds', 'EADGBe.wav'))

SOUNDS = [GALL, G1, G2, G3, G4, G5, G6]

# Levels

NEXT0 = data.filepath('level1.jpg') 

BG1 = data.filepath('bg1.jpg')
CANCION1 = data.filepath(os.path.join('sounds', 'cancion1.wav'))
NEXT1 = data.filepath('level2.jpg') 
L1 = {'cuerdas': '1234', 'cancion': '1122334', 'bg': BG1, 'wav': CANCION1, 'next': NEXT1}

BG2 = data.filepath('bg2.jpg')
CANCION2 = data.filepath(os.path.join('sounds', 'cancion2.wav'))
NEXT2 = data.filepath('level3.jpg') 
L2 = {'cuerdas': '1234', 'cancion': '1414222333', 'bg': BG2, 'wav': CANCION2, 'next': NEXT2}

BG3 = data.filepath('bg3.jpg')
CANCION3 = data.filepath(os.path.join('sounds', 'cancion3.wav'))
NEXT3 = data.filepath('level4.jpg') 
L3 = {'cuerdas': '12345', 'cancion': '555111234', 'bg': BG3, 'wav': CANCION3, 'next': NEXT3}

BG4 = data.filepath('bg4.jpg')
CANCION4 = data.filepath(os.path.join('sounds', 'cancion4.wav'))
NEXT4 = data.filepath('level5.jpg') 
L4 = {'cuerdas': '12345', 'cancion': '543543123123', 'bg': BG4, 'wav': CANCION4, 'next': NEXT4}

BG5 = data.filepath('bg5.jpg')
CANCION5 = data.filepath(os.path.join('sounds', 'cancion5.wav'))
NEXT5 = data.filepath('level6.jpg') 
L5 = {'cuerdas': '123456', 'cancion': '126126456333', 'bg': BG5, 'wav': CANCION5, 'next': NEXT5}

BG6 = data.filepath('bg6.jpg')
CANCION6 = data.filepath(os.path.join('sounds', 'cancion6.wav'))
NEXT6 = data.filepath('fin.jpg') 
L6 = {'cuerdas': '123456', 'cancion': '6546541212123344', 'bg': BG6, 'wav': CANCION6, 'next': NEXT6}

LEVELS = [L1, L2, L3, L4, L5, L6]
