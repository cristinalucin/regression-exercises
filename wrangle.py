import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
import numpy as np
import env

from env import user, password, host

def get_zillow_data():
    ''' Retrieve data from Zillow database within codeup, selecting specific features 
    '''
    filename = "zillow.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        query = '''
            
        SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
        FROM properties_2017

        LEFT JOIN propertylandusetype USING(propertylandusetypeid)

        WHERE propertylandusedesc IN ("Single Family Residential",                       
                              "Inferred Single Family Residential")'''
        df = pd.read_sql(query, get_connection('zillow'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)

        # Return the dataframe to the calling code
        return df
    
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    
def remove_outliers(df,feature_list):
    ''' utilizes IQR to remove data which lies beyond 
    three standard deviations of the mean
    '''
    for feature in feature_list:
    
        #define interquartile range
        Q1= df[feature].quantile(0.25)
        Q3 = df[feature].quantile(0.75)
        IQR = Q3 - Q1
        #Set limits
        upper_limit = Q3 + 1.5 * IQR
        lower_limit = Q1 - 1.5 * IQR
        #remove outliers
        df = df[(df[feature] > lower_limit) & (df[feature] < upper_limit)]
    
    return df
    
def clean_zillow(df):
    ''' This function takes in zillow data and returns a clean dataset.
    '''
    # renaming columns
    df = df.rename(columns = {'bedroomcnt':'bedrooms', 
                          'bathroomcnt':'bathrooms', 
                          'calculatedfinishedsquarefeet':'area',
                          'taxvaluedollarcnt':'tax_value', 
                          'yearbuilt':'year_built',
                          'taxamount':'tax_amount'
                    })
    
    # Replace a whitespace sequence or empty with a NaN value and reassign this manipulation to df. 
    df = df.replace(r'^\s*$', np.nan, regex=True)
    
    return df
    