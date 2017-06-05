#python average_runs.py "Average runs" /atlantis_base/average_loss /atlantis_ddqn/average_loss /atlantis_dueling/average_loss /atlantis_dueling_ddqn/average_loss
#python average_runs.py "Average Q" /atlantis_base/average_q /atlantis_ddqn/average_q /atlantis_dueling/average_q /atlantis_dueling_ddqn/average_q
#python average_runs.py "Average reward" /atlantis_base/average_reward /atlantis_ddqn/average_reward /atlantis_dueling/average_reward /atlantis_dueling_ddqn/average_reward
#python average_runs.py "Average reward per episode" /atlantis_base/episode_avg_reward /atlantis_ddqn/episode_avg_reward /atlantis_dueling/episode_avg_reward /atlantis_dueling_ddqn/episode_avg_reward


#python average_runs.py "Average loss" average_loss "atlantis" "Atlantis" base ddqn dueling dueling_ddqn;
#python average_runs.py "Average Reward" average_reward "atlantis" "Atlantis" base ddqn dueling dueling_ddqn;
#python average_runs.py "Average Q" average_q "atlantis" "Atlantis" base ddqn dueling dueling_ddqn;
#python average_runs.py "Max reward per episode" episode_max_reward "atlantis" "Atlantis" base ddqn dueling dueling_ddqn;


#python average_runs.py "Average loss" average_loss "space" "Space Invaders" base ddqn dueling dueling_ddqn;
#python average_runs.py "Average Reward" average_reward "space" "Space Invaders" base ddqn dueling dueling_ddqn;
#python average_runs.py "Average Q" average_q "space" "Space Invaders" base ddqn dueling dueling_ddqn;
#python average_runs.py "Max reward per episode" episode_max_reward "space" "Space Invaders" base ddqn dueling dueling_ddqn;

#python average_runs.py "Average reward per episode" episode_avg_reward "space" "Space Invaders" base prior prior_dueling_ddqn;
python average_runs.py "Average reward per episode" episode_avg_reward "atlantis" "Atlantis" base prior prior_dueling_ddqn;
#python average_runs.py "Average reward per episode" episode_avg_reward "space" "Space Invaders" base ddqn;
#python average_runs.py "Average reward per episode" episode_avg_reward "space" "Space Invaders" base dueling;
#python average_runs.py "Average reward per episode" episode_avg_reward "space" "Space Invaders" base dueling_ddqn;
#python average_runs.py "Average reward per episode" episode_avg_reward "space" "Space Invaders" base ddqn dueling dueling_ddqn;

#python average_runs.py "Average reward per episode" episode_avg_reward "atlantis" "Atlantis" base ddqn;
#python average_runs.py "Average reward per episode" episode_avg_reward "atlantis" "Atlantis" base dueling;
#python average_runs.py "Average reward per episode" episode_avg_reward "atlantis" "Atlantis" base dueling_ddqn;
#python average_runs.py "Average reward per episode" episode_avg_reward "atlantis" "Atlantis" base ddqn dueling dueling_ddqn;