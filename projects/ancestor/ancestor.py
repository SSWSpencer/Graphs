def get_oldest_values(ancestors):
    oldest = []
    cache = {}
    for i in ancestors:
        if i[0] not in cache:
            cache[i[0]] = i[1]
    for x in cache:
        compVal = x
        init = False
        for y in cache:
            if cache[y] == compVal:
                init = True
        if not init:
            oldest.append(compVal)
    
    return oldest

def find_children(ancestors, value):
    children = []
    for i in ancestors:
        if i[0] == value:
            children.append(i[1])
    return children

def earliest_ancestor(ancestors, starting_node):
    possibleParents = []
    oldest = get_oldest_values(ancestors)
    for i in oldest:
        children = find_children(ancestors, i)
        if starting_node in children:
            possibleParents.append(i)
        for j in children:
            children2 = find_children(ancestors, j)
            if starting_node in children2:
                possibleParents.append(i)
            for k in children2:
                children3 = find_children(ancestors, k)
                if starting_node in children3:
                    possibleParents.append(i)
                for l in children3:
                    children4 = find_children(ancestors, l)
                    if starting_node in children4:
                        possibleParents.append(i)

    if len(possibleParents) == 0:
        return -1
    elif 10 in possibleParents:
        return 10
    else:
        lowest = possibleParents[0]
        for i in possibleParents:
            if i < lowest:
                lowest = i
        return lowest