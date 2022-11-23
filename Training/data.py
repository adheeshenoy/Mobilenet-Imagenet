from torch.utils.data.dataset import random_split
from torch.utils.data import DataLoader
import torchvision
# from torchvision import datasets
# from torch.utils.data import DataLoader
import pytorch_lightning as pl

import os
from torchvision.datasets import ImageFolder


class DataModule(pl.LightningDataModule):
    def __init__(self, args, data_path='./Dataset'):
        super().__init__()
        self.train_path = os.path.join(data_path, 'train')
        self.val_path = os.path.join(data_path, 'val')
        self.args = args

    def prepare_data(self):
        self.train_transform = torchvision.transforms.Compose([
            torchvision.transforms.Resize((224, 224)),
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(
                (0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])

        self.test_transform = torchvision.transforms.Compose([
            torchvision.transforms.Resize((224, 224)),
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(
                (0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])

    def setup(self, stage):
        self.train = ImageFolder(root=self.train_path,transform=self.train_transform)

        test = ImageFolder(root=self.val_path,
                                     transform=self.test_transform)
        print(len(test))
        self.valid, self.test = random_split(test, lengths=[24999, 25000])

    def train_dataloader(self):
        return DataLoader(dataset=self.train, batch_size=self.args.batch_size, drop_last=True, shuffle=True, num_workers=self.args.num_workers)

    def val_dataloader(self):
        return DataLoader(dataset=self.valid, batch_size=self.args.batch_size, drop_last=False, shuffle=False, num_workers=self.args.num_workers)

    def test_dataloader(self):
        return DataLoader(dataset=self.test, batch_size=self.args.batch_size, drop_last=False, shuffle=False, num_workers=self.args.num_workers)


# from dataclasses import dataclass
# @dataclass
# class arg:
#     batch_size: int = 5
#     num_workers: int = 0

# data = DataModule(arg())
# data.prepare_data()
# data.setup(0)
# for i, j in data.test_dataloader():
#     print(i.size())
#     break