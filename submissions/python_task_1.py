#!/usr/bin/env python
# coding: utf-8

# ## PYTHON TASK 1

# In[1]:


#import_libraries:
import pandas as pd
import numpy as np


# In[66]:


#read_csv:
df1= pd.read_csv("/Users/preethireddy/Downloads/dataset-1.csv")
df2= pd.read_csv("/Users/preethireddy/Downloads/dataset-2.csv")
df3= pd.read_csv("/Users/preethireddy/Downloads/dataset-3.csv")


# In[3]:


#Question 1: Car Matrix Generation:
def generate_car_matrix(dataframe):
    car_matrix = dataframe.pivot(index='id_1', columns='id_2', values='car') #id1 as index, id2 as columns and values of column car
    car_matrix = car_matrix.fillna(0) #diagonal values as 0
    return car_matrix

df1_new = generate_car_matrix(df1)
df1_new


# In[4]:


#Question 2: Car Type Count Calculation:

def get_type_count(dataframe):
    dataframe['car_type'] = dataframe['car'].apply(lambda x: 'low' if x <= 15 else ('medium' if x <= 25 else 'high')) 
    type_count = dataframe['car_type'].value_counts().to_dict() #counting low/medium/high
    sorted_type_count = dict(sorted(type_count.items())) #sort in ascending order
    return sorted_type_count

get_type_count(df1)


# In[5]:


#Question 3: Bus Count Index Retrieval:

def get_bus_indexes(dataframe):   
    mean_bus_twice = 2 * (dataframe['bus'].mean())
    bus_indices = dataframe[dataframe['bus'] > mean_bus_twice].index.tolist() #bus values greater than twice the mean value of the bus column
    bus_indices.sort() #sorting indices
    return bus_indices

get_bus_indexes(df1) 


# In[6]:


#Question 4: Route Filtering:   
   
def filter_routes(df):
    #Check if 'route' and 'truck' columns exist in the DataFrame
    if 'route' not in df.columns or 'truck' not in df.columns:
        raise ValueError("DataFrame must contain 'route' and 'truck' columns.")

    #Group by 'route' and calculate the average of 'truck'
    route_avg_truck = df.groupby('route')['truck'].mean()

    #Filter routes where the average of 'truck' is greater than 7
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    #Sort the list of routes
    sorted_filtered_routes = sorted(filtered_routes)

    return sorted_filtered_routes

filter_routes(df1)


# In[7]:


#Question 5: Matrix Value Modification:

def multiply_matrix(dataframe):
    dataframe = dataframe.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25) #If a value in the DataFrame is greater than 20 multiply those values by 0.75 and if a value is 20 or less multiply those values by 1.25
    dataframe = dataframe.round(1) #rounding up
    return dataframe 

multiply_matrix(df1_new)


# In[48]:


#Question 6: Time Check:

def check_timestamps(df):
    # Convert 'startDay' and 'endDay' to datetime objects
    df['start_datetime'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_datetime'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    # Check if timestamps are within the correct range
    correct_range = (df['start_datetime'] >= pd.to_datetime('00:00:00')) &                     (df['end_datetime'] <= pd.to_datetime('23:59:59'))

    # Check if timestamps span all 7 days of the week
    correct_days = (df['start_datetime'].dt.dayofweek == 0) &                    (df['end_datetime'].dt.dayofweek == 6)

    # Combine both conditions
    correct_timestamps = correct_range & correct_days

    # Create a boolean series with multi-index (id, id_2)
    bool_series = correct_timestamps.groupby(['id', 'id_2']).all()

    return bool_series


check_timestamps(df2)


# In[73]:


df2


# In[ ]:




