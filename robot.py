from barcode import bar_code
from navigator import Navigator
from bellman.path_finder import find_path
from bellman.path_finder import visualize_plan
from utils import Brick
from bellman.config import Config
import time



try:
    b = Brick()
    b.move_follow_line(b.stop_if_line, degrees=354.06519295616334)
    n = Navigator(b)
    bs = bar_code(b)
    b.move_follow_line(b.stop_if_line)
    b.move_follow_line(b.stop_if_line)
    path, fin_state = find_path('a3f', bs)
    b.move_for_degrees(140)
    n.move(path)
    time.sleep(2.5)
    Config.edges = {}
    print("Fin state.")
    print(fin_state)
    path, fin_state = find_path(fin_state, 'a3')
    n.move(path)
    n.move({
        'b' : '',
        'r' : 'r',
        'l' : 'l'}[fin_state[2]])
    b.move_follow_line(b.stop_if_line, degrees=354.06519295616334)
    b.move_for_degrees(505)
    b.move_follow_line(b.stop_if_line)
    b.move_for_degrees(360)

finally: 
    b.reset_all()

