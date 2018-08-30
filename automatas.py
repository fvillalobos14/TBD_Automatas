import re
import pandas as pd
from collections import OrderedDict
from prettytable import PrettyTable
from helpers import Remove, atoi, natural_keys

class Automata:
    def __init__(self, type, alphabet, initial, finale, states, transitions):
        self.type = type
        self.alphabet = alphabet
        self.initial = initial
        self.finale = finale
        self.states = states
        self.transitions = transitions
        self.table = pd.DataFrame(self.transitions)

    # the following print functions are mainly for debugging and/or showcase purposes

    def printType(self):
        print("\nThis automata is a " + self.type + ".")

    def printAplhabet(self):
        print("\nThis automata has an alphabet consisting of: ")
        print(self.alphabet)

    def printInitial(self):
        print("\nThis automata has the following initial state: ")
        print(self.initial)

    def printFinal(self):
        print("\nThis automata has the following final states: ")
        print(self.finale)

    def printStates(self):
        print("\nThis automata has the following states: ")
        print(self.states)

    def printTransitions(self):
        print("\nThis automata has the following transitions: ")
        print(self.transitions)

    def printTransitionsTable(self):
        print("\nThis automata has the following transition table: ")
        table = PrettyTable([''] + list(self.table.columns))
        for row in self.table.itertuples():
            table.add_row(row)
        print(str(table) + "\n")

    def printAll(self):
        self.printType()
        self.printStates()
        self.printInitial()
        self.printFinal()
        self.printAplhabet()
        self.printTransitionsTable()

    def updateTransitionTable(self):
        self.table = pd.DataFrame(self.transitions)

    def getNewStates(self):
        newstates = []
        # this is for the first set of immediate states that we can get
        for x in range(len(self.transitions)):
            y = 0
            while y < len(self.alphabet):
                if self.alphabet[y] in self.transitions[x]:
                    if type(self.transitions[x][self.alphabet[y]]) is str and len(self.transitions[x][self.alphabet[y]]) <= 2:
                        y = y + 0
                    elif type(self.transitions[x][self.alphabet[y]]) is list:
                        ns = ''.join(self.transitions[x][self.alphabet[y]])
                        newstates.append(ns)
                y = y + 1

        newstates = self.states + list(set(newstates))
        print(newstates)
        # now we split combined states to check for their inputs later
        indivstates = []
        nst = []
        for w in range(len(newstates)):
            if len(newstates[w]) <= 1:
                continue
            else:
                if len(newstates[w]) % 2 == 0:
                    lista = []
                    listares = []
                    for i in range(0, len(newstates[w]), 1):
                        res = newstates[w][i:i+1]
                        lista.append(res)

                    z = 0
                    while z < len(self.alphabet):
                        for item in lista:
                            for x in range(len(self.transitions)): # x is int type
                                if self.alphabet[z] in self.transitions[x]:
                                    if self.transitions[x]['(estado)'] == item:
                                        listares.append(self.transitions[x][self.alphabet[z]])  
                        z = z + 1
                    
                    for i in range(len(listares)):
                        temp = []
                        if i % 2 != 0:    
                            temp.append(listares[i-1])
                            temp.append(listares[i])
                            res = ''.join(str(v) for v in temp)
                            n1 = res.replace(" ", "")
                            n2 = n1.replace(",", "")
                            n3 = n2.replace("[", "")
                            n4 = n3.replace("]", "")
                            n5 = n4.replace("\'", "")
                            tempstr = []
                            for i in range(0, len(n5), 1):
                                res = n5[i:i+1]
                                tempstr.append(res)
                            
                            tempstr.sort(key=int)
                            orderedset = Remove(tempstr)
                            sta = ''.join(orderedset)
                            nst.append(sta)
                    
                else:
                    print("Wrong JSON format. Please edit it accordingly.")
                    exit

        indivstates =  list(set(nst))
        newstates.extend(indivstates)
        newstates = Remove(newstates)
        return newstates

    def getTransitions(self, new_states, alphabet):
        transitions = [] 
        for k in range(len(self.transitions)): #for already existing ones
            temptrans = {}
            state = self.transitions[k]['(estado)']
            temptrans.update({"(estado)" : state})
            
            j = 0 
            while j < len(self.alphabet):
                if self.alphabet[j] in self.transitions[k]:
                    letter = self.alphabet[j]
                    ns = ''.join(self.transitions[k][letter])
                    temptrans.update({letter : ns})
                j = j + 1
            
            transitions.append(temptrans)
        
        #print(transitions[0]['a'])
        #get all new states into a list
        new_ones = list(set(new_states).difference(self.states))

        for index in range(len(new_ones)):
            temptrans = []
            alltrans = {}
            current_new = new_ones[index]
            chara = 0
            # aca metemos el estado y las letras
            alltrans.update({"(estado)" : new_ones[index]})
            while chara < len(self.alphabet):
                # aca unimos las letras
                lettertemp = []
                for item in range(len(self.transitions)):
                   if self.alphabet[chara] in self.transitions[item]:
                        #agregar aca lo de letras indiv
                        current_st = self.transitions[item]['(estado)']
                        if new_ones[index].find(current_st) != -1:
                            lettertemp.extend(self.transitions[item][self.alphabet[chara]])
                            lettertemp = Remove(lettertemp)
                lettertemp.sort(key=int)
                ns = ''.join(lettertemp)
                alltrans.update({self.alphabet[chara] : ns})
                chara = chara + 1
            transitions.append(alltrans)
                    
        return transitions

    def convertToRegEx(self):
        print("Regex")

    def convertToDFA(self):
        typ = "DFA"
        alph = self.alphabet
        ini = self.initial
        finale = []
        new_states = self.getNewStates()
        new_transitions = self.getTransitions(new_states, alph)
        
        #check for any state that contains the final one
        for i in range(len(new_states)):
            if self.finale in new_states[i]:
                finale.append(new_states[i])
            else:
                continue

        dfa = Automata(typ, alph, ini, finale, new_states, new_transitions)
        return dfa

    def convertToNFA(self):
        print("NFA")
