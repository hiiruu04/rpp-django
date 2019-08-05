from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import View
from django.core.files.storage import FileSystemStorage
from sklearn.model_selection import train_test_split

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# import os
import matplotlib.pyplot as plt
import seaborn as sns
import math
import collections
import time


def dataframe(file_dataset, separator):
    pd.set_option('colheader_justify', 'center')
    df = pd.DataFrame()
    if separator == 'koma':
        df = pd.read_csv(file_dataset, sep=',')
    elif separator == 'titik_koma':
        df = pd.read_csv(file_dataset, sep=';')
    elif separator == 'tab':
        df = pd.read_csv(file_dataset, sep='\t')
    elif separator == 'enter':
        df = pd.read_csv(file_dataset, sep='\n')

    return df


def cross_val_split(X, fold=2, seed=0):
    np.random.seed(seed)
    n_folds = fold
    size = X.shape[0]/n_folds
    X_idx = list(range(X.shape[0]))
    folds_data = []
    for i in range(n_folds):
        #         print(X_idx)
        random_idx = list(np.random.choice(X_idx, int(size), replace=False))
#         print(random_idx)
        X_idx = [idx for idx in X_idx if idx not in random_idx]
#         print(X_idx)

        folds_data.append(random_idx)
#         print("--")
    return folds_data

def confussion_matrik(actual,predict):
    TP,FP,FN,TN = 0,0,0,0
    for i,val in enumerate(actual):
        if val == 0:
            if val == predict[i]:
                TN += 1
            else:
                FP += 1
        if val == 1:
            if val == predict[i]:
                TP += 1
            else:
                FN += 1
    return TP,FP,FN,TN
 
def acc_sens_spec(actual,predict):
    TP,FP,FN,TN = confussion_matrik(actual,predict)
    accuracy,sensitivity,specifity = 0,0,0
    if (TP+FP+FN+TN) > 0 :
        accuracy = (TP+TN)/(TP+FP+FN+TN)
    if (TP+FN) > 0 :
        sensitivity = TP/(TP+FN)
    if (TN +FP) > 0 :
        specifity = TN/(TN +FP)
    
    return accuracy,sensitivity,specifity

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
    #how many correct predictions?
    correct = 0
    #for each actual label
    for i in range(len(actual)):
        #if actual matches predicted label
        if actual[i] == predicted[i]:
            #add 1 to the correct iterator
            correct += 1
    #return percentage of predictions that were correct
    return correct / float(len(actual)) * 100.0

def kfold_cross_validation(model, X, y, n_fold=2, n_seed=0):
    folds = cross_val_split(X, fold=n_fold, seed=n_seed)
    fold_result = []
    for i in range(len(folds)):
        #     print(i)
        train = []
        for j in range(len(folds)):
            if j != i:
                train = train + folds[j]
        test = folds[i]

        X_train = X.iloc[train, :].reset_index(drop=True)
        y_train = y[train].reset_index(drop=True)

        X_test = X.iloc[test, :].reset_index(drop=True)
        y_test = y[test].reset_index(drop=True)

        t0 = time.time()
        model.fit(X_train, y_train)
        t1 = time.time()
        waktu = t1 - t0

        predict = model.predict(X_test)
        accuracy, sensitivity, specifity = acc_sens_spec(y_test, predict)

        result = [accuracy, sensitivity, specifity, waktu]
        fold_result.append(result)

    return fold_result

def prec_rec_f1score(actual,predict):
    TP,FP,FN,TN = confussion_matrik(actual,predict)

    df_heatmap = pd.DataFrame([[TP,FN],[FP,TN]],['Aktual Fraud','Aktual Normal'],['Prediksi Fraud','Prediksi Normal'])
    plt.figure(figsize=(8,8))
    plot = sns.set(font_scale =1.4)
    plot = sns.heatmap(df_heatmap,annot=True, annot_kws={'size':16},fmt='g')

    figure = plot.get_figure() 
    figure.savefig("random_forest/static/random_forest/cm/cm.png")
    # figure.savefig("coba.png")


    accuracy,sensitivity,specifity = 0,0,0
# precision
    if (TP+FP) == 0 :
        precision = 0
    else :
        precision = TP/(TP+FP)

# recall
    if (TP+FN) == 0 :
        recall = 0
    else :
        recall = TP/(TP+FN)

# f1_score
    if (precision+recall) == 0 :
        f1_score = 0
    else :
        f1_score = 2*((precision*recall)/(precision+recall))

    
    return precision,recall,f1_score

def train_test_validation(model, X, y, prosentase=30, n_seed=0):
    end_result =[]
    prosentase_dec = prosentase / 100
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=prosentase_dec, random_state=n_seed,stratify=y)
    print(X_train.shape)
    print(X_test.shape)

    model.fit(X_train, y_train)
    predict = model.predict(X_test)

    precision, recall, f1_score = prec_rec_f1score(y_test, predict)

    result = [precision, recall, f1_score]
    end_result.append(result)

    return end_result
