
# Adventures in the Realm

Engineering Thesis - RPG game based on natural language processing for text generation



## Abstract 
The aim of the thesis is to apply Natural Language Processing mechanisms to a real, interactive Role
Playing Game. As part of the implementation of the game, several races of characters were created to
choose from, as well as varied lands with characters living in them. Each race has different characteristics
and its own series of adventures in which it performs interactions with Non-Playable Characters (NPCs).
The work presents the language modelling techniques used to generate a description of the hero, answer
the hero’s questions for gameplay clues, conduct dialogue, and recognise sentiment when asking NPCs
to get a quest for the hero. The thesis is of an experimental nature, due to the fact that in the current
world there is not yet a solution to the problem at hand, hence with a working project basis, any future
improvements can be applied to improve the quality of the result of this work.



## Setup
In order to run this project you need to have a python compiler installed (e.g. Pycharm, Visual Code)

*It will take a while to run because of all dependencies needed to startup the game, so be patient :)*


1. Clone the project

```bash
  $ git clone https://github.com/Rudaq/MagicalWorld.git
```

2. Go to the project directory

```bash
  $ cd MagicalWorld
```

3. Install Requirements

```bash
  $ pip install -r requirements.txt
```

4. Create the GPT-2 model, if you run this project for the first time
- Full path to the model.py file is *MagicalWorld/NLP/description_generation*
```bash
  $ cd NLP/description_generation
  $ python model.py
```

5. Run bash file/something that will work :D
- Full path to the menu.py file is *MagicalWorld/game* 
```bash
  $ cd ../../game 
  $ python menu.py
```


## 🔗 Collaborators
[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/Rudaq)  
[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/KrzeminskaWeronika)  
[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/AleksandraRuminska)  
[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/milenzaml)  
