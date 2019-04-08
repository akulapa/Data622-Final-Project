#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:51:32 2018

References:
- https://community.hortonworks.com/articles/92321/interacting-with-hadoop-hdfs-using-python-codes.html

"""
import gzip
import pickle
import subprocess
import numpy as np

def run_cmd(args_list):
    """
    run linux commands
    """
    # import subprocess
    print('Running system command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = proc.communicate()
    s_return =  proc.returncode
    return s_return, s_output, s_err 

f = gzip.open('/home/hadoop/final-622/data/mnist.pkl.gz', 'rb')
training_data, validation_data, test_data = pickle.load(f, encoding='latin1')
f.close()

files = [['/home/hadoop/final-622/data/training_X.csv', 'training_data[0]', '/user/pavan/final-622/data/training_X.csv', 'hdfs:///user/pavan/final-622/data/training_X.csv'],
         ['/home/hadoop/final-622/data/training_Y.csv', 'training_data[1]', '/user/pavan/final-622/data/training_Y.csv', 'hdfs:///user/pavan/final-622/data/training_Y.csv'],
         ['/home/hadoop/final-622/data/validation_X.csv', 'validation_data[0]', '/user/pavan/final-622/data/validation_X.csv', 'hdfs:///user/pavan/final-622/data/validation_X.csv'],
         ['/home/hadoop/final-622/data/validation_Y.csv', 'validation_data[1]', '/user/pavan/final-622/data/validation_Y.csv', 'hdfs:///user/pavan/final-622/data/validation_Y.csv'],
         ['/home/hadoop/final-622/data/test_X.csv', 'test_data[0]', '/user/pavan/final-622/data/test_X.csv', 'hdfs:///user/pavan/final-622/data/test_X.csv'],
         ['/home/hadoop/final-622/data/test_Y.csv', 'test_data[1]', '/user/pavan/final-622/data/test_Y.csv', 'hdfs:///user/pavan/final-622/data/test_Y.csv']]

hdfsCmd = '/home/hadoop/hadoop285/bin/hdfs' 

for r in files:
    p = 'np.savetxt("' + str(r[0][:]) + '",' + str(r[1][:]) + ', delimiter=",")'
    exec(p)
    
    #Run Hadoop ls command in Python
    (ret, out, err)= run_cmd([hdfsCmd, 'dfs', '-ls', str(r[2][:])])
    
    #Upload file to Hadoop
    if ret:
        (ret, out, err) = run_cmd([hdfsCmd, "dfs", "-put", str(r[0][:]), str(r[3][:])])


