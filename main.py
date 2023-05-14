def read_grammar_file(filename):
    """
    Read a regular grammar in CNF from a file.
    """
    grammar = {}
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            nonterminal, productions = line.split('->')
            productions = [prod.split() if prod != 'lambda' else 'l' for prod in productions.split('|')]
            productions = [list(p) if p !='l' else 'l' for prod in productions for p in prod]
            grammar[nonterminal] = productions
            
    return grammar

grammar = read_grammar_file('LFA 3 - All the words of a grammar\grammar.txt')
# grammar = {'S':[('a', 'A'), ('d', 'E')],'A':[('a', 'B'), ('a', 'S')], 'B':[('b', 'C')], 'C':[('b', 'D'), ('b', 'B')], 'D':[('c', 'D'),'l'], 'E':['l']}

print(grammar)

def is_word_accepted(grammar, start_symbol, word):
    if len(word) == 0 and 'l' in grammar[start_symbol]:
        return True
    
    for rule in grammar[start_symbol]:
        if len(rule) == 1 and isinstance(rule[0], str) and rule[0].islower():
            if word and word[0] == rule[0]:
                if len(word) == 1:
                    return True
                elif is_word_accepted(grammar, start_symbol, word[1:]):
                    return True
        elif word and word[0] == rule[0] and rule[0].islower():
            if is_word_accepted(grammar, rule[1], word[1:]):
                return True
        elif rule[0].isupper():
            if is_word_accepted(grammar, rule[0], rule[1]+word):
                return True
                    
    return False


def getAlphabet(grammar):
    letters =set()
    for letter in grammar.values():
        for l in letter:
            if l[0] != 'l':
                letters.add(l[0])
    return list(letters)

alphabet =getAlphabet(grammar)

def generateWorld(grammar, word, n,alphabet):
    if len(word) >= n:
        if is_word_accepted(grammar, 'S', word):
            print(word)
    else:
        for letter in alphabet:
            generateWorld(grammar,word + letter,n,alphabet)
    return
n= int(input('n=?'))

# print(is_word_accepted(grammar,'S','aaaabbbbe'))
generateWorld(grammar,'',n,alphabet)
