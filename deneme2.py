#!/usr/bin/env python
# coding: utf-8

# In[5]:


times = int(input("Hoe many times should I say 'I loveyou'")
for i in range(times):
            
    print('I love you')


# In[6]:


number = int(input("enter a number between 1-10 :"))

for i in range(11):
    print("{}*{} = ".format(number, i),number * i)
    


# In[7]:


text = ['one', 'two', 'three', 'four', 'five']
numbers = [1, 2, 3, 4, 5]
for x, y in zip(text, numbers):
    print(x, ':', y)


# In[8]:


print(list(range(0,10,2)))
print(list(range(1,10,2)))


# In[10]:


evens_count = 0
odds_count = 0
list = [27,98,23,68,41,73,37, 35]
for i in list:
    if i%2==0:
        evens_count += 1
    else:
        odds_count += 1
print("The number of even numbers : ",evens_count)
print("The number of odd numbers : ",odds_count)


# In[12]:


for i in range(1,10):
    print(str(i) * i)


# In[17]:


names = ["susan", "tom", "edward"]
mood = ["happy", "sad"]
for i in names:
    for ii in mood:
        print(i  +  ' is '  +  ii)


# In[ ]:


names = ["susan", "tom", "edward"]
mood = ["happy", "sad"]
for i in names:
    for ii in mood:
        print(i  +  ' is '  +  ii)


# In[1]:


x = 6
y = 9
print ("is x equal to y?                 :" , x == y)
print ("is x not equal to y?             :" , x != y)
print ("is x less than y?                :" , x < y)
print ("is x greater than y?             :" , x > y)
print ("is x less than or equal to y?    :" , x <= y)
print ("is x greater than or equal to y? :" , x >= y)


# In[2]:


number = 23
if number >= 10:
    print('The number is equal or greater than 10')
elif number < 10:
    print('The number is less than 10')
    


# In[3]:


number = 23
if number >= 10:
    print('The number is equal or greater than 10')
elif number < 10:
    print('The number is less than 10')
else:
    print('do not write anything')


# In[4]:


score = int (input("Enter your score :"))

if score >= 90:
    if score >= 95:
        Score_letter="A+"
    else:
        Score_letter="A"
elif score >= 80:
    if score >= 85:
        Score_letter="B+"
    else:
        Score_letter="B"
else:
    Score_letter="below B"

print ("Your degree: %s" % Score_letter)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




