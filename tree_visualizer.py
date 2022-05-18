from copy import deepcopy

def viz_tree(dictionary, depth = [], has_parent = False):
    for index, key in enumerate(dictionary):
        string = ''
        new_depth = deepcopy(depth)
        for i in depth:
            string += i

        first = (index == 0)
        last = (index == len(dictionary) - 1)

        if first and last:
            if not has_parent:
                string += "─"
            else:
                string += "└"
            new_depth.append('  ')

        elif first:
            if not has_parent:
                string += "┌"
            else:
                string += "├"
            new_depth.append('│ ')

        elif last:
            string += "└"
            new_depth.append('  ')

        else:    
            string += '├'
            new_depth.append('│ ')

        string += "─"

        if has_children(dictionary, key):
            string += "┬"
        else:
            pass
        string += key
        print(string)
        child_dictionary = dictionary[key]
            
        viz_tree(child_dictionary, new_depth, has_parent = True)

def has_children(dictionary, key):
    if len(dictionary[key]):
        return True
    else:
        return False

example_dict = {
'pets':{
    'cat': 
        {'frita':{},
        'george':{},
        'carl':{}},
    'dog':  
        {'fido':{}}
},
'children':{
    'fam1':
        {'frita':{}},
    'fam2': {},
    }
}

if __name__ == '__main__':
    viz_tree(example_dict)

# ┌├└│ ─
# unicode: http://www.unicode.org/charts/PDF/U2500.pdf
