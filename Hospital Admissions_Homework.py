#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


admission_df = pd.read_csv('admission_data.csv', sep=',')
print(admission_df)


# In[3]:


print("\nDataset Info:")
print(admission_df.head(5))


# In[4]:


print(admission_df.tail(5))


# In[5]:


print(admission_df.describe)
print(admission_df.info)


# In[6]:


print(admission_df.isnull().sum())


# In[7]:


print(admission_df.keys())


# In[8]:


print(admission_df['AGE'].describe())


# In[9]:


print("\n=== Unique Values in Each Column ===")
for column in admission_df.columns:
    print(f"\n{column}:")
    print(admission_df[column].value_counts().head())


# In[12]:


medical_measurements = ['HB', 'TLC', 'PLATELETS', 'GLUCOSE', 'UREA', 'CREATININE', 'BNP', 'EF']


plt.figure(figsize=(15, 10))
for i, column in enumerate(medical_measurements, 1):
    plt.subplot(2, 4, i)
    sns.histplot(data=admission_df[column].dropna(), kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
plt.tight_layout()
plt.show()


print("\nMedical Measurements Summary Statistics:")
print(admission_df[medical_measurements].describe())


# In[13]:


print("\nPatient Demographics:")
print("Gender distribution:")
print(admission_df['GENDER'].value_counts(normalize=True) * 100)

print("\nAge statistics:")
print(admission_df['AGE'].describe())


# In[14]:


admission_df.to_csv('new_admission.csv', sep=',')


# In[ ]:




