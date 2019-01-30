mySentence = 'loves the color'

color_list = {'green', 'blue', 'red', 'cyan', 'magenta'}

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name, mySentence, i)
        lst.append(msg)
    return lst


lst = color_function('ALLAN')
for i in lst:
    print(i)

