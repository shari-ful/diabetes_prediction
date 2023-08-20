import os
import pandas as pd
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, '..', 'dataset', 'kaggle_diabetes.csv')
print(BASE_DIR, DATASET_DIR)
df = pd.read_csv(DATASET_DIR)