open_file = open('CupcakeInvoices.csv')

# for row in open_file:
#     print(row)

for line in open_file:
    line = line.rstrip('/n').split(',')
    print(line[2])
    quantities = int(line[3])
    price = float(line[4])
    total_price = round(quantities * price, 2)
    print(total_price)

total_invoice = 0

for line2 in open_file:
  line2 = line2.split(',')
  total_invoice = total_invoice + (int(line2[3]) * float(line2[4]))
    
print(round(total_invoice,2))

open_file.close()

import matplotlib.pyplot as plt 


open_file = open('CupcakeInvoices.csv')

types = []
sales = []

for row in open_file:
  row = row.split(',')
  types.append(row[2])
  sales.append(int(row[3]))

plt.bar(types, sales, color = 'g', label = 'File Data')

plt.xlabel('types of cupcakes', fontsize = 12)
plt.ylabel('sales', fontsize = 12)

plt.title('Cupcake Sales', fontsize = 20)
plt.legend()
plt.show()