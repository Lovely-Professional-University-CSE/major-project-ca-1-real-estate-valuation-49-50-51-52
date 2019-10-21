{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "accuracy score :  1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "F:\\anaconda\\lib\\site-packages\\sklearn\\utils\\validation.py:578: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "from sklearn import datasets\n",
    "import pandas as pd\n",
    "dataset = pd.read_csv('wine.csv')\n",
    "x = dataset.iloc[:,1:10]\n",
    "y = dataset.iloc[:,0:1]\n",
    "from sklearn.cross_validation import train_test_split\n",
    "x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 0)\n",
    "from sklearn.svm import SVC\n",
    "sm = SVC(kernel = 'linear', C=1 ,random_state = 0)\n",
    "sm.fit(x_train,y_train)\n",
    "y_pred = sm.predict(x_test)\n",
    "#print('misclassified samples %d'%(y_test!=y_pred).sum())\n",
    "from sklearn.metrics import accuracy_score\n",
    "print(\"accuracy score : %2.f\" % accuracy_score(y_pred,y_test))\n"
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
