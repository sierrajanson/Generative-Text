"""
Project: Generative Text 
Author: Sierra Janson
Date Version Completed: 07-15-23
Function: Generates a themed paragraph in response to words inputted, patterns based on training_text.txt
Input: Text word length and prompt for generation text
Future Plans: Turning into a type-tester
Needs-to-be-implemented: Base next word off previous three words to increase accuracy, simplify code
"""

import random
from numpy.random import choice

words = []
freq_holder = {}
training_text = open('training_text.txt','r')

for i in training_text:
  word_list = i.strip().split(" ")
  for i in word_list:
    words.append(i)
for i in range(len(words)-1): # for each word excluding last
  if not (words[i] in freq_holder): # if the valid word doesn't exist yet
    first_list = [] # add it and its data structure
    first_list.append(1)
    following_freqs = {}
    following_freqs[words[i+1]] = 1
    first_list.append(following_freqs)
    freq_holder[words[i]] = first_list
  else: # if the word already exists
    freq_holder[words[i]][0] += 1 # increase frequency
    following_word_dict = freq_holder[words[i]][1]
    following_word = words[i+1]
    if not(following_word in following_word_dict):
      following_word_dict[following_word] = 1
    else:
      following_word_dict[following_word] += 1
    freq_holder[words[i]][1] = following_word_dict

for i in freq_holder:
  final_freq = freq_holder[i][0] 
  temp_dict = freq_holder[i][1]
  for j in temp_dict:
    temp_dict[j] = temp_dict[j]/final_freq

def best_answer_finder(historic_word):
  if(historic_word in freq_holder):
    temp_dict = freq_holder[historic_word][1]
    keys_in_list = list(temp_dict.keys())
    probs_in_list = []
    for i in keys_in_list:
      probs_in_list.append(temp_dict[i])
    weighted_list = choice(keys_in_list, 1, p=probs_in_list)
    weighted_answer = ""
    for i in weighted_list: weighted_answer += i
    return weighted_answer

  else:
    return best_answer_finder(random.choice(words))
    
extend_count = int(input("Enter in number of words the themed-generative text should be: \n"))
user_input = input("Enter in a few random words, spaced normally.\n").strip()
# simplify this
if " " in user_input:
  input_words = user_input.split(" ")
  historic_word = input_words[len(input_words)-1]
  final = ""
  for i in range(extend_count):
    generated_word = best_answer_finder(historic_word)
    final += generated_word + " "
    historic_word = generated_word
  print(user_input + " " + final)
else:
  historic_word = user_input
  final = ""
  for i in range(extend_count):
    generated_word = best_answer_finder(historic_word)
    final += generated_word + " "
    historic_word = generated_word
  print(user_input + " " + final)