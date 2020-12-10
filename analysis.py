import numpy as np
import pandas as pd
import datetime
import dateutil
import os


BaseData = r'C:\Users\kming\Documents\git\lianjia-beike-spider\data\ke\ershou\sh\\'

targets = []
for date in os.listdir(BaseData):
    if os.path.isdir(os.path.join(BaseData, date)):
        targets.append(date)


files = []
for f in os.listdir(os.path.join(BaseData, targets[0])):
    files.append(f)

def compareDate(ydate, tdate, flist):
    for ff in flist:

        yfile = os.path.join(BaseData, ydate, ff)
        tfile = os.path.join(BaseData, tdate, ff)

        if not(os.path.exists(yfile) and os.path.exists(tfile)):
            print(f'Skip file {ff}')
            continue

        print(f'Comparing for {ff}')

        yday = pd.read_csv(os.path.join(BaseData, ydate, ff))
        yday['priceNum'] = yday['price'].str.replace('万', '').astype(float)
        print(f'yday len: {len(yday)}')
        tday = pd.read_csv(os.path.join(BaseData, tdate, ff))
        print(f'tday len: {len(tday)}')
        tday['priceNum'] = tday['price'].str.replace('万', '').astype(float)
        m = yday.merge(tday, on=['href'], how='outer')
        changed = m[~m.price_x.isnull() & ~m.price_y.isnull() & (m.priceNum_x != m.priceNum_y)][['priceNum_x', 'priceNum_y', 'href']]
        print(f'price changed {len(changed)}')
        if len(changed) > 0:
            l1 = len(changed[changed.priceNum_x < changed.priceNum_y])
            l2 = len(changed[changed.priceNum_x > changed.priceNum_y])
            print(f'Price Up {l1}')
            print(f'Price Down {l2}')
        #   print(changed)
        gone = m[m.district_y.isnull() & ~m.href.isnull()][['desc_x', 'price_x', 'href']]
        new  = m[m.district_x.isnull() &~m.href.isnull()][['desc_y', 'price_y', 'href']]
        print(f'gone: {len(gone)}')

        #if len(gone) > 0:
        #    print(gone)
        print(f'new: {len(new)}')
        #if len(new) > 0:
        #    print(new)
