import numpy as np
import xgboost as xgb

from sagemaker_xgboost_container.metrics.custom_metrics import accuracy, f1, mse


binary_train_data = np.random.rand(10, 2)
binary_train_label = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
binary_dtrain = xgb.DMatrix(binary_train_data, label=binary_train_label)
binary_preds = np.ones(10)


def test_binary_accuracy():
    accuracy_name, accuracy_result = accuracy(binary_preds, binary_dtrain)
    assert accuracy_name == 'accuracy'
    assert accuracy_result == .5


def test_binary_f1():
    f1_score_name, f1_score_result = f1(binary_preds, binary_dtrain)
    assert f1_score_name == 'f1'
    assert f1_score_result == 1/3


def test_mse():
    mse_score_name, mse_score_result = mse(binary_preds, binary_dtrain)
    assert mse_score_name == 'mse'
    assert mse_score_result == .5


multiclass_train_data = np.random.rand(10, 2)
multiclass_train_label = np.array([0, 0, 1, 1, 1, 1, 1, 2, 2, 2])
multiclass_dtrain = xgb.DMatrix(multiclass_train_data, label=multiclass_train_label)
multiclass_preds = np.ones(10)


def test_multiclass_accuracy():
    accuracy_name, accuracy_result = accuracy(multiclass_preds, multiclass_dtrain)
    assert accuracy_name == 'accuracy'
    assert accuracy_result == .5


def test_multiclass_f1():
    f1_score_name, f1_score_result = f1(binary_preds, binary_dtrain)
    assert f1_score_name == 'f1'
    assert f1_score_result == 1/3
