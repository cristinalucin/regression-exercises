import os
import pandas as pd
import numpy as np
import scipy.stats as stats

import env

from sklearn.model_selection import train_test_split

def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 15% of the original dataset, validate is .1765*.85= 15% of the 
    original dataset, and train is 75% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.15, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.1765, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test
