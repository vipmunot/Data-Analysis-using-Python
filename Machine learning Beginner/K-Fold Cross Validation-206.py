## 2. Partititioning the data ##

import pandas as pd

admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)

shuffled_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[shuffled_index]
admissions = shuffled_admissions.reset_index()
admissions.ix[0:128, "fold"] = 1
admissions.ix[129:257, "fold"] = 2
admissions.ix[258:386, "fold"] = 3
admissions.ix[387:514, "fold"] = 4
admissions.ix[515:644, "fold"] = 5
# Ensure the column is set to integer type.
admissions["fold"] = admissions["fold"].astype('int')

print(admissions.head())
print(admissions.tail())

## 3. First iteration ##

from sklearn.linear_model import LogisticRegression
train = admissions[admissions['fold']!=1]
test = admissions[admissions['fold']==1]
lr = LogisticRegression()
lr.fit(train[['gpa']],train['actual_label'])
labels = lr.predict(test[['gpa']])
iteration_one_accuracy = len(test[test['actual_label']==labels])/len(test)

## 4. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]
def train_and_test(data,fold):
    from sklearn.linear_model import LogisticRegression
    accuracy_list = []
    for item in fold:
        train = data[data['fold']!=item]
        test = data[data['fold']==item]
        lr = LogisticRegression()
        lr.fit(train[['gpa']],train['actual_label'])
        labels = lr.predict(test[['gpa']])
        accuracy = len(test[test['actual_label']==labels])/len(test)
        accuracy_list.append(accuracy)
    return accuracy_list
accuracies = train_and_test(admissions, [1,2,3,4,5])
average_accuracy = sum(accuracies)/len(accuracies)
print('All Fold Accuracies:',accuracies)
print('Average Accuracy: ',average_accuracy)

## 5. Sklearn ##

import numpy as np
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LogisticRegression
admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)
kf = KFold(n  = len(admissions), n_folds = 5,shuffle = True,random_state = 8)
lr = LogisticRegression()
accuracies = cross_val_score(estimator = lr,X = admissions[['gpa']],y = admissions['actual_label'],scoring = 'accuracy',cv = kf)
average_accuracy = np.mean(accuracies)
print(accuracies)
print(average_accuracy)