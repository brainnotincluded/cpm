import json
 
def json_reader(file_path):
    with open(file_path, newline='\n') as csvfile:
        reader = json.load(csvfile)
            
        tr = {'А':'a',
              'Б':'b',
              'В':'c',
              'Г':'d',
              'Д':'e',
              'Е':'f',
              'Ж':'g'}
        re_f = {}
        for i in reader:
            re_f[(tr[i[0][0]]+i[0][1], tr[i[1][0]]+i[1][1])]=-int(i[2])
        return re_f
    
    
if __name__ == '__main__':
    print(json_reader('/home/pi/Documents/cpm/edges.txt'))
