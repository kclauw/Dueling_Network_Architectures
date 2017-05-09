#!/bin/bash -l

bash $HOME/Dueling_Network_Architectures/average2/hydra_atlantis_base.sh
bash $HOME/Dueling_Network_Architectures/average2/hydra_atlantis_ddqn.sh
bash $HOME/Dueling_Network_Architectures/average2/hydra_atlantis_dueling.sh
bash $HOME/Dueling_Network_Architectures/average2/hydra_atlantis_dueling_ddqn.sh

bash $HOME/Dueling_Network_Architectures/average2/hydra_space_base.sh
bash $HOME/Dueling_Network_Architectures/average2/hydra_space_ddqn.sh
bash $HOME/Dueling_Network_Architectures/average2/hydra_space_dueling.sh
bash $HOME/Dueling_Network_Architectures/average2/hydra_space_dueling_ddqn.sh