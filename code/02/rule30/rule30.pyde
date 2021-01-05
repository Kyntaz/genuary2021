# RULE 30

# PARAMETERS
GRAIN = 3
EXT = 3
TRANS = 0.1
R = 0.0002
# /PARAMETERS

FIELD = None

def reset():
    global FIELD
    FIELD = [[random(1) < R for _ in range(ceil(width / GRAIN) + 1)] for _ in range(ceil(height / GRAIN) + 1)]

def setup():
    size(800, 800, P2D)
    noStroke()
    fill(255, 255, 255, TRANS  * 255)
    frameRate(12)
    
    reset()
    
def draw():
    global FIELD
    
    background(0)
    
    field_ = [[v for v in l] for l in FIELD]
    for row, l in enumerate(FIELD[:-1]):
        for col, val in enumerate(l):
            row_ = (row + 1) % len(FIELD)
            col_ = (col + 1) % len(l)
            _row = row - 1 if row > 0 else len(FIELD) - 1
            _col = col - 1 if col > 0 else len(l) - 1
            field_[row_][col] = (FIELD[row][_col] != (FIELD[row][col] or FIELD[row][col_])) or FIELD[row_][col]
            if field_[row][col]:
                circle(col * GRAIN, row * GRAIN, GRAIN * EXT)
    
    FIELD = field_

def keyPressed():
    if key == " ":
        reset()
    if key == "s":
        save("frame.png")
