class Navigator:
    def __init__(self, brickPi):
        self._brickPi = brickPi
        self._rot_deg = 135
        
    def move(self, ncode):
        d = {
            'f': self.forward,
            'l': self.left,
            'r': self.right,
            's': self.start
        }
        for i in range(len(ncode)):
            c=ncode[i]
            non_stop=False
            if len(ncode) > i+1 and ncode[i+1] == c:
                non_stop = True
            d[c](non_stop)
                
    def forward(self,nonstop=False):
        b = self._brickPi
        
        b.move_follow_line(b.stop_if_line, do_motor_stop=False)
        b.move_for_degrees_new(140, nonstop)
        
        print('f')
    
    def right(self,nonstop=False):
        self._brickPi.rotate(-self._rot_deg)
        print('r')
        
    def left(self,nonstop=False):
        self._brickPi.rotate(self._rot_deg)
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
    