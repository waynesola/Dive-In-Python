# create a dictionary named a_dict
a_dict = {'a1': 100, 'a2': 500, 'a3': 900}
print(a_dict)

# create a dictionary named b_dict
info = [('b1', 3000), ('b2', 4500), ('b3', 6000)]
b_dict = dict(info)
print(b_dict)

# create a dictionary named c_dict, using 'fromkeys()'
c_dict = {}.fromkeys(['wang', 'chen', 'zhang'], 1000)
print(c_dict)

# sorted()，排列字典key，返回列表
print(sorted(c_dict))

# create a dictionary named d_dict, using 'zip()'
pList = [('AAPL', '蘋果公司', '132.040'), ('AXP', 'American Express Company', '77.800'),
         ('BA', 'The Boeing Company', '163.810'), ('CAT', 'Caterpillar Inc.', '92.910'),
         ('CSCO', '思科系統公司', '31.270'), ('CVX', 'Chevron Corporation', '111.580'),
         ('DD', 'E. I. du Pont de Nemours and Company', '75.960'),
         ('DIS', 'The Walt Disney Company', '109.000'), ('GE', 'General Electric Company', '29.430'),
         ('GS', 'The Goldman Sachs Group, Inc.', '237.730'), ('HD', 'The Home Depot, Inc.', '137.880'),
         ('IBM', 'International Business Machines Corporation', '176.170'), ('INTC', '英特爾公司', '36.380'),
         ('JNJ', 'Johnson &amp; Johnson', '113.400'), ('JPM', 'JPMorgan Chase &amp; Co.', '85.960'),
         ('KO', 'The Coca-Cola Company', '42.020'), ('MCD', "McDonald's Corporation", '124.670'),
         ('MMM', '3M Company', '177.070'), ('MRK', 'Merck &amp; Co., Inc.', '64.320'),
         ('MSFT', '微軟公司', '63.340'), ('NKE', 'NIKE, Inc.', '53.880'),
         ('PFE', 'Pfizer Inc.', '32.140'), ('PG', 'The Procter &amp; Gamble Company', '88.330'),
         ('TRV', 'The Travelers Companies, Inc.', '117.810'), ('UNH', 'UnitedHealth Group Incorporated', '160.310'),
         ('UTX', 'United Technologies Corporation', '110.400'), ('V', 'Visa Inc.', '85.090'),
         ('VZ', 'Verizon Communications Inc.', '48.370'), ('WMT', 'Wal-Mart Stores, Inc.', '67.810'),
         ('XOM', 'Exxon Mobil Corporation', '81.480')]

aList = []
bList = []

for i in range(30):
    companyStr = pList[i][0]
    priceStr = pList[i][2]
    aList.append(companyStr)
    bList.append(priceStr)

d_dict = dict(zip(aList, bList))

print(d_dict)
