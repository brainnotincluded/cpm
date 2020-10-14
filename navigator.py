class Navigator:
    def __init__(self, brickPi):
        self._brickPi = brickPi
        
    def move(self, ncode):
        d = {
            'f': self.forward,
            'l': self.left,
            'r': self.right,
            's': self.start
        }
        for c in ncode:
            d[c]()
                
    def forward(self):
        b = self._brickPi
        
        b.move_follow_line(b.stop_if_line)
        b.move_for_degrees(140)
        
        print('f')
    
    def right(self):
        self._brickPi.rotate(-135)
        print('r')
        
    def left(self):
        self._brickPi.rotate(135)
        print('l')
        
    def start(self):
        pass
        
if __name__ == '__main__':
    from utils import Brick
    
    b = Brick()
    nv = Navigator(b)
    try:
        nv.move('flfrflfrflfr')    
    finally: # except the program gets interrupted by Ctrl+C on the keyboard.
        b.reset_all()    
    