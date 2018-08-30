from automatas import Automata
from builder import load_json, build_automata
from evaluator import evaluateString

def print_options():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Load JSON file")
    print("2. Evaluate word")
    print("3. Convert to DFA")
    print("4. Convert to NFA")
    print("5. Convert to Regex")
    print("6. Quit Program")
    print(67 * "-")

def menu():
    loop = True
    nier = ""
    data = ""
    dfa = ""
    while loop:
        print_options()
        options = input("Please enter your choice! [1-6] \n")
        tipo, alfabeto, inicial, final, transiciones, estados = build_automata(data)
        nier = Automata(tipo, alfabeto, inicial, final, estados, transiciones)

        if str(options) == "1":     
            print("Please enter the json file name.\n\n")
            fn = input()
            data = load_json("./" + fn + '.json')
            nier.printAll()
        elif str(options) == "2":
            print("Please enter the word you want to evaluate.\n\n")

        elif str(options) == "3":
            print("Converting to DFA...\n\n")
            
        elif str(options) == 4:
            print("Coming soon :)\n\n")
        elif str(options) == 5:
            print("Coming soon :)\n\n")
        elif str(options) == 6:
            print("Goodbye!\n\n")
            exit
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Incorrect choice. Please try again.\n\n\n\n")

def main():
    data = load_json("./test.json")
    tipo, alfabeto, inicial, final, transiciones, estados = build_automata(data)
    nier = Automata(tipo, alfabeto, inicial, final, estados, transiciones)
    #nier.printAll()
    dfa = nier.convertToDFA()
    dfa.printAll()
    
    cad = "aabbb"
    evalu  = str(evaluateString(dfa.transitions,dfa.initial,dfa.finale,cad))
    result = 'Yes.' if evalu == 'True' else 'No.'
    print("\nDoes the string \'" + cad + "\' belong to the automata's language? " + result + "\n")
    
if __name__ == "__main__":
    main()

    '''
        data = load_json("./test.json")
        tipo, alfabeto, inicial, final, transiciones, estados = build_automata(data)
        nier = Automata(tipo, alfabeto, inicial, final, estados, transiciones)
        nier.printAll()
        dfa = nier.convertToDFA()
        dfa.printAll()

        cad = "010110"
        evalu  = str(evaluateString(nier.transitions,nier.initial,nier.finale,cad))
        result = 'Yes.' if evalu == 'True' else 'No.'
        print("\nDoes the string \'" + cad + "\' belong to the automata's language? " + result + "\n")
        
        nier.printTransitions()
        nier.transitions[0]['c'] = cad
        print(len(nier.getNewStates()[1]))
    '''
    #print(len(nier.transitions[0]['b']))
