# -*- coding: utf-8 -*-
"""dm_hw3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EopV_IMkIGoDLm4_Aog_hyj8Uv6SeyUw
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

training_data = pd.read_csv('training.csv')

X_train = training_data.drop(columns=['lettr'])
y_train = training_data['lettr']

test_data = pd.read_csv('test_X.csv')

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(test_data)

from sklearn.neighbors import NearestNeighbors

k = 5
knn = NearestNeighbors(n_neighbors=k)
knn.fit(X_train_scaled)

distances, indices = knn.kneighbors(X_train_scaled)

train_scores = np.mean(distances, axis=1)

X_test_scores, _ = knn.kneighbors(X_test_scaled)
test_scores = np.mean(X_test_scores, axis=1)

threshold = np.percentile(train_scores, 95)

num_test_samples = len(test_data)
outliers = np.where(test_scores > threshold, test_scores, 0)
output_df = pd.DataFrame({'id': range(num_test_samples), 'outliers': outliers})

output_df.to_csv('submission_knn.csv', index=False)