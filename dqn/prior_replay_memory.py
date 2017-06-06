#Code from https://github.com/Damcy/prioritized-experience-replay
import os
import random
import logging
import numpy as np
import binary_heap
import math 
from .utils import save_npy, load_npy
class PrioritizedMemory:
  def __init__(self, config, model_dir):
    self.model_dir = model_dir
    self.cnn_format = config.cnn_format
    self.memory_size = config.memory_size
    self.batch_size = config.batch_size
    self.learn_start = config.learn_start
    self.total_steps = config.max_step
    self.alpha = 0.7
    self.beta_zero = 0.5
    self.replace_flag = True
    self.count = 0
    self.partition_num = 30

    self.index = 0
    self.record_size = 0
    self.isFull = False

    self._experience = {}
    self.priority_queue = binary_heap.BinaryHeap(self.memory_size)
    #self.distributions = self.build_distributions()

    self.beta_grad = (1 - self.beta_zero) / (self.total_steps - self.learn_start)


  def build_distribution(self):
      # P(i) = (rank i) ^ (-alpha) / sum ((rank i) ^ (-alpha))
      pdf = list(
          map(lambda x: math.pow(x, -self.alpha), range(1, self.priority_queue.size + 1))
      )
      pdf_sum = math.fsum(pdf)
      return list(map(lambda x: x / pdf_sum, pdf))


  def fix_index(self):
      """
      get next insert index
      :return: index, int
      """
      if self.record_size <= self.memory_size:
          self.record_size += 1
      if self.index % self.memory_size == 0:
          self.isFull = True if len(self._experience) == self.memory_size else False
          if self.replace_flag:
              self.index = 1
              return self.index
          else:
              sys.stderr.write('Experience replay buff is full and replace is set to FALSE!\n')
              return -1
      else:
          self.index += 1
          return self.index

  def store(self, experience):
      """
      store experience, suggest that experience is a tuple of (s1, a, r, s2, t)
      so each experience is valid
      :param experience: maybe a tuple, or list
      :return: bool, indicate insert status
      """
      insert_index = self.fix_index()

      if insert_index > 0:
          if insert_index in self._experience:
              del self._experience[insert_index]
          self._experience[insert_index] = experience
          # add to priority queue
          priority = self.priority_queue.get_max_priority()
          self.priority_queue.update(priority, insert_index)
          self.count += 1
          return True
      else:
          sys.stderr.write('Insert failed\n')
          return False
  def update_priority(self, indices, delta):
      """
      update priority according indices and deltas
      """
      for i in range(0, len(indices)):
          self.priority_queue.update(math.fabs(delta[i]), indices[i])
      

  def retrieve(self, indices):
      """
      get experience from indices
      :param indices: list of experience id
      :return: experience replay sample
      """
      return [self._experience[v] for v in indices]

  def rebalance(self):
      """
      rebalance priority queue
      :return: None
      """
      self.priority_queue.balance_tree()





  def sample(self, global_step):
    
      distribution = self.build_distribution()
      rank_list = []
      for n in range(1, self.batch_size + 1):
          index = random.randint(1,self.priority_queue.size)
          rank_list.append(index)


      # beta, increase by global_step, max 1
      beta = min(self.beta_zero + (global_step - self.learn_start - 1) * self.beta_grad, 1)
      # find all alpha pow, notice that pdf is a list, start from 0
      prob_i = [distribution[v - 1] for v in rank_list]
      # w = (N * P(i)) ^ (-beta) / max w
      w = np.power(np.array(prob_i) * self.memory_size, -beta)
      w_max = max(w)
      w = np.divide(w, w_max)
      # rank list is priority id
      # convert to experience id
      rank_e_id = 0
      try:
          rank_e_id = self.priority_queue.priority_to_experience(rank_list)
      except:
          print('ERRROR')
      # get experience id according rank_e_id
      experiences = self.retrieve(rank_e_id)

      s_ts = np.array([experience[0] for experience in experiences])
      rewards = np.array([experience[1] for experience in experiences])
      actions = np.array([experience[2] for experience in experiences])
      s_t_plus_1s = np.array([experience[3] for experience in experiences])
      terminals = np.array([experience[4] for experience in experiences])
      return s_ts, actions, rewards ,s_t_plus_1s,terminals, w, rank_e_id
