
QUESTS = {
    # Faerie
    'Faerie': {
        'good': {
            # Quest 1
            'save_snowman': {
                'name': 'save_snowman',
                'description': 'You have to prove that you have a good heart. There is someone in trouble.. '
                               'Go to the Elf to get to know how to save the life of poor Snowman.',
                'points': 20,
                'tasks': [
                    {
                        'name': 'yeti_horn',
                        'description': 'Elf: Poor Snowman is in trouble.. The Ice Monster is haunting on him! Kill '
                                       'the Ice '
                                       'Monster and give his tusk to a Snowman to prove that his life is safe.',
                        'artefact': 'Ice Monster Tusk',
                        'points': 15,
                        'npc_give_task': 'Elf',
                        'npc_take_artifact': 'Friendly Snowman',
                        'next_npc': None,
                        'gift': None
                    }
                ]
            },
            # Quest 2
            'gain_recognition': {
                'name': 'gain_recognition',
                'description': 'You are a great hero! You gain more and more fame. To gain even greater recognition, '
                               'go to the Smith, he will have a task for you!',
                'points': 50,
                'tasks': [
                    {
                        'name': 'gold',
                        'description': 'Smith: I need some gold for my work... Please go to the Leprechaun and '
                                       'convince him to give you a gold bar and bring it back to me.',
                        'artefact': 'Gold Bar',
                        'points': 15,
                        'npc_give_task': 'Smith',
                        'npc_take_artifact': 'Smith',
                        'next_npc': 'Leprechaun',
                        'gift': None
                    },
                    {
                        'name': 'rainbow',
                        'description': 'Leprechaun: Find a rainbow and bring it back to the me! Little tip - you can '
                                       'find rainbows in the land where the Elves live',
                        'artefact': 'Rainbow',
                        'points': 20,
                        'npc_give_task': 'Leprechaun',
                        'npc_take_artifact': 'Leprechaun',
                        'next_npc': None,
                        'gift': 'Gold Bar'
                    }

                ]
            },
            # Quest 3
            'mermaid_voice': {
                'name': 'mermaid_voice',
                'description': 'The Smith is an influential man, thanks to the fact that you helped him, '
                               'your fame spread across all lands. Mermaid came for help. There is one problem .. The '
                               'Dark Wizard has stolen the mermaids voice. Go to Druid, he will tell you '
                               'how you can get a task from Mermaid.',
                'points': 60,
                'tasks': [
                    {
                        'name': 'kill_dark_wizard',
                        'description': 'The Dark Wizard has stolen the Mermaids necklace, without it she cannot talk. '
                                       'In order for her to assign a task for you, you must first kill the Dark '
                                       'Wizard and bring her voice back!',
                        'artefact': 'Mermaid Necklace',
                        'points': 20,
                        'npc_give_task': 'Druid',
                        'npc_take_artifact': 'Mermaid',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'rainbow',
                        'description': 'Mermaid: Oh no, poor Panda. Her ball got stuck on a bamboo tree. Find the '
                                       'ball and give it to the Panda so she can play again.',
                        'artefact': 'Ball',
                        'points': 20,
                        'npc_give_task': 'Mermaid',
                        'npc_take_artifact': 'Panda',
                        'next_npc': None,
                        'gift': None
                    }
                ]
            },
            # Quest 4
            'immortality_flower': {
                'name': 'immortality_flower',
                'description': 'Now you are ready for the greatest mission .. You have to help the Fairies regain '
                               'immortality back. Go to the Little Fairies for more details',
                'points': 70,
                'tasks': [
                    {
                        'name': 'lost_piece_of_paper',
                        'description': 'Little Faeries: Find the lost Flower of Immortality, which was stolen by the '
                                       'Dwarf years ago .. Friendly Snowman wrote down on a piece of '
                                       'paper where the flower is, but he has lost this paper '
                                       'somewhere in his Land.. Find this paper and give it to him and ask for '
                                       'reading of its content!',
                        'artefact': 'Paper',
                        'points': 20,
                        'npc_give_task': 'Faerie',
                        'npc_take_artifact': 'Friendly Snowman',
                        'next_npc': 'Friendly Snowman',
                        'gift': None
                    },
                    {
                        'name': 'snowman_nose',
                        'description': 'Friendly Snowman: I will read the content of this paper for you, but first '
                                       'you have to help me .. The Donkey took my carrot nose and wants to eat it .. '
                                       'Please go to him, get my nose back and bring it back to me',
                        'artefact': 'Snowman Nose',
                        'points': 15,
                        'npc_give_task': 'Friendly Snowman',
                        'npc_take_artifact': 'Friendly Snowman',
                        'next_npc': 'Donkey',
                        'gift': None
                    },
                    {
                        'name': 'orc_blood',
                        'description': 'The Orc keeps attacking me and the poor rats, kill him and bring his blood '
                                       'as an evidence and you will get the carrot back.',
                        'artefact': 'Orc Blood',
                        'points': 15,
                        'npc_give_task': 'Donkey',
                        'npc_take_artifact': 'Donkey',
                        'next_npc': None,
                        'gift': 'Snowman Nose'
                    },
                    {
                        'name': 'flower',
                        'description': 'Content of the Paper: "The Immortality Flower is hidden in the Great Tree in '
                                       'the Dreary Forest.." Find the Flower and give it back to Faeries!',
                        'artefact': 'Immortality Flower',
                        'points': 15,
                        'npc_give_task': 'Friendly Snowman',
                        'npc_take_artifact': 'Faerie',
                        'next_npc': None,
                        'gift': None
                    }

                ]
            }

        },
        'evil': {
            # # Quest 1
            'kill_unicorn': {
                'name': 'kill_unicorn',
                'description': 'You have to prove on which side you are ... go to the Dark Wizard for tips on how to '
                               'do it.',
                'points': 20,
                'tasks': [
                    {
                        'name': 'unicorn_horn',
                        'description': 'Unicorns are powerful creatures... They are friendly, but who knows ... Maybe '
                                       'then they will use their power against us. Better not let that happen! Go and '
                                       'kill the unicorn and bring its horn back to me',
                        'artefact': 'Unicorn Horn',
                        'points': 15,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': None
                    }
                ]
            },
            # Quest 2
            'smiths_tools': {
                'name': 'smiths_tools',
                'description': 'You are a brave warrior. You can gain great fame by helping creatures in all lands. '
                               'The Dark Elf has a job for you, go to him for the rest of the details',
                'points': 50,
                'tasks': [
                    {
                        'name': 'tools',
                        'description': 'Dark Elf: I need tools to work... I used to have them, but a Smith stole them '
                                       'from me! '
                                       'Go to Smith and tell him to give the tools back! ',
                        'artefact': 'Tools',
                        'points': 10,
                        'npc_give_task': 'Dark Elf',
                        'npc_take_artifact': 'Dark Elf',
                        'next_npc': 'Smith',
                        'gift': None
                    },
                    {
                        'name': 'farmer_blood',
                        'description': 'Smith: I will give you my tools, but first you need to help me with the '
                                       'Farmer. He recently sold me poisoned potatoes. As revenge, you must kill him '
                                       'and bring me back his blood',
                        'artefact': 'Farmer Blood',
                        'points': 10,
                        'npc_give_task': 'Smith',
                        'npc_take_artifact': 'Smith',
                        'next_npc': None,
                        'gift': 'Tools',

                    }
                ]
            },
            # Quest 3
            'prove_bravery': {
                'name': 'prove_bravery',
                'description': 'Well done, the Dark Elf spreads the word about your strength. Apparently, Big Ravens '
                               'know how you can prove your bravery, go to him for details',
                'points': 60,
                'tasks': [
                    {
                        'name': 'feed_ravens',
                        'description': 'Big Ravens: We will tell you how you can prove your bravery, but first bring '
                                       'us food. We feed on the skin of a snake, I think you know what to do..',
                        'artefact': 'Snake Skin',
                        'points': 15,
                        'npc_give_task': 'Big Raven',
                        'npc_take_artifact': 'Big Raven',
                        'next_npc': 'Big Ravens',
                        'gift': None
                    },
                    {
                        'name': 'mermaid_blood',
                        'description': 'Vampires are powerful creatures. You can gain fame by giving them a favor. '
                                       'Vampires need Mermaid blood to live. Bring it to them and tell everyone about'
                                       ' your bravery',
                        'artefact': 'Mermaid Blood',
                        'points': 15,
                        'npc_give_task': 'Big Raven',
                        'npc_take_artifact': 'Vampire',
                        'next_npc': None,
                        'gift': None,

                    }
                ]
            },
            # Quest 4
            'bamboo_island': {
                'name': 'bamboo_island',
                'description': 'Great, everyone has heard about you now. Even the Big Monkey from Bamboo Island. He '
                               'has a task fot you, go to the Bamboo Island and ask for the details.',
                'points': 60,
                'tasks': [
                    {
                        'name': 'pandas_skull',
                        'description': 'Big Monke: Someone like you can help me! I lost a panda skull somewhere .. '
                                       'Someone buried it. It is said to be buried 5 meters on the right from the Big '
                                       'Tree in the Dreary Forest. You will need a shovel to dig it. First, '
                                       'go to the Smith '
                                       'for a shovel, and then find skull. Go back to me '
                                       'with the Pandas skull',
                        'artefact': 'Pandas Skull',
                        'points': 15,
                        'npc_give_task': 'Big Monke',
                        'npc_take_artifact': 'Big Monke',
                        'next_npc': 'Smith',
                        'gift': None
                    },
                    {
                        'name': 'tigers_fur',
                        'description': 'Smith: It is getting colder .. I need a Tiger fur keep warm. Bring it to me '
                                       'and I will give you a shovel',
                        'artefact': 'Tiger Fur',
                        'points': 15,
                        'npc_give_task': 'Smith',
                        'npc_take_artifact': 'Smith',
                        'next_npc': None,
                        'gift': 'Shovel',

                    }
                ]
            },
            # Quest 5
            'kill_dragon': {
                'name': 'kill_dragon',
                'description': 'Now you are ready for the biggest mission... Go to Dar Wizard for the details!',
                'points': 60,
                'tasks': [
                    {
                        'name': 'dragon_blood',
                        'description': 'Dark Wizard: Now you are ready for the biggest mission... The dragon has been '
                                       'tormenting the people of the land for too long. Put an end to his bestiality '
                                       'and kill him. Be careful though, the dragon is not so easy to defeat. To '
                                       'prove that the dragons reign is over, bring his blood to the me.',
                        'artefact': 'Dragon Blood',
                        'points': 15,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': None
                    }
                ]
            }
        }
    },
    'Dwarf': {
        'good': {
            # Quest 1
            'artisanal_skill': {
                'name': 'artisanal_skill',
                'description': 'Dwarves are known for their great ability in crafting. Find a Smith and learn it.',
                'points': 20,
                'tasks': [
                    {
                        'name': 'own_hammer',
                        'description': 'Smith: First you need to have your own hammer. Go find a Farmer and ask him '
                                       'for it.',
                        'artefact': 'Hammer',
                        'points': 15,
                        'npc_give_task': 'Smith',
                        'npc_take_artifact': None,
                        'next_npc': 'Farmer',
                        'gift': None
                    },
                    {
                        'name': 'kill_ravens',
                        'description': 'Farmer: You need a hammer? Well, nothing comes for free. Kill bastards '
                                       'destroying my crops and bring me their feathers back.',
                        'artefact': 'Raven feathers',
                        'points': 15,
                        'npc_give_task': 'Farmer',
                        'npc_take_artifact': 'Farmer',
                        'next_npc': 'Smith',
                        'gift': 'Hammer'
                    },
                    {
                        'name': 'nutritious_food',
                        'description': 'Smith: Fine, now that you own a hammer, we need a lot of energy. Kill wheat '
                                       'monster so that we have something to eat.',
                        'artefact': 'Food',
                        'points': 15,
                        'npc_give_task': 'Smith',
                        'npc_take_artifact': 'Smith',
                        'next_npc': None,
                        'gift': 'Hammer'
                    }
                ]
                # outcome: Learning for 30 seconds, improved attack
            },
            # Quest 2
            'primaeval_help': {
                'name': 'primaeval_help',
                'description': 'Now that you learnt how to craft, it’s time to make yourself useful. Help the amazons.',
                'points': 50,
                'tasks': [
                    {
                        'name': 'gold',
                        'description': 'Amazon: We want to improve our weapons with the fangs of our greatest enemies '
                                       'killing animals from our bush. Kill vampires and bring their fangs back. ',
                        'artefact': 'Vampire fang',
                        'points': 15,
                        'npc_give_task': 'Amazon',
                        'npc_take_artifact': 'Amazon',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'weapon_help',
                        'description': 'Amazon: Now, please help us improve our weapon.',
                        'artefact': None,
                        'points': 20,
                        'npc_give_task': 'Amazon',
                        'npc_take_artifact': None,
                        'next_npc': None,
                        'gift': 'Banana'  # you will need this to kill Big Monke
                    }

                ]
            },
            # Quest 3
            'home_sweet_home': {
                'name': 'home_sweet_home',
                'description': 'Time to go home, you dwarf! The Frozen Empire is waiting for you to make it safe '
                               'again! See the Snowman',
                'points': 60,
                'tasks': [
                    {
                        'name': 'kill_yeti',
                        'description': 'Snowman: You have to help me my friend! Since those of your kind are no longer '
                                       'here, the place is haunted by the Ice Monster... They call it Yeti. Please kill'
                                       'it.',
                        'artefact': 'Yetis fur',
                        'points': 20,
                        'npc_give_task': 'Snowman',
                        'npc_take_artifact': 'Snowman',
                        'next_npc': None,
                        'gift': 'Yetis fur'
                    },
                    {
                        'name': 'kill_wolves',
                        'description': 'Snowman: Great! Now please kill a pack of wolves. There are many hungry '
                                       'wolves here!',
                        'artefact': 'Wolves fangs',
                        'points': 20,
                        'npc_give_task': 'Snowman',
                        'npc_take_artifact': 'Snowman',
                        'next_npc': None,
                        'gift': 'Wolves fangs'
                    }
                ]
            },
            # Quest 4
            'brace_yourself': {
                'name': 'brace_yourself',
                'description': 'You’d better prepare for the ultimate adventure of yours. How to do that? Better make '
                               'friends with magic itself. Find a Dark Wizard.',
                'points': 70,
                'tasks': [
                    {
                        'name': 'gold_for_wizard',
                        'description': 'Dark Wizard: Well, well, well. As they say - Nothing comes for free my dwarf.'
                                       'Bring me some gold which you will probably obtain by dealing with Leprechaun...',
                        'artefact': 'Gold Bar',
                        'points': 20,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'potion_making',
                        'description': 'Dark Wizard: Back to the business. Now kill the unicorn so that we have '
                                       'unicorns horn.',
                        'artefact': 'Unicorn horn',
                        'points': 20,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'bring_fire',
                        'description': 'Dark Wizard: Now we need a flame. Deal with Fire Elemental to obtain it.',
                        'artefact': 'Flame',
                        'points': 20,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'vampire_goods',
                        'description': 'Dark Wizard: And the last thing we need is hair of a vampire. Kill it and '
                                       'bring what we need.',
                        'artefact': 'Vampire hair',
                        'points': 20,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': None
                    }
                ]
            },
            # Quest 5
            'dwarven_empire_mistery': {
                'name': 'dwarven_empire_mistery',
                'description': 'There we are. It’s time to solve the greatest mistery of the dwarves. Find the thief '
                               'of the Greatest Gem of the Dwarven Empire. See Druid for clues.',
                'points': 100,
                'tasks': [
                    {
                        'name': 'find_witness',
                        'description': 'Druid: The only one, who survived... is hidden on the mountain of the Frozen '
                                       'Empire. You had better find him. He is hidden next to an ice ball.',
                        'artefact': 'Ice ball',
                        'points': 20,
                        'npc_give_task': 'Druid',
                        'npc_take_artifact': None,
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'the_snowman',
                        'description': 'Snowman: I will help you as long as you bring me my nose! Kill escaping '
                                       'vegetables so I can get a carrot.',
                        'artefact': 'Carrot',
                        'points': 20,
                        'npc_give_task': 'Snowman',
                        'npc_take_artifact': 'Snowman',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'bring_fire',
                        'description': 'Big Monke: Come find me! You can kill me, but so that you know - I am not a '
                                       'thief. '
                                       'I am just a keeper. You wanna know who is the thief? Give me something that I '
                                       'sense you have.',
                        'artefact': 'Banana',
                        'points': 20,
                        'npc_give_task': 'Big Monke',
                        'npc_take_artifact': 'Big Monke',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'banana',
                        'description': 'Big Monke: Follow the flame into the desolation of abomination. Kill the '
                                       'creature.',
                        'artefact': 'Dragons fang',
                        'points': 20,
                        'npc_give_task': 'Big Monke',
                        'npc_take_artifact': 'Big Monke',
                        'next_npc': None,
                        'gift': 'The greatest gem of dwarven empire'
                    }
                ]
            }
        },
        'evil': {
            # Quest 1
            'destroy_primeval_bush': {
                'name': 'destroy_primeval_bush',
                'description': 'Your journey here will focus on doing bad, bad things... Lets start with eliminating '
                               'some of your enemies so that you can gain their weapon. Go kill the tigers first.',
                'points': 20,
                'tasks': [
                    {
                        'name': 'kill_tigers',
                        'description': 'Kill the tigers so that you have their fur.',
                        'artefact': 'Tigers fur',
                        'points': 15,
                        'npc_give_task': None,
                        'npc_take_artifact': None,
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'kill_snakes',
                        'description': 'Kill the snakes so that you have their skin.',
                        'artefact': 'Snakes skin',
                        'points': 15,
                        'npc_give_task': None,
                        'npc_take_artifact': None,
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'kill_amazons',
                        'description': 'The last thing you need to do to take over the primaeval bush is to... Kill '
                                       'its keepers! Amazons! Kill them and take their weapon. You may need it '
                                       'later..',
                        'artefact': 'Amazons spare',
                        'points': 15,
                        'npc_give_task': None,
                        'npc_take_artifact': None,
                        'next_npc': None,
                        'gift': 'Amazons spare'
                    }
                ]
            },
            # Quest 2
            'trade_weapons': {
                'name': 'trade_weapons',
                'description': 'Congratulations. Now you have a leverage. Trade your javelin with the Smith.',
                'points': 50,
                'tasks': [
                    {
                        'name': 'trade',
                        'description': 'Smith: Well... I will improve your weapons strength only if you bring me '
                                       'gold. You will get it by killing the leprechaun. You seem shady lad. ',
                        'artefact': 'Gold',
                        'points': 10,
                        'npc_give_task': 'Smith',
                        'npc_take_artifact': 'Smith',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'bring_food',
                        'description': 'Smith: Okay. I have the gold. But I am hungry you know. I would like to eat '
                                       'something. Maybe a fish?',
                        'artefact': 'Fish',
                        'points': 10,
                        'npc_give_task': 'Smith',
                        'npc_take_artifact': 'Smith',
                        'next_npc': None,
                        'gift': 'Weapon',  # improved strength

                    }
                ]
            },
            # Quest 3
            'trick_orcs': {
                'name': 'prove_bravery',
                'description': 'Now your task is to trick orcs into giving you more power. See them for the clues.',
                'points': 60,
                'tasks': [
                    {
                        'name': 'clean_feet',
                        'description': 'Orcs: You want what? Regain your life? Ha ha ha... Fine, but you have to do '
                                       'couple '
                                       'of things first. For example... Clean my feet! Take water from Specular Lake.',
                        'artefact': 'Water',
                        'points': 15,
                        'npc_give_task': 'Orc',
                        'npc_take_artifact': 'Orc',
                        'next_npc': None,
                        'gift': 'Life potion'
                    }
                ]
            },
            # Quest 4
            'steal_treasure': {
                'name': 'steal_treasure',
                'description': 'There we are. It’s time to solve the greatest mistery of the dwarves. Find the thief '
                               'of the Greatest Gem of the Dwarven Empire. See Druid for clues.',
                'points': 100,
                'tasks': [
                    {
                        'name': 'find_witness',
                        'description': 'Druid: The only one, who survived... is hidden on the mountain of the Frozen '
                                       'Empire. You had better find him. If you are looking for clues, find the ice ball first.',
                        'artefact': 'Ice ball',
                        'points': 20,
                        'npc_give_task': 'Druid',
                        'npc_take_artifact': None,
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'the_snowman',
                        'description': 'Snowman: I will help you as long as you bring me my nose! Kill escaping '
                                       'vegetables so I can get a carrot.',
                        'artefact': 'Carrot',
                        'points': 20,
                        'npc_give_task': 'Snowman',
                        'npc_take_artifact': 'Snowman',
                        'next_npc': 'Big Monke',
                        'gift': None
                    },
                    {
                        'name': 'bring_fire',
                        'description': 'Big Monke: You want the treasure? It wont be easy for you little one.',
                        'artefact': 'The Greatest Gem of Dwarven Empire', # nie wiem, obojetnie co no
                        'points': 20,
                        'npc_give_task': 'Big Monke',
                        'npc_take_artifact': None,
                        'next_npc': None,
                        'gift': 'The Greatest Gem of Dwarven Empire'
                    }
                ]
            }
        }
    },
    'Wizard': {
        'good': {
            # Quest 1
            'make_wand': {
                'name': 'make_wand',
                'description': 'You are a wizard! You are the one to know best what wizards have... A wand! Make '
                               'yourself one. Find Druid in Enchanted Forest.',
                'points': 20,
                'tasks': [
                    {
                        'name': 'find_a_tree',
                        'description': 'Druid: First you need to gain materials. Find a tree in Enchanted Forest and '
                                       'take a stick from it..',
                        'artefact': 'Stick',
                        'points': 15,
                        'npc_give_task': 'Druid',
                        'npc_take_artifact': 'Druid',
                        'next_npc': None, #Druid?
                        'gift': None
                    },
                    {
                        'name': 'kill_mermaid',
                        'description': 'Druid: I know you do not kill the innocent but we may have no other choice. '
                                       'Bring mermaids blood so that we can put magic into your wand.',
                        'artefact': 'Mermaids blood',
                        'points': 15,
                        'npc_give_task': 'Druid',
                        'npc_take_artifact': 'Druid',
                        'next_npc': None, #Druid?
                        'gift': None
                    },
                    {
                        'name': 'kill_vampire',
                        'description': 'Druid: There is one more thing we need. Do not get scared... Vampires fang. '
                                       'Kill the vampire and bring its venomous fang back.',
                        'artefact': 'Vampires fang',
                        'points': 15,
                        'npc_give_task': 'Druid',
                        'npc_take_artifact': 'Druid',
                        'next_npc': None,
                        'gift': 'wand'
                    }
                ]
                # outcome: More mana?
            },
            # Quest 2
            'make_a_companion': {
                'name': 'make_a_companion',
                'description': 'Good wizards do not tend to travel the realm solo. Make a donkey your companion.',
                'points': 50,
                'tasks': [
                    {
                        'name': 'gold',
                        'description': 'Donkey: I am so lonely! I want to travel the world with you! But you have to '
                                       'find a way to put me in your backpack! I think you should ask the Dark Elves '
                                       'to help you... ',
                        'artefact': 'Mud',
                        'points': 15,
                        'npc_give_task': 'Donkey',
                        'npc_take_artifact': None,
                        'next_npc': 'Dark Elf',
                        'gift': None
                    },
                    {
                        'name': 'get mud',
                        'description': 'Dark Elf: Ohh... I know a solution to that. You have to give donkey so much '
                                       'mud that he will turn into stone. Mud? Oh thats orcs water. Find their land '
                                       'and you will find mud..',
                        'artefact': 'Mud', # mud laying in the swamp to collect it
                        'points': 20,
                        'npc_give_task': 'Dark Elf',
                        'npc_take_artifact': 'Donkey',
                        'next_npc': 'Donkey', #?
                        'gift': 'stone donkey'
                    }

                ]
            },
            # Quest 3
            'make_healing_potion': {
                'name': 'make_healing_potion',
                'description': 'You are a wizard. You can make potions. Try it.',
                'points': 60,
                'tasks': [
                    {
                        'name': 'obtain_flame',
                        'description': 'Faerie: Kill the fire elemental so that you have a flame.',
                        'artefact': 'Flame',
                        'points': 20,
                        'npc_give_task': 'Faerie',
                        'npc_take_artifact': 'Faerie',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'obtain_earth',
                        'description': 'Faerie: Great! Now please kill an earth elemental.',
                        'artefact': 'Earth',
                        'points': 20,
                        'npc_give_task': 'Faerie',
                        'npc_take_artifact': 'Faerie',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'powder_of_faeries',
                        'description': 'Faerie: Great! Now the trickiest one. Ask little faeries for their magic '
                                       'powder.',
                        'artefact': 'Magic powder',
                        'points': 20,
                        'npc_give_task': 'Faerie',
                        'npc_take_artifact': 'Faerie',
                        'next_npc': 'Little faeries',
                        'gift': 'Healing potion'
                    },
                    { # tutaj chodzi o to, zeby byl dialog, po prostu prosisz i dostajesz powder i masz healing potion
                        'name': 'little_faeries',
                        'description': 'Little faerie: What do you want? I sense you are a good person.',
                        'artefact': 'Magic powder',
                        'points': 20,
                        'npc_give_task': 'Faerie',
                        'npc_take_artifact': 'Faerie',
                        'next_npc': None,
                        'gift': 'Magic powder'
                    }
                ]
            },
            # Quest 4
            'beat_dark_wizards': {
                'name': 'beat_dark_wizards',
                'description': 'You’d better prepare for the ultimate adventure of yours. How to do that? Better make '
                               'friends with magic itself. Find a Druid.',
                'points': 70,
                'tasks': [
                    {
                        'name': 'gold_for_druid',
                        'description': 'Druid: Well, well, well. You want our help in beating dark wizards? As they '
                                       'say - Nothing comes for free fellow wizard. '
                                       'Bring me some gold which you will probably obtain by dealing with Leprechaun...',
                        'artefact': 'Gold Bar',
                        'points': 20,
                        'npc_give_task': 'Druid',
                        'npc_take_artifact': 'Druid',
                        'next_npc': 'Leprechaun',
                        'gift': None
                    },
                    {  # dialog ?
                        'name': 'leprechaun_gold',
                        'description': 'Leprechaun: I will give you gold if you ask me nicely...',
                        'artefact': 'Gold Bar',
                        'points': 20,
                        'npc_give_task': 'Leprechaun', #?
                        'npc_take_artifact': 'Druid',
                        'next_npc': 'Druid',
                        'gift': None
                    },
                    {
                        'name': 'bring_fire',
                        'description': 'Druid: Thank you for the gold. You have druids providence. Now lets find '
                                       'those bloody bastards. You should follow the spiders...',
                        'artefact': 'spiders web',
                        'points': 20,
                        'npc_give_task': 'Druid',
                        'npc_take_artifact': 'Druid',
                        'next_npc': 'Spider',
                        'gift': None
                    },
                    { # dialog
                        'name': 'follow_the_web',
                        'description': 'Spider: You want to find dark wizards? Follow our web and kill them.',
                        'artefact': 'wand',
                        'points': 20,
                        'npc_give_task': 'Spider',
                        'npc_take_artifact': None,
                        'next_npc': None,
                        'gift': None
                    }
                ]
            }
        },
        'evil': {
            # Quest 1
            'destroy_specular_lake': {
                'name': 'destroy_primeval_bush',
                'description': 'Your journey here will focus on doing bad, bad things... Lets start with eliminating '
                               'some of the innocent. Go kill the mermaid first.',
                'points': 20,
                'tasks': [
                    {
                        'name': 'kill_mermaid',
                        'description': 'Dark Wizard: Kill the mermaid so that you have their fur.',
                        'artefact': 'Mermaid necklace',
                        'points': 15,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'kill_big_fishes',
                        'description': 'Kill the big fish so that you have something to eat.',
                        'artefact': 'fish',
                        'points': 15,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'kill_crabs',
                        'description': 'Last ones! The crabs! Kill the crabs and specular lakes will be completely '
                                       'under your surveillance. ',
                        'artefact': 'crabs corpse',
                        'points': 15,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': 'healing potion'
                    }
                ]
            },
            # Quest 2
            'steal_the_gold': {
                'name': 'the_thief',
                'description': 'As you are evil, your task will be to become a thief. See the Dragon.',
                'points': 50,
                'tasks': [
                    {
                        'name': 'thief_gorilla',
                        'description': 'Dragon: Dragons love to be wealthy. You know what do do. First -  gorillas '
                                       'stolen gem.',
                        'artefact': 'The Greatest Gem of Dwarven Empire',
                        'points': 10,
                        'npc_give_task': 'Dragon',
                        'npc_take_artifact': 'Dragon',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'description': 'Dragon: Thank you for the gem. Next step -  mermaid.'
                                       'stolen gem.',
                        'artefact': 'mermaid necklace',
                        'points': 10,
                        'npc_give_task': 'Dragon',
                        'npc_take_artifact': 'Dragon',
                        'next_npc': None,
                        'gift': None

                    },
                    {
                        'description': 'Dragon: Lastly... gold... lots of gold. Leprechaun!',
                        'artefact': 'pot of gold',
                        'points': 10,
                        'npc_give_task': 'Dragon',
                        'npc_take_artifact': 'Dragon',
                        'next_npc': None,
                        'gift': 'flame'
                    }
                ]
            },
            # Quest 3
            'trick_orcs': {
                'name': 'stinky_orcs',
                'description': 'Now your task is to trick orcs into giving you more power. See them for the clues.',
                'points': 60,
                'tasks': [
                    {
                        'name': 'clean_feet',
                        'description': 'Orcs: You want what? Regain your life? Ha ha ha... Fine, but you have to do '
                                       'couple '
                                       'of things first. For example... Clean my feet! Take water from Specular Lake.',
                        'artefact': 'Water',
                        'points': 15,
                        'npc_give_task': 'Orc',
                        'npc_take_artifact': 'Orc',
                        'next_npc': None,
                        'gift': 'Life potion'
                    }
                ]
            },
            # Quest 4
            'prove_your_worth': {
                'name': 'prove_your_worth',
                'description': 'Dark Wizard: There we are. It’s time to prove that you are worthy to join us. ',
                'points': 100,
                'tasks': [
                    {
                        'name': 'find_leaves',
                        'description': 'Dark Wizard: Find the amazons. Next to them, there are leaves sealed '
                                       'with dark magic. Kill the amazons, find the leaves and bring them to us.',
                        'artefact': 'Leaf',
                        'points': 20,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'bravery',
                        'description': 'Dark Wizard: Now bring as much tigers meet as possible. We have to eat.',
                        'artefact': 'Tigers Meat',
                        'points': 15,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'tools',
                        'description': 'Dark Wizard: There is one more thing that we need. We require you to bring '
                                       'skin of a dead snake.',
                        'artefact': 'Snake Skin',
                        'points': 15,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': None
                    }
                ]
            }
        }
    },
    'Barbarian': {
        # Quest 1 - True Barbarian
        'good': {
            'true_barbarian': {
                'name': 'true_barbarian',
                'side': 'good',
                'description': 'You have just become a newly trained Barbarian. You are young and strong, but you are '
                               'missing a certain thing that will make you a true barbarian. It is time for you to '
                               'get your own '
                               'powerful weapon that will accompany you to the end of your days. To find out more, '
                               'find a blacksmith in the village and ask him for details.',
                'points': 20,
                'tasks': [
                    {
                        'name': 'new_weapon',
                        'description': 'A brave and mighty warrior like you needs a powerful weapon. But for that, '
                                       'you will need a magical crystal that is guarded by fairies. Head to their '
                                       'land, where various magical creatures lurk, and find a magic crystal to '
                                       'upgrade your sword, some of the faeries can be helpful. Take it to the '
                                       'blacksmith and show '
                                       'patience.',
                        'artefact': 'Magical Crystal',
                        'points': 15,
                        'npc_give_task': 'Smith',
                        'npc_take_artifact': 'Smith',
                        'next_npc': 'Faerie',
                        'gift': 'New Sword'
                    },
                    {
                        'name': 'evil_spiders',
                        'description': 'One of the dark spiders, dared to enter the land of fairies and ate one of us! As '
                                       'fairies, we are a very tasty snack. What is worse, the news spread and now another '
                                       'spider is trying to invade our magical territory. Help us by killing spider '
                                       'and bringing to us his fang. Then you will get the magical crystal.',
                        'artefact': 'Spider Fang',
                        'points': 10,
                        'npc_give_task': 'Faerie',
                        'npc_take_artifact': 'Faerie',
                        'next_npc': None,
                        'gift': 'Magical Crystal'
                    }
                ]
            },
            # Quest 2 - Prove your worth
            'prove_worth': {
                'name': 'prove_worth',
                'side': 'good',
                'description': 'Now that you have a powerful weapon, it\'s time to make use of it. Head to the nearby lands '
                               'and see if you can be of some service to the people there, starting with the village of the '
                               'Great People.',
                'points': 40,
                'tasks': [
                    {
                        'name': 'save_the_villagers',
                        'description': 'Oh no! The Blacksmith has run out of materials with which to build a new '
                                       'house for the settlers, if he does not get stones as soon as possible, '
                                       'the villagers will get sick from lack of a roof over their heads or worse, '
                                       'die…Stones… sound similar to the Earth Element remains from the Desolation of '
                                       'Abomination, go and kill him.',
                        'artefact': 'Stones',
                        'points': 10,
                        'npc_give_task': 'Smith',
                        'npc_take_artifact': 'Smith',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'kill_ravens',
                        'description': 'For several days now, Big Ravens have been destroying the villagers\' harvest. They '
                                       'can\'t cope with them alone and need a big strong hero to do the job for them. Kill '
                                       'the ravens and bring its feathers to the Farmer.',
                        'artefact': 'Raven Feathers',
                        'points': 15,
                        'npc_give_task': 'Farmer',
                        'npc_take_artifact ': 'Farmer',
                        'next_npc ': None,
                        'gift': None
                    },
                    {
                        'name': 'feed_wild_tiger',
                        'description': 'Dark times have come, evil is spreading faster and faster through the world and its '
                                       'corruption is infecting various creatures, which are beginning to go wild. Only a '
                                       'brave hero, who has savagery written in his blood, will be able to cure the sick '
                                       'creature. Maybe the tiger is hungry..? He feeds on the meat of Big Ravens. After finishing this task, your life will '
                                       'increase by 20.',
                        'artefact': 'Raven Meat',
                        'points': 15,
                        'npc_give_task': 'Amazon',
                        'npc_take_artifact': 'Tiger',
                        'next_npc': None,
                        'gift': None
                    },
                    {
                        'name': 'tiger_magic_necklace',
                        'description': 'There are rumours that the spiritual connection is one big scam. Show everyone that '
                                       'they are wrong and find your animal in the deep wilderness and convince him to give '
                                       'you one of the magic necklaces, which allows him to communicate with you. Go '
                                       'for necklace and bring it back to Farmer to prove your connection with your '
                                       'Spirit Animal.',
                        'artefact': 'Magic Necklace',
                        'points': 15,
                        'npc_give_task': 'Farmer',
                        'npc_take_artifact': 'Farmer',
                        'next_npc': 'Tiger',
                        'gift': None
                    },
                    {
                        'name': 'poor_tiger',
                        'description': 'The Snake has bitten the poor Tiger for a long time, and he cannot go on like '
                                       'this anymore. Kill the Snake and bring back its skin as evidence and then '
                                       'your Spirit Animal will give you a Magic Necklace.',
                        'artefact': 'Snake Skin',
                        'points': 15,
                        'npc_give_task': 'Tiger',
                        'npc_take_artifact': 'Tiger',
                        'next_npc': None,
                        'gift': 'Magic Necklace'
                    }
                ]
            }
        },
        'evil': {
            # Quest 1 - Power and disruption
            'power_and_disruption': {
                'name': 'power_and_disruption',
                'side': 'evil',
                'description': '',
                'points': 30,
                'tasks': [
                    {
                        'name': 'berserk_blessing',
                        'description': 'To stay in touch with the source of your supernatural power, you must regularly '
                                       'sacrifice the most venomous snake. No one knows where their hiding place is... except '
                                       'the Dark Wizard. Go to him and find out more, try not to come back with a curse. If '
                                       'you would finish the task, your power will increase by 10.',
                        'artefact': 'Snake Skin',
                        'points': 15,
                        'npc_give_task': 'Druid',
                        'npc_take_artifact': 'Druid',
                        'next_npc': 'Dark Wizard',
                        'gift': None
                    },
                    {
                        'name': 'prove_strength',
                        'description': 'News of your power has spread throughout the land, but there will be those who do not '
                                       'believe it without proof.... Prove the Dark Wizard, one of the most powerful dark '
                                       'beings, wrong, defeat the dragon and bring him his eyeball. If you\'ll achieve it, '
                                       'maybe he will fulfil one of your wishes.',
                        'artefact': 'Dragon Eyeball',
                        'points': 20,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': 'Snake Skin'
                    },
                    {
                        'name': 'evil_and_allies',
                        'description': 'Your greatest enemy is the good barbarians, they spread goodness and help... The '
                                       'opposite of what you represent. Don\'t let them be the ones to win this eternal war '
                                       'between the sides of good and evil. Go to the wilderness, find a tiger and bring its '
                                       'fur to the Orc who is your ally.',
                        'artefact': 'Tiger Fur',
                        'points': 15,
                        'npc_give_task': 'Orc',
                        'npc_take_artifact': 'Orc',
                        'next_npc': None,
                        'gift': 'Unicorn Horn'
                    }
                ]
            },
            # Quest 2 - Money, money, money…
            'money_money': {
                'name': 'money_money',
                'side': 'evil',
                'description': '',
                'points': 25,
                'tasks': [
                    {
                        'name': 'kill_orc',
                        'description': 'The orcs were your allies, but you decided that you want their mace, and they would '
                                       'not voluntarily give it up... Stand in battle with an orc, defeat him and take his '
                                       'mace. Exchange it for Purple Gem at the blacksmith.',
                        'artefact': 'Orc Mace',
                        'points': 20,
                        'npc_give_task': 'Smith',
                        'npc_take_artifact': 'Smith',
                        'next_npc': None,
                        'gift': 'Purple Gem'
                    },
                    {
                        'name': 'never_enough_gold',
                        'description': 'You love gold, and it just so happens that the Leprikons have too much of it, '
                                       'well why do they need so much anyway? If one pot disappears for them nothing '
                                       'will '
                                       'happen... Find a pot of gold that belongs to a Leprechaun and steal it, '
                                       'take the gold, and sell the pot to a dark wizard.',
                        'artefact': 'Pot',
                        'points': 5,
                        'npc_give_task': 'Dark Wizard',
                        'npc_take_artifact': 'Dark Wizard',
                        'next_npc': None,
                        'gift': 'Magic Potion'
                    }
                ]
            }
        }
    },
    'Elf': {
        'good': {
            # Quest 1
            'get_healing_potion ': {
                'name': 'get_healing_potion',
                'description': 'It is not too late to safe the sacred oak and the land of Magic. You can be the hero '
                               'that is so needed, but you’ll have too show your bravery, wisdom and cleverness. The '
                               'first step of your journey is the dreary Forest were the Dark Wizard prepares the '
                               'healing potion you’ll need.',
                'points': 40,
                'tasks': [
                    {
                        'name': 'gold_leprechaun_fight',
                        'description': 'Healing potion is hard too prepare. Not only will it need multiple uncommon '
                                       'ingredients, but it’ll cost you. If you don’t have a Leprechaun’s gold, '
                                       'you’ll have to get it.',
                        'artefact': 'Gold Bar',
                        'points': 10,
                        'npc_give_task ': 'Dark Wizard',
                        'npc_take_artifact ': 'Dark Wizard',
                        'next_npc ': 'Leprechaun',
                        'gift': None
                    },
                    {
                        'name': 'wheat_from_monsters',
                        'description': 'Gold is Leprechaun’s greatest and most beloved treasure, but even he will '
                                       'part with it for the right price. His land suffers, the drops has diet and '
                                       'the great hunger is spreading among fellow inhabitants. Bring him some wheat '
                                       'from the wheat monsters and you will get the gold.',
                        'artefact': 'Wheat',
                        'points': 10,
                        'npc_give_task ': 'Leprechaun',
                        'npc_take_artifact ': 'Leprechaun',
                        'next_npc ': 'Dark Wizard',
                        'gift': 'Gold Bar'
                    },
                    {
                        'name': 'fight_the_dragon',
                        'description': 'Now that you’ve paid, the Dark Wizard will judge if you are worthy of his '
                                       'help. You will face the challenges that defeated the wisest, the fights that '
                                       'killed the strongest. It’s time for the first one. The Dark Wizard need the '
                                       'dragon’s eyeballs for the potion, find it and kill.',
                        'artefact': 'Dragon Eyeball',
                        'points': 25,
                        'npc_give_task ': 'Dark Wizard',
                        'npc_take_artifact ': 'Dark Wizard',
                        'next_npc ': 'Fairies',
                        'gift': None
                    },
                    {
                        'name': 'fairies_magic_dust',
                        'description': 'Fairies are often dismissed as small and weak, but their magic is powerfull. '
                                       'Even a handful of a fairy’s dust can cause miracles. Go to the Fairies and '
                                       'ask them for a sprinkle of their magic  dust.',
                        'artefact': 'Magic Dust',
                        'points': 20,
                        'npc_give_task ': 'Dark Wizard',
                        'npc_take_artifact ': 'Dark Wizard',
                        'next_npc ': 'Dark Wizard',
                        'gift': 'Healing Potion'
                    },
                    {
                        'name': 'kill_the_gorilla',
                        'description': 'The fairies found your intentions as noble and want to help you in your '
                                       'mission. But the forces of darkness influenced the wilderness, causing the '
                                       'animals to go mad and attacking their brothers and sisters. Kill the great '
                                       'gorilla to save them from becoming its food, and bring its heart as a totem.',
                        'artefact': 'Monke Heart',
                        'points': 20,
                        'npc_give_task ': 'Faerie',
                        'npc_take_artifact ': 'Faerie',
                        'next_npc ': 'Treant',
                        'gift': 'Magic Dust'
                    },
                    {
                        'name': 'pour_potion_oak',
                        'description': 'You now have a potion that can stop the illness of the sacred oak. Find the '
                                       'treant and pour the potion on it.',
                        'artefact': 'Healing Potion',
                        'points': 20,
                        'npc_give_task ': 'Treant',
                        'npc_take_artifact ': 'Treant',
                        'next_npc ': None,
                        'gift': None
                    }

                ]
            },
            # Quest 2
                'help_restore_land ': {
                    'name': 'help_restore_land',
                    'description': 'You may have healed the sacred Treant that keeps the balance of good and evil, but harm was already done. The crops suffered and soon people of Medieville will starve. Help them and their Farmers.',
                    'points': 25,
                    'tasks': [
                        {
                            'name': 'talk_to_farmer',
                            'description': 'All the crops are destroyed. The dark fire burnt them to the ground. There is nothing to eat, nothing to sow. But there still is hope. Wheat monsters have wheat that with a little soil can grow and save us.',
                            'artefact': 'Wheat',
                            'points': 20,
                            'npc_give_task ': 'Farmer',
                            'npc_take_artifact ': None,
                            'next_npc ': 'Farmer',
                            'gift': None
                        },
                        {
                            'name': 'get_some_wheat',
                            'description': 'The wheat will be useful for sure. But we cannot only eat bread. Some vegetables would be better for our well being as well as health. Find the running vegetables and bring them to us.',
                            'artefact': '',
                            'points': 20,
                            'npc_give_task ': 'Farmer',
                            'npc_take_artifact ': 'Farmer',
                            'next_npc ': None,
                            'gift': 'Vegetables'
                        }
                    ]
                }
            },
            'evil': {
                'get_incantation_scroll': {
                    'name': 'get_incantation_scroll',
                    'description': "You decided to come to the dark side. But you are still new in the ways of evil. You are gonna need some teaching and a person to do that would be a Dark Elf, who once was in your place.",
                    'points': 40,
                    'tasks': [
                        {
                            'name': 'get_the_incantation',
                            'description': "The evil incantation that you're preparing yourself to perform won't happen "
                                           "without the spell you need to cast. But right now its the Dark Wizard who "
                                           "has the scroll you need. Find him.",
                            'artefact': 'Incantation Scroll',
                            'points': 10,
                            'npc_give_task ': 'Dark Elf',
                            'npc_take_artifact ': 'Dark Elf',
                            'next_npc ': 'Dark Wizard',
                            'gift': None
                        },
                        {
                            'name': 'kill_the_tiger',
                            'description': "The Dark Wizard knows the scroll you want well. He learnt everything from it by heart a long time ago. He does not need it anymore, but nothing is free in this world. He will give you the scroll in exchange for the necklace that is guarded by the Tiger.",
                            'artefact': 'Tiger Necklace',
                            'points': 10,
                            'npc_give_task ': 'Dark Wizard',
                            'npc_take_artifact ': 'Dark Wizard',
                            'next_npc ': None,
                            'gift': 'Incantation Scroll'
                        }
                    ]
                },
                'get_immortality ': {
                    'name': 'get_immortality',
                    'description': "Whispers say you seek immortality. The road to it is long and not easy. You'll face "
                                   "challenges, fight enemies from the nightmares, face the god of destruction, "
                                   "but if you have what it takes, you'll get what you want. The Dark Elf, as creatures of "
                                   "the night can help you start your journey.",
                    'points': 40,
                    'tasks': [
                        {
                            'name': 'kill_the_raven',
                            'description': 'Vampire knows only one way of gaining immortality, besides being born with '
                                           'it. It requires a dangerous ritual, that many tried to follow, but failed. '
                                           'But if you will persevere you will be rewarded. But first, you need to get '
                                           'the blood of a big Raven scaring the people of Medieville.',
                            'artefact': 'Raven Blood',
                            'points': 20,
                            'npc_give_task ': 'Dark Elf',
                            'npc_take_artifact ': 'Dark Elf',
                            'next_npc ': 'Vampire',
                            'gift': None
                        },
                        {
                            'name': 'sage_from_forest',
                            'description': "Blood was just a first step of many on your way. But not every of them "
                                           "requires you to dirty your hands. This time your predator instincts won't be "
                                           "needed. All you need to do is asked the Amazon for some sage, because it's "
                                           "not news that plants have powerful magic capabilities. Then you need to give it to the Druid for their sacred fire",
                            'artefact': None,
                            'points': 10,
                            'npc_give_task ': 'Dark Elf',
                            'npc_take_artifact ': 'Dark Elf',
                            'next_npc ': 'Amazon',
                            'gift': None,
                        },
                        {
                            'name': 'kill_yeti',
                            'description': "Sage is one of the gifts of the wild. Amazon can not only give it to you, they can show you when to look for it, but you need pay the price for that useful gift and lesson and the price is a skin of yeti.",
                            'artefact': 'Yeti Skin',
                            'points': 10,
                            'npc_give_task ': 'Amazon',
                            'npc_take_artifact ': 'Amazon',
                            'next_npc ': 'Druid',
                            'gift': 'Sage',
                        },
                        {
                            'name': 'get_sacred_fire',
                            'description': "Amazons offered you their help when you did them a favour. The sage they gave you will help you get "
                                           "some sacred fire from the Druids. Beware they are the balance keepers and "
                                           "they serve the powers of light. If you want to live, you better drink the "
                                           "potion.",
                            'artefact': 'Sage',
                            'points': 10,
                            'npc_give_task ': 'Dark Elf',
                            'npc_take_artifact ': 'Druid',
                            'next_npc ': 'Dark Elf',
                            'gift': 'Sacred Fire'
                        },
                        {
                            'name': 'voice_of_mermaid',
                            'description': "You're almost there. Keep going and don't loose courage. Find the beaches of "
                                           "the lake and those who live there. Their voice can maim you, but it's power "
                                           "is exactly what you're going to need. Steal the creatures necklace, "
                                           "cause it hides the true magic of their voice.",
                            'artefact': 'Mermaid Necklace',
                            'points': 10,
                            'npc_give_task ': 'Dark Elf',
                            'npc_take_artifact ': 'Dark Elf',
                            'next_npc ': 'Dark Elf',
                            'gift': 'Magic Blood'
                        },
                        {
                            'name': 'prepare_magic_blood',
                            'description': "You brought everything needed to make a magic blood for a Vampire that is the only one that can give you the immortality. We will now prepare it according to the recipe on the scroll you obtained. When its ready, take it to the Vampire and exchange for your immortality.",
                            'artefact': 'Magic Blood',
                            'points': 10,
                            'npc_give_task ': 'Dark Elf',
                            'npc_take_artifact ': 'Vampire',
                            'next_npc ': None,
                            'gift': 'Immortality Potion'
                        }

                    ]
                }
            }
    }
}





