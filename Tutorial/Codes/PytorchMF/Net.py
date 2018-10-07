#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 09:51:06 2018

@author: Wenming Ma
Matrix Facotrization using Pytorch
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd
from torch.utils.data import TensorDataset,Dataset, DataLoader
import torch.optim as optim
import numpy as np

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.userNum=1000
        self.itemNum=1700
        self.UFLen=8
        self.IFLen=8
        self.uembeddings=nn.Embedding(self.userNum,self.UFLen)
        self.iembeddings=nn.Embedding(self.itemNum,self.IFLen)
    def forward(self, users,items):
        uembs=self.uembeddings(users)
        iembs=self.uembeddings(users)
        score=(uembs*iembs).sum(1)        
        return score

def loadData(path):
    data = pd.DataFrame(pd.read_table(path,header=None))
    users=torch.tensor(data.iloc[:,0].values)-1
    items=torch.tensor(data.iloc[:,0].values)-1
    scores=torch.tensor(data.iloc[:,2].values,dtype=torch.float32)    
    dataset = TensorDataset(users,items, scores)
    loader = DataLoader(dataset, batch_size = 16, shuffle = True)
    return loader

if __name__ == "__main__":
    net=Net()
    train_loader=loadData('./ml-100k/u1.base')
    test_loader=loadData('./ml-100k/u1.base')
    optimizer = optim.SGD(net.parameters(), lr=0.005)
    index=0
    #lambda_l2=0.001
    mse = nn.MSELoss()
    for epoch in range (1,50):
        totloss=0
        num=0
        for i_batch, sample_batched in enumerate(train_loader):        
            optimizer.zero_grad()   # zero the gradient buffers
            output=net(sample_batched[0],sample_batched[1])
            target=sample_batched[2]
            loss = mse(output, target)
            
            loss.backward()
            optimizer.step()    # Does the update
            
            size=target.data.size()[0]
            num+=size
            
            totloss+=loss.data.numpy()*size
            
           
        meanloss=np.mean(totloss/num)
        rmse=np.sqrt(meanloss)
        print meanloss, rmse,'\n'
    totloss=0
    num=0
    for i_batch, sample_batched in enumerate(test_loader):        
        output=net(sample_batched[0],sample_batched[1])
        target=sample_batched[2]
        loss = mse(output, target)
            
        
            
        size=target.data.size()[0]
        num+=size
            
        totloss+=loss.data.numpy()*size
            
           
    meanloss=np.mean(totloss/num)
    rmse=np.sqrt(meanloss)
    print 'test-','MSE:',meanloss,'RMSE', rmse,'\n'
        
        
    
    
    
        
