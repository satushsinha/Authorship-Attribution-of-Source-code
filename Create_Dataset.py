import numpy as np

import pandas as pd
dataset=pd.read_csv("data_dir/train.csv")
'''
for i in range(0,50000):
    print(dataset.iloc[i,1])


list1=[]
from guesslang import Guess
guess=Guess()

for i in range(0,50000):
    list1.append(guess.language_name(dataset.iloc[i,0]))

for i in range(0,50000):
    print(list1[i])
'''












































'''
list=[]
for i in range(0,30):
    list.append(dataset.iloc[i,0])
    print(dataset.iloc[i,0])
print(len(list))

random_list=pd.read_csv("50_tweets_per_user_8_random_numbers.csv")

list=[]
for i in range(0,50):
    list.append(random_list.iloc[i,0])

#For making 50,100,200 tweets per user
!apt-get install p7zip-full
!p7zip -d '/content/varying_number_of_authors'.tar.7z 
!tar -xvf '/content/varying_number_of_authors'.tar
#For making 500,1000 tweets per user
#apt-get install p7zip-full

p7zip -d 'Data/twitter_authorship/varying_training_set_size'.tar.7z 
tar -xvf '/content/varying_training_set_size'.tar

import random

#list=random.sample(range(7000),1000)

f=open("Human_like_authors_new.txt","r")
list=f.readlines()

print("done")
'''

for a in range(1):
    
    import bz2

    train_text_100=[]
    train_user_100=[]

    train_text_1000=[]
    train_user_1000=[]

    for i in range(0,50000,50):
        data=open('data_dir/' + "train" + '/' +str(dataset.iloc[i,1]),'r')
        train_text_100.append(data.read())
        train_user_100.append(dataset.iloc[i,0])
    


    train_text_100=pd.DataFrame(train_text_100)
    train_user_100=pd.DataFrame(train_user_100)



    train_text_100=train_text_100.iloc[:,:].values
    train_user_100=train_user_100.iloc[:,:].values



    print(train_text_100.shape)




    import numpy as np

    dataset_train_100=np.concatenate((train_text_100,train_user_100),axis=1)
    



    dataset_train_100=pd.DataFrame(dataset_train_100)




    dataset_train_100.to_csv('Train_check_new_4.csv', header=True, index=False)



data=open('data_dir/train/52000', 'r')
print(data.read())

'''

for i in range(0,100):
  a=0
  train_text=[]
  train_user=[]
  for j in range(0,10):
    data=bz2.open('/content/' + str(dataset.iloc[i,0]) + '/' + str(dataset.iloc[i,0]) + '_' + str(j) + '.bz2' ,'rb')
    for k in data:
      if len(k.split()) > 15: 
        train_text.append(k)
        train_user.append(dataset.iloc[i,0])
        a+=1
        if(a==50):
          break
    if(a==50):
      break
  if(a==50):
    train_text_main.append(train_text)
    train_user_main.append(train_user)
  if(len(train_text_main)==50):
    break;
    
'''
