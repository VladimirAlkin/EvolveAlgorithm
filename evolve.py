import random

# The project is targeted at one specific sentence but it's not a problem to tweak an algoritm as you wish. Check README

# Create a strater list of 100 random strings
def random_sentence_list(target):
  abc = "abcdefghijklmnopqrstuvwxyz "
  random_sentences = []
  target_len = len(target)+1
  for i in range (1,101):
   sentence = ''.join(random.choice(abc) for _ in range(1,target_len))
   random_sentences.append(sentence)
  for i in range (0, len(random_sentences)):
    print(i+1, ')' , random_sentences[i])
  return random_sentences

# Checking every sentence in list by score* for the best match.
# score - how many same letters are in the same positions with the target sentence
def evolving_research(evloving_list, target):
  target_sentence = list(target)
  evolved_sentence = evloving_list[0]
  best_score = 0
  for sentence in evloving_list:
    counter = 0
    for letter in range(0,len(sentence)):
      if sentence[letter]==target_sentence[letter]:
        counter +=1
    if counter > best_score:
      evolved_sentence = sentence
      best_score = counter
  return evolved_sentence


# Creating a list of a best match sentence and dropping a random mutations with a user's probability {prob}
def create_mutated_list(sentence, prob):
  mutated_list = []
  for i in range(1,101):      
    mutated_list.append(create_mutated_sentence(sentence, prob))
  return mutated_list  



# Possible creation of mutation is the sentence. Probability of appearing a mutation is given parameter
def create_mutated_sentence(sentence, prob):
  abc = "abcdefghijklmnopqrstuvwxyz "
  sentence = list(sentence)
  for i in range(len(sentence)):
    if random.random() < prob:
      sentence[i] = random.choice(abc)
  return "".join(sentence)