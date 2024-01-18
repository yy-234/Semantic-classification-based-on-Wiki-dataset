








中文文本分类，TextCNN，TextRNN，FastText，TextRCNN，BiLSTM_Attention, DPCNN, Transformer, 基于pytorch，开箱即用。


## 环境
python 3.7  
pytorch 1.1  
tqdm  
sklearn  
tensorboardX

## 中文数据集
我从wiki中抽取了20万条新闻标题，已上传至github，文本长度在20到30之间。一共11个类别，每类2万条。

一级学科类别11个

数据集划分：

数据集|数据量
--|--
训练集|18万
验证集|1万
测试集|1万





## 效果

模型|acc|备注
--|--|--
TextCNN|91.22%|Kim 2014 经典的CNN文本分类
TextRNN|91.12%|BiLSTM 
TextRNN_Att|90.90%|BiLSTM+Attention
TextRCNN|91.54%|BiLSTM+池化
FastText|92.23%|bow+bigram+trigram， 效果出奇的好
DPCNN|91.25%|深层金字塔CNN
Transformer|89.91%|效果较差
bert|94.83%|bert + fc  
ERNIE|94.61%|比bert略差


## 使用说明
```
# 训练并测试：
# TextCNN
python run.py --model TextCNN

# TextRNN
python run.py --model TextRNN

# TextRNN_Att
python run.py --model TextRNN_Att

# TextRCNN
python run.py --model TextRCNN

# FastText, embedding层是随机初始化的
python run.py --model FastText --embedding random 

# DPCNN
python run.py --model DPCNN

# Transformer
python run.py --model Transformer
```

### 参数
模型都在models目录下，超参定义和模型定义在同一文件中。  


## 对应论文
[1] Convolutional Neural Networks for Sentence Classification  
[2] Recurrent Neural Network for Text Classification with Multi-Task Learning  
[3] Attention-Based Bidirectional Long Short-Term Memory Networks for Relation Classification  
[4] Recurrent Convolutional Neural Networks for Text Classification  
[5] Bag of Tricks for Efficient Text Classification  
[6] Deep Pyramid Convolutional Neural Networks for Text Categorization  
[7] Attention Is All You Need  
