#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
import random as rnd


# In[212]:


class game2048():
    def __init__(self,seed=5):
        self.empty_record=[]
        self.seed=seed
        self.game=game2048.start_generator(self)
        self.input='e'
        self.end_token=0
        
    def start_generator(self):
        a=[0]*16
        a=np.array(a)
        rnd.seed(self.seed)
        smple=rnd.sample(range(16),2)
        a[smple]=2
        a=a.reshape(4,4)
        return a

    def new_element(self):
        if(len(self.empty_record)==0):self.end_token=1;return
        r=rnd.choice(self.empty_record)
        self.game[r//4,r%4]=2
        return
    
    def where_empty(self):#could be optimazied
        count=0
        for i in self.game:
            for j in i:
                if(j==0): self.empty_record.append(count)
                if(j==2048): self.end_token=1;return True
                count+=1
        return #True
        
                    
    def show_interface(self):
        rlist=[]
        for i in self.game:
            temp='|'
            for j in i:
                crt=str(j)
                if(crt=='0'): crt=' '
                if(len(crt)>5): crt=crt[0:5]
                else:
                    temp+=(crt.rjust(5,' ')+'|')
            rlist.append(temp)
        l=len(rlist[0])
        bl='-'*l
        print(bl)
        for i in rlist:
            print(i)
            print(bl)
            
    def accept_input(self):
        a=input('Your next move: ') 
        try:
            self.input=str(a[0]).lower()
        except:
            print('Invalid input, please only enter WASD or E to exit Game.')
            game2048.accept_input()
        return 
    
    def start_game(self):
        print('Game Start!')
        game2048.show_interface(self)
        while self.end_token==0:
            game2048.accept_input(self)
            token=False
            if(self.input=='e'):self.end_token=1;break
            for i in range(4):
                if(self.input=='w'):
                    wl=self.game[:,i]
                    self.game[:,i]=game2048.process(wl)
                elif(self.input=='s'):
                    wl=list(reversed(self.game[:,i]))
                    self.game[:,i]=list(reversed(game2048.process(wl)))
                elif(self.input=='a'):
                    wl=self.game[i,:]
                    self.game[i,]=game2048.process(wl)
                elif(self.input=='d'):
                    wl=list(reversed(self.game[i,:]))
                    self.game[i,:]=list(reversed(game2048.process(wl)))
                else:
                    token=True
            if(token):
                print('Invalid input, please only enter WASD or E to exit Game.')
                continue
            if(game2048.where_empty(self)):
                print('You Win, y to restart, n to exit')
                game2048.accept_input(self)
                if(self.input=='y'):game2048.start_game(self)
                else: end_token=1;break
            game2048.new_element(self)
            game2048.show_interface(self)
    #The core function that process a fixed length list in 2048 method
    def process(wl):
        start_pos=0
        end_pos=1
        l=len(wl)
        while True:
            if(start_pos>=l):break
            if(end_pos>=l):start_pos+=1;end_pos=start_pos+1;continue
            if(wl[start_pos]==0):
                start_pos+=1;end_pos+=1
            else:
                if(wl[start_pos]==wl[end_pos]): 
                    wl[start_pos]=wl[start_pos]*2
                    wl[end_pos]=0
                    start_pos=end_pos+1
                    end_pos=start_pos+1
                elif(wl[end_pos]==0): end_pos+=1
                else:start_pos+=1;end_pos+=1
        z1=[];z2=[]
        for i in wl:
            if(i==0):z2.append(i)
            else:z1.append(i)
        return(z1+z2)


# In[ ]:




