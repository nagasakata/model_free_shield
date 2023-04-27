import os
import re
import csv

from pprint import pprint
from benchmarks.scripts.common import get_scalars

dir_list = os.listdir('./logs/PC-B110.local/WaterTank-c100-i50-v0/')
log_a, log_b, log_c, log_d = [], [], [], []

for i in dir_list:
    if i == '.DS_Store':
        pass
    else:
        dir_list2 = os.listdir('./logs/PC-B110.local/WaterTank-c100-i50-v0/' + i)
        print(dir_list2)
        a = re.match('Shield-learnng-True-evaluation-True', dir_list2[0])
        b = re.match('Shield-learnng-True-evaluation-False', dir_list2[0])
        c = re.match('None-learnng-False-evaluation-True', dir_list2[0])
        d = re.match('None-learnng-False-evaluation-False', dir_list2[0])
        if a:
            log = './logs/PC-B110.local/WaterTank-c100-i50-v0/' + i + '/' + dir_list2[0] + '/ppo_1'
            dir_list_a = os.listdir('./logs/PC-B110.local/WaterTank-c100-i50-v0/' + i + '/' + dir_list2[0] + '/ppo_1')
            print(log)
            log_a.append(log)
        elif b:
            log = './logs/PC-B110.local/WaterTank-c100-i50-v0/' + i + '/' + dir_list2[0] + '/ppo_1'
            dir_list_b = os.listdir('./logs/PC-B110.local/WaterTank-c100-i50-v0/' + i + '/' + dir_list2[0] + '/ppo_1')
            print(log)
            log_b.append(log)
        elif c:
            log = './logs/PC-B110.local/WaterTank-c100-i50-v0/' + i + '/' + dir_list2[0] + '/ppo_1'
            dir_list_c = os.listdir('./logs/PC-B110.local/WaterTank-c100-i50-v0/' + i + '/' + dir_list2[0] + '/ppo_1')
            print(log)
            log_c.append(log)
        elif d:
            log = './logs/PC-B110.local/WaterTank-c100-i50-v0/' + i + '/' + dir_list2[0] + '/ppo_1'
            dir_list_d = os.listdir('./logs/PC-B110.local/WaterTank-c100-i50-v0/' + i + '/' + dir_list2[0] + '/ppo_1')
            print(log)
            log_d.append(log)

print(log_a)
data_a = get_scalars(log_a)
data_b = get_scalars(log_b)
data_c = get_scalars(log_c)
data_d = get_scalars(log_d)

a_dict, b_dict, c_dict, d_dict = {}, {}, {}, {}

for a_key in data_a:
    a_item = data_a[a_key]
    for a_item_key in a_item:
        if a_item_key in a_dict:
            a_dict[a_item_key] = a_dict[a_item_key] + a_item[a_item_key]
        else:
            a_dict[a_item_key] = a_item[a_item_key]

for b_key in data_b:
    b_item = data_b[b_key]
    for b_item_key in b_item:
        if b_item_key in b_dict:
            b_dict[b_item_key] = b_dict[b_item_key] + b_item[b_item_key]
        else:
            b_dict[b_item_key] = b_item[b_item_key]

for c_key in data_c:
    c_item = data_c[c_key]
    for c_item_key in c_item:
        if c_item_key in c_dict:
            c_dict[b_item_key] = c_dict[c_item_key] + c_item[c_item_key]
        else:
            c_dict[c_item_key] = c_item[c_item_key]

for d_key in data_d:
    d_item = data_d[d_key]
    for d_item_key in d_item:
        if d_item_key in d_dict:
            d_dict[d_item_key] = d_dict[d_item_key] + d_item[d_item_key]
        else:
            d_dict[d_item_key] = d_item[d_item_key]

with open(r"./csv_file/data_a.csv", "w", encoding='utf-8') as outfile:
    writerfile = csv.writer(outfile)
    writerfile.writerow(a_dict.keys())
    writerfile.writerows(zip(*a_dict.values()))

with open(r"./csv_file/data_b.csv", "w", encoding='utf-8') as outfile:
    writerfile = csv.writer(outfile)
    writerfile.writerow(b_dict.keys())
    writerfile.writerows(zip(*b_dict.values()))

with open(r"./csv_file/data_c.csv", "w", encoding='utf-8') as outfile:
    writerfile = csv.writer(outfile)
    writerfile.writerow(c_dict.keys())
    writerfile.writerows(zip(*c_dict.values()))

with open(r"./csv_file/data_d.csv", "w", encoding='utf-8') as outfile:
    writerfile = csv.writer(outfile)
    writerfile.writerow(d_dict.keys())
    writerfile.writerows(zip(*d_dict.values()))