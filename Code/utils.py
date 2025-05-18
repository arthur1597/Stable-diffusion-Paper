import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms, models
from torch.utils.data import DataLoader
import cv2
from glob import glob
from collections import Counter
import numpy as np
from PIL import Image
import torch.nn.functional as F
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
from tqdm import tqdm
from torchvision.models import ResNet18_Weights
from sklearn.model_selection import train_test_split
import random
import os

# GPU 설정
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using Pytorch version :', torch.__version__, ' Device :', DEVICE)

# 성능 평가 함수
def evaluate(model, dataloader):
    model.eval()
    correct = 0
    total = 0
    y_true = []
    y_pred = []

    with torch.no_grad():
        for images, labels in dataloader:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            y_true.extend(labels.cpu().numpy())
            y_pred.extend(predicted.cpu().numpy())

    acc = 100 * correct / total
    precision = precision_score(y_true, y_pred, average='macro')
    recall = recall_score(y_true, y_pred, average='macro')
    f1 = f1_score(y_true, y_pred, average='macro')
    print(f'Test Accuracy: {acc:.2f}%, Precision: {precision:.2f}, Recall: {recall:.2f}, F1-score: {f1:.2f}')
    return acc, precision, recall, f1

# 모델 저장 함수
def save_model(model, path):
    torch.save(model.state_dict(), path)

# 모델 불러오기 함수
def load_model(model, path):
    model.load_state_dict(torch.load(path, map_location=DEVICE))
    model.to(DEVICE)
    return model
