def bar_code(b):
    bs = []
    b.move_for_degrees(20)
    b.move_follow_line(b.stop_if_line)
    b.move_for_degrees(20)
    b.move_for_degrees(20)
    for i in range(7):        
        b.move_for_degrees(19)
        bs += [b.black_or_white()]
        print(bs)
    return to_position(bs)

def to_position(bs):
    s = ''
    d = {1:'a',
         2:'b',
         3:'c',
         4:'d',
         5:'e',
         6:'f',
         7:'g'
         }
    m = 0
    for i,j in enumerate(bs):
        m += j*(2**i)
    assert 10 <= m < 100, "Bad barcode:{}".format(m)
    high = m // 10
    low = m % 10
    s += d[high]
    s += str(low)
    return s
    
        
if __name__ == '__main__':
    from utils import Brick
    b = Brick()
    b.move_for_degrees(20)
    b.follow_line(b.stop_if_line)
    b.move_for_degrees(20)
    print(to_position([1,1,0,0,0,1,0]))
