import pandas as pd
from math import log2, log
import tqdm

def compute_mec(filename = 'encoded_data.csv', classes = 1000):
    '''
    32 -> 41024
    64 -> 82
    
    '''
    df = pd.read_csv(filename, header = None)
    latent_dimension = df.shape[1] - 1
    
    print('latent space dimension:', latent_dimension)
    
    df['sums'] = df[df.columns[:-1]].sum(axis = 1)
    df['labels'] = df[df.columns[-2]]
    df = df[['labels', 'sums']].sort_values(by = 'sums')
    print(df.head())

    threshold = 0
    cls = None
    s = None
    for _, row in tqdm.tqdm(df.iterrows()):
        if row['labels'] != cls:
            threshold += 2 if row['sums'] != s else 1
            cls = row['labels']
            s = row['sums']

    min_thresh = log2(threshold + 1)
    
    return (min_thresh * (latent_dimension + 1)) + ((min_thresh + 1) * classes)

if __name__ == '__main__':
    print('mec = ', compute_mec())