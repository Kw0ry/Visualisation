import pandas as pd
import numpy as np

df = pd.read_csv(
    'data.csv',
    sep='\t',
    names=['ticker', 'per', 'date', 'time', 'open', 'high', 'low', 'close', 'vol'],
    skiprows=1
)

data = df.tail(10)

data['close'] = data['close'].astype('float')
data['date'] = data['date'].astype('string')
data['date'] = np.array([dt[6:8] + "-" + dt[4:6] + "-" + dt[0:4] for dt in data['date']])

with open('data.js', 'w', encoding='utf') as file:
    file.write('const names = ' + str(data['date'].tolist()) + '\n')
    file.write('const values = ' + str(data['close'].tolist()) + '\n')

    file.close()
