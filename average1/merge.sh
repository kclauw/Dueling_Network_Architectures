#!/bin/bash -l

qsub  hydra_atlantis_prior.sh;qsub hydra_atlantis_prior_ddqn.sh;qsub hydra_atlantis_prior_ddqn_duel.sh;qsub  hydra_space_prior.sh;qsub hydra_space_prior_ddqn.sh;qsub hydra_space_prior_ddqn_duel.sh