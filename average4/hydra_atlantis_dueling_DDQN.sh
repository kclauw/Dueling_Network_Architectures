#!/bin/bash -l
# number of nodes and cores 
#PBS -l nodes=1:ppn=8
# memory requirements change this when using more/less experience replay samples
#PBS -l mem=16gb
# max run time
#PBS -l walltime=120:00:00
# output and error files
#PBS -o atl_dueling_DDQN1.out
#PBS -e atl_dueling_DDQN1.err
#PBS -N atl_dueling_DDQN1
#PBS -V

module add openblas
cd $HOME
source .bashrc
source activate dqn2
cd Dueling_Network_Architectures
python main.py --use_gpu 0 --env_name Atlantis-v0 --is_train 1 --double_q 1 --dueling 1 --random_seed 91046

