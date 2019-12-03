import math

data = [x.split(',') for x in open('Coinbase_BTCUSD_1h.csv', 'r+').readlines()[1:]]

print(data[0])

minimum, mini, maximum, maxi = 999999999.9, 0.0, 0, 0

for i in range(150):
    if minimum>float(data[i][4]):
        minimum=float(data[i][4])
        mini=i
    if maximum<float(data[i][3]):
        maximum=float(data[i][3])
        maxi=i
print(minimum, maximum, mini, maxi)

maximum_B, maxi_B = 999999999999.0, 0

if maxi<mini:
    for i in range(maxi):
        if maximum_B>float(data[i][4]):
            maximum_B=float(data[i][4])
            maxi_B=i
    print(maximum_B, maxi_B)
    maximum_B=0.0
    for i in range(maxi_B):
        if maximum_B<float(data[i][3]):
            maximum_B=float(data[i][3])
            maxi_B=i
    print(maximum_B, maxi_B)
else:
    #TODO
    pass