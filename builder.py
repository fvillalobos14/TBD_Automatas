import json
from automatas import Automata

def load_json(file_path):
    with open(file_path, "r") as read_file:
        data = json.load(read_file)

    return data

def build_automata(data):
    typ = data['grafo']['tipo']
    alphabet = data['grafo']['alfabeto']
    initial = data['grafo']['inicial']
    finale = data['grafo']['final']
    states = []
    transitions = data['grafo']['transiciones']

    for x in range(len(data['grafo']['transiciones'])):
        states.append(data['grafo']['transiciones'][x]['(estado)'])

    return typ, alphabet, initial, finale, transitions, states