from bellman.path_finder import find_path
from bellman.config import Config
from json_reader import json_reader


Config.edges = json_reader('/home/pi/Documents/cpm/edges.txt')

path = find_path('a3f', 'e4', debug=True, iterations=170)
print(path)