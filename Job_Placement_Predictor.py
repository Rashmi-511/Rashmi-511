{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c612c200",
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
   "execution_count": 2,
   "id": "094c204b",
   "metadata": {},
   "outputs": [],
   "source": [
    "job=pd.read_csv('Job_Placement_Data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6452b8a2",
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
       "      <th>gender</th>\n",
       "      <th>ssc_percentage</th>\n",
       "      <th>ssc_board</th>\n",
       "      <th>hsc_percentage</th>\n",
       "      <th>hsc_board</th>\n",
       "      <th>hsc_subject</th>\n",
       "      <th>degree_percentage</th>\n",
       "      <th>undergrad_degree</th>\n",
       "      <th>work_experience</th>\n",
       "      <th>emp_test_percentage</th>\n",
       "      <th>specialisation</th>\n",
       "      <th>mba_percent</th>\n",
       "      <th>status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M</td>\n",
       "      <td>67.00</td>\n",
       "      <td>Others</td>\n",
       "      <td>91.00</td>\n",
       "      <td>Others</td>\n",
       "      <td>Commerce</td>\n",
       "      <td>58.00</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>No</td>\n",
       "      <td>55.0</td>\n",
       "      <td>Mkt&amp;HR</td>\n",
       "      <td>58.80</td>\n",
       "      <td>Placed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>79.33</td>\n",
       "      <td>Central</td>\n",
       "      <td>78.33</td>\n",
       "      <td>Others</td>\n",
       "      <td>Science</td>\n",
       "      <td>77.48</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>Yes</td>\n",
       "      <td>86.5</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>66.28</td>\n",
       "      <td>Placed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>M</td>\n",
       "      <td>65.00</td>\n",
       "      <td>Central</td>\n",
       "      <td>68.00</td>\n",
       "      <td>Central</td>\n",
       "      <td>Arts</td>\n",
       "      <td>64.00</td>\n",
       "      <td>Comm&amp;Mgmt</td>\n",
       "      <td>No</td>\n",
       "      <td>75.0</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>57.80</td>\n",
       "      <td>Placed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M</td>\n",
       "      <td>56.00</td>\n",
       "      <td>Central</td>\n",
       "      <td>52.00</td>\n",
       "      <td>Central</td>\n",
       "      <td>Science</td>\n",
       "      <td>52.00</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>No</td>\n",
       "      <td>66.0</td>\n",
       "      <td>Mkt&amp;HR</td>\n",
       "      <td>59.43</td>\n",
       "      <td>Not Placed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>M</td>\n",
       "      <td>85.80</td>\n",
       "      <td>Central</td>\n",
       "      <td>73.60</td>\n",
       "      <td>Central</td>\n",
       "      <td>Commerce</td>\n",
       "      <td>73.30</td>\n",
       "      <td>Comm&amp;Mgmt</td>\n",
       "      <td>No</td>\n",
       "      <td>96.8</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>55.50</td>\n",
       "      <td>Placed</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gender  ssc_percentage ssc_board  hsc_percentage hsc_board hsc_subject  \\\n",
       "0      M           67.00    Others           91.00    Others    Commerce   \n",
       "1      M           79.33   Central           78.33    Others     Science   \n",
       "2      M           65.00   Central           68.00   Central        Arts   \n",
       "3      M           56.00   Central           52.00   Central     Science   \n",
       "4      M           85.80   Central           73.60   Central    Commerce   \n",
       "\n",
       "   degree_percentage undergrad_degree work_experience  emp_test_percentage  \\\n",
       "0              58.00         Sci&Tech              No                 55.0   \n",
       "1              77.48         Sci&Tech             Yes                 86.5   \n",
       "2              64.00        Comm&Mgmt              No                 75.0   \n",
       "3              52.00         Sci&Tech              No                 66.0   \n",
       "4              73.30        Comm&Mgmt              No                 96.8   \n",
       "\n",
       "  specialisation  mba_percent      status  \n",
       "0         Mkt&HR        58.80      Placed  \n",
       "1        Mkt&Fin        66.28      Placed  \n",
       "2        Mkt&Fin        57.80      Placed  \n",
       "3         Mkt&HR        59.43  Not Placed  \n",
       "4        Mkt&Fin        55.50      Placed  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "job.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "21a13a37",
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
       "      <th>ssc_percentage</th>\n",
       "      <th>hsc_percentage</th>\n",
       "      <th>degree_percentage</th>\n",
       "      <th>emp_test_percentage</th>\n",
       "      <th>mba_percent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>215.000000</td>\n",
       "      <td>215.000000</td>\n",
       "      <td>215.000000</td>\n",
       "      <td>215.000000</td>\n",
       "      <td>215.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>67.303395</td>\n",
       "      <td>66.333163</td>\n",
       "      <td>66.370186</td>\n",
       "      <td>72.100558</td>\n",
       "      <td>62.278186</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>10.827205</td>\n",
       "      <td>10.897509</td>\n",
       "      <td>7.358743</td>\n",
       "      <td>13.275956</td>\n",
       "      <td>5.833385</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>40.890000</td>\n",
       "      <td>37.000000</td>\n",
       "      <td>50.000000</td>\n",
       "      <td>50.000000</td>\n",
       "      <td>51.210000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>60.600000</td>\n",
       "      <td>60.900000</td>\n",
       "      <td>61.000000</td>\n",
       "      <td>60.000000</td>\n",
       "      <td>57.945000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>67.000000</td>\n",
       "      <td>65.000000</td>\n",
       "      <td>66.000000</td>\n",
       "      <td>71.000000</td>\n",
       "      <td>62.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>75.700000</td>\n",
       "      <td>73.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>83.500000</td>\n",
       "      <td>66.255000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>89.400000</td>\n",
       "      <td>97.700000</td>\n",
       "      <td>91.000000</td>\n",
       "      <td>98.000000</td>\n",
       "      <td>77.890000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       ssc_percentage  hsc_percentage  degree_percentage  emp_test_percentage  \\\n",
       "count      215.000000      215.000000         215.000000           215.000000   \n",
       "mean        67.303395       66.333163          66.370186            72.100558   \n",
       "std         10.827205       10.897509           7.358743            13.275956   \n",
       "min         40.890000       37.000000          50.000000            50.000000   \n",
       "25%         60.600000       60.900000          61.000000            60.000000   \n",
       "50%         67.000000       65.000000          66.000000            71.000000   \n",
       "75%         75.700000       73.000000          72.000000            83.500000   \n",
       "max         89.400000       97.700000          91.000000            98.000000   \n",
       "\n",
       "       mba_percent  \n",
       "count   215.000000  \n",
       "mean     62.278186  \n",
       "std       5.833385  \n",
       "min      51.210000  \n",
       "25%      57.945000  \n",
       "50%      62.000000  \n",
       "75%      66.255000  \n",
       "max      77.890000  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "job.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "99b993e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 215 entries, 0 to 214\n",
      "Data columns (total 13 columns):\n",
      " #   Column               Non-Null Count  Dtype  \n",
      "---  ------               --------------  -----  \n",
      " 0   gender               215 non-null    object \n",
      " 1   ssc_percentage       215 non-null    float64\n",
      " 2   ssc_board            215 non-null    object \n",
      " 3   hsc_percentage       215 non-null    float64\n",
      " 4   hsc_board            215 non-null    object \n",
      " 5   hsc_subject          215 non-null    object \n",
      " 6   degree_percentage    215 non-null    float64\n",
      " 7   undergrad_degree     215 non-null    object \n",
      " 8   work_experience      215 non-null    object \n",
      " 9   emp_test_percentage  215 non-null    float64\n",
      " 10  specialisation       215 non-null    object \n",
      " 11  mba_percent          215 non-null    float64\n",
      " 12  status               215 non-null    object \n",
      "dtypes: float64(5), object(8)\n",
      "memory usage: 22.0+ KB\n"
     ]
    }
   ],
   "source": [
    "job.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "334d4f64",
   "metadata": {},
   "outputs": [],
   "source": [
    "status_=pd.get_dummies(job['status'],drop_first=True)\n",
    "work_experience_=pd.get_dummies(job['work_experience'],drop_first=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "8dc33988",
   "metadata": {},
   "outputs": [],
   "source": [
    "job=pd.concat([job,status_,work_experience_],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0bb3dfb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "job = job.rename(columns={'Yes': 'work_experience_', 'Placed': 'status_'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ac309c08",
   "metadata": {},
   "outputs": [],
   "source": [
    "job.drop(['status','work_experience'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7ff0e2e5",
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
       "      <th>gender</th>\n",
       "      <th>ssc_percentage</th>\n",
       "      <th>ssc_board</th>\n",
       "      <th>hsc_percentage</th>\n",
       "      <th>hsc_board</th>\n",
       "      <th>hsc_subject</th>\n",
       "      <th>degree_percentage</th>\n",
       "      <th>undergrad_degree</th>\n",
       "      <th>emp_test_percentage</th>\n",
       "      <th>specialisation</th>\n",
       "      <th>mba_percent</th>\n",
       "      <th>status_</th>\n",
       "      <th>work_experience_</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M</td>\n",
       "      <td>67.00</td>\n",
       "      <td>Others</td>\n",
       "      <td>91.00</td>\n",
       "      <td>Others</td>\n",
       "      <td>Commerce</td>\n",
       "      <td>58.00</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>55.0</td>\n",
       "      <td>Mkt&amp;HR</td>\n",
       "      <td>58.80</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>79.33</td>\n",
       "      <td>Central</td>\n",
       "      <td>78.33</td>\n",
       "      <td>Others</td>\n",
       "      <td>Science</td>\n",
       "      <td>77.48</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>86.5</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>66.28</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>M</td>\n",
       "      <td>65.00</td>\n",
       "      <td>Central</td>\n",
       "      <td>68.00</td>\n",
       "      <td>Central</td>\n",
       "      <td>Arts</td>\n",
       "      <td>64.00</td>\n",
       "      <td>Comm&amp;Mgmt</td>\n",
       "      <td>75.0</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>57.80</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M</td>\n",
       "      <td>56.00</td>\n",
       "      <td>Central</td>\n",
       "      <td>52.00</td>\n",
       "      <td>Central</td>\n",
       "      <td>Science</td>\n",
       "      <td>52.00</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>66.0</td>\n",
       "      <td>Mkt&amp;HR</td>\n",
       "      <td>59.43</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>M</td>\n",
       "      <td>85.80</td>\n",
       "      <td>Central</td>\n",
       "      <td>73.60</td>\n",
       "      <td>Central</td>\n",
       "      <td>Commerce</td>\n",
       "      <td>73.30</td>\n",
       "      <td>Comm&amp;Mgmt</td>\n",
       "      <td>96.8</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>55.50</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gender  ssc_percentage ssc_board  hsc_percentage hsc_board hsc_subject  \\\n",
       "0      M           67.00    Others           91.00    Others    Commerce   \n",
       "1      M           79.33   Central           78.33    Others     Science   \n",
       "2      M           65.00   Central           68.00   Central        Arts   \n",
       "3      M           56.00   Central           52.00   Central     Science   \n",
       "4      M           85.80   Central           73.60   Central    Commerce   \n",
       "\n",
       "   degree_percentage undergrad_degree  emp_test_percentage specialisation  \\\n",
       "0              58.00         Sci&Tech                 55.0         Mkt&HR   \n",
       "1              77.48         Sci&Tech                 86.5        Mkt&Fin   \n",
       "2              64.00        Comm&Mgmt                 75.0        Mkt&Fin   \n",
       "3              52.00         Sci&Tech                 66.0         Mkt&HR   \n",
       "4              73.30        Comm&Mgmt                 96.8        Mkt&Fin   \n",
       "\n",
       "   mba_percent  status_  work_experience_  \n",
       "0        58.80        1                 0  \n",
       "1        66.28        1                 1  \n",
       "2        57.80        1                 0  \n",
       "3        59.43        0                 0  \n",
       "4        55.50        1                 0  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "job.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "b5cf5276",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='work_experience_', ylabel='count'>"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjMAAAGxCAYAAACXwjeMAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAvrElEQVR4nO3de1SVdaL/8c8WFTcJmLe9JVFxhLzgpdRxxAyy5BxqPBmNWXo6djKPRTeiCYcfWVtHoayMObF0slNqx2FsVmV3DeokWWSDHi2zjmky4IwQXRBQERS+vz8a9rjDCyLw7Ifer7WetXy+z+3zsBbyWc9lb4cxxggAAMCmOlkdAAAA4HxQZgAAgK1RZgAAgK1RZgAAgK1RZgAAgK1RZgAAgK1RZgAAgK1RZgAAgK11tjpAW2toaNDBgwcVHBwsh8NhdRwAANAMxhhVV1crLCxMnTqd+dpLhy8zBw8eVHh4uNUxAABACxw4cED9+/c/4zodvswEBwdL+uGHERISYnEaAADQHFVVVQoPD/f+HT+TDl9mGm8thYSEUGYAALCZ5jwiwgPAAADA1igzAADA1igzAADA1jr8MzMAANhNfX29jh8/bnWMNtWlSxcFBAS0yr4oMwAA+AljjMrKynTo0CGro7SLHj16yO12n/fnwFFmAADwE41Fpm/fvgoKCuqwH/ZqjNHRo0dVXl4uSerXr9957Y8yAwCAH6ivr/cWmV69elkdp805nU5JUnl5ufr27Xtet5x4ABgAAD/Q+IxMUFCQxUnaT+O5nu/zQZQZAAD8SEe9tXQqrXWulBkAAGBrlBkAAGBrlBkAAGzulltu0fTp0895O4/HozFjxrR6nvZGmQEAALZGmQEAwCZefPFFjRw5Uk6nU7169dJVV12lBx54QGvXrtWrr74qh8Mhh8OhzZs3S5IWLFigqKgoBQUFafDgwVq4cKH3zaE1a9Zo0aJF+uSTT7zbrVmzRn/5y1/kcDi0c+dO73EPHTrks9+KigrNnj1bffr0kdPpVGRkpFavXt3OP41/4HNmAACwgdLSUt10001atmyZrrvuOlVXV2vLli36t3/7N5WUlKiqqspbKHr27ClJCg4O1po1axQWFqZdu3Zp3rx5Cg4OVmpqqmbOnKnPPvtMmzZt0jvvvCNJCg0N1ddff33WLAsXLtTnn3+ujRs3qnfv3tq3b59qamra7uTPgjKDDqdk8UirI+DvBjy0y+oIQIdRWlqqEydOKDExUQMHDpQkjRz5w/93TqdTtbW1crvdPts8+OCD3n8PGjRI999/v1544QWlpqbK6XSqe/fu6ty5c5PtzqakpESXXHKJxo0b5923lSgzAADYwOjRo3XllVdq5MiR+qd/+ifFx8frV7/6lS688MLTbvPiiy8qKytL+/bt0+HDh3XixAmFhIScd5Y77rhD119/vf73f/9X8fHxmj59umJiYs57vy3FMzMAANhAQECA8vLytHHjRg0fPlxPPfWULr74YhUVFZ1y/a1bt+rGG29UQkKC3njjDe3YsUPp6emqq6s743E6dfqhGhhjvGM//oTehIQEFRcXKzk5WQcPHtSVV16pX//61+d5hi1HmQEAwCYcDocmTZqkRYsWaceOHeratas2bNigrl27qr6+3mfdDz/8UAMHDlR6errGjRunyMhIFRcX+6xzqu369Okj6YfbWo1Ofhj45PVuueUWrVu3TllZWVq1alUrneW54zYTAAA28PHHH+vdd99VfHy8+vbtq48//ljffPONhg0bpmPHjuntt9/Wnj171KtXL4WGhmrIkCEqKSnR+vXrNX78eL355pvasGGDzz4HDRqkoqIi7dy5U/3791dwcLCcTqd+8Ytf6JFHHtGgQYP07bff+jx7I0kPPfSQxo4dqxEjRqi2tlZvvPGGhg0b1p4/Dh9cmQEAwAZCQkL0/vvv6+qrr1ZUVJQefPBBPfHEE0pISNC8efN08cUXa9y4cerTp48+/PBDXXvttbrvvvt01113acyYMSooKNDChQt99nn99dfrn//5n3XFFVeoT58++uMf/yhJeu6553T8+HGNGzdO9957r5YsWeKzXdeuXZWWlqZRo0bp8ssvV0BAgNavX99uP4sfc5iTb4p1QFVVVQoNDVVlZWWrPPQE/8fbTP6Dt5mA5jt27JiKiooUERGhbt26WR2nXZzpnM/l7zdXZgAAgK1RZgAAQKvIyMhQ9+7dTzklJCS02XF5ABgAALSK22+/XTfccMMplzmdzjY7LmUGAAC0ip49e3q/SqE9cZsJAADYmqVl5sSJE3rwwQcVEREhp9OpwYMHa/HixWpoaPCuY4yRx+NRWFiYnE6n4uLitHv3bgtTAwAAf2JpmXn00Uf1+9//XtnZ2friiy+0bNkyPfbYY3rqqae8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l112xvWvuuoqTZw4UdOnT9ejjz6qiy++WAcPHtRbb72l6dOna9y4cUpPT1dlZaX+8z//U927d9fGjRs1d+5cvfHGG979dOvWTXPmzNHjjz+uqqoq3XPPPbrhhhvkdrsl/fDG0z333KOQkBAlJCSotrZW27ZtU0VFhVJSUpp9fg899JB++ctfKjw8XDNmzFCnTp306aefateuXVqyZEmz9nHXXXfpqaee0o033qi0tDSFhoZq69at+vnPf66LL7641bICP3lWP7QDoHXdf//9RpL57LPPvGOjR482ffr0MQ0NDd6xF1980QwfPtx06dLFDBgwwDz22GM++xk4cKB58sknfcZOfpup0RNPPGGCg4PNhx9+eNZsVVVV5u677zZhYWGmS5cuJjw83MyePduUlJSY9957z3Tu3Nls2bLFu35xcbEJDQ01K1asMMb88ADw6NGjzYoVK0xYWJjp1q2bSUxMNN9//73Pcf7whz+YMWPGmK5du5oLL7zQXH755ebll18+7TkY0/QBYGN+eKMpJibGOJ1OExISYn7+85+bVatWeZdLMhs2bPDZJjQ01OetsE8++cTEx8eboKAgExwcbCZPnmy++uqrZmUF0DwOY05xoxwA/JDH49Err7zSIb9OAUDL8aF5AADA1igzAFrFH/7wB3Xv3v2U04gRI6yOZzsZGRmn/XkmJCRYHQ/wK9xmAtAqqqur9fXXX59yWZcuXTRw4MB2TmRv33//vb7//vtTLnM6nbrooovaORHgvygzAADA1rjNBAAAbI0yAwAAbI0yAwAAbI0yAwAAbI0yAwAAbI0yAwAAbI0yAwAAbI0yAwAAbO3/A4tD6xHtkbVlAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='work_experience_',data=job,hue='status_')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "b214bd48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='work_experience_', ylabel='count'>"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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0CA988wzuvfee/X+++9r9erV1/WXNI899pgqKyt15513atu2bbr11luvuv9tt92mIUOGaNy4cVq6dKluvPFGnThxQn/4wx80btw4DRw4UPPnz1dpaal++ctfqnXr1tq2bZumTZum3//+9+7jBAQEaPLkyVq+fLnKyso0c+ZM3XPPPYqMjJT07V88zZw5UyEhIRo9erTKy8u1b98+FRcXKyUlpdbv7+mnn9add96pmJgYTZgwQT4+Pvr444/1ySefaPHixbU6xqOPPqpnn31W9913n1JTUxUaGqo9e/bolltu0Y033thgswLfe07ftAOgYc2dO9dIMn/+85/d6/r06WPat29vqqqq3OteffVV07NnT+Pn52c6depkfvGLX3gcp3PnzmbVqlUe677710zVVqxYYYKDg82uXbuuOVtZWZl57LHHTHR0tPHz8zMxMTFm0qRJ5vjx4+a9994zLVq0MLm5ue79jx07ZkJDQ82aNWuMMd/eANynTx+zZs0aEx0dbQICAsz48ePN6dOnPV7nxRdfNH379jUtW7Y0P/jBD8yIESPMa6+9dsX3YEzNG4CN+fYvmoYOHWoCAwNNSEiIueWWW8y6devc2yWZrVu3ejwnNDTU46/CDhw4YJKSkkxQUJAJDg42w4cPN19++WWtZgVQOy5jLnOhHAC8UFpaml5//fVm+XUKAOqOD80DAABWI2YANIgXX3xRrVu3vuyjV69eTo9nnfT09Cv+e44ePdrp8QCvwmUmAA3izJkz+utf/3rZbX5+furcuXMTT2S306dP6/Tp05fdFhgYqA4dOjTxRID3ImYAAIDVuMwEAACsRswAAACrETMAAMBqxAwAALAaMQMAAKxGzAAAAKsRMwAAwGrEDAAAsNr/ARLzrYXOsyyqAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='work_experience_',data=job,hue='gender',palette='viridis')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "1da90c5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.JointGrid at 0x217ea83d460>"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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KjXc5HnIJz/5yeG/r1ixgt/7vd/j3//93/noRz9KNBqlsLAQy7LG3e5Kzpw5w/bt29m5c+fwucXCJomUEEKIeW3r1q3cfvvtbN68mbvvvpu77rqLn/u5nxu3D+to3/zmN/nyl7/M8ePH6e/vx3XdnKxi+//+v/+P97znPezevZu77rqLd77znXOyQbQs2M8dqZESQggxr5mmyRNPPMH3v/99NmzYwF//9V+zdu1aTp06lfH6L7zwAr/wC7/APffcw2OPPcarr77KJz7xCdLp9KT3YxjBR+boJOTyruP33HMPzc3N3H///Vy4cIHbb7+d3//937/KR5h7zoFn8h3CgiGJlBBCiHlPKcXrXvc6HnjgAV599VVCoRCPPvoooVAIz/PGXPfZZ5+loaGBT3ziE+zcuZOmpiaam5vHXCfT7SorK4FgKnHI6MLz0df74Ac/yNe//nW+/OUv8/DDD+foUeaO35o5yRTTJ1N7Qggh5rUXX3yRp556irvuuouqqipefPFF2tvbWb9+Pclkkh/+8IccOXKE8vJySkpKWL16NWfOnOHf/u3fuPbaa/nud7/Lo48+OuacK1asGN62bNmyZRQVFRGNRrnhhhv40z/9U1asWEFHR8eYWiuAT3/60+zYsYONGzeSSqV47LHHWL9+/Ww+HWKWyYiUEEKIea24uJif/vSnvPnNb2bNmjV88pOf5C/+4i+45557+NVf/VXWrl3Lzp07qays5Nlnn+Ud73gHv/M7v8Nv/MZvsG3bNp577jk+9alPjTnne97zHt70pjdx2223UVlZyb/+678C8H/+z//BcRx27tzJb//2b/O5z31uzO1CoRAf//jH2bJlC294wxswTZN/+7d/m7XnQsw+2SIGaZkvhBBznWwRk9stYi5+66+pevdv5OSci52MSAkhhBBCZEkSKSGEEGKGPfjggxQWFmb8ueeee/IdnrgKUmwuhBBCzLBf+7Vf4+d//uczHotGo7McjcglSaSEEEKIGVZWVja8PY1YWGRqTwghhBAiS5JICSGEEEJkSRIpIYQQQogsSSIlhBBCCJElSaSEEEIIIbIkiZQQQgghRJYkkRJCCCFmwd/+7d8Ob/eyY8cOfvazn+U7JJEDkkgJIYRYVLTWtPVoznQEf87GlrP//u//zv33388nPvEJXn31VV7/+tdzzz33cObMmRm/bzGzJJES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UkqpHBRPCJEYlOVrb9S50EBKKaWUykHNbc6/JXkj246xTgMppZRSKge1tIHbgnz/SLdkbNNASimllMpBrVEoCoIxOrR3LjSQUkoppXJQuD2QUufGPdINUEoppdTwEoFIDAoD2ht1rrRHSimllMox0QTYAgWBkW7J2KeBlFJKKZVj2mLOvzrR/NxpIKWUUkrlmFjS+TfoHdl2jAcaSCmllFI5KOAFy9I5UudKAymllFIqBwV9I92C8UEDKaWUUioH6bDe4NBASimllMpBfs9It2B80EBKKaWUykF+j86PGgwaSCmllFI5yKc9UoNCAymllFIqB/m0tsmg0EBKKaWUykFe7ZEaFBpIKaWUUjnI4xrpFowPGkgppZRSOUgDqcGhgZRSSimVgzSQGhwaSCmllFI5yK2B1KDQQEoppZTKQcZoHqnBoIGUUkoppVSWNJBSSimllMqSBlJKKaWUUlnSQEoppZRSKksaSCmllFJKZUkDKaWUUkqpLGkgpZRSSimVJQ2klFJKKaWypIGUUkoppVSWNJBSSimllMqSBlJKKaWUUlnSQEoppZRSKksaSCmllFJKZUkDKaWUUkqpLGkgpZRSSimVJQ2klFJKKaWypIGUUkoplWNmVY90C8YPDaSUUkqpHDN3kn78Dxa9kkoppZRSWdJASimllFIqSxpIKaWUUkplSQMppZRSSqksaSCllFJKKZUlDaSUUkoppbI0pgKpBx54AGMMd911V+c2EWH16tXU1NQQCAS4/PLL2bZt28g1UimllFI5Y8wEUu+88w6PP/44CxcuTNn+4IMPsnbtWh599FHeeecdqqqqWLVqFc3NzSPUUqWUUkrlijERSLW0tHDTTTfxi1/8gpKSks7tIsJPf/pTvve973H99dczf/58nnzyScLhML/97W9HsMVKKaWUygVjIpC64447uOaaa7jyyitTtu/bt49jx45x1VVXdW7z+XysXLmSt956K+PjRaNRQqFQypdSSik13ujn3dAb9YHUU089xcaNG3nggQd67Dt27BgAlZWVKdsrKys796XzwAMPUFRU1PlVW1s7uI1WSimlRgH9vBt6ozqQOnToEHfeeSe/+c1v8Pv9GY8zxqR8LyI9tnV377330tTU1Pl16NChQWuzUkopNVro593Qc490A3qzceNGGhoaWLJkSee2ZDLJa6+9xqOPPsqOHTsAp2equrqrlHVDQ0OPXqrufD4fPp9v6BqulFJKjQL6eTf0RnWP1BVXXMHWrVvZvHlz59fSpUu56aab2Lx5M9OmTaOqqop169Z1nhOLxVi/fj3Lly8fwZYrpZRSKheM6h6pgoIC5s+fn7ItLy+PsrKyzu133XUXa9asob6+nvr6etasWUMwGOQLX/jCSDRZKaWUUjlkVAdS/XH33XcTiUS4/fbbaWxsZNmyZbz44osUFBSMdNOUUkopNc4ZEZGRbsRIC4VCFBUV0dTURGFh4Ug3RymllBoS+nk3+MZ8j9Rg6IglNb+GUkqpsaSgoKDXVepq6GkgBZw6dQpA82sopZQaU7RnaeRpIAWUlpYCcPDgQYqKika4NbkhFApRW1vLoUOH9E1gmOg1Hxl63YdfLl3zgc4HLigooKmpSecRDyINpADLcrJAFBUVjfs/utGmsLBQr/kw02s+MvS6Dz+95j0ZY/SaDLJRnUdKKaWUUmo000BKKaWUUipLGkjhpND/wQ9+oGn0h5Fe8+Gn13xk6HUffnrN1XDSPFJKKaWUUlnSHimllFJKqSxpIKWUUkoplSUNpJRSSimlspQzgdQDDzzABRdcQEFBARMmTOC6665jx44dKceICKtXr6ampoZAIMDll1/Otm3bRqjF488DDzyAMYa77rqrc5te86Fx5MgRvvjFL1JWVkYwGOS8885j48aNnfv1ug+uRCLB97//ferq6ggEAkybNo0f/ehH2LbdeYxe83Pz2muv8ZnPfIaamhqMMfy///f/Uvb35/pGo1G+8Y1vUF5eTl5eHp/97Gc5fPjwML4KNR7lTCC1fv167rjjDt5++23WrVtHIpHgqquuorW1tfOYBx98kLVr1/Loo4/yzjvvUFVVxapVq2hubh7Blo8P77zzDo8//jgLFy5M2a7XfPA1NjayYsUKPB4Pzz//PB9++CEPP/wwxcXFncfodR9cP/7xj3nsscd49NFH2b59Ow8++CAPPfQQP/vZzzqP0Wt+blpbW1m0aBGPPvpo2v39ub533XUXzzzzDE899RRvvPEGLS0tXHvttSSTyeF6GWo8khzV0NAggKxfv15ERGzblqqqKvn7v//7zmPa2tqkqKhIHnvssZFq5rjQ3Nws9fX1sm7dOlm5cqXceeedIqLXfKjcc889cskll2Tcr9d98F1zzTXyV3/1Vynbrr/+evniF78oInrNBxsgzzzzTOf3/bm+Z86cEY/HI0899VTnMUeOHBHLsuSFF14Ytrar8SdneqTO1tTUBHTV2du3bx/Hjh3jqquu6jzG5/OxcuVK3nrrrRFp43hxxx13cM0113DllVembNdrPjR+//vfs3TpUm644QYmTJjA4sWL+cUvftG5X6/74Lvkkkv44x//yM6dOwF4//33eeONN/j0pz8N6DUfav25vhs3biQej6ccU1NTw/z58/VnoM5JTtbaExG+/e1vc8kllzB//nwAjh07BkBlZWXKsZWVlRw4cGDY2zhePPXUU2zcuJF33323xz695kNj7969/PznP+fb3/42f/M3f8OGDRv45je/ic/n40tf+pJe9yFwzz330NTUxOzZs3G5XCSTSe6//35uvPFGQH/Xh1p/ru+xY8fwer2UlJT0OKbjfKWykZOB1Ne//nW2bNnCG2+80WOfMSblexHpsU31z6FDh7jzzjt58cUX8fv9GY/Taz64bNtm6dKlrFmzBoDFixezbds2fv7zn/OlL32p8zi97oPnn//5n/n1r3/Nb3/7W+bNm8fmzZu56667qKmp4eabb+48Tq/50Mrm+urPQJ2rnBva+8Y3vsHvf/97XnnlFSZNmtS5vaqqCqDHnUlDQ0OPuxzVPxs3bqShoYElS5bgdrtxu92sX7+eRx55BLfb3Xld9ZoPrurqaubOnZuybc6cORw8eBDQ3/Wh8N/+23/ju9/9Ln/xF3/BggUL+Mu//Eu+9a1v8cADDwB6zYdaf65vVVUVsViMxsbGjMcolY2cCaREhK9//es8/fTTvPzyy9TV1aXsr6uro6qqinXr1nVui8VirF+/nuXLlw93c8eFK664gq1bt7J58+bOr6VLl3LTTTexefNmpk2bptd8CKxYsaJHao+dO3cyZcoUQH/Xh0I4HMayUt9OXS5XZ/oDveZDqz/Xd8mSJXg8npRjjh49ygcffKA/A3VuRm6e+/C67bbbpKioSF599VU5evRo51c4HO485u///u+lqKhInn76adm6davceOONUl1dLaFQaARbPr50X7Unotd8KGzYsEHcbrfcf//9smvXLvnNb34jwWBQfv3rX3ceo9d9cN18880yceJE+bd/+zfZt2+fPP3001JeXi5333135zF6zc9Nc3OzbNq0STZt2iSArF27VjZt2iQHDhwQkf5d31tvvVUmTZokL730krz33nvyyU9+UhYtWiSJRGKkXpYaB3ImkALSfv3yl7/sPMa2bfnBD34gVVVV4vP55LLLLpOtW7eOXKPHobMDKb3mQ+PZZ5+V+fPni8/nk9mzZ8vjjz+esl+v++AKhUJy5513yuTJk8Xv98u0adPke9/7nkSj0c5j9Jqfm1deeSXte/jNN98sIv27vpFIRL7+9a9LaWmpBAIBufbaa+XgwYMj8GrUeGJEREamL0wppZRSamzLmTlSSimllFKDTQMppZRSSqksaSCllFJKKZUlDaSUUkoppbKkgZRSSimlVJY0kFJKKaWUypIGUkoppZRSWdJASimllFIqSxpIKTVKXH755dx1110j3QyllFIDoIGUUmrMWr16Needd95IN0MplcM0kFJKDbpYLDbSTVBKqWGhgZRSo4ht29x9992UlpZSVVXF6tWrO/etXr2ayZMn4/P5qKmp4Zvf/Gbnvmg0yt13301tbS0+n4/6+nr+9//+330+36uvvooxhueee45Fixbh9/tZtmwZW7duTTnurbfe4rLLLiMQCFBbW8s3v/lNWltbO/dPnTqV++67jy9/+csUFRVxyy23APDmm2+ycuVKgsEgJSUlXH311TQ2NgIgIjz44INMmzaNQCDAokWL+N3vftejbX/84x9ZunQpwWCQ5cuXs2PHDgCeeOIJfvjDH/L+++9jjMEYwxNPPAHA2rVrWbBgAXl5edTW1nL77bfT0tKS8pp+8YtfUFtbSzAY5HOf+xxr166luLg45Zhnn32WJUuW4Pf7mTZtGj/84Q9JJBJ9XlelVA4Z4aLJSql2K1eulMLCQlm9erXs3LlTnnzySTHGyIsvvij/9//+XyksLJR///d/lwMHDsif/vQnefzxxzvP/fznPy+1tbXy9NNPy549e+Sll16Sp556qs/nfOWVVwSQOXPmyIsvvihbtmyRa6+9VqZOnSqxWExERLZs2SL5+fnyk5/8RHbu3ClvvvmmLF68WL785S93Ps6UKVOksLBQHnroIdm1a5fs2rVLNm3aJD6fT2677TbZvHmzfPDBB/Kzn/1MTpw4ISIif/M3fyOzZ8+WF154Qfbs2SO//OUvxefzyauvvprStmXLlsmrr74q27Ztk0svvVSWL18uIiLhcFj++q//WubNmydHjx6Vo0ePSjgcFhGRn/zkJ/Lyyy/L3r175Y9//KPMmjVLbrvtts72vvHGG2JZljz00EOyY8cO+R//439IaWmpFBUVdR7zwgsvSGFhoTzxxBOyZ88eefHFF2Xq1KmyevXqLH/CSqnxSAMppUaJlStXyiWXXJKy7YILLpB77rlHHn74YZk5c2ZncNPdjh07BJB169YN+Dk7gpXuQdepU6ckEAjIP//zP4uIyF/+5V/Kf/2v/zXlvNdff10sy5JIJCIiTiB13XXXpRxz4403yooVK9I+b0tLi/j9fnnrrbdStn/1q1+VG2+8MaVtL730Uuf+5557ToDO5/3BD34gixYt6vN1/su//IuUlZV1fv+f//N/lmuuuSblmJtuuiklkLr00ktlzZo1Kcf80z/9k1RXV/f5fEqp3KFDe0qNIgsXLkz5vrq6moaGBm644QYikQjTpk3jlltu4ZlnnukcYtq8eTMul4uVK1dm/bwXX3xx5/9LS0uZNWsW27dvB2Djxo088cQT5Ofnd35dffXV2LbNvn37Os9bunRpymNu3ryZK664Iu3zffjhh7S1tbFq1aqUx/3Vr37Fnj17Ml6T6upqABoaGnp9Pa+88gqrVq1i4sSJFBQU8KUvfYlTp051Dkfu2LGDCy+8MOWcs7/fuHEjP/rRj1Lad8stt3D06FHC4XCvz6+Uyh3ukW6AUqqLx+NJ+d4Yg23b1NbWsmPHDtatW8dLL73E7bffzkMPPcT69esJBAJD0hZjDODM2/ra176WMierw+TJkzv/n5eXl7Kvt3bZtg3Ac889x8SJE1P2+Xy+lO+7X5PubcrkwIEDfPrTn+bWW2/l7/7u7ygtLeWNN97gq1/9KvF4HHDmZ3U8VgcR6dHGH/7wh1x//fU9nsPv92d8fqVUbtFASqkxIhAI8NnPfpbPfvaz3HHHHcyePZutW7eyYMECbNtm/fr1XHnllVk99ttvv90ZFDU2NrJz505mz54NwPnnn8+2bduYMWPGgB5z4cKF/PGPf+SHP/xhj31z587F5/Nx8ODBc+pJ83q9JJPJlG3vvvsuiUSChx9+GMtyOt3/5V/+JeWY2bNns2HDhh7ndXf++eezY8eOAb9upVRu0UBKqTHgiSeeIJlMsmzZMoLBIP/0T/9EIBBgypQplJWVcfPNN/NXf/VXPPLIIyxatIgDBw7Q0NDA5z//+X49/o9+9CPKysqorKzke9/7HuXl5Vx33XUA3HPPPVx00UXccccd3HLLLeTl5bF9+3bWrVvHz372s4yPee+997JgwQJuv/12br31VrxeL6+88go33HAD5eXlfOc73+Fb3/oWtm1zySWXEAqFeOutt8jPz+fmm2/uV7unTp3Kvn372Lx5M5MmTaKgoIDp06eTSCT42c9+xmc+8xnefPNNHnvssZTzvvGNb3DZZZexdu1aPvOZz/Dyyy/z/PPPp/RS/e3f/i3XXnsttbW13HDDDViWxZYtW9i6dSv33Xdfv9qnlMoBIz1JSynlWLlypdx5550p2/7sz/5Mbr75ZnnmmWdk2bJlUlhYKHl5eXLRRRelTMKORCLyrW99S6qrq8Xr9cqMGTPk//yf/9Pnc3ZM6H722Wdl3rx54vV65YILLpDNmzenHLdhwwZZtWqV5OfnS15enixcuFDuv//+zv1TpkyRn/zkJz0e/9VXX5Xly5eLz+eT4uJiufrqq6WxsVFERGzbln/8x3+UWbNmicfjkYqKCrn66qtl/fr1KW3rOF5EZNOmTQLIvn37RESkra1N/vzP/1yKi4sFkF/+8pciIrJ27Vqprq6WQCAgV199tfzqV7/q8ViPP/64TJw4UQKBgFx33XVy3333SVVVVUr7X3jhBVm+fLkEAgEpLCyUCy+8MGW1pFJKGZGzJgYopXLGq6++yic+8QkaGxt75FDKNbfccgsfffQRr7/++kg3RSk1hujQnlIqJ/3DP/wDq1atIi8vj+eff54nn3yS//k//+dIN0spNcZo+gOlxrFbb701Zfl+969bb711pJs3ojZs2MCqVatYsGABjz32GI888gj/5b/8l5FullJqjNGhPaXGsYaGBkKhUNp9hYWFTJgwYZhbpJRS44sGUkoppZRSWdKhPaWUUkqpLGkgpZRSSimVJQ2klFJKKaWypIGUUkoppVSWNJBSSimllMqSBlJKKaWUUlnSQEoppZRSKksaSCmllFJKZen/B5DRJAh/44s9AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 600x600 with 3 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.jointplot(y='degree_percentage',x='hsc_percentage',data=job,hue='status_',kind='scatter',palette='coolwarm')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "83e4bc73",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='gender', ylabel='emp_test_percentage'>"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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AFYJ9ORJDzzwgH73u9/p4MGDqqqq0muvvaZdu3ZpyZIlWrFihdUZAQAAPObRyM7VV1+tpUuX6u2335ZhGLr//vv1+eef680339SAAQOszggAAOAxj0Z2JGngwIEaOHCglVkAAAAsxxmUAQCAo3k0stOkSRMZhlFju2EYCgkJUfv27TV69GiNGTPG64AAAADe8Kjs3H///ZoxY4YGDx6syy67TKZpavPmzXr33Xf1hz/8QXl5ebr99tt18uRJ3XbbbVZnBgAAOGcelZ3169dr+vTpGj9+fLXtf/vb37Rq1SotW7ZMXbp00WOPPUbZAQAAtvJozc7KlSvVv3//Gtv79eunlStXSpJ+9atfua+ZBQAAYBePyk7Tpk315ptv1tj+5ptvqmnTppKk77//XuHh4d6lAwAA8JJH01hTp07V7bffrjVr1uiyyy6TYRj66KOP9Pbbb2v+/PmSpJycHKWmploaFgAA4Hx5VHZuu+02de7cWU888YRee+01maapiy66SGvXrlVKSook6e6777Y0KAAAgCc8Pqlgr1691KtXLyuzAAAAWM7jsnNaaWlpjSudR0REePttAQAALOHRAuXjx4/rjjvuUIsWLdSoUSM1adKk2g0AAMBfeFR27rnnHr333nt66qmn5HK59Mwzz2jatGmKjY3VkiVLrM4IAADgMY+msd58800tWbJEffr00dixY3XllVeqffv2at26tV588UWNHDnS6pwAAAAe8Whk5/Dhw4qPj5d0an3O4cOHJUlXXHGF1q1bZ106AAAAL3lUdtq2bauvv/5aktS5c2f9/e9/l3RqxKdx48ZWZQMAAPCaR2VnzJgx2r59uyRp8uTJ7rU7EyZM0D333GNpQAAAAG94tGZnwoQJ7q/79u2rL774Qh9//LHatWunrl27WhYOAADAWx6N7CxZskTl5eXu+61atdKwYcPUqVMnjsYCAAB+xeNprKKiohrbS0pKNGbMGK9DnXby5Endd999io+PV2hoqNq2basHH3xQVVVV7seYpqmsrCzFxsYqNDRUffr00Y4dOyzLAAAA6jaPprFM05RhGDW2HzhwQJGRkV6HOu3hhx/W/PnztXjxYiUmJurjjz/WmDFjFBkZqbvuukuSNHv2bM2ZM0eLFi1Shw4dNH36dA0YMEC7du3iqusAUM+YpqmysjK7Y3iltLT0rF/XRSEhIWft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Sy1btqy2z+VyVbvfsGHDc/6+AOxF2QFgu3bt2ikoKEgfffSR4uLiJEnFxcXavXu3UlNT1a1bN1VWVqqwsFBXXnmlR68RGRmpmJgYffjhh+rdu7ck6eTJk9qyZYsuueQSSVLnzp3lcrm0b98+paamWvPmANiOsgPAduHh4Ro1apTuueceNW3aVC1atNADDzygBg0ayDAMdejQQSNHjtTNN9+sRx55RN26ddO3336r9957T0lJSfrVr351Tq9z1113adasWUpISFCnTp00Z84cHT16tFqOSZMmacKECaqqqtIVV1yh4uJi5ebmqlGjRho1apSPfgIAfImyA8AvzJkzR+PHj9eQIUMUERGhzMxM7d+/XyEhIZKkhQsXavr06br77rt18OBBNWvWTD179jznoiNJd999t/Lz8zV69Gg1aNBAY8eO1W9+8xsVFRW5H/PQQw+pRYsWmjlzpr766is1btxYl1xyif7f//t/lr9nALXDMM9nQhsAasn333+vli1b6pFHHtEtt9xidxwAdRgjOwD8wieffKIvvvhCl112mYqKivTggw9KkoYOHWpzMgB1HWUHgN/4y1/+ol27dik4OFjdu3fXBx98oAsuuMDuWADqOKaxAACAo3G5CAAA4GiUHQAA4GiUHQAA4GiUHQAA4GiUHQAA4GiUHQAA4GiUHQAA4GiUHQAA4Gj/H/i7VUGbMEjTAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(x='gender',y='emp_test_percentage',data=job,hue='status_',palette='viridis')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "bd3a55c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x217eadb47c0>"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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6U/L1hYiIqoePL5O7eWXX5YAJv1s2LChLO0hqiZCyoyJJERERERERETkGiZSIyIiIiIiIioSBt1EVDTTZUp961vfWu7mERERVSUeX4mqC4eXE1HRDA4OYnBwMOd9dXV1zJJKRERUAB5fiaoLg24iIiIiIiKiIuHwciIiIiIiIqIiYdBNREREREREVCQ1H3RLKREOh8FR9ERERO7h8ZWIiCg/NR90j4yMoKGhASMjI+VuChERUc3g8ZWIiCg/NR90ExEREREREZULg24iIiIiIiKiImHQTURERERERFQkDLqJiIiIiIiIioRBNxEREREREVGRMOgmIiIiIiIiKhIG3URERERERERFwqCbiIiIiIiIqEgYdBMREREREREVCYNuIiIiIiIioiJh0E1ERERERERUJAy6iYiIiIiIiIqEQTcRERERERFRkXjK3QAiIiIimj3Hkdh1JIzBaBxNfi9Wd4SgKKLczSIiogkYdBMRERFVmR09A9i6vRe9/RGYtoSmCnS2BLBpQyfWdzWXu3lERJSBw8uJiIiIqsiOngFs3taN3UfDqNc9aAnqqNc92H10BJu3dWNHz0C5m0hERBkYdBMRERFVCceR2Lq9FxHDQlvIB5+mQlEEfJqKtpCOiGFj6/ZeOI4sd1OJiCiJQTcRERFRldh1JIze/ggW+L0QInv+thACjX4Nvf0R7DoSLlMLiYhoIgbdRERERFViMBqHaUt41dyncLqqwHQkBqPxEreMiIimwqCbiIiIqEo0+b3QVIG47eS837AdaIpAk99b4pYREdFUGHQTERERVYnVHSF0tgQwFDUhZfa8bSklTkZNdLYEsLojVKYWEhHRRAy6iYiIiKqEoghs2tCJgK6iL2xgzLThOBJjpo2+sIGArmLThk7W6yYiqiBlD7pHRkZw3XXXYdmyZairq8P69evx1FNPpe+XUuKLX/wiOjo6UFdXh/PPPx+7du0qY4uJiIiIymd9VzO2XLoGq9qDiBoW+iMGooaFVe1BbLl0Det0ExFVGE+5G/CRj3wEf/nLX/D9738fHR0d+MEPfoC3vOUtePHFF7F48WLccccduPPOO3Hfffdh5cqVuPXWW3HhhRdiz549CAaD5W4+ERERUcmt72rGecsXYteRMAajcTT5vVjdEWIPNxFRBRJy4oSgEhobG0MwGMTPfvYzvO1tb0vf/prXvAb/43/8D3z5y19GR0cHrrvuOtx4440AAMMw0Nraittvvx1XX331jO8RDofR0NCA4eFhhEKc30REROQGHl+JiIjyU9bh5ZZlwbZt+Hy+rNvr6urwxBNP4OWXX0ZfXx8uuuii9H26rmPDhg3YsWNHqZtLRERERERENCtlHV4eDAbx+te/Hl/+8pexatUqtLa24j//8z/x5JNPYsWKFejr6wMAtLa2Zj2vtbUV+/fvz/mahmHAMIz0/+FwuHgLQERENE/w+EpERFSYsidS+/73vw8pJRYvXgxd1/Ev//Iv2LhxI1RVTT9GiOz5SVLKSbelfOUrX0FDQ0P6Z8mSJUVtPxER0XzA4ysREVFhyh50d3Z2Yvv27YhEIjh48CB27twJ0zRx2mmnoa2tDQDSPd4p/f39k3q/U2666SYMDw+nfw4ePFj0ZSAiIqp1PL4SEREVpuxBd0p9fT3a29sxNDSEhx9+GJdcckk68H700UfTj4vH49i+fTvWr1+f83V0XUcoFMr6ISIiornh8ZWIiKgwZS8Z9vDDD0NKidNPPx09PT341Kc+hdNPPx1XXXUVhBC47rrrsGXLFqxYsQIrVqzAli1b4Pf7sXHjxnI3nYiIiIiIiGhaZQ+6h4eHcdNNN+HQoUNoamrCZZddhttuuw2apgEAPv3pT2NsbAzXXHMNhoaGcO655+KRRx5hjW4iIiIiIiKqeGWt010KrCNKRETkPh5fiYiI8lMxc7qJiIiIiIiIag2DbiIiIiIiIqIiYdBNREREREREVCQMuomIiIiIiIiKhEE3ERERERERUZEw6CYiIiIiIiIqEgbdREREREREREXCoJuIiIiIiIioSBh0ExERERERERUJg24iIiIiIiKiImHQTURERERERFQkDLqJiIiIiIiIioRBNxEREREREVGRMOgmIiIiIiIiKhIG3URERERERERFwqCbiIiIiIiIqEgYdBMREREREREVCYNuIiIiIiIioiJh0E1ERERERERUJAy6iYiIiIiIiIqEQTcRERERERFRkTDoJiIiIiIiIioSBt1ERERERERERcKgm4iIiIiIiKhIGHQTERERERERFQmDbiIiIiIiIqIiYdBNREREREREVCQMuomIiIiIiIiKhEE3ERERERERUZEw6CYiIiIiIiIqEgbdREREREREREXCoJuIiIiIiIioSBh0ExERERERERUJ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OphOEUKg0a/hpb4R7OkbmfYxvf0R7DoSLmXTyQUMuomIiIiIiIpoMBqHaUt41dzhl64qMG2JuO1M/xhHYjAaL2ZTqQgYdBMRERERERVRk98LTRWI207O+w3bgaaK9BzuKR+jCDT5vcVsKhUBg24iIiIiIqIiWt0RQmdLAENRExPzWEspcTJq4oy2IE5vC077mM6WAFZ3MHlltWHQTUREREREVESKIrBpQycCuoq+sIEx04bjSIyZNvrCBgK6imvO78I150//mE0bOplErQqxZBgRERHNGo+vlclxJOvuElWwrBrcjoSmzFCne4rHUHUpa9BtWRa++MUv4oc//CH6+vrQ3t6OK6+8Ep/73OegKIlOeCklbrnlFtxzzz0YGhrCueeei7vuugurV6/O6z14UkBEROQ+Hl8rT9aJui2hqTxRJ6pE+Vwc4wW02lLWOt233347vvvd7+L+++/H6tWr8fTTT+Oqq65CQ0MDPv7xjwMA7rjjDtx555247777sHLlStx666248MILsWfPHgSDwXI2n4iIiKgi7OgZwOZt3YgYFhb4velkTLuPjmDztm5suXQNA2+iCqEoAmtOaZjzY6h6lHVO9x//+EdccskleNvb3oZTTz0V7373u3HRRRfh6aefBpDo5f7Wt76Fz372s3jXu96FV73qVbj//vsRjUbxwAMPlLPpRERERBXBcSS2bu9FxLDQFvLBp6lQFAGfpqItpCNi2Ni6vReOU9MzComIKlZZg+6/+Zu/wW9+8xvs3bsXAPD888/jiSeewN///d8DAF5++WX09fXhoosuSj9H13Vs2LABO3bsyPmahmEgHA5n/RAREdHc8PhauXYdCaO3P4IFfi+EyB5+KoRAo19Db38Eu47wMyMiKoeyBt033ngj3v/+9+OMM86ApmlYu3YtrrvuOrz//e8HAPT19QEAWltbs57X2tqavm+ir3zlK2hoaEj/LFmypLgLQURENA/w+Fq5BqNxmLaEV819WqerCkxHYjAaL3HLiIgIKHPQ/V//9V/4wQ9+gAceeADPPPMM7r//fnz961/H/fffn/W4iVdtpZSTbku56aabMDw8nP45ePBg0dpPREQ0X/D4Wrma/F5oqkDcdnLeb9gONEWgye8tccuIiAgocyK1T33qU/jMZz6D973vfQCANWvWYP/+/fjKV76CD33oQ2hrawOAdGbz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rysVyGVikc/EIZeJRT4TK5n57PMTqQEAAAAAkCp80w0AAAAAQJLQdAMAAAAAkCQ03QAAAAAAJAlNdwcWL14sl8sV8yguLo6Om5kWL16s0tJS+f1+TZkyRbW1tSmMOP19+umn+uEPf6gBAwYoNzdXZ599tt5+++3oODmN38iRI9vtny6XS9dff70kctkVra2t+uUvf6lRo0bJ7/dr9OjRuv322+U4TnQd8tk1hw8f1vz58zVixAj5/X5VVlZq8+bN0XHyeWKvvfaaLrvsMpWWlsrlculPf/pTzHg8uQuHw/rJT36igQMHKi8vT//4j/+oTz75pAdfxclRXxOL2po41NbEor4mFrX11KVNbTW0s2jRIhs7dqzt378/+mhoaIiO33333VZQUGDPPvus1dTU2Pe//30rKSmxYDCYwqjT1+eff24jRoyw2bNn28aNG23v3r328ssv2+7du6PrkNP4NTQ0xOyba9asMUm2du1aMyOXXXHHHXfYgAED7IUXXrC9e/faf//3f1t+fr7dd9990XXIZ9f88z//s5111llWXV1tu3btskWLFlkgELBPPvnEzMjnyfz5z3+2hQsX2rPPPmuS7LnnnosZjyd3c+fOtSFDhtiaNWtsy5Yt9s1vftPGjx9vra2tPfxqOkZ9TRxqa2JRWxOL+ppY1NZTly61laa7A4sWLbLx48d3OOY4jhUXF9vdd98dXXb06FErLCy0Bx98sIci7F0WLFhg559//gnHyWn33HTTTVZWVmaO45DLLrrkkkvsmmuuiVk2Y8YM++EPf2hm7JtdFQqFzOPx2AsvvBCzfPz48bZw4ULy2QVf/sMgntwdPHjQvF6vPfXUU9F1Pv30U3O73bZy5coei/1kqK+JQ21NLmpr91BfE4famjiprK2cXn4Cu3btUmlpqUaNGqUrr7xSe/bskSTt3btX9fX1uuiii6Lr+nw+VVVVacOGDakKN6397//+r84991xdccUVGjRokCZMmKCHH344Ok5OT11zc7NWrFiha665Ri6Xi1x20fnnn69XXnlFO3fulCS98847Wr9+vb7zne9IYt/sqtbWVkUiEeXk5MQs9/v9Wr9+Pfnshnhy9/bbb6ulpSVmndLSUn31q19Nq/xSXxOD2po81Nbuo74mDrU1eXqyttJ0d2DixIl67LHHtGrVKj388MOqr69XZWWlDhw4oPr6eknS4MGDY35n8ODB0THE2rNnj5YtW6YzzjhDq1at0ty5c3XjjTfqsccekyRy2g1/+tOfdPDgQc2ePVsSueyqBQsWaObMmRozZoy8Xq8mTJig+fPna+bMmZLIZ1cVFBRo8uTJ+vWvf619+/YpEoloxYoV2rhxo/bv308+uyGe3NXX1ys7O1v9+/c/4TqpRn1NHGpr8lBbu4/6mjjU1uTpydqa1c1Y+6SLL744+u+KigpNnjxZZWVlevTRRzVp0iRJksvlivkdM2u3DMc4jqNzzz1XS5YskSRNmDBBtbW1WrZsmf7lX/4luh457br/+q//0sUXX6zS0tKY5eQyPk8//bRWrFihJ598UmPHjtW2bds0f/58lZaWatasWdH1yGf8Hn/8cV1zzTUaMmSIPB6PzjnnHF111VXasmVLdB3yeepOJXfplF/qa+JQW5OH2tp91NfEorYmV0/UVr7pjkNeXp4qKiq0a9eu6CyrXz6y0dDQ0O4oCY4pKSnRWWedFbOsvLxcH330kSSR01P04Ycf6uWXX9aPf/zj6DJy2TX//u//rp///Oe68sorVVFRoauvvlo333yz7rrrLknk81SUlZWpurpaTU1N+vjjj7Vp0ya1tLRo1KhR5LMb4sldcXGxmpub1djYeMJ10g319dRRW5OD2poY1NfEorYmR0/WVpruOITDYW3fvl0lJSXRnXvNmjXR8ebmZlVXV6uysjKFUaavr3/969qxY0fMsp07d2rEiBGSRE5P0fLlyzVo0CBdcskl0WXksmtCoZDc7tiPQY/HE72lCfk8dXl5eSopKVFjY6NWrVqlf/qnfyKf3RBP7r72ta/J6/XGrLN//3699957aZtf6uupo7YmB7U1MaivyUFtTawera2nMvNbX/fTn/7U1q1bZ3v27LE333zTLr30UisoKLAPPvjAzI5NLV9YWGh//OMfraamxmbOnMm0/CexadMmy8rKsjvvvNN27dplTzzxhOXm5tqKFSui65DTrolEIjZ8+HBbsGBBuzFyGb9Zs2bZkCFDorc0+eMf/2gDBw60n/3sZ9F1yGfXrFy50l566SXbs2ePrV692saPH2/nnXeeNTc3mxn5PJnDhw/b1q1bbevWrSbJli5dalu3brUPP/zQzOLL3dy5c23o0KH28ssv25YtW+xb3/pWWt0yjPqaONTWxKO2Jg71NbGoracuXWorTXcH2u7P5vV6rbS01GbMmGG1tbXRccdxbNGiRVZcXGw+n88uuOACq6mpSWHE6e/555+3r371q+bz+WzMmDH20EMPxYyT065ZtWqVSbIdO3a0GyOX8QsGg3bTTTfZ8OHDLScnx0aPHm0LFy60cDgcXYd8ds3TTz9to0ePtuzsbCsuLrbrr7/eDh48GB0nnye2du1ak9TuMWvWLDOLL3dHjhyxG264wYqKiszv99ull15qH330UQpeTceor4lFbU0samviUF8Ti9p66tKltrrMzLrxrTwAAAAAADgBrukGAAAAACBJaLoBAAAAAEgSmm4AAAAAAJKEphsAAAAAgCSh6QYAAAAAIElougEAAAAASBKabgAAAAAAkoSmGwAAAACAJKHpBgAAAAAgSWi6gV5u5MiRuu+++xK6zSlTpmj+/PkJ3WY6W7x4sc4+++xUhwEASCPU1+6jvgLH0HQDSFvNzc2pDgEAgD6H+gr0LJpuoAvMTL/5zW80evRo+f1+jR8/Xv/zP/8jSVq3bp1cLpdWrVqlCRMmyO/361vf+pYaGhr00ksvqby8XIFAQDNnzlQoFIpuc8qUKbrhhht0ww03qF+/fhowYIB++ctfysw6jWfKlCn68MMPdfPNN8vlcsnlckXHNmzYoAsuuEB+v1/Dhg3TjTfeqC+++CI6/oc//EFnnHGGcnJyNHjwYH3ve9+TJM2ePVvV1dW6//77o9v84IMPThpH22t/8cUXNX78eOXk5GjixImqqamJWa+zmEaOHKk77rhDs2fPVmFhoa699lpJ0htvvKGqqirl5uaqf//+mjZtmhobGzt9T46P7ZVXXtG5556r3NxcVVZWaseOHZKkRx55RLfddpveeeed6Ot95JFHJElLly5VRUWF8vLyNGzYMF133XVqamqKeU0PP/ywhg0bptzcXE2fPl1Lly5Vv379YtZ5/vnn9bWvfU05OTkaPXq0brvtNrW2tp40pwCQSaivHaO+Ul/RRxiAuN166602ZswYW7lypdXV1dny5cvN5/PZunXrbO3atSbJJk2aZOvXr7ctW7bY6aefblVVVXbRRRfZli1b7LXXXrMBAwbY3XffHd1mVVWV5efn20033WR/+ctfbMWKFZabm2sPPfRQp/EcOHDAhg4darfffrvt37/f9u/fb2Zm7777ruXn59u9995rO3futDfeeMMm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\n",
      "text/plain": [
       "<Figure size 1000x500 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lmplot(x='emp_test_percentage',y='degree_percentage',data=job,col='status_')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "43fe7fd9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x217ec6657c0>"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAHqCAYAAAAZLi26AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAC5/klEQVR4nOzdeXwb9Z0//tfMaHRZh6/4yh2bkBDCtTRAKISyhB58e1C2pYSlhbZ8aeC3LYW2FHoBhVCgpXy7Cyl0d7kKu9uWpl3YtkAPAjRbEkoAN4SEOJDLcRzHtmRZ12jm8/tjJFmy5ViWdev1bP1wkGTpI81oPvOez+fzfktCCAEiIiIiIiIiyju51A0gIiIiIiIiqlYMuomIiIiIiIgKhEE3ERERERERUYEw6CYiIiIiIiIqEAbdRERERERERAXCoJuIiIiIiIioQBh0ExERERERERUIg24iIiIiIiKiAmHQTURERERERFQgDLqJysS7774LSZLw2muvlbopeffwww+jvr6+1M0gIqIaw76ViMoBg24iKriLL74YO3fuLHUzSu7JJ5/EcccdB5vNhuOOOw4bNmwodZOIiKhCsW8Ftm3bhosuuggLFiyAJEm49957S90koowYdBOVgWg0WuomFIymaXA4HGhpaSl1U0rqf//3f3HxxRfjsssuw+uvv47LLrsMn/zkJ/Hyyy+XumlERFWJfWv1CwaDWLRoEb73ve+hra2t1M0hmhSDbqIpPPXUU6ivr4dhGACA1157DZIk4atf/WryMVdddRUuueSS5H8/+eSTWLZsGWw2GxYsWIAf/OAHac+5YMEC3Hbbbbj88svh9Xpx5ZVXTnhdwzBw5ZVXYvHixdizZ8+U7fT5fPi///f/oqWlBR6PB+eeey5ef/11AMDhw4fR1taGdevWJR//8ssvw2q14tlnnwUA3HzzzTjppJPwwAMPYO7cuXA6nfjEJz6B4eHhtNd56KGHsHTpUtjtdixZsgT3339/8r7ENL6f/exnOOecc2C32/HTn/404xS4p556Cn/3d38Hu92ORYsW4ZZbbkEsFkveL0kS/vVf/xUXXnghnE4njjnmGPz3f/932nNs27YNF1xwATweD9xuN8466yz09PRk1dZiu/fee7F69WrceOONWLJkCW688Ub8/d//Pa/KE1FNYt86nPY67Ftz8573vAd33303PvWpT8Fms5WsHURTEkR0VMPDw0KWZfHKK68IIYS49957RXNzs3jPe96TfMzixYvF+vXrhRBCvPLKK0KWZXHrrbeKHTt2iIceekg4HA7x0EMPJR8/f/584fF4xN133y3efvtt8fbbb4t33nlHABBbt24VkUhEXHTRReKkk04Shw4dmrKNhmGIM888U3z4wx8WW7ZsETt37hTXX3+9aGpqEkeOHBFCCPE///M/QlVVsWXLFjEyMiK6urrEl770peRzfOc73xF1dXXi3HPPFVu3bhUbN24UXV1dYs2aNcnHPPjgg6K9vV08+eSTYvfu3eLJJ58UjY2N4uGHHxZCiOR7WLBgQfIxBw4cEA899JDwer3J5/nd734nPB6PePjhh0VPT4949tlnxYIFC8TNN9+cfAwAMWfOHPHEE0+It99+W3zxi18ULpcr+X72798vGhsbxcc//nGxZcsWsWPHDvHv//7v4q233sqqrdN1++23i7q6uqP+vPDCC5P+/dy5c8U999yTdts999wj5s2bl1N7iIgqGftW9q1CzLxvTTV//nzxwx/+MKd2EBUag26iLJxyyini+9//vhBCiI997GPi9ttvF1arVfj9fnHw4EEBQGzfvl0IIcSaNWvE6tWr0/7+q1/9qjjuuOOS/z1//nzxsY99LO0xiU71xRdfFOedd54488wzxfDwcFbt+8Mf/iA8Ho8Ih8Npt3d2dooHHngg+d9XX321WLx4sbj00kvF8ccfL0KhUPK+73znO0JRFLFv377kbb/97W+FLMvi4MGDQggzcHziiSfSXuO73/2uOOOMM9Lew7333pv2mPEnBmeddZZYt25d2mMee+wx0d7envxvAOKb3/xm8r8DgYCQJEn89re/FUIIceONN4qFCxeKaDSa8TOZqq3TdeTIkeRJ3GQ/wWBw0r9XVVU8/vjjabc9/vjjwmq15tQeIqJKx76VfetM+9ZUDLqpnFlKMbpOVGnOOeccPP/887juuuvw4osv4rbbbsOTTz6Jl156CcPDw2htbcWSJUsAANu3b8dHP/rRtL8/88wzce+990LXdSiKAgA49dRTM77WJZdcgjlz5uAPf/gDnE5nVu3761//ikAggKamprTbQ6FQ2pSw73//+zj++OPxs5/9DK+88grsdnva4+fNm4c5c+Yk//uMM86AYRjYsWMHFEXBvn378LnPfS5tyl4sFoPX6017nsneW2p7t2zZgttvvz15m67rCIfDCAaDyfd9wgknJO+vq6uD2+1Gf38/AHMq4llnnQVVVSc8/+HDh7Nua7YaGxvR2NiY098mSJKU9t9CiAm3ERHVCvat7Fvz0bcSVQIG3URZOOecc/Bv//ZveP311yHLMo477jisWrUKGzduxNDQEFatWpV8bKZASggx4Tnr6uoyvtaHPvQh/PSnP8Vf/vIXnHvuuVm1zzAMtLe34/nnn59wX+p6r927d6O3txeGYWDPnj1pHW8mifchSVJy3d1PfvITnHbaaWmPS5zsJEz23lLbe8stt+DjH//4hPtST1bGd/qp7XA4HEd9/mzbmq1169alrdvL5Le//S3OOuusjPe1tbWhr68v7bb+/n60trbm1B4iokrHvpV960z7VqJKwaCbKAtnn302RkZGcO+992LVqlWQJAmrVq3CHXfcgaGhIXzpS19KPva4447DSy+9lPb3mzZtwuLFi7PqlNauXYvjjz8eH/nIR/A///M/aScdkznllFPQ19cHi8WCBQsWZHxMNBrFpZdeiosvvhhLlizB5z73OXR3d6cFfXv37kVvby86OjoAmBm3ZVnG4sWL0draitmzZ2P37t249NJLp2zTVO3dsWMHurq6cn6OE044AY888gg0TZtwApHPtiZ84QtfwCc/+cmjPmb27NmT3nfGGWfgueeew5e//OXkbc8++yxWrlyZl/YREVUa9q3sW2fatxJVjJJObieqIKeccopQFEX8y7/8ixBCiMHBQaGqqgAgtm3blnzcX//617RkLw8//HDGZC/j1x2lJnsRQogf/vCHwuVyiRdffHHKthmGId773veKE088Ufzud78T77zzjvjzn/8svvGNb4gtW7YIIYT4yle+IhYsWCB8Pp/QdV2cffbZ4oILLkg+RyLZy3nnnSdee+018cILL4jFixeLT33qU8nH/OQnPxEOh0Pce++9YseOHeKNN94Q//7v/y5+8IMfZHwPCZmSvVgsFvGd73xH/O1vfxNvvvmm+M///E/xjW98I/kYAGLDhg1pz+P1epOf48DAgGhqakome9m5c6d49NFHk8lepmprsf35z38WiqKI733ve2L79u3ie9/7nrBYLOIvf/lLSdpDRFQO2Leyb52JSCQitm7dKrZu3Sra29vFV77yFbF161bx9ttvl6Q9RJNh0E2Upeuvv14AEH/729+St5144oli1qxZwjCMtMf+4he/EMcdd5xQVVXMmzdP3H333Wn3Z3NiIIQQP/jBD4Tb7RZ//vOfp2yf3+8X//RP/yQ6OjqEqqpi7ty54tJLLxV79+4Vf/rTn4TFYkk7ydizZ4/wer3i/vvvF0KYJwYnnniiuP/++0VHR4ew2+3i4x//uBgcHEx7nccff1ycdNJJwmq1ioaGBnH22WeLX/7yl5O+ByEmnhgIYZ4crFy5UjgcDuHxeMSKFSvEgw8+mLx/qhMDIYR4/fXXxfnnny+cTqdwu93irLPOEj09PVm1tRR+/vOfi2OPPVaoqiqWLFkinnzyyZK1hYioHLBvNbFvzU3isxn/s2rVqpK0h2gykhAZFsQQUc25+eab8atf/QqvvfZaqZtCRERUFdi3EhEAyKVuABEREREREVG1YtBNVAEef/xxuFyujD/Lli0rdfMqzrp16yb9PD/4wQ+WunlERFQE7Fvzi30r0eQ4vZyoAoyMjODQoUMZ71NVFfPnzy9yiyrb4OAgBgcHM97ncDiYKZWIqAawb80v9q1Ek2PQTURERERERFQgnF5OREREREREVCAMuomIiIiIiIgKpOqDbiEE/H4/OIueiIgof9i/EhERZafqg+6RkRF4vV6MjIyUuilERERVg/0rERFRdqo+6CYiIiIiIiIqFQbdRERERERERAXCoJuIiIiIiIioQBh0ExERERERERUIg24iIiIiIiKiAmHQTURERERERFQgDLqJiIiIiIiICoRBNxEREREREVGBMOgmIiIiIiIiKhAG3UREREREREQFwqCbiIiIiIiIqEAYdBMREREREREVCINuIiIiIiIiogKxlLoBVP0MQ2Bbrx+DwSganVYs6/BAlqVSN4uIiIiIiKjgGHRTQW3aNYD1G3vQ0x+ApguoioTOFhfWrurEyq7mUjePiIiIiIiooDi9nApm064B3LShG9sP+lFns6DFbUOdzYLtB0dw04ZubNo1UOomEhERERERFRSDbioIwxBYv7EHgUgMbR477KoCWZZgVxW0eWwIRHSs39gDwxClbioREREREVHBMOimgtjW60dPfwANTiskKX39tiRJqHeq6OkPYFuvv0QtJCIiIiIiKjwG3VQQg8EoNF3AqmTexWyKDM0QGAxGi9wyIiIiIiKi4mHQTQXR6LRCVSREdSPj/RHdgCpLaHRai9wyIiIiIiKi4mHQTQWxrMODzhYXhoIahEhfty2EwHBQQ2eLC8s6PCVqIRERERERUeEx6KaCkGUJa1d1wmVT0OePIKTpMAyBkKajzx+By6Zg7apO1usmIiIiIqKqVvKge2RkBNdeey3mz58Ph8OBlStXYsuWLcn7hRC4+eab0dHRAYfDgXPOOQfbtm0rYYspWyu7mrHuwuVY2u5GMBJDfyCCYCSGpe1urLtwOet0ExERERFR1bOUugGf//zn8be//Q2PPfYYOjo68NOf/hTnnXce3nzzTcyePRt33XUX7rnnHjz88MNYvHgxbrvtNqxevRo7duyA2+0udfNpCiu7mnH6oiZs6/VjMBhFo9OKZR0ejnATEREREVFNkMT4BbdFFAqF4Ha78etf/xoXXHBB8vaTTjoJ/+f//B9897vfRUdHB6699lrccMMNAIBIJILW1lbceeeduOqqq6Z8Db/fD6/XC5/PB4+H64eJiIjygf0rERFRdko6vTwWi0HXddjt9rTbHQ4HXnrpJbzzzjvo6+vD+eefn7zPZrNh1apV2LRpU7GbS0RERERERDQtJZ1e7na7ccYZZ+C73/0uli5ditbWVvzHf/wHXn75ZRxzzDHo6+sDALS2tqb9XWtrK/bs2ZPxOSORCCKRSPK//X5/4d4AERFRjWD/SkRElJuSJ1J77LHHIITA7NmzYbPZ8KMf/Qhr1qyBoijJx0hS+vpfIcSE2xLuuOMOeL3e5M/cuXML2n4iIqJawP6ViIgoNyUPujs7O7Fx40YEAgHs27cPmzdvhqZpWLhwIdra2gAgOeKd0N/fP2H0O+HGG2+Ez+dL/uzbt6/g74GIiKjasX8lIiLKTcmD7oS6ujq0t7djaGgIzzzzDD760Y8mA+/nnnsu+bhoNIqNGzdi5cqVGZ/HZrPB4/Gk/RAREdHMsH8lIiLKTclLhj3zzDMQQuDYY4/Frl278NWvfhXHHnssrrjiCkiShGuvvRbr1q3DMcccg2OOOQbr1q2D0+nEmjVrSt10IiIiIiIioqMqedDt8/lw4403Yv/+/WhsbMRFF12E22+/HaqqAgC+9rWvIRQK4eqrr8bQ0BBOO+00PPvss6zRTURERERERGWvpHW6i4F1RImIiPKP/SsREVF2ymZNNxEREREREVG1YdBNREREREREVCAMuomIiIiIiIgKhEE3ERERERERUYEw6CYiIiIiIiIqEAbdRERERERERAXCoJuIiIiIiIioQBh0ExERERERERUIg24iIiIiIiKiAmHQTURERERERFQgDLqJiIiIiIiICoRBNxEREREREVGBMOgmIiIiIiIiKhAG3UREREREREQFwqCbiIiIiIiIqEAYdBMREREREREVCINuIiIiIiIiogJh0E1ERERERERUIAy6iYiIiIiIiAqEQTcRERERERFRgTDoJiIiIiIiIioQBt1EREREREREBcKgm4iIiIiIiKhAGHQTERERERERFQiDbiIiIiIiIqICYdBNREREREREVCAMuomIiIiIiIgKhEE3ERERERERUYEw6CYiIiIiIiIqEAbdRERERERERAXCoJuIiIiIiIioQBh0ExERERERERUIg24iIiIiIiKiAmHQTURERERERFQgllI3gIiIqBwYhsC2Xj8Gg1E0Oq1Y1uGBLEulbhYRERFVOAbdRERU8zbtGsD6jT3o6Q9A0wVURUJniwtrV3ViZVdzqZtHREREFYzTy4mIqKZt2jWAmzZ0Y/tBP+psFrS4baizWbD94Ahu2tCNTbsGSt1EIiIiqmAMuomIqGYZhsD6jT0IRGJo89hhVxXIsgS7qqDNY0MgomP9xh4Yhih1U4mIiKhCMegmIqKata3Xj57+ABqcVkhS+vptSZJQ71TR0x/Atl5/iVpIRERElY5BNxER1azBYBSaLmBVMneHNkWGZggMBqNFbhkRERFVCwbdRERUsxqdVqiKhKhuZLw/ohtQZQmNTmuRW0ZERETVgkE3ERHVrGUdHnS2uDAU1CBE+rptIQSGgxo6W1xY1uEpUQuJiIio0jHoJiKimiXLEtau6oTLpqDPH0FI02EYAiFNR58/ApdNwdpVnazXTURERDlj0E1ERDVtZVcz1l24HEvb3QhGYugPRBCMxLC03Y11Fy7Pa51uwxDo3u/Dxp2H0b3fx6zoRERENcBS6gYQERGV2squZpy+qAnbev0YDEbR6LRiWYcnryPcm3YNYP3GHvT0B6DpAqoiobPFhbWrOvMa2BMREVF5kcT4RWxVxu/3w+v1wufzwePhmjwiIiq+TbsGcNOGbgQiMTQ4rbAqMqK6gaGgBpdNyfuIejGwfyUiIsoOp5cTEREVkGEIrN/Yg0AkhjaPHXZVgSxLsKsK2jw2BCI61m/s4VRzIiKi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\n",
      "text/plain": [
       "<Figure size 1000x500 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lmplot(x='emp_test_percentage',y='degree_percentage',data=job,col='work_experience_')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "124958c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['gender', 'ssc_percentage', 'ssc_board', 'hsc_percentage', 'hsc_board',\n",
       "       'hsc_subject', 'degree_percentage', 'undergrad_degree',\n",
       "       'emp_test_percentage', 'specialisation', 'mba_percent', 'status_',\n",
       "       'work_experience_'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "job.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "40e2922d",
   "metadata": {},
   "outputs": [],
   "source": [
    "job.drop(['ssc_board','hsc_board',],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "71a4fc67",
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
       "      <th>gender</th>\n",
       "      <th>ssc_percentage</th>\n",
       "      <th>hsc_percentage</th>\n",
       "      <th>hsc_subject</th>\n",
       "      <th>degree_percentage</th>\n",
       "      <th>undergrad_degree</th>\n",
       "      <th>emp_test_percentage</th>\n",
       "      <th>specialisation</th>\n",
       "      <th>mba_percent</th>\n",
       "      <th>status_</th>\n",
       "      <th>work_experience_</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M</td>\n",
       "      <td>67.00</td>\n",
       "      <td>91.00</td>\n",
       "      <td>Commerce</td>\n",
       "      <td>58.00</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>55.0</td>\n",
       "      <td>Mkt&amp;HR</td>\n",
       "      <td>58.80</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>79.33</td>\n",
       "      <td>78.33</td>\n",
       "      <td>Science</td>\n",
       "      <td>77.48</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>86.5</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>66.28</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>M</td>\n",
       "      <td>65.00</td>\n",
       "      <td>68.00</td>\n",
       "      <td>Arts</td>\n",
       "      <td>64.00</td>\n",
       "      <td>Comm&amp;Mgmt</td>\n",
       "      <td>75.0</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>57.80</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M</td>\n",
       "      <td>56.00</td>\n",
       "      <td>52.00</td>\n",
       "      <td>Science</td>\n",
       "      <td>52.00</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>66.0</td>\n",
       "      <td>Mkt&amp;HR</td>\n",
       "      <td>59.43</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>M</td>\n",
       "      <td>85.80</td>\n",
       "      <td>73.60</td>\n",
       "      <td>Commerce</td>\n",
       "      <td>73.30</td>\n",
       "      <td>Comm&amp;Mgmt</td>\n",
       "      <td>96.8</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>55.50</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gender  ssc_percentage  hsc_percentage hsc_subject  degree_percentage  \\\n",
       "0      M           67.00           91.00    Commerce              58.00   \n",
       "1      M           79.33           78.33     Science              77.48   \n",
       "2      M           65.00           68.00        Arts              64.00   \n",
       "3      M           56.00           52.00     Science              52.00   \n",
       "4      M           85.80           73.60    Commerce              73.30   \n",
       "\n",
       "  undergrad_degree  emp_test_percentage specialisation  mba_percent  status_  \\\n",
       "0         Sci&Tech                 55.0         Mkt&HR        58.80        1   \n",
       "1         Sci&Tech                 86.5        Mkt&Fin        66.28        1   \n",
       "2        Comm&Mgmt                 75.0        Mkt&Fin        57.80        1   \n",
       "3         Sci&Tech                 66.0         Mkt&HR        59.43        0   \n",
       "4        Comm&Mgmt                 96.8        Mkt&Fin        55.50        1   \n",
       "\n",
       "   work_experience_  \n",
       "0                 0  \n",
       "1                 1  \n",
       "2                 0  \n",
       "3                 0  \n",
       "4                 0  "
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "job.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "6c38223d",
   "metadata": {},
   "outputs": [],
   "source": [
    "gender_=pd.get_dummies(job['gender'],drop_first=True)\n",
    "hsc_subject_=pd.get_dummies(job['hsc_subject'],drop_first=True)\n",
    "undergrad_degree_=pd.get_dummies(job['undergrad_degree'],drop_first=True)\n",
    "specialisation_=pd.get_dummies(job['specialisation'],drop_first=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "16985a71",
   "metadata": {},
   "outputs": [],
   "source": [
    "job=pd.concat([job,gender_,hsc_subject_,undergrad_degree_,specialisation_],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "e1cc2b14",
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
       "      <th>gender</th>\n",
       "      <th>ssc_percentage</th>\n",
       "      <th>hsc_percentage</th>\n",
       "      <th>hsc_subject</th>\n",
       "      <th>degree_percentage</th>\n",
       "      <th>undergrad_degree</th>\n",
       "      <th>emp_test_percentage</th>\n",
       "      <th>specialisation</th>\n",
       "      <th>mba_percent</th>\n",
       "      <th>status_</th>\n",
       "      <th>work_experience_</th>\n",
       "      <th>M</th>\n",
       "      <th>Commerce</th>\n",
       "      <th>Science</th>\n",
       "      <th>Others</th>\n",
       "      <th>Sci&amp;Tech</th>\n",
       "      <th>Mkt&amp;HR</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M</td>\n",
       "      <td>67.00</td>\n",
       "      <td>91.00</td>\n",
       "      <td>Commerce</td>\n",
       "      <td>58.00</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>55.0</td>\n",
       "      <td>Mkt&amp;HR</td>\n",
       "      <td>58.80</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>79.33</td>\n",
       "      <td>78.33</td>\n",
       "      <td>Science</td>\n",
       "      <td>77.48</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>86.5</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>66.28</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>M</td>\n",
       "      <td>65.00</td>\n",
       "      <td>68.00</td>\n",
       "      <td>Arts</td>\n",
       "      <td>64.00</td>\n",
       "      <td>Comm&amp;Mgmt</td>\n",
       "      <td>75.0</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>57.80</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M</td>\n",
       "      <td>56.00</td>\n",
       "      <td>52.00</td>\n",
       "      <td>Science</td>\n",
       "      <td>52.00</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>66.0</td>\n",
       "      <td>Mkt&amp;HR</td>\n",
       "      <td>59.43</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>M</td>\n",
       "      <td>85.80</td>\n",
       "      <td>73.60</td>\n",
       "      <td>Commerce</td>\n",
       "      <td>73.30</td>\n",
       "      <td>Comm&amp;Mgmt</td>\n",
       "      <td>96.8</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>55.50</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gender  ssc_percentage  hsc_percentage hsc_subject  degree_percentage  \\\n",
       "0      M           67.00           91.00    Commerce              58.00   \n",
       "1      M           79.33           78.33     Science              77.48   \n",
       "2      M           65.00           68.00        Arts              64.00   \n",
       "3      M           56.00           52.00     Science              52.00   \n",
       "4      M           85.80           73.60    Commerce              73.30   \n",
       "\n",
       "  undergrad_degree  emp_test_percentage specialisation  mba_percent  status_  \\\n",
       "0         Sci&Tech                 55.0         Mkt&HR        58.80        1   \n",
       "1         Sci&Tech                 86.5        Mkt&Fin        66.28        1   \n",
       "2        Comm&Mgmt                 75.0        Mkt&Fin        57.80        1   \n",
       "3         Sci&Tech                 66.0         Mkt&HR        59.43        0   \n",
       "4        Comm&Mgmt                 96.8        Mkt&Fin        55.50        1   \n",
       "\n",
       "   work_experience_  M  Commerce  Science  Others  Sci&Tech  Mkt&HR  \n",
       "0                 0  1         1        0       0         1       1  \n",
       "1                 1  1         0        1       0         1       0  \n",
       "2                 0  1         0        0       0         0       0  \n",
       "3                 0  1         0        1       0         1       1  \n",
       "4                 0  1         1        0       0         0       0  "
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "job.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "16e972e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "job = job.rename(columns={'M': 'gender_', 'Science': 'hsc_subject_','Commerce': 'hsc_subject_','Others': 'hsc_subject_','Sci&Tech':'undergrad_degree_','Mkt&HR':'specialisation_'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "b3be61f7",
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
       "      <th>gender</th>\n",
       "      <th>ssc_percentage</th>\n",
       "      <th>hsc_percentage</th>\n",
       "      <th>hsc_subject</th>\n",
       "      <th>degree_percentage</th>\n",
       "      <th>undergrad_degree</th>\n",
       "      <th>emp_test_percentage</th>\n",
       "      <th>specialisation</th>\n",
       "      <th>mba_percent</th>\n",
       "      <th>status_</th>\n",
       "      <th>work_experience_</th>\n",
       "      <th>gender_</th>\n",
       "      <th>hsc_subject_</th>\n",
       "      <th>hsc_subject_</th>\n",
       "      <th>hsc_subject_</th>\n",
       "      <th>undergrad_degree_</th>\n",
       "      <th>specialisation_</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M</td>\n",
       "      <td>67.00</td>\n",
       "      <td>91.00</td>\n",
       "      <td>Commerce</td>\n",
       "      <td>58.00</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>55.0</td>\n",
       "      <td>Mkt&amp;HR</td>\n",
       "      <td>58.80</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>79.33</td>\n",
       "      <td>78.33</td>\n",
       "      <td>Science</td>\n",
       "      <td>77.48</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>86.5</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>66.28</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>M</td>\n",
       "      <td>65.00</td>\n",
       "      <td>68.00</td>\n",
       "      <td>Arts</td>\n",
       "      <td>64.00</td>\n",
       "      <td>Comm&amp;Mgmt</td>\n",
       "      <td>75.0</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>57.80</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M</td>\n",
       "      <td>56.00</td>\n",
       "      <td>52.00</td>\n",
       "      <td>Science</td>\n",
       "      <td>52.00</td>\n",
       "      <td>Sci&amp;Tech</td>\n",
       "      <td>66.0</td>\n",
       "      <td>Mkt&amp;HR</td>\n",
       "      <td>59.43</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>M</td>\n",
       "      <td>85.80</td>\n",
       "      <td>73.60</td>\n",
       "      <td>Commerce</td>\n",
       "      <td>73.30</td>\n",
       "      <td>Comm&amp;Mgmt</td>\n",
       "      <td>96.8</td>\n",
       "      <td>Mkt&amp;Fin</td>\n",
       "      <td>55.50</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gender  ssc_percentage  hsc_percentage hsc_subject  degree_percentage  \\\n",
       "0      M           67.00           91.00    Commerce              58.00   \n",
       "1      M           79.33           78.33     Science              77.48   \n",
       "2      M           65.00           68.00        Arts              64.00   \n",
       "3      M           56.00           52.00     Science              52.00   \n",
       "4      M           85.80           73.60    Commerce              73.30   \n",
       "\n",
       "  undergrad_degree  emp_test_percentage specialisation  mba_percent  status_  \\\n",
       "0         Sci&Tech                 55.0         Mkt&HR        58.80        1   \n",
       "1         Sci&Tech                 86.5        Mkt&Fin        66.28        1   \n",
       "2        Comm&Mgmt                 75.0        Mkt&Fin        57.80        1   \n",
       "3         Sci&Tech                 66.0         Mkt&HR        59.43        0   \n",
       "4        Comm&Mgmt                 96.8        Mkt&Fin        55.50        1   \n",
       "\n",
       "   work_experience_  gender_  hsc_subject_  hsc_subject_  hsc_subject_  \\\n",
       "0                 0        1             1             0             0   \n",
       "1                 1        1             0             1             0   \n",
       "2                 0        1             0             0             0   \n",
       "3                 0        1             0             1             0   \n",
       "4                 0        1             1             0             0   \n",
       "\n",
       "   undergrad_degree_  specialisation_  \n",
       "0                  1                1  \n",
       "1                  1                0  \n",
       "2                  0                0  \n",
       "3                  1                1  \n",
       "4                  0                0  "
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "job.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "d28dee99",
   "metadata": {},
   "outputs": [],
   "source": [
    "job.drop('hsc_subject_',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "50852155",
   "metadata": {},
   "outputs": [],
   "source": [
    "job.drop(['hsc_subject','undergrad_degree','gender','specialisation'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "ad773523",
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
       "      <th>ssc_percentage</th>\n",
       "      <th>hsc_percentage</th>\n",
       "      <th>degree_percentage</th>\n",
       "      <th>emp_test_percentage</th>\n",
       "      <th>mba_percent</th>\n",
       "      <th>status_</th>\n",
       "      <th>work_experience_</th>\n",
       "      <th>gender_</th>\n",
       "      <th>undergrad_degree_</th>\n",
       "      <th>specialisation_</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>67.00</td>\n",
       "      <td>91.00</td>\n",
       "      <td>58.00</td>\n",
       "      <td>55.0</td>\n",
       "      <td>58.80</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>79.33</td>\n",
       "      <td>78.33</td>\n",
       "      <td>77.48</td>\n",
       "      <td>86.5</td>\n",
       "      <td>66.28</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>65.00</td>\n",
       "      <td>68.00</td>\n",
       "      <td>64.00</td>\n",
       "      <td>75.0</td>\n",
       "      <td>57.80</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>56.00</td>\n",
       "      <td>52.00</td>\n",
       "      <td>52.00</td>\n",
       "      <td>66.0</td>\n",
       "      <td>59.43</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>85.80</td>\n",
       "      <td>73.60</td>\n",
       "      <td>73.30</td>\n",
       "      <td>96.8</td>\n",
       "      <td>55.50</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ssc_percentage  hsc_percentage  degree_percentage  emp_test_percentage  \\\n",
       "0           67.00           91.00              58.00                 55.0   \n",
       "1           79.33           78.33              77.48                 86.5   \n",
       "2           65.00           68.00              64.00                 75.0   \n",
       "3           56.00           52.00              52.00                 66.0   \n",
       "4           85.80           73.60              73.30                 96.8   \n",
       "\n",
       "   mba_percent  status_  work_experience_  gender_  undergrad_degree_  \\\n",
       "0        58.80        1                 0        1                  1   \n",
       "1        66.28        1                 1        1                  1   \n",
       "2        57.80        1                 0        1                  0   \n",
       "3        59.43        0                 0        1                  1   \n",
       "4        55.50        1                 0        1                  0   \n",
       "\n",
       "   specialisation_  \n",
       "0                1  \n",
       "1                0  \n",
       "2                0  \n",
       "3                1  \n",
       "4                0  "
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "job.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "4457b0e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x217ea05f790>"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 2310.74x2250 with 90 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(job,hue='status_')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "21432fc4",
   "metadata": {},
   "outputs": [],
   "source": [
    "X=job.drop('status_',axis=1)\n",
    "y=job['status_']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "97ad7594",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "7808cb3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "f3d22c90",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.svm import SVC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "8cfce695",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=SVC()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "4e112af8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SVC()"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "af9cc59f",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred=model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "6e47da87",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import classification_report,confusion_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "9d56b1fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[13  7]\n",
      " [ 0 45]]\n",
      "\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       1.00      0.65      0.79        20\n",
      "           1       0.87      1.00      0.93        45\n",
      "\n",
      "    accuracy                           0.89        65\n",
      "   macro avg       0.93      0.82      0.86        65\n",
      "weighted avg       0.91      0.89      0.88        65\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(confusion_matrix(y_test,pred))\n",
    "print('\\n')\n",
    "print(classification_report(y_test,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "79eb68bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "52b88f2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "knn=KNeighborsClassifier(n_neighbors=5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "f08989e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier()"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "de23bda3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\anaconda3\\lib\\site-packages\\sklearn\\neighbors\\_classification.py:228: FutureWarning: Unlike other reduction functions (e.g. `skew`, `kurtosis`), the default behavior of `mode` typically preserves the axis it acts along. In SciPy 1.11.0, this behavior will change: the default value of `keepdims` will become False, the `axis` over which the statistic is taken will be eliminated, and the value None will no longer be accepted. Set `keepdims` to True or False to avoid this warning.\n",
      "  mode, _ = stats.mode(_y[neigh_ind, k], axis=1)\n"
     ]
    }
   ],
   "source": [
    "predict=knn.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "cc96183f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[16  4]\n",
      " [ 1 44]]\n",
      "\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.94      0.80      0.86        20\n",
      "           1       0.92      0.98      0.95        45\n",
      "\n",
      "    accuracy                           0.92        65\n",
      "   macro avg       0.93      0.89      0.91        65\n",
      "weighted avg       0.92      0.92      0.92        65\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(confusion_matrix(y_test,predict))\n",
    "print('\\n')\n",
    "print(classification_report(y_test,predict))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99d96225",
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