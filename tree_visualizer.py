from copy import deepcopy
example_dict = {
'pets':[{
    'cat': [
        {'frita':[]},
        {'george':[]},
        {'carl':[]},
    ],
    'dog': [ 
        {'fido':[]},
    ]
}],
'children':[{
    'fam1': [
        {'frita':[]},
        {'george':[]},
        {'carl':[]},
    ],
    'fam2': []},
    ]
}

#print(example_dict)

def viz_tree(dictionary, depth, has_parent, has_sibling):
    for index, key in enumerate(dictionary):
        pass
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
        for list_index, child_dictionary in enumerate(dictionary[key]):
            has_sibling = (list_index != len(dictionary[key]) - 1)
            viz_tree(child_dictionary, new_depth, has_parent = True, has_sibling =has_sibling)

def has_children(dictionary, key):
    if len(dictionary[key]):
        return True
    else:
        return False

viz_tree(example_dict, [], has_parent = False, has_sibling = False)

# ┌├└│ ─
# unicode: http://www.unicode.org/charts/PDF/U2500.pdf
