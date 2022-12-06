def spc(input_data):
    data = [line.replace(' ', '') for line in input_data.splitlines()]
    scores1 = {'AX': 1 + 3,'BX': 1 + 0,'CX': 1 + 6,'AY': 2 + 6,'BY': 2 + 3,'CY': 2 + 0,'AZ': 3 + 0,'BZ': 3 + 6,'CZ': 3 + 3}
    print("Solution 1:",sum([scores1[game] for game in data]))

    scores2 = {'AX': 3,'BX': 1,'CX': 2,'AY': 1+3,'BY': 2+3,'CY': 3+3,'AZ': 2+6,'BZ': 3+6,'CZ': 1+6}
    print("Solution 2:",sum([scores2[game] for game in data]))
    
input_data = open('input.txt').read()
spc(input_data)


