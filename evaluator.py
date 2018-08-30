import json
import pandas as pd

def checkforState(transitions, state):
    idx = -1
    for x in range(len(transitions)):
        if transitions[x]['(estado)'] == state:
            idx = x
    return idx

def evaluateString(transitions, initial_state, final_states, data):
    state = initial_state
    for letter in data:
        idx = checkforState(transitions, state)
        state = transitions[idx][letter]

    return state in final_states

    
