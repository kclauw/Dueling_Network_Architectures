#!/bin/bash -l
# number of nodes and cores 
#PBS -l nodes=1:ppn=1
# memory requirements change this when using more/less experience replay samples
#PBS -l mem=16gb
# max run time
#PBS -l walltime=72:00:00
# output and error files
#PBS -o dqn.out
#PBS -e dqn.err
#PBS -N dqn
#PBS -V

module add openblas
cd $HOME
source .bashrc
source activate dqn2
cd Dueling_Network_Architectures
python main.py --use_gpu 0 --env_name Atlantis-v0 --is_train 1
