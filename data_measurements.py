import pandas as pd
from math import log2
import tqdm

def compute_mec(filename = 'encoded_data.csv', image_h = 224, image_w = 224, image_c = 3):
    df = pd.read_csv(filename, header = None)
    df['labels'] = df[df.columns[-1]]
    df['sums'] = df[df.columns[:-1]].sum(axis = 1)
    df = df[['labels', 'sums']].sort_values(by = 'sums')
    print(df.head())

    threshold = 0
    cls = None
    for i, row in tqdm.tqdm(df.iterrows()):
        if row['labels'] != cls:
            cls = row['labels']
            threshold += 1

    min_thresh = log2(threshold + 1)
    
    return (min_thresh * (image_h * image_w * image_c) + 1) + (min_thresh + 1)
    

if __name__ == '__main__':
    print('mec = ', compute_mec())