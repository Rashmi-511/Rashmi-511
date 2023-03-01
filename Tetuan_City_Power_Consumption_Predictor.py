{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "94e8606a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "a72f2994",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('Tetuan City power consumption.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "7c65d670",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['DateTime', 'Temperature', 'Humidity', 'Wind Speed',\n",
       "       'general diffuse flows', 'diffuse flows', 'Zone 1 Power Consumption',\n",
       "       'Zone 2  Power Consumption', 'Zone 3  Power Consumption'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "a6078c1d",
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
       "      <th>Temperature</th>\n",
       "      <th>Humidity</th>\n",
       "      <th>Wind Speed</th>\n",
       "      <th>general diffuse flows</th>\n",
       "      <th>diffuse flows</th>\n",
       "      <th>Zone 1 Power Consumption</th>\n",
       "      <th>Zone 2  Power Consumption</th>\n",
       "      <th>Zone 3  Power Consumption</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>52416.000000</td>\n",
       "      <td>52416.000000</td>\n",
       "      <td>52416.000000</td>\n",
       "      <td>52416.000000</td>\n",
       "      <td>52416.000000</td>\n",
       "      <td>52416.000000</td>\n",
       "      <td>52416.000000</td>\n",
       "      <td>52416.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>18.810024</td>\n",
       "      <td>68.259518</td>\n",
       "      <td>1.959489</td>\n",
       "      <td>182.696614</td>\n",
       "      <td>75.028022</td>\n",
       "      <td>32344.970564</td>\n",
       "      <td>21042.509082</td>\n",
       "      <td>17835.406218</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>5.815476</td>\n",
       "      <td>15.551177</td>\n",
       "      <td>2.348862</td>\n",
       "      <td>264.400960</td>\n",
       "      <td>124.210949</td>\n",
       "      <td>7130.562564</td>\n",
       "      <td>5201.465892</td>\n",
       "      <td>6622.165099</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>3.247000</td>\n",
       "      <td>11.340000</td>\n",
       "      <td>0.050000</td>\n",
       "      <td>0.004000</td>\n",
       "      <td>0.011000</td>\n",
       "      <td>13895.696200</td>\n",
       "      <td>8560.081466</td>\n",
       "      <td>5935.174070</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>14.410000</td>\n",
       "      <td>58.310000</td>\n",
       "      <td>0.078000</td>\n",
       "      <td>0.062000</td>\n",
       "      <td>0.122000</td>\n",
       "      <td>26310.668692</td>\n",
       "      <td>16980.766032</td>\n",
       "      <td>13129.326630</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>18.780000</td>\n",
       "      <td>69.860000</td>\n",
       "      <td>0.086000</td>\n",
       "      <td>5.035500</td>\n",
       "      <td>4.456000</td>\n",
       "      <td>32265.920340</td>\n",
       "      <td>20823.168405</td>\n",
       "      <td>16415.117470</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>22.890000</td>\n",
       "      <td>81.400000</td>\n",
       "      <td>4.915000</td>\n",
       "      <td>319.600000</td>\n",
       "      <td>101.000000</td>\n",
       "      <td>37309.018185</td>\n",
       "      <td>24713.717520</td>\n",
       "      <td>21624.100420</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>40.010000</td>\n",
       "      <td>94.800000</td>\n",
       "      <td>6.483000</td>\n",
       "      <td>1163.000000</td>\n",
       "      <td>936.000000</td>\n",
       "      <td>52204.395120</td>\n",
       "      <td>37408.860760</td>\n",
       "      <td>47598.326360</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Temperature      Humidity    Wind Speed  general diffuse flows  \\\n",
       "count  52416.000000  52416.000000  52416.000000           52416.000000   \n",
       "mean      18.810024     68.259518      1.959489             182.696614   \n",
       "std        5.815476     15.551177      2.348862             264.400960   \n",
       "min        3.247000     11.340000      0.050000               0.004000   \n",
       "25%       14.410000     58.310000      0.078000               0.062000   \n",
       "50%       18.780000     69.860000      0.086000               5.035500   \n",
       "75%       22.890000     81.400000      4.915000             319.600000   \n",
       "max       40.010000     94.800000      6.483000            1163.000000   \n",
       "\n",
       "       diffuse flows  Zone 1 Power Consumption  Zone 2  Power Consumption  \\\n",
       "count   52416.000000              52416.000000               52416.000000   \n",
       "mean       75.028022              32344.970564               21042.509082   \n",
       "std       124.210949               7130.562564                5201.465892   \n",
       "min         0.011000              13895.696200                8560.081466   \n",
       "25%         0.122000              26310.668692               16980.766032   \n",
       "50%         4.456000              32265.920340               20823.168405   \n",
       "75%       101.000000              37309.018185               24713.717520   \n",
       "max       936.000000              52204.395120               37408.860760   \n",
       "\n",
       "       Zone 3  Power Consumption  \n",
       "count               52416.000000  \n",
       "mean                17835.406218  \n",
       "std                  6622.165099  \n",
       "min                  5935.174070  \n",
       "25%                 13129.326630  \n",
       "50%                 16415.117470  \n",
       "75%                 21624.100420  \n",
       "max                 47598.326360  "
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "baf2d9de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 52416 entries, 0 to 52415\n",
      "Data columns (total 9 columns):\n",
      " #   Column                     Non-Null Count  Dtype  \n",
      "---  ------                     --------------  -----  \n",
      " 0   DateTime                   52416 non-null  object \n",
      " 1   Temperature                52416 non-null  float64\n",
      " 2   Humidity                   52416 non-null  float64\n",
      " 3   Wind Speed                 52416 non-null  float64\n",
      " 4   general diffuse flows      52416 non-null  float64\n",
      " 5   diffuse flows              52416 non-null  float64\n",
      " 6   Zone 1 Power Consumption   52416 non-null  float64\n",
      " 7   Zone 2  Power Consumption  52416 non-null  float64\n",
      " 8   Zone 3  Power Consumption  52416 non-null  float64\n",
      "dtypes: float64(8), object(1)\n",
      "memory usage: 3.6+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "8f1bbaf0",
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
       "      <th>DateTime</th>\n",
       "      <th>Temperature</th>\n",
       "      <th>Humidity</th>\n",
       "      <th>Wind Speed</th>\n",
       "      <th>general diffuse flows</th>\n",
       "      <th>diffuse flows</th>\n",
       "      <th>Zone 1 Power Consumption</th>\n",
       "      <th>Zone 2  Power Consumption</th>\n",
       "      <th>Zone 3  Power Consumption</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1/1/2017 0:00</td>\n",
       "      <td>6.559</td>\n",
       "      <td>73.8</td>\n",
       "      <td>0.083</td>\n",
       "      <td>0.051</td>\n",
       "      <td>0.119</td>\n",
       "      <td>34055.69620</td>\n",
       "      <td>16128.87538</td>\n",
       "      <td>20240.96386</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1/1/2017 0:10</td>\n",
       "      <td>6.414</td>\n",
       "      <td>74.5</td>\n",
       "      <td>0.083</td>\n",
       "      <td>0.070</td>\n",
       "      <td>0.085</td>\n",
       "      <td>29814.68354</td>\n",
       "      <td>19375.07599</td>\n",
       "      <td>20131.08434</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1/1/2017 0:20</td>\n",
       "      <td>6.313</td>\n",
       "      <td>74.5</td>\n",
       "      <td>0.080</td>\n",
       "      <td>0.062</td>\n",
       "      <td>0.100</td>\n",
       "      <td>29128.10127</td>\n",
       "      <td>19006.68693</td>\n",
       "      <td>19668.43373</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1/1/2017 0:30</td>\n",
       "      <td>6.121</td>\n",
       "      <td>75.0</td>\n",
       "      <td>0.083</td>\n",
       "      <td>0.091</td>\n",
       "      <td>0.096</td>\n",
       "      <td>28228.86076</td>\n",
       "      <td>18361.09422</td>\n",
       "      <td>18899.27711</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1/1/2017 0:40</td>\n",
       "      <td>5.921</td>\n",
       "      <td>75.7</td>\n",
       "      <td>0.081</td>\n",
       "      <td>0.048</td>\n",
       "      <td>0.085</td>\n",
       "      <td>27335.69620</td>\n",
       "      <td>17872.34043</td>\n",
       "      <td>18442.40964</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        DateTime  Temperature  Humidity  Wind Speed  general diffuse flows  \\\n",
       "0  1/1/2017 0:00        6.559      73.8       0.083                  0.051   \n",
       "1  1/1/2017 0:10        6.414      74.5       0.083                  0.070   \n",
       "2  1/1/2017 0:20        6.313      74.5       0.080                  0.062   \n",
       "3  1/1/2017 0:30        6.121      75.0       0.083                  0.091   \n",
       "4  1/1/2017 0:40        5.921      75.7       0.081                  0.048   \n",
       "\n",
       "   diffuse flows  Zone 1 Power Consumption  Zone 2  Power Consumption  \\\n",
       "0          0.119               34055.69620                16128.87538   \n",
       "1          0.085               29814.68354                19375.07599   \n",
       "2          0.100               29128.10127                19006.68693   \n",
       "3          0.096               28228.86076                18361.09422   \n",
       "4          0.085               27335.69620                17872.34043   \n",
       "\n",
       "   Zone 3  Power Consumption  \n",
       "0                20240.96386  \n",
       "1                20131.08434  \n",
       "2                19668.43373  \n",
       "3                18899.27711  \n",
       "4                18442.40964  "
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "66266919",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x11930b3d520>"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 2000x2000 with 72 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "20ac9c3c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(df.corr())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "317ede40",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Temperature', ylabel='Count'>"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(df['Temperature'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "45303e91",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(['Wind Speed',\n",
    "       'general diffuse flows', 'diffuse flows'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "9cf7984c",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df[['Temperature', 'Humidity']]\n",
    "y = df['Zone 3  Power Consumption']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "57cf895c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "12565cdb",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=101)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "8f2fc8de",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "84b6d21d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lm = LinearRegression()\n",
    "lm.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "fb64e819",
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions = lm.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "bca2c440",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import metrics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "4af3c275",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE: 4452.735592328345\n",
      "MSE: 32732703.45899012\n",
      "RMSE: 5721.250165740887\n"
     ]
    }
   ],
   "source": [
    "print('MAE:', metrics.mean_absolute_error(y_test, predictions))\n",
    "print('MSE:', metrics.mean_squared_error(y_test, predictions))\n",
    "print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77923782",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}