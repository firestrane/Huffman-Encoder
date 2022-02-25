from Nodes import *


def getTree(s, delim=None):
    #returns huffman tree from string
    return __huffman__(s, delim)
    
def getCodex(node):
    #returns codex from huffman tree
    return __getEndNodes__(node)


def huffEncode(codex, s, delim=None):
    #encodes a string into compressed binary using a given huffman tree codex
    if delim:
        s = s.split(delim)
        
    str = ''
    for char in s:
        str += codex[char]
    return str
    
def huffDecode(bits, tree, delim=''):
    #returns character from given huffman tree
    node = tree
    str = ''
    for i in range(len(bits)):
            
        if bits[i] == '0':
            node = node.leftNode
        elif bits[i] == '1':
            node = node.rightNode
        else:
            return False
            
        if type(node) == endNode:
            str += node.char + delim #add original delimiter (e.g space)
            node = tree
    
    return str[:-1] #remove last delimiter (e.g space)

def __countEntity__(s, delim=None):
    counts = {}
    if delim:
        s = s.split(delim)
    
    for char in s:
            if char in counts:
                counts[char]+=1
            else:
                counts[char] = 1
    
    
    return counts




def __huffman__(s, delim=None):
    #takes a string and returns huffman tree (node object)
    
    #count each unique character and store values in a dictionary
    counts = __countEntity__(s, delim)
    
    #sort the dictionary by count into a list of tuples (ascending order)
    tree = sorted([y for y in counts.items()], key=lambda y:y[1])
    
    for i in range(len(tree)):
        eN = endNode(tree[i]) #convert all tuples into endNode objects
        tree[i] = eN
    
    while True:
        
        
        n = node(tree[0], tree[1]) #join first two elements into a node
        tree[0].parentNode = tree[1].parentNode = n #set parent nodes
        
        tree[0].path += '0' #if left node, relative path from parent is 0
        tree[1].path += '1' #if right node then 1
        
        if len(tree) == 2:
            tree = n
            break
        
        else:
            tree = tree[2:] #pop first two elements
            for i in range(len(tree)):
                if n.value < tree[i].value:
                    
                    tree.insert(i, n)
                    break
                
                if i+1 == len(tree):
                    tree.append(n)
              
    return tree


def __getEndNodes__(node, x={}, p=''):
    #returns dictionary of all unique endNode objects with corresponding bit string
        
    if type(node) == endNode:
        node.path = p + node.path
        return node
    else:
        
        p += node.path 
        
        l = __getEndNodes__(node.leftNode, x, p)
        r = __getEndNodes__(node.rightNode, x, p)
        
        #if statement required to avoid adding lists to list x
        if type(l) == endNode:
            x[l.char] = l.path
            
        if type(r) == endNode:
            x[r.char] = r.path
        
        return x





















