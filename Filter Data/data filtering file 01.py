# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ktiy78VLg_Ui7B4_QYgPc5sKaLQ_m_6s
"""

import pandas as pd
import glob

##add path
path = "/content/"
all_files = glob.glob(path + "*.csv")
all_files

import csv
import math
search_result = []
word = "as a user"
for filename in all_files:
  print(filename)
  df = pd.read_csv(filename, index_col=None, header = 0)
  df = df.dropna()
  search_result = []
  for index, row in df.iterrows():
    description = row["description"]

    if(description.lower().startswith(word)):
        search_result.append(row)
  
  print(search_result)
  file = open('/content/result.csv', 'a+', newline ='')
  with file:   
      write = csv.writer(file)
      write.writerows(search_result)

