from __future__ import absolute_import
from __future__ import division
from __future__ import print_function #enforces python 3 syntax
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.metric_spec import MetricSpec
import numpy as np
from sklearn import datasets, metrics, preprocessing
from sklearn.preprocessing import LabelBinarizer
from sklearn import svm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation
from timeit import Timer # measure time
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import precision_score
from pylab import savefig
import sys


class tfLinearClassifier:
    def __init__(self , model_dir , learningRate = 0.1 , l1Regularization = 0.001 ,optimization=None):
        """Tensor Flow Linear Classifier"""
        t_fit=0
        t_predict=0

    def fit(self , X_train,y_train , step = 2000):
        # Specify that all features have real-value data
        feature_columns = [tf.contrib.layers.real_valued_column("", dimension=X_train[0].shape[0])]
    
        #validation_metrics = {"accuracy": tf.contrib.metrics.streaming_accuracy}
        validation_metrics = {
            "accuracy" : MetricSpec(metric_fn=tf.contrib.metrics.streaming_accuracy,prediction_key="classes"),
            "precision" : MetricSpec(metric_fn=tf.contrib.metrics.streaming_precision,prediction_key="classes"),
            "recall" : MetricSpec(metric_fn=tf.contrib.metrics.streaming_recall,prediction_key="classes")}

        #instantiate a validaition monitor
        #validation_monitor = tf.contrib.learn.monitors.ValidationMonitor(X_test,y_test,every_n_steps=50)
        """
        validation_monitor = tf.contrib.learn.monitors.ValidationMonitor(
            X_test,
            y_test,
            every_n_steps=50,
            metrics=validation_metrics,
            early_stopping_metric="loss",
            early_stopping_metric_minimize=True,
            early_stopping_rounds=200)
        """

        # Linear Classifier
        self.classifier = tf.contrib.learn.LinearClassifier(feature_columns=feature_columns,
                                                       model_dir="data/linear",
                                                       config=tf.contrib.learn.RunConfig(save_checkpoints_secs=1))
        self.classifier.fit(x=X_train,y=y_train,steps=2000)
        
        # Fit model.
        #t_fit = Timer(lambda: classifier.fit(x=X_train,y=y_train,steps=2000,monitors=[validation_monitor]))


    def predict(self,X_test):
        return list(self.classifier.predict(X_test))



