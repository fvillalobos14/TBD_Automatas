import re

def Remove(liste):
	result = []
	for item in liste:
		if item not in result:
			result.append(item)
	return result

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]