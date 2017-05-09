#!/bin/bash -l

qsub hydra_atlantis_base.sh
qsub hydra_atlantis_ddqn.sh
qsub hydra_atlantis_dueling.sh
qsub hydra_atlantis_dueling_ddqn.sh
qsub hydra_space_base.sh
qsub hydra_space_ddqn.sh
qsub hydra_space_dueling.sh
qsub hydra_space_dueling_ddqn.sh