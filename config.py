import os

WHITE = (255,155,255)
BLACK = (0,0,0)

WINDOW_TITLE = "Cecilia Music Game"
WINDOW = 640,480

FONDO = 'fondo.jpg'
PORTA = 'portacuerdas.jpg'
PLAYBG = 'play.jpg'

C = 5

CUERDAS = [0, 5, 10, 15, 30, 50, 65]

# Sounds

G1 = os.path.join('sounds', '1ra-e.wav')
G2 = os.path.join('sounds', '2da-B.wav')
G3 = os.path.join('sounds', '3ra-G.wav')
G4 = os.path.join('sounds', '4ta-D.wav')
G5 = os.path.join('sounds', '5ta-A.wav')
G6 = os.path.join('sounds', '6ta-E.wav')
GALL = os.path.join('sounds', 'EADGBe.wav')

SOUNDS = [GALL, G1, G2, G3, G4, G5, G6]

# Levels

BG1 = 'bg1.jpg'
L1 = {'cuerdas': '1234', 'cancion': '1122334', 'bg': BG1}

BG2 = 'bg2.jpg'
L2 = {'cuerdas': '1234', 'cancion': '14142223331212', 'bg': BG2}

BG3 = 'bg3.jpg'
L3 = {'cuerdas': '12345', 'cancion': '555111234', 'bg': BG3}

BG4 = 'bg4.jpg'
L4 = {'cuerdas': '12345', 'cancion': '543543123123', 'bg': BG4}

BG5 = 'bg5.jpg'
L5 = {'cuerdas': '123456', 'cancion': '123124125126', 'bg': BG5}

BG6 = 'bg6.jpg'
L6 = {'cuerdas': '123456', 'cancion': '654654121212334434', 'bg': BG6}

LEVELS = [L1, L2, L3, L4, L5, L6]
