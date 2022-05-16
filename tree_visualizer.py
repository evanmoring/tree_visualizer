from copy import deepcopy
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
        {'frita':{},
        'george':{},
        'carl':{}},
    'fam2': {},
    }
}

def viz_tree(dictionary, depth = [], has_parent = False, has_sibling = False):
    for index, key in enumerate(dictionary):
        string = ''
        new_depth = deepcopy(depth)
        for i in depth:
            string += i

        first = (index == 0)
        last = (index == len(dictionary) - 1)
        if first and last:
            if has_sibling:
                if not has_parent:
                    string += "┌"
                else:
                    string += "├"
            else:
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
        has_children(dictionary, key)
        child_dictionary = dictionary[key]
            
        has_sibling = False#(list_index != len(dictionary))
        viz_tree(child_dictionary, new_depth, has_parent = True, has_sibling =has_sibling)

def viz_tree_2(dictionary):
    for i in dictionary:
        print(i)
        viz_tree_2(dictionary[i])

def has_children(dictionary, key):
    if len(dictionary[key]):
        return True
    else:
        return False

viz_tree(example_dict, has_sibling = False)
#viz_tree_2(example_dict)

# ┌├└│ ─
# unicode: http://www.unicode.org/charts/PDF/U2500.pdf
