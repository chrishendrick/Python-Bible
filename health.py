# Health potion adds to user's health - 3 different difficulty levels

import random

difficulty = 1

while (difficulty<4):
    print('------')
    if (difficulty == 1): print('Difficulty Easy')
    if (difficulty == 2): print('Difficulty Normal')
    if (difficulty == 3): print('Difficulty Hard')
    health = 50
    print('Original Health =',health);
    potionHealth = int(random.randint(25,50) / difficulty);
    print('Potion Health =',potionHealth);
    health = health + potionHealth;
    print('Final Health =',health);
    difficulty += 1
    
print('------')

