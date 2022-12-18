# MobileNet-ImageNet

## Dataset Creation

The dataset can be created using the notebook "dataset-creator.ipynb. This was run on kaggle on [this dataset](https://www.kaggle.com/competitions/imagenet-object-localization-challenge/data)

The processed tar file can be found [here](https://drive.google.com/file/d/1x9ziCKJYUtfuJtmzAD7KzA5vRS6J-IF3/view?usp=sharing)

The encoded dataset used to compute the MEC of the model was created using Encoded_data_Creator.ipynb

## Training

All training was performed using the experimental_tensorflow.ipynb file. 

## Measurement

The algorithm 2 mentioned in the paper can be found in data_measurements.py
s
## Acknowledgements
Initially based on [this notebook](https://github.com/rasbt/deeplearning-models/blob/master/pytorch-lightning_ipynb/cnn/cnn-mobilenet-v2-cifar10.ipynb)