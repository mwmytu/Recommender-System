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
from numpy.random import RandomState

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.userNum=1000
        self.itemNum=1700
        self.UFLen=3
        self.IFLen=3
        self.random_state = RandomState(1)
        self.uembeddings=nn.Embedding(self.userNum,self.UFLen)
        #torch.nn.init.uniform_(self.uembeddings.weight.data, a=0, b=1)
        
        self.iembeddings=nn.Embedding(self.itemNum,self.IFLen)
        #torch.nn.init.uniform_(self.iembeddings.weight.data, a=0, b=1)
        
        self.ubiase=nn.Embedding(self.userNum,1)
        self.ibiase=nn.Embedding(self.itemNum,1)
        #self.ufact=torch.rand(self.userNum,self.UFLen,requires_grad=True)
        #self.ifact=torch.rand(self.itemNum,self.IFLen,requires_grad=True)
        #self.ub=torch.rand(self.userNum,1,requires_grad=True)
        #self.ib=torch.rand(self.itemNum,1,requires_grad=True)
        #self.pars=[self.ufact,self.ifact,self.ub,self.ib]
    def forward(self, users,items):
        uembs=self.uembeddings(users)
        iembs=self.iembeddings(items)
        ubias=self.ubiase(users)
        ibias=self.ibiase(items)
        score=(uembs*iembs).sum(1) +ubias.view(ubias.numel())+ibias.view(ibias.numel())       
        #score=(uembs*iembs).sum(1)     
        
        #ufact=self.ufact[users,:]
        #ifact=self.ifact[items,:]
        #ub=self.ub[users,:]
        #ib=self.ib[items,:]
        #score=(ufact*ifact).sum(1)+ub.view(ub.numel())+ib.view(ib.numel())
        
        return score

def loadData(path):
    data = pd.DataFrame(pd.read_table(path,header=None,sep='\t',names="user_id,item_id,rating,timestamp".split(",") ))
    #data.user_id = data.user_id.astype('category').cat.codes.values
    #data.item_id = data.item_id.astype('category').cat.codes.values
    #print data.head()
    users=torch.tensor(data.iloc[:,0].values,dtype=torch.long)
    #print users[1:5]
    items=torch.tensor(data.iloc[:,1].values,dtype=torch.long)
    #print len(users.unique()),len(items.unique())
    scores=torch.tensor(data.iloc[:,2].values,dtype=torch.float32)    
    dataset = TensorDataset(users,items, scores)
    loader = DataLoader(dataset, batch_size = 32, shuffle = True)
    return loader

if __name__ == "__main__":
    net=Net()
    train_loader=loadData('./ml-100k/u1.base')
    test_loader=loadData('./ml-100k/u1.test')
    #print net.parameters()
    optimizer = optim.Adam(net.parameters(), lr=0.001,weight_decay=1e-4)
    index=0
    lambda_l2=0.1
    mse = nn.MSELoss(size_average=True)
    mae=nn.L1Loss(size_average=True)
    for epoch in range (1,100):
        tmse_loss=0.0
        tmae_loss=0.0
        num=0
        print epoch
        for i_batch, sample_batched in enumerate(train_loader):        
            optimizer.zero_grad()   # zero the gradient buffers
            #print sample_batched[0],sample_batched[1]
            output=net(sample_batched[0],sample_batched[1])
            #print output
            target=sample_batched[2]
            
            mseloss = mse(output, target)
            maeloss=mae(output,target)
            #print loss.data,'\n'
            '''
            regL2Loss=0.0
            for W in net.parameters():
                
                regL2Loss+=torch.pow(W,2).sum()
            loss=mseloss+regL2Loss*1e-5
            '''
            loss=mseloss
            loss.backward()
            optimizer.step()    # Does the update
            
            tmse_loss+=mseloss.data.numpy()
            tmae_loss+=maeloss.data.numpy()
            num+=1
            #sprint totloss/num
            
        #print len(train_loader) 
        tmse=tmse_loss/num
        rmse=np.sqrt(tmse)
        tmae=tmae_loss/num
        print tmse,rmse,tmae,'\n'
    tmse_loss=0.0
    tmae_loss=0.0
    num=0
    for i_batch, sample_batched in enumerate(test_loader):        
        output=net(sample_batched[0],sample_batched[1])
        target=sample_batched[2]
        mseloss = mse(output, target)
        maeloss=mae(output,target)
    
            
        tmse_loss+=mseloss.data.numpy()
        tmae_loss+=maeloss.data.numpy()
        num+=1
            #sprint totloss/num
            
        #print len(train_loader) 
    tmse=tmse_loss/num
    rmse=np.sqrt(tmse)
    tmae=tmae_loss/num
    print tmse,rmse,tmae,'\n'
        
        
    
    
    
        
