#!/bin/bash
python3 train_roberta_model.py --dataset data --num_epochs 30 --model_folder saved_model_roberta --seed 2021 --device_num '0' --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 32 --num_outer_iterations 5 --train_or_predict 1
for seed_idx in $(seq 2020 2029);
do
python3 train_roberta_model.py --dataset data --num_epochs 30 --model_folder saved_model_roberta --seed ${seed_idx} --device_num '0' --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 32 --train_or_predict 2 --digit2zero
done
python3 data/transfer_json2txt.py
python3 train_roberta_model.py --dataset data --model_folder saved_model_roberta_valid- --seed 2029 --device_num '0' --bert_model_dir chinese_roberta_wwm_ext_pytorch --batch_size 32 --train_or_predict 3 --digit2zero