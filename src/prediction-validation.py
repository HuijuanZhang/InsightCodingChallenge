# Read data
act = [i.rstrip('\n').split('|') for i in open('./input/actual.txt', 'r')]
pred = [i.rstrip('\n').split('|') for i in open('./input/predicted.txt', 'r')]

# Read window size
with open('./input/window.txt', 'r') as f:
    win = int(f.read()[0])

# Create a dictionary for actual and predicted separately
dict_act = {(int(i), j):float(k) for i,j,k in act}
dict_pred = {(int(i), j):float(k) for i,j,k in pred}

# Calculate error for each stock at each hour
dict_err = {}
for i in dict_act.items():
    if i[0] in dict_pred:
        diff = round(abs(i[1] - dict_pred[i[0]]), 2)
        dict_err[i[0]] = diff

# Calculate average error
compar = {}
for j in list(range(min([i[0] for i in dict_act.keys()]), max([i[0] for i in dict_act.keys()])-win+2)):
    err = []
    for i in dict_err.keys():
        if i[0] in range(j, j+win):
            err.append(dict_err[i])
    ave_err = sum(err)/len(err)
    compar[(j, j+win-1)] = format(ave_err, '.2f')

# Output to a text file
f = open('./output/comparison.txt', 'w')
for i in compar.items():
    f.write(str(i[0][0])+'|'+str(i[0][1])+'|'+i[1]+'\n')
f.close()
