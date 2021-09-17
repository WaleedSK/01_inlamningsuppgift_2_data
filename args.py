from types import new_class
import pandas as pd
import argparse
from os import write
import pandas as pd
from pandas.io import parsers
import seaborn as sns
from argparse import ArgumentParser


class Covid():
       def __init__(self) :
       
         df= pd.read_csv(r'C:\Users\User-tru\Documents\AllShit\KLAR\DataScience\Ec-python-course\assignments\01_inlamningsuppgift_2_data.csv')
         print(df.head())
        
       def compare(self,country1 , country2) :
          names= self.df['country']
          if country1=='sweden' :
           print(country1)
          else:
              print('Did not find both countries in the data')
              return


if __name__ == "__main__":
    
  
    parser=ArgumentParser()
    parser.add_argument( "--country1"   , type=str , required=True )
    parser.add_argument( "--country2"  ,  type=str, required=True)

    args = parser.parse_args()
    
    print(args.country1 , args.country2)


  
  
   
