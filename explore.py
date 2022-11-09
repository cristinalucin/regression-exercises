import matplotlib.pyplot as plt
import seaborn as sns

import env
import os

def plot_variable_pair(df):
    '''This function accepts a dataframe as input and plots all of the pairwise relationships
    along with the regression line for each pair '''
    columns = df.columns.to_list()
    for i, col in enumerate(columns):
        sns.lmplot(data=df, x=col, y='tax_value', line_kws={'color':'red'})
        plt.show()
        
def plot_categorical_and_continuous_vars(df, cat_vars, cont_vars):
    ''' This function accepts a dataframe and the name of the columns that hold the continuous
        and categorical features and outputs 3 different plots for visualizing a categorical 
        variable and a continuous variable'''
    for col in cat_vars:
        for col2 in cont_vars:
            fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(16,6))
            fig.suptitle(f'{col} vs. {col2}')
            sns.boxplot(data=df, x=col, y=col2, ax=ax1)
            sns.violinplot(data=df, x=col, y=col2, ax=ax2)
            sns.barplot(data=df, x=col, y=col2, ax=ax3)
            plt.show()
