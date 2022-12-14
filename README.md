
# Adventures in the Realm

:fairy_woman: Engineering Thesis - RPG game based on natural language processing for text generation



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
In order to run this project you need to have a python compiler installed (e.g. prefferable Pycharm, Visual Code)

:hourglass: *It will take a while to run because of all dependencies needed to startup the game, so be patient :)*


1. Clone the project

```
  git clone https://github.com/Rudaq/MagicalWorld.git
```

2. Install Requirements

```
  pip install -r requirements.txt
```
or your compiler will offer to install them for you

3. Create a new virtual environment (venv) in *Add Python Interpreter*

![Alt text](resources/readme/interpreter.png?raw=true "Optional Title")

4. If you run this project for the first time, create the GPT-2 model
    -  Full path to the model.py file is *MagicalWorld/NLP/description_generation*
    - click run button on the model.py file
```
  cd NLP/description_generation
  python model.py
```

5. Start the game 
    - Full path to the menu.py file is *MagicalWorld/game* 
    - click run button on the menu.py file
```
  cd ../../game 
  python menu.py
```


## :star: Collaborators :star:
[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/Rudaq) Paulina Puchalska

[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/KrzeminskaWeronika) Weronika Krzemińska

[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/AleksandraRuminska)  Aleksandra Rumińska

[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/milenzaml)  Milena Zamłyńska
