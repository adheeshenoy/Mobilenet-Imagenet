import tarfile
import os
import json


def extract(path = 'dataset.tar'):
    file = tarfile.TarFile.open(path)
    file.extractall()
    
# def rename_folders(path = 'imagenette2'):
#     mapping = dict(
#     n01440764='tench',
#     n02102040='English springer',
#     n02979186='cassette player',
#     n03000684='chain saw',
#     n03028079='church',
#     n03394916='French horn',
#     n03417042='garbage truck',
#     n03425413='gas pump',
#     n03445777='golf ball',
#     n03888257='parachute'
#     )
    
#     os.rename(os.path.join(path, 'val'), os.path.join(path, 'test'))
    
#     info = {'train': {}, 'test': {}}
    
#     for folder in ('train', 'test'):
#         folder_path = os.path.join(path, folder)
#         for k, v in mapping.items():
#             os.rename(os.path.join(folder_path, k), os.path.join(folder_path, v))
            
#             info[folder][v] = len(os.listdir(os.path.join(folder_path, v)))

#         info[folder]['total'] = sum(info[folder].values())

#     with open('data_description.json', 'w') as f:
#         json.dump(info, f)

if __name__ == '__main__':
    extract()
    # rename_folders()