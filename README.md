# NLPCC-2020-Task-3-AutoIE-
## NLPCC 2020 Task 季军技术方案及实现
                                                           
## requirements

1.预训练模型下载（RoBERTa-wwm-ext, Chinese）：
http://pan.iflytek.com/#/link/92ADD2C34C91F3B44E0EC97F101F89D8  
密码：waV5

解压后将三个模型文件
bert_config.json、
pytorch_model.bin、
vocab.txt放入’HW/chinese_roberta_wwm_ext_pytorch‘文件夹下

2.数据集

将train.txt、
valid.txt、
Test.json放在’HW/data‘文件夹下

3 所需空间及耗时

磁盘空间>30G
总耗时约5Hours


## 模型训练及预测

linux下运行脚本文件'HW/run_train_predict.sh'
将依次得到
1. 基本模型（存于'HW/saved_model_roberta'）
2. 10个运用valid数据调参的预测模型（存于'HW/saved_model_roberta_valid-0'...'HW/saved_model_roberta_valid-9'）
3. 利用十个预测模型对测试集进行voting预测，生成测试集答案预测文件（'submission/Hermers.json'）
