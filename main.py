import evolve

print('Starting an evolution process')
print('Enter the target sentence')
target_sentence = input().lower()
print('Target sentence is: ', target_sentence)
print('\n\n'+'*'*40 + '\n\n')

print('First list of random sentences: \n\n' + '*'*40 + '\n\n')
random_sentences = evolve.random_sentence_list(target_sentence)
print('\n\n'+'*'*40 + '\n\n')

prob = float(input('Enter the probability of mutation in float format: '))
evolved_sentece = evolve.evolving_research(random_sentences, target_sentence)
print('First generation evolved sentence is: ', evolved_sentece)
print('\n\n'+'*'*40 + '\n\n')


success = False
cycles = 0
# Cycle of evolution with mutations till the target is reached or 1000 cycles are done
for i in range (1, 1001):
  if evolved_sentece == target_sentence:
    success = True
    break
  mutated_list = evolve.create_mutated_list(evolved_sentece, prob)
  evolved_sentece = evolve.evolving_research(mutated_list, target_sentence)
  cycles += 1

# Succses of evoltion checking
if success:
  print('Evolution is successfull. Final result is:\n ', evolved_sentece, '\nCycles compited:',cycles)
else:
  print('Evolution did not reach the target. Final result is:\n '+ evolved_sentece, '\nCycles compited:',cycles)