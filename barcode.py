def bar_code(b):    
    b.move_for_degrees(20)
    b.move_follow_line(b.stop_if_line)
    b.move_for_degrees(20)
    b.move_for_degrees(20)
    for i in range(7):        
        b.move_for_degrees(20)
        print(b.black_or_white(),end='')
    print()
        
if __name__ == '__main__':
    from utils import Brick
    import sys
    print(sys.version)

    b = Brick()
    
    try:
        bar_code(b)
    finally: 
        b.reset_all()