{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset = pd.read_excel('Real estate valuation data set.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>No</th>\n",
       "      <th>X1 transaction date</th>\n",
       "      <th>X2 house age</th>\n",
       "      <th>X3 distance to the nearest MRT station</th>\n",
       "      <th>X4 number of convenience stores</th>\n",
       "      <th>X5 latitude</th>\n",
       "      <th>X6 longitude</th>\n",
       "      <th>Y house price of unit area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2012.916667</td>\n",
       "      <td>32.0</td>\n",
       "      <td>84.87882</td>\n",
       "      <td>10</td>\n",
       "      <td>24.98298</td>\n",
       "      <td>121.54024</td>\n",
       "      <td>37.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2012.916667</td>\n",
       "      <td>19.5</td>\n",
       "      <td>306.59470</td>\n",
       "      <td>9</td>\n",
       "      <td>24.98034</td>\n",
       "      <td>121.53951</td>\n",
       "      <td>42.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2013.583333</td>\n",
       "      <td>13.3</td>\n",
       "      <td>561.98450</td>\n",
       "      <td>5</td>\n",
       "      <td>24.98746</td>\n",
       "      <td>121.54391</td>\n",
       "      <td>47.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2013.500000</td>\n",
       "      <td>13.3</td>\n",
       "      <td>561.98450</td>\n",
       "      <td>5</td>\n",
       "      <td>24.98746</td>\n",
       "      <td>121.54391</td>\n",
       "      <td>54.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2012.833333</td>\n",
       "      <td>5.0</td>\n",
       "      <td>390.56840</td>\n",
       "      <td>5</td>\n",
       "      <td>24.97937</td>\n",
       "      <td>121.54245</td>\n",
       "      <td>43.1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   No  X1 transaction date  X2 house age  \\\n",
       "0   1          2012.916667          32.0   \n",
       "1   2          2012.916667          19.5   \n",
       "2   3          2013.583333          13.3   \n",
       "3   4          2013.500000          13.3   \n",
       "4   5          2012.833333           5.0   \n",
       "\n",
       "   X3 distance to the nearest MRT station  X4 number of convenience stores  \\\n",
       "0                                84.87882                               10   \n",
       "1                               306.59470                                9   \n",
       "2                               561.98450                                5   \n",
       "3                               561.98450                                5   \n",
       "4                               390.56840                                5   \n",
       "\n",
       "   X5 latitude  X6 longitude  Y house price of unit area  \n",
       "0     24.98298     121.54024                        37.9  \n",
       "1     24.98034     121.53951                        42.2  \n",
       "2     24.98746     121.54391                        47.3  \n",
       "3     24.98746     121.54391                        54.8  \n",
       "4     24.97937     121.54245                        43.1  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['No', 'X1 transaction date', 'X2 house age',\n",
       "       'X3 distance to the nearest MRT station',\n",
       "       'X4 number of convenience stores', 'X5 latitude', 'X6 longitude',\n",
       "       'Y house price of unit area'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset.drop('No',axis = 1,inplace =True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>X1 transaction date</th>\n",
       "      <th>X2 house age</th>\n",
       "      <th>X3 distance to the nearest MRT station</th>\n",
       "      <th>X4 number of convenience stores</th>\n",
       "      <th>X5 latitude</th>\n",
       "      <th>X6 longitude</th>\n",
       "      <th>Y house price of unit area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2012.916667</td>\n",
       "      <td>32.0</td>\n",
       "      <td>84.87882</td>\n",
       "      <td>10</td>\n",
       "      <td>24.98298</td>\n",
       "      <td>121.54024</td>\n",
       "      <td>37.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2012.916667</td>\n",
       "      <td>19.5</td>\n",
       "      <td>306.59470</td>\n",
       "      <td>9</td>\n",
       "      <td>24.98034</td>\n",
       "      <td>121.53951</td>\n",
       "      <td>42.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2013.583333</td>\n",
       "      <td>13.3</td>\n",
       "      <td>561.98450</td>\n",
       "      <td>5</td>\n",
       "      <td>24.98746</td>\n",
       "      <td>121.54391</td>\n",
       "      <td>47.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2013.500000</td>\n",
       "      <td>13.3</td>\n",
       "      <td>561.98450</td>\n",
       "      <td>5</td>\n",
       "      <td>24.98746</td>\n",
       "      <td>121.54391</td>\n",
       "      <td>54.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2012.833333</td>\n",
       "      <td>5.0</td>\n",
       "      <td>390.56840</td>\n",
       "      <td>5</td>\n",
       "      <td>24.97937</td>\n",
       "      <td>121.54245</td>\n",
       "      <td>43.1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   X1 transaction date  X2 house age  X3 distance to the nearest MRT station  \\\n",
       "0          2012.916667          32.0                                84.87882   \n",
       "1          2012.916667          19.5                               306.59470   \n",
       "2          2013.583333          13.3                               561.98450   \n",
       "3          2013.500000          13.3                               561.98450   \n",
       "4          2012.833333           5.0                               390.56840   \n",
       "\n",
       "   X4 number of convenience stores  X5 latitude  X6 longitude  \\\n",
       "0                               10     24.98298     121.54024   \n",
       "1                                9     24.98034     121.53951   \n",
       "2                                5     24.98746     121.54391   \n",
       "3                                5     24.98746     121.54391   \n",
       "4                                5     24.97937     121.54245   \n",
       "\n",
       "   Y house price of unit area  \n",
       "0                        37.9  \n",
       "1                        42.2  \n",
       "2                        47.3  \n",
       "3                        54.8  \n",
       "4                        43.1  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>X1 transaction date</th>\n",
       "      <th>X2 house age</th>\n",
       "      <th>X3 distance to the nearest MRT station</th>\n",
       "      <th>X4 number of convenience stores</th>\n",
       "      <th>X5 latitude</th>\n",
       "      <th>X6 longitude</th>\n",
       "      <th>Y house price of unit area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>414.000000</td>\n",
       "      <td>414.000000</td>\n",
       "      <td>414.000000</td>\n",
       "      <td>414.000000</td>\n",
       "      <td>414.000000</td>\n",
       "      <td>414.000000</td>\n",
       "      <td>414.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2013.148953</td>\n",
       "      <td>17.712560</td>\n",
       "      <td>1083.885689</td>\n",
       "      <td>4.094203</td>\n",
       "      <td>24.969030</td>\n",
       "      <td>121.533361</td>\n",
       "      <td>37.980193</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.281995</td>\n",
       "      <td>11.392485</td>\n",
       "      <td>1262.109595</td>\n",
       "      <td>2.945562</td>\n",
       "      <td>0.012410</td>\n",
       "      <td>0.015347</td>\n",
       "      <td>13.606488</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>2012.666667</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>23.382840</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>24.932070</td>\n",
       "      <td>121.473530</td>\n",
       "      <td>7.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2012.916667</td>\n",
       "      <td>9.025000</td>\n",
       "      <td>289.324800</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>24.963000</td>\n",
       "      <td>121.528085</td>\n",
       "      <td>27.700000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>2013.166667</td>\n",
       "      <td>16.100000</td>\n",
       "      <td>492.231300</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>24.971100</td>\n",
       "      <td>121.538630</td>\n",
       "      <td>38.450000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2013.416667</td>\n",
       "      <td>28.150000</td>\n",
       "      <td>1454.279000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>24.977455</td>\n",
       "      <td>121.543305</td>\n",
       "      <td>46.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2013.583333</td>\n",
       "      <td>43.800000</td>\n",
       "      <td>6488.021000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>25.014590</td>\n",
       "      <td>121.566270</td>\n",
       "      <td>117.500000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       X1 transaction date  X2 house age  \\\n",
       "count           414.000000    414.000000   \n",
       "mean           2013.148953     17.712560   \n",
       "std               0.281995     11.392485   \n",
       "min            2012.666667      0.000000   \n",
       "25%            2012.916667      9.025000   \n",
       "50%            2013.166667     16.100000   \n",
       "75%            2013.416667     28.150000   \n",
       "max            2013.583333     43.800000   \n",
       "\n",
       "       X3 distance to the nearest MRT station  \\\n",
       "count                              414.000000   \n",
       "mean                              1083.885689   \n",
       "std                               1262.109595   \n",
       "min                                 23.382840   \n",
       "25%                                289.324800   \n",
       "50%                                492.231300   \n",
       "75%                               1454.279000   \n",
       "max                               6488.021000   \n",
       "\n",
       "       X4 number of convenience stores  X5 latitude  X6 longitude  \\\n",
       "count                       414.000000   414.000000    414.000000   \n",
       "mean                          4.094203    24.969030    121.533361   \n",
       "std                           2.945562     0.012410      0.015347   \n",
       "min                           0.000000    24.932070    121.473530   \n",
       "25%                           1.000000    24.963000    121.528085   \n",
       "50%                           4.000000    24.971100    121.538630   \n",
       "75%                           6.000000    24.977455    121.543305   \n",
       "max                          10.000000    25.014590    121.566270   \n",
       "\n",
       "       Y house price of unit area  \n",
       "count                  414.000000  \n",
       "mean                    37.980193  \n",
       "std                     13.606488  \n",
       "min                      7.600000  \n",
       "25%                     27.700000  \n",
       "50%                     38.450000  \n",
       "75%                     46.600000  \n",
       "max                    117.500000  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "X1 transaction date                       0\n",
       "X2 house age                              0\n",
       "X3 distance to the nearest MRT station    0\n",
       "X4 number of convenience stores           0\n",
       "X5 latitude                               0\n",
       "X6 longitude                              0\n",
       "Y house price of unit area                0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = dataset.iloc[:,:-1]\n",
    "y = dataset.iloc[:,-1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "F:\\anaconda\\lib\\site-packages\\sklearn\\cross_validation.py:41: DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved. Also note that the interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.\n",
      "  \"This module will be removed in 0.20.\", DeprecationWarning)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.cross_validation import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(331, 1)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)\n",
    "y_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(331, 6)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.svm import SVR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "regressor = SVR(kernel = 'linear',degree = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "F:\\anaconda\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "SVR(C=1.0, cache_size=200, coef0=0.0, degree=1, epsilon=0.1, gamma='auto',\n",
       "  kernel='linear', max_iter=-1, shrinking=True, tol=0.001, verbose=False)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "regressor.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Y house price of unit area</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>320</th>\n",
       "      <td>18.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>131</th>\n",
       "      <td>30.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>60</th>\n",
       "      <td>21.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>18.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>15.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>43.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>279</th>\n",
       "      <td>31.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>118</th>\n",
       "      <td>30.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>290</th>\n",
       "      <td>37.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>208</th>\n",
       "      <td>26.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>278</th>\n",
       "      <td>44.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>46.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>49.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>117</th>\n",
       "      <td>13.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>191</th>\n",
       "      <td>37.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>139</th>\n",
       "      <td>42.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>181</th>\n",
       "      <td>55.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>152</th>\n",
       "      <td>28.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>172</th>\n",
       "      <td>58.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>302</th>\n",
       "      <td>23.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>70</th>\n",
       "      <td>59.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>64</th>\n",
       "      <td>25.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>140</th>\n",
       "      <td>51.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>358</th>\n",
       "      <td>45.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>59.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>314</th>\n",
       "      <td>41.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>62</th>\n",
       "      <td>27.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>73</th>\n",
       "      <td>20.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>103</th>\n",
       "      <td>45.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>347</th>\n",
       "      <td>11.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>273</th>\n",
       "      <td>29.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>147</th>\n",
       "      <td>43.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>231</th>\n",
       "      <td>14.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>411</th>\n",
       "      <td>40.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>197</th>\n",
       "      <td>48.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>27.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>374</th>\n",
       "      <td>49.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>39.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>263</th>\n",
       "      <td>31.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>298</th>\n",
       "      <td>16.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>215</th>\n",
       "      <td>48.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>345</th>\n",
       "      <td>37.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>161</th>\n",
       "      <td>39.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>332</th>\n",
       "      <td>39.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>38.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>24.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>313</th>\n",
       "      <td>42.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>408</th>\n",
       "      <td>28.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>184</th>\n",
       "      <td>21.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>25.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>40.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>225</th>\n",
       "      <td>49.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>241</th>\n",
       "      <td>41.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>134</th>\n",
       "      <td>42.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>361</th>\n",
       "      <td>63.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>37.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122</th>\n",
       "      <td>32.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>284</th>\n",
       "      <td>34.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>34.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93</th>\n",
       "      <td>16.1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>83 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Y house price of unit area\n",
       "320                        18.6\n",
       "131                        30.7\n",
       "60                         21.3\n",
       "41                         18.2\n",
       "40                         15.9\n",
       "4                          43.1\n",
       "279                        31.1\n",
       "118                        30.6\n",
       "290                        37.0\n",
       "208                        26.2\n",
       "278                        44.0\n",
       "39                         46.2\n",
       "33                         49.3\n",
       "117                        13.0\n",
       "191                        37.8\n",
       "139                        42.5\n",
       "181                        55.9\n",
       "152                        28.9\n",
       "172                        58.1\n",
       "302                        23.2\n",
       "70                         59.0\n",
       "64                         25.3\n",
       "140                        51.4\n",
       "358                        45.1\n",
       "96                         59.5\n",
       "314                        41.6\n",
       "62                         27.7\n",
       "73                         20.0\n",
       "103                        45.7\n",
       "347                        11.2\n",
       "..                          ...\n",
       "273                        29.3\n",
       "147                        43.2\n",
       "231                        14.7\n",
       "411                        40.6\n",
       "197                        48.2\n",
       "35                         27.3\n",
       "374                        49.5\n",
       "12                         39.3\n",
       "263                        31.7\n",
       "298                        16.7\n",
       "215                        48.1\n",
       "345                        37.9\n",
       "161                        39.6\n",
       "332                        39.6\n",
       "24                         38.8\n",
       "22                         24.6\n",
       "313                        42.8\n",
       "408                        28.1\n",
       "184                        21.8\n",
       "31                         25.0\n",
       "6                          40.3\n",
       "225                        49.0\n",
       "241                        41.4\n",
       "134                        42.2\n",
       "361                        63.3\n",
       "0                          37.9\n",
       "122                        32.5\n",
       "284                        34.4\n",
       "14                         34.3\n",
       "93                         16.1\n",
       "\n",
       "[83 rows x 1 columns]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y_predicted = regressor.predict(x_test)\n",
    "y_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([18.6, 30.7, 21.3, 18.2, 15.9, 43.1, 31.1, 30.6, 37. , 26.2, 44. ,\n",
       "       46.2, 49.3, 13. , 37.8, 42.5, 55.9, 28.9, 58.1, 23.2, 59. , 25.3,\n",
       "       51.4, 45.1, 59.5, 41.6, 27.7, 20. , 45.7, 11.2, 21.8, 18.3, 40.6,\n",
       "       25.7, 37.2, 34.2, 23.1, 48.6, 34.1, 50.2, 19.2, 52.5, 15.5, 53. ,\n",
       "       29.3, 27.3, 28.5, 44.5, 25.9, 36.8, 44.3, 38.3, 18.3, 29.3, 43.2,\n",
       "       14.7, 40.6, 48.2, 27.3, 49.5, 39.3, 31.7, 16.7, 48.1, 37.9, 39.6,\n",
       "       39.6, 38.8, 24.6, 42.8, 28.1, 21.8, 25. , 40.3, 49. , 41.4, 42.2,\n",
       "       63.3, 37.9, 32.5, 34.4, 34.3, 16.1])"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_t = y_test.iloc[:,-1].values\n",
    "y_t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import r2_score\n",
    "i = r2_score(Y_predicted,y_t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "69.03200430696224"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "i*100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}