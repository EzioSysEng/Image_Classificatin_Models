""" train and test dataset

author zixuan
"""
import os,random,glob
import sys
import pickle
from PIL import Image

from skimage import io
import matplotlib.pyplot as plt
import numpy 
import torch
from torch.utils.data import Dataset

class CIFAR100Train(Dataset):
    """cifar100 test dataset, derived from
    torch.utils.data.DataSet
    """

    def __init__(self, path, transform=None):
        #if transform is given, we transoform data using
        with open(os.path.join(path, 'train'), 'rb') as cifar100:
            self.data = pickle.load(cifar100, encoding='bytes')
        self.transform = transform
        
    def __len__(self):
        return len(self.data['fine_labels'.encode()])

    def __getitem__(self, index):
        label = self.data['fine_labels'.encode()][index]
        r = self.data['data'.encode()][index, :1024].reshape(32, 32)
        g = self.data['data'.encode()][index, 1024:2048].reshape(32, 32)
        b = self.data['data'.encode()][index, 2048:].reshape(32, 32)
        image = numpy.dstack((r, g, b))

        if self.transform:
            image = self.transform(image)
        return label, image

class CIFAR100Test(Dataset):
    """cifar100 test dataset, derived from
    torch.utils.data.DataSet
    """

    def __init__(self, path, transform=None):
        with open(os.path.join(path, 'test'), 'rb') as cifar100:
            self.data = pickle.load(cifar100, encoding='bytes')
        self.transform = transform 

    def __len__(self):
        return len(self.data['data'.encode()])
    
    def __getitem__(self, index):
        label = self.data['fine_labels'.encode()][index]
        r = self.data['data'.encode()][index, :1024].reshape(32, 32)
        g = self.data['data'.encode()][index, 1024:2048].reshape(32, 32)
        b = self.data['data'.encode()][index, 2048:].reshape(32, 32)
        image = numpy.dstack((r, g, b))

        if self.transform:
            image = self.transform(image)
        return label, image

class DogCatDataSetTrain(Dataset):
    """cifar100 test dataset, derived from
        torch.utils.data.DataSet
        """
    #img_dir = 'C:/Users/YIZ3SZH/Documents/15_AI_Projects/cat_dog_dataset/training_set/training_set'
    def __init__(self, img_dir, transform=None):
        self.transform = transform
        dog_dir = os.path.join(img_dir, "/dogs")
        cat_dir = os.path.join(img_dir, "/cats")
        imgsLib = []
        imgsLib.extend(glob.glob(r"C:/Users/YIZ3SZH/Documents/15_AI_Projects/cat_dog_dataset/training_set/training_set/dogs/**.jpg"))
        imgsLib.extend(glob.glob(r"C:/Users/YIZ3SZH/Documents/15_AI_Projects/cat_dog_dataset/training_set/training_set/cats/**.jpg"))
        random.shuffle(imgsLib)  # 打乱数据集
        self.imgsLib = imgsLib

    def __len__(self):
        return len(self.imgsLib)

    def __getitem__(self, index):
        img_path = self.imgsLib[index]
        label = 1 if 'dog' in img_path.split('/')[-1] else 0  # 狗的label设为1，猫的设为0
        img = Image.open(img_path).convert("RGB")
        img = self.transform(img)
        return img, label

class DogCatDataSetTest(Dataset):
    """cifar100 test dataset, derived from
        torch.utils.data.DataSet
        """
    #img_dir = 'C:/Users/YIZ3SZH/Documents/15_AI_Projects/cat_dog_dataset/test_set/test_set'
    def __init__(self, img_dir, transform=None):
        self.transform = transform
        dog_dir = os.path.join(img_dir, "/dogs")
        cat_dir = os.path.join(img_dir, "/cats")
        imgsLib = []
        imgsLib.extend(glob.glob(r"C:/Users/YIZ3SZH/Documents/15_AI_Projects/cat_dog_dataset/test_set/test_set/dogs/**.jpg"))
        imgsLib.extend(glob.glob(r"C:/Users/YIZ3SZH/Documents/15_AI_Projects/cat_dog_dataset/test_set/test_set/cats/**.jpg"))
        random.shuffle(imgsLib)  # 打乱数据集
        self.imgsLib = imgsLib

    def __len__(self):
        return len(self.imgsLib)

    def __getitem__(self, index):
        img_path = self.imgsLib[index]
        label = 1 if 'dog' in img_path.split('/')[-1] else 0  # 狗的label设为1，猫的设为0
        img = Image.open(img_path).convert("RGB")
        img = self.transform(img)
        return img, label




train_path = 'C:/Users/YIZ3SZH/Documents/15_AI_Projects/cat_dog_dataset/training_set/training_set'
test_path = 'C:/Users/YIZ3SZH\Documents/15_AI_Projects/cat_dog_dataset/test_set/test_set'
data_root = 'D:/AIdata/dog vs cat/'


class DogCatTrain(Dataset):
    def __init__(self, data_path: str, train=True, transform=None):
        self.data_path = data_path
        self.train_flag = train
        if transform is None:
            self.transform = transforms.Compose(
                [
                    transforms.Resize(size=(224, 224)),  # 尺寸规范
                    transforms.ToTensor(),  # 转化为tensor
                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                ])
        else:
            self.transform = transform
        self.path_list = os.listdir(data_path)

    def __getitem__(self, idx: int):
        # img to tensor and label to tensor
        img_path = self.path_list[idx]
        if self.train_flag is True:
            if img_path.split('.')[0] == 'dog' :
                label = 1
            else:
                label = 0
        else:
            label = int(img_path.split('.')[0]) # split 的是str类型要转换为int
        label = torch.as_tensor(label, dtype=torch.int64) # 必须使用long 类型数据，否则后面训练会报错 expect long
        img_path = os.path.join(self.data_path, img_path)
        img = Image.open(img_path)
        img = self.transform(img)
        return img, label

    def __len__(self) -> int:
        return len(self.path_list)