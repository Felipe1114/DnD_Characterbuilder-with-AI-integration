**class_data for Ranger**:

```
Base_data_for_class:  
"""  
{  
        "index": "ranger",  
        "name": "Ranger",  
        "hit_die": 10,  
        "proficiency_choices": [  
            {  
                "desc": "Choose three from Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, and Survival",  
                "choose": 3,  
                "type": "proficiencies",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-animal-handling",  
                                "name": "Skill: Animal Handling",  
                                "url": "/api/2014/proficiencies/skill-animal-handling"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-athletics",  
                                "name": "Skill: Athletics",  
                                "url": "/api/2014/proficiencies/skill-athletics"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-insight",  
                                "name": "Skill: Insight",  
                                "url": "/api/2014/proficiencies/skill-insight"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-investigation",  
                                "name": "Skill: Investigation",  
                                "url": "/api/2014/proficiencies/skill-investigation"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-nature",  
                                "name": "Skill: Nature",  
                                "url": "/api/2014/proficiencies/skill-nature"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-perception",  
                                "name": "Skill: Perception",  
                                "url": "/api/2014/proficiencies/skill-perception"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-stealth",  
                                "name": "Skill: Stealth",  
                                "url": "/api/2014/proficiencies/skill-stealth"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-survival",  
                                "name": "Skill: Survival",  
                                "url": "/api/2014/proficiencies/skill-survival"  
                            }  
                        }  
                    ]  
                }  
            }  
        ],  
        "proficiencies": [  
            {  
                "index": "light-armor",  
                "name": "Light Armor",  
                "url": "/api/2014/proficiencies/light-armor"  
            },  
            {  
                "index": "medium-armor",  
                "name": "Medium Armor",  
                "url": "/api/2014/proficiencies/medium-armor"  
            },  
            {  
                "index": "shields",  
                "name": "Shields",  
                "url": "/api/2014/proficiencies/shields"  
            },  
            {  
                "index": "simple-weapons",  
                "name": "Simple Weapons",  
                "url": "/api/2014/proficiencies/simple-weapons"  
            },  
            {  
                "index": "martial-weapons",  
                "name": "Martial Weapons",  
                "url": "/api/2014/proficiencies/martial-weapons"  
            },  
            {  
                "index": "saving-throw-dex",  
                "name": "Saving Throw: DEX",  
                "url": "/api/2014/proficiencies/saving-throw-dex"  
            },  
            {  
                "index": "saving-throw-str",  
                "name": "Saving Throw: STR",  
                "url": "/api/2014/proficiencies/saving-throw-str"  
            }  
        ],  
        "saving_throws": [  
            {  
                "index": "str",  
                "name": "STR",  
                "url": "/api/2014/ability-scores/str"  
            },  
            {  
                "index": "dex",  
                "name": "DEX",  
                "url": "/api/2014/ability-scores/dex"  
            }  
        ],  
        "starting_equipment": [  
            {  
                "equipment": {  
                    "index": "longbow",  
                    "name": "Longbow",  
                    "url": "/api/2014/equipment/longbow"  
                },  
                "quantity": 1  
            },  
            {  
                "equipment": {  
                    "index": "arrow",  
                    "name": "Arrow",  
                    "url": "/api/2014/equipment/arrow"  
                },  
                "quantity": 20  
            }  
        ],  
        "starting_equipment_options": [  
            {  
                "desc": "(a) scale mail or (b) leather armor",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "scale-mail",  
                                "name": "Scale Mail",  
                                "url": "/api/2014/equipment/scale-mail"  
                            }  
                        },  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "leather-armor",  
                                "name": "Leather Armor",  
                                "url": "/api/2014/equipment/leather-armor"  
                            }  
                        }  
                    ]  
                }  
            },  
            {  
                "desc": "(a) two shortswords or (b) two simple melee weapons",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 2,  
                            "of": {  
                                "index": "shortsword",  
                                "name": "Shortsword",  
                                "url": "/api/2014/equipment/shortsword"  
                            }  
                        },  
                        {  
                            "option_type": "choice",  
                            "choice": {  
                                "desc": "two simple melee weapons",  
                                "choose": 2,  
                                "type": "equipment",  
                                "from": {  
                                    "option_set_type": "equipment_category",  
                                    "equipment_category": {  
                                        "index": "simple-melee-weapons",  
                                        "name": "Simple Melee Weapons",  
                                        "url": "/api/2014/equipment-categories/simple-melee-weapons"  
                                    }  
                                }  
                            }  
                        }  
                    ]  
                }  
            },  
            {  
                "desc": "(a) a dungeoneer\u2019s pack or (b) an explorer\u2019s pack",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "dungeoneers-pack",  
                                "name": "Dungeoneer's Pack",  
                                "url": "/api/2014/equipment/dungeoneers-pack"  
                            }  
                        },  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "explorers-pack",  
                                "name": "Explorer's Pack",  
                                "url": "/api/2014/equipment/explorers-pack"  
                            }  
                        }  
                    ]  
                }  
            }  
        ],  
        "class_levels": "/api/2014/classes/ranger/levels",  
        "multi_classing": {  
            "prerequisites": [  
                {  
                    "ability_score": {  
                        "index": "dex",  
                        "name": "DEX",  
                        "url": "/api/2014/ability-scores/dex"  
                    },  
                    "minimum_score": 13  
                },  
                {  
                    "ability_score": {  
                        "index": "wis",  
                        "name": "WIS",  
                        "url": "/api/2014/ability-scores/wis"  
                    },  
                    "minimum_score": 13  
                }  
            ],  
            "proficiencies": [  
                {  
                    "index": "light-armor",  
                    "name": "Light Armor",  
                    "url": "/api/2014/proficiencies/light-armor"  
                },  
                {  
                    "index": "medium-armor",  
                    "name": "Medium Armor",  
                    "url": "/api/2014/proficiencies/medium-armor"  
                },  
                {  
                    "index": "shields",  
                    "name": "Shields",  
                    "url": "/api/2014/proficiencies/shields"  
                },  
                {  
                    "index": "simple-weapons",  
                    "name": "Simple Weapons",  
                    "url": "/api/2014/proficiencies/simple-weapons"  
                },  
                {  
                    "index": "martial-weapons",  
                    "name": "Martial Weapons",  
                    "url": "/api/2014/proficiencies/martial-weapons"  
                }  
            ],  
            "proficiency_choices": [  
                {  
                    "choose": 1,  
                    "type": "proficiencies",  
                    "from": {  
                        "option_set_type": "options_array",  
                        "options": [  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-animal-handling",  
                                    "name": "Skill: Animal Handling",  
                                    "url": "/api/2014/proficiencies/skill-animal-handling"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-athletics",  
                                    "name": "Skill: Athletics",  
                                    "url": "/api/2014/proficiencies/skill-athletics"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-insight",  
                                    "name": "Skill: Insight",  
                                    "url": "/api/2014/proficiencies/skill-insight"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-investigation",  
                                    "name": "Skill: Investigation",  
                                    "url": "/api/2014/proficiencies/skill-investigation"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-nature",  
                                    "name": "Skill: Nature",  
                                    "url": "/api/2014/proficiencies/skill-nature"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-perception",  
                                    "name": "Skill: Perception",  
                                    "url": "/api/2014/proficiencies/skill-perception"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-stealth",  
                                    "name": "Skill: Stealth",  
                                    "url": "/api/2014/proficiencies/skill-stealth"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-survival",  
                                    "name": "Skill: Survival",  
                                    "url": "/api/2014/proficiencies/skill-survival"  
                                }  
                            }  
                        ]  
                    }  
                }  
            ]  
        },  
        "subclasses": [  
            {  
                "index": "hunter",  
                "name": "Hunter",  
                "url": "/api/2014/subclasses/hunter"  
            }  
        ],  
        "spellcasting": {  
            "level": 2,  
            "spellcasting_ability": {  
                "index": "wis",  
                "name": "WIS",  
                "url": "/api/2014/ability-scores/wis"  
            },  
            "info": [  
                {  
                    "name": "Spell Slots",  
                    "desc": [  
                        "The Ranger table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.",  
                        "For example, if you know the 1st-level spell animal friendship and have a 1st-level and a 2nd-level spell slot available, you can cast animal friendship using either slot."  
                    ]  
                },  
                {  
                    "name": "Spells Known of 1st Level and Higher",  
                    "desc": [  
                        "You know two 1st-level spells of your choice from the ranger spell list.",  
                        "The Spells Known column of the Ranger table shows when you learn more ranger spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 5th level in this class, you can learn one new spell of 1st or 2nd level.",  
                        "Additionally, when you gain a level in this class, you can choose one of the ranger spells you know and replace it with another spell from the ranger spell list, which also must be of a level for which you have spell slots."  
                    ]  
                },  
                {  
                    "name": "Spellcasting Ability",  
                    "desc": [  
                        "Wisdom is your spellcasting ability for your ranger spells, since your magic draws on your attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a ranger spell you cast and when making an attack roll with one.",  
                        "Spell save DC = 8 + your proficiency bonus + your Wisdom modifier.",  
                        "Spell attack modifier = your proficiency bonus + your Wisdom modifier."  
                    ]  
                }  
            ]  
        },  
        "spells": "/api/2014/classes/ranger/spells",  
        "url": "/api/2014/classes/ranger"  
    }  
"""  
      
  
level_features:  
"""  
[  
    [  
        {  
            "level": 1,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "favored-enemy-1-type",  
                    "name": "Favored Enemy (1 type)",  
                    "details": {  
                        "index": "favored-enemy-1-type",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (1 type)",  
                        "level": 1,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-1-type",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "natural-explorer-1-terrain-type",  
                    "name": "Natural Explorer (1 terrain type)",  
                    "details": {  
                        "index": "natural-explorer-1-terrain-type",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (1 terrain type)",  
                        "level": 1,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-1-terrain-type",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 0,  
                "spell_slots_level_1": 0,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-1"  
        },  
        {  
            "level": 2,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-fighting-style",  
                    "name": "Fighting Style",  
                    "details": {  
                        "index": "ranger-fighting-style",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Fighting Style",  
                        "level": 2,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 2nd level, you adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again."  
                        ],  
                        "feature_specific": {  
                            "subfeature_options": {  
                                "choose": 1,  
                                "type": "feature",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-archery",  
                                                "name": "Fighting Style: Archery",  
                                                "url": "/api/2014/features/ranger-fighting-style-archery"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-defense",  
                                                "name": "Fighting Style: Defense",  
                                                "url": "/api/2014/features/ranger-fighting-style-defense"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-dueling",  
                                                "name": "Fighting Style: Dueling",  
                                                "url": "/api/2014/features/ranger-fighting-style-dueling"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-two-weapon-fighting",  
                                                "name": "Fighting Style: Two-Weapon Fighting",  
                                                "url": "/api/2014/features/ranger-fighting-style-two-weapon-fighting"  
                                            }  
                                        }  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/ranger-fighting-style",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "spellcasting-ranger",  
                    "name": "Spellcasting: Ranger",  
                    "details": {  
                        "index": "spellcasting-ranger",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Spellcasting: Ranger",  
                        "level": 2,  
                        "prerequisites": [],  
                        "desc": [  
                            "By the time you reach 2nd level, you have learned to use the magical essence of nature to cast spells, much as a druid does."  
                        ],  
                        "reference": "/api/2014/classes/ranger/spellcasting",  
                        "url": "/api/2014/features/spellcasting-ranger",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 2,  
                "spell_slots_level_1": 2,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-2"  
        },  
        {  
            "level": 3,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-archetype",  
                    "name": "Ranger Archetype",  
                    "details": {  
                        "index": "ranger-archetype",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ranger Archetype",  
                        "level": 3,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 3rd level, you choose an archetype that you strive to emulate, such as the Hunter. Your choice grants you features at 3rd level and again at 7th, 11th, and 15th level."  
                        ],  
                        "url": "/api/2014/features/ranger-archetype",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "primeval-awareness",  
                    "name": "Primeval Awareness",  
                    "details": {  
                        "index": "primeval-awareness",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Primeval Awareness",  
                        "level": 3,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 3rd level, you can use your action and expend one ranger spell slot to focus your awareness on the region around you. For 1 minute per level of the spell slot you expend, you can sense whether the following types of creatures are present within 1 mile of you (or within up to 6 miles if you are in your favored terrain): aberrations, celestials, dragons, elementals, fey, fiends, and undead. This feature doesn't reveal the creatures' location or number."  
                        ],  
                        "url": "/api/2014/features/primeval-awareness",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 3,  
                "spell_slots_level_1": 3,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-3"  
        },  
        {  
            "level": 4,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-1",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-1",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 4,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-1",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 3,  
                "spell_slots_level_1": 3,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-4"  
        },  
        {  
            "level": 5,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "ranger-extra-attack",  
                    "name": "Extra Attack",  
                    "details": {  
                        "index": "ranger-extra-attack",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Extra Attack",  
                        "level": 5,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."  
                        ],  
                        "url": "/api/2014/features/ranger-extra-attack",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 4,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 2,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-5"  
        },  
        {  
            "level": 6,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "favored-enemy-2-types",  
                    "name": "Favored Enemy (2 types)",  
                    "details": {  
                        "index": "favored-enemy-2-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (2 types)",  
                        "level": 6,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-2-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "natural-explorer-2-terrain-types",  
                    "name": "Natural Explorer (2 terrain types)",  
                    "details": {  
                        "index": "natural-explorer-2-terrain-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (2 terrain types)",  
                        "level": 6,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-2-terrain-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 4,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 2,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-6"  
        },  
        {  
            "level": 7,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 5,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-7"  
        },  
        {  
            "level": 8,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-2",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-2",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 8,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-2",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "ranger-lands-stride",  
                    "name": "Land's Stride",  
                    "details": {  
                        "index": "ranger-lands-stride",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Land's Stride",  
                        "level": 8,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 8th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.",  
                            "In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such those created by the entangle spell."  
                        ],  
                        "url": "/api/2014/features/ranger-lands-stride",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 5,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-8"  
        },  
        {  
            "level": 9,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 6,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 2,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-9"  
        },  
        {  
            "level": 10,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [  
                {  
                    "index": "natural-explorer-3-terrain-types",  
                    "name": "Natural Explorer (3 terrain types)",  
                    "details": {  
                        "index": "natural-explorer-3-terrain-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (3 terrain types)",  
                        "level": 10,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-3-terrain-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "hide-in-plain-sight",  
                    "name": "Hide in Plain Sight",  
                    "details": {  
                        "index": "hide-in-plain-sight",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Hide in Plain Sight",  
                        "level": 10,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 10th level, you can spend 1 minute creating camouflage for yourself. You must have access to fresh mud, dirt, plants, soot, and other naturally occurring materials with which to create your camouflage.",  
                            "Once you are camouflaged in this way, you can try to hide by pressing yourself up against a solid surface, such as a tree or wall, that is at least as tall and wide as you are. You gain a +10 bonus to Dexterity (Stealth) checks as long as you remain there without moving or taking actions. Once you move or take an action or a reaction, you must camouflage yourself again to gain this benefit."  
                        ],  
                        "url": "/api/2014/features/hide-in-plain-sight",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 6,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 2,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-10"  
        },  
        {  
            "level": 11,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 7,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-11"  
        },  
        {  
            "level": 12,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 4,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-3",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-3",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 12,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-3",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 7,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-12"  
        },  
        {  
            "level": 13,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 8,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 1,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-13"  
        },  
        {  
            "level": 14,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [  
                {  
                    "index": "favored-enemy-3-enemies",  
                    "name": "Favored Enemy (3 enemies)",  
                    "details": {  
                        "index": "favored-enemy-3-enemies",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (3 enemies)",  
                        "level": 14,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-3-enemies",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "vanish",  
                    "name": "Vanish",  
                    "details": {  
                        "index": "vanish",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Vanish",  
                        "level": 14,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 14th level, you can use the Hide action as a bonus action on your turn. Also, you can't be tracked by nonmagical means, unless you choose to leave a trail."  
                        ],  
                        "url": "/api/2014/features/vanish",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 8,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 1,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-14"  
        },  
        {  
            "level": 15,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 9,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 2,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-15"  
        },  
        {  
            "level": 16,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 5,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-4",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-4",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 16,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-4",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 9,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 2,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-16"  
        },  
        {  
            "level": 17,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 6,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 10,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 1  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-17"  
        },  
        {  
            "level": 18,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "feral-senses",  
                    "name": "Feral Senses",  
                    "details": {  
                        "index": "feral-senses",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Feral Senses",  
                        "level": 18,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 18th level, you gain preternatural senses that help you fight creatures you can't see. When you attack a creature you can't see, your inability to see it doesn't impose disadvantage on your attack rolls against it.",  
                            "You are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn't hidden from you and you aren't blinded or deafened."  
                        ],  
                        "url": "/api/2014/features/feral-senses",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 10,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 1  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-18"  
        },  
        {  
            "level": 19,  
            "ability_score_bonuses": 5,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-5",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-5",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 19,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-5",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 11,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 2  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-19"  
        },  
        {  
            "level": 20,  
            "ability_score_bonuses": 5,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "foe-slayer",  
                    "name": "Foe Slayer",  
                    "details": {  
                        "index": "foe-slayer",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Foe Slayer",  
                        "level": 20,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 20th level, you become an unparalleled hunter of your enemies. Once on each of your turns, you can add your Wisdom modifier to the attack roll or the damage roll of an attack you make against one of your favored enemies. You can choose to use this feature before or after the roll, but before any effects of the roll are applied."  
                        ],  
                        "url": "/api/2014/features/foe-slayer",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 11,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 2  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-20"  
        }  
    ]  
]  
"""  
  
spells:  
"""  
[  
    [  
        {  
            "index": "alarm",  
            "name": "Alarm",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "alarm",  
                "name": "Alarm",  
                "desc": [  
                    "You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area. When you cast the spell, you can designate creatures that won't set off the alarm. You also choose whether the alarm is mental or audible.",  
                    "A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping.",  
                    "An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A tiny bell and a piece of fine silver wire.",  
                "ritual": true,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 minute",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "cube",  
                    "size": 20  
                },  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/alarm",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "animal-friendship",  
            "name": "Animal Friendship",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "animal-friendship",  
                "name": "Animal Friendship",  
                "desc": [  
                    "This spell lets you convince a beast that you mean it no harm. Choose a beast that you can see within range. It must see and hear you. If the beast's Intelligence is 4 or higher, the spell fails. Otherwise, the beast must succeed on a wisdom saving throw or be charmed by you for the spell's duration. If you or one of your companions harms the target, the spells ends."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A morsel of food.",  
                "ritual": false,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "dc": {  
                    "dc_type": {  
                        "index": "wis",  
                        "name": "WIS",  
                        "url": "/api/2014/ability-scores/wis"  
                    },  
                    "dc_success": "none"  
                },  
                "school": {  
                    "index": "enchantment",  
                    "name": "Enchantment",  
                    "url": "/api/2014/magic-schools/enchantment"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/animal-friendship",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "cure-wounds",  
            "name": "Cure Wounds",  
            "level": 1,  
            "details": {  
                "index": "cure-wounds",  
                "name": "Cure Wounds",  
                "desc": [  
                    "A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d8 for each slot level above 1st."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "heal_at_slot_level": {  
                    "1": "1d8 + MOD",  
                    "2": "2d8 + MOD",  
                    "3": "3d8 + MOD",  
                    "4": "4d8 + MOD",  
                    "5": "5d8 + MOD",  
                    "6": "6d8 + MOD",  
                    "7": "7d8 + MOD",  
                    "8": "8d8 + MOD",  
                    "9": "9d8 + MOD"  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "life",  
                        "name": "Life",  
                        "url": "/api/2014/subclasses/life"  
                    }  
                ],  
                "url": "/api/2014/spells/cure-wounds",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "detect-magic",  
            "name": "Detect Magic",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "detect-magic",  
                "name": "Detect Magic",  
                "desc": [  
                    "For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic, and you learn its school of magic, if any.",  
                    "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/detect-magic",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "detect-poison-and-disease",  
            "name": "Detect Poison and Disease",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "detect-poison-and-disease",  
                "name": "Detect Poison and Disease",  
                "desc": [  
                    "For the duration, you can sense the presence and location of poisons, poisonous creatures, and diseases within 30 feet of you. You also identify the kind of poison, poisonous creature, or disease in each case.",  
                    "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A yew leaf.",  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/detect-poison-and-disease",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "fog-cloud",  
            "name": "Fog Cloud",  
            "level": 1,  
            "details": {  
                "index": "fog-cloud",  
                "name": "Fog Cloud",  
                "desc": [  
                    "You create a 20-foot-radius sphere of fog centered on a point within range. The sphere spreads around corners, and its area is heavily obscured. It lasts for the duration or until a wind of moderate or greater speed (at least 10 miles per hour) disperses it."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, the radius of the fog increases by 20 feet for each slot level above 1st."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 20  
                },  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/fog-cloud",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "goodberry",  
            "name": "Goodberry",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "goodberry",  
                "name": "Goodberry",  
                "desc": [  
                    "Up to ten berries appear in your hand and are infused with magic for the duration. A creature can use its action to eat one berry. Eating a berry restores 1 hit point, and the berry provides enough nourishment to sustain a creature for a day.",  
                    "The berries lose their potency if they have not been consumed within 24 hours of the casting of this spell."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A sprig of mistletoe.",  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/goodberry",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "hunters-mark",  
            "name": "Hunter's Mark",  
            "level": 1,  
            "details": {  
                "index": "hunters-mark",  
                "name": "Hunter's Mark",  
                "desc": [  
                    "You choose a creature you can see within range and mystically mark it as your quarry. Until the spell ends, you deal an extra 1d6 damage to the target whenever you hit it with a weapon attack, and you have advantage on any Wisdom (Perception) or Wisdom (Survival) check you make to find it. If the target drops to 0 hit points before this spell ends, you can use a bonus action on a subsequent turn of yours to mark a new creature."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 3rd or 4th level, you can maintain your concentration on the spell for up to 8 hours. When you use a spell slot of 5th level or higher, you can maintain your concentration on the spell for up to 24 hours."  
                ],  
                "range": "90 feet",  
                "components": [  
                    "V"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 bonus action",  
                "level": 1,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/hunters-mark",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "jump",  
            "name": "Jump",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "jump",  
                "name": "Jump",  
                "desc": [  
                    "You touch a creature. The creature's jump distance is tripled until the spell ends."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A grasshopper's hind leg.",  
                "ritual": false,  
                "duration": "1 minute",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/jump",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "longstrider",  
            "name": "Longstrider",  
            "level": 1,  
            "details": {  
                "index": "longstrider",  
                "name": "Longstrider",  
                "desc": [  
                    "You touch a creature. The target's speed increases by 10 feet until the spell ends."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each spell slot above 1st."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A pinch of dirt.",  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/longstrider",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "speak-with-animals",  
            "name": "Speak with Animals",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "speak-with-animals",  
                "name": "Speak with Animals",  
                "desc": [  
                    "You gain the ability to comprehend and verbally communicate with beasts for the duration. The knowledge and awareness of many beasts is limited by their intelligence, but at a minimum, beasts can give you information about nearby locations and monsters, including whatever they can perceive or have perceived within the past day. You might be able to persuade a beast to perform a small favor for you, at the GM's discretion."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "10 minutes",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/speak-with-animals",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "animal-messenger",  
            "name": "Animal Messenger",  
            "level": 2,  
            "details": {  
                "index": "animal-messenger",  
                "name": "Animal Messenger",  
                "desc": [  
                    "By means of this spell, you use an animal to deliver a message. Choose a Tiny beast you can see within range, such as a squirrel, a blue jay, or a bat. You specify a location, which you must have visited, and a recipient who matches a general description, such as \"a man or woman dressed in the uniform of the town guard\" or \"a red-haired dwarf wearing a pointed hat.\" You also speak a message of up to twenty-five words. The target beast travels for the duration of the spell toward the specified location, covering about 50 miles per 24 hours for a flying messenger, or 25 miles for other animals.",  
                    "When the messenger arrives, it delivers your message to the creature that you described, replicating the sound of your voice. The messenger speaks only to a creature matching the description you gave. If the messenger doesn't reach its destination before the spell ends, the message is lost, and the beast makes its way back to where you cast this spell."  
                ],  
                "higher_level": [  
                    "If you cast this spell using a spell slot of 3nd level or higher, the duration of the spell increases by 48 hours for each slot level above 2nd."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A morsel of food.",  
                "ritual": true,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "enchantment",  
                    "name": "Enchantment",  
                    "url": "/api/2014/magic-schools/enchantment"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/animal-messenger",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "barkskin",  
            "name": "Barkskin",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "barkskin",  
                "name": "Barkskin",  
                "desc": [  
                    "You touch a willing creature. Until the spell ends, the target's skin has a rough, bark-like appearance, and the target's AC can't be less than 16, regardless of what kind of armor it is wearing."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A handful of oak bark.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/barkskin",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "darkvision",  
            "name": "Darkvision",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "darkvision",  
                "name": "Darkvision",  
                "desc": [  
                    "You touch a willing creature to grant it the ability to see in the dark. For the duration, that creature has darkvision out to a range of 60 feet."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Either a pinch of dried carrot or an agate.",  
                "ritual": false,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/darkvision",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "find-traps",  
            "name": "Find Traps",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "find-traps",  
                "name": "Find Traps",  
                "desc": [  
                    "You sense the presence of any trap within range that is within line of sight. A trap, for the purpose of this spell, includes anything that would inflict a sudden or unexpected effect you consider harmful or undesirable, which was specifically intended as such by its creator. Thus, the spell would sense an area affected by the alarm spell, a glyph of warding, or a mechanical pit trap, but it would not reveal a natural weakness in the floor, an unstable ceiling, or a hidden sinkhole.",  
                    "This spell merely reveals that a trap is present. You don't learn the location of each trap, but you do learn the general nature of the danger posed by a trap you sense."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/find-traps",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "lesser-restoration",  
            "name": "Lesser Restoration",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "lesser-restoration",  
                "name": "Lesser Restoration",  
                "desc": [  
                    "You touch a creature and can end either one disease or one condition afflicting it. The condition can be blinded, deafened, paralyzed, or poisoned."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "life",  
                        "name": "Life",  
                        "url": "/api/2014/subclasses/life"  
                    },  
                    {  
                        "index": "devotion",  
                        "name": "Devotion",  
                        "url": "/api/2014/subclasses/devotion"  
                    }  
                ],  
                "url": "/api/2014/spells/lesser-restoration",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-animals-or-plants",  
            "name": "Locate Animals or Plants",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "locate-animals-or-plants",  
                "name": "Locate Animals or Plants",  
                "desc": [  
                    "Describe or name a specific kind of beast or plant. Concentrating on the voice of nature in your surroundings, you learn the direction and distance to the closest creature or plant of that kind within 5 miles, if any are present."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A bit of fur from a bloodhound.",  
                "ritual": true,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-animals-or-plants",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-object",  
            "name": "Locate Object",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "locate-object",  
                "name": "Locate Object",  
                "desc": [  
                    "Describe or name an object that is familiar to you. You sense the direction to the object's location, as long as that object is within 1,000 feet of you. If the object is in motion, you know the direction of its movement.",  
                    "The spell can locate a specific object known to you, as long as you have seen it up close--within 30 feet--at least once. Alternatively, the spell can locate the nearest object of a particular kind, such as a certain kind of apparel, jewelry, furniture, tool, or weapon.",  
                    "This spell can't locate an object if any thickness of lead, even a thin sheet, blocks a direct path between you and the object."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A forked twig.",  
                "ritual": false,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-object",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "pass-without-trace",  
            "name": "Pass Without Trace",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "pass-without-trace",  
                "name": "Pass Without Trace",  
                "desc": [  
                    "A veil of shadows and silence radiates from you, masking you and your companions from detection. For the duration, each creature you choose within 30 feet of you (including you) has a +10 bonus to Dexterity (Stealth) checks and can't be tracked except by magical means. A creature that receives this bonus leaves behind no tracks or other traces of its passage."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Ashes from a burned leaf of mistletoe and a sprig of spruce.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/pass-without-trace",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "protection-from-poison",  
            "name": "Protection from Poison",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "protection-from-poison",  
                "name": "Protection from Poison",  
                "desc": [  
                    "You touch a creature. If it is poisoned, you neutralize the poison. If more than one poison afflicts the target, you neutralize one poison that you know is present, or you neutralize one at random.",  
                    "For the duration, the target has advantage on saving throws against being poisoned, and it has resistance to poison damage."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/protection-from-poison",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "silence",  
            "name": "Silence",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "silence",  
                "name": "Silence",  
                "desc": [  
                    "For the duration, no sound can be created within or pass through a 20-foot-radius sphere centered on a point you choose within range. Any creature or object entirely inside the sphere is immune to thunder damage, and creatures are deafened while entirely inside it.",  
                    "Casting a spell that includes a verbal component is impossible there."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 20  
                },  
                "school": {  
                    "index": "illusion",  
                    "name": "Illusion",  
                    "url": "/api/2014/magic-schools/illusion"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/silence",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "spike-growth",  
            "name": "Spike Growth",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "spike-growth",  
                "name": "Spike Growth",  
                "desc": [  
                    "The ground in a 20-foot radius centered on a point within range twists and sprouts hard spikes and thorns. The area becomes difficult terrain for the duration. When a creature moves into or within the area, it takes 2d4 piercing damage for every 5 feet it travels.",  
                    "The transformation of the ground is camouflaged to look natural. Any creature that can't see the area at the time the spell is cast can make a Wisdom (Perception) check against your spell save DC to recognize the terrain as hazardous before entering it."  
                ],  
                "range": "150 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Seven sharp thorns or seven small twigs, each sharpened to a point.",  
                "ritual": false,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "area_of_effect": {  
                    "type": "cylinder",  
                    "size": 20  
                },  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/spike-growth",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "conjure-animals",  
            "name": "Conjure Animals",  
            "level": 3,  
            "details": {  
                "index": "conjure-animals",  
                "name": "Conjure Animals",  
                "desc": [  
                    "You summon fey spirits that take the form of beasts and appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:",  
                    "- One beast of challenge rating 2 or lower",  
                    "- Two beasts of challenge rating 1 or lower",  
                    "- Four beasts of challenge rating 1/2 or lower",  
                    "- Eight beasts of challenge rating 1/4 or lower",  
                    "- Each beast is also considered fey, and it disappears when it drops to 0 hit points or when the spell ends.",  
                    "The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which has its own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.",  
                    "The GM has the creatures' statistics."  
                ],  
                "higher_level": [  
                    "When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 5th-level slot, three times as many with a 7th-level."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/conjure-animals",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "daylight",  
            "name": "Daylight",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "daylight",  
                "name": "Daylight",  
                "desc": [  
                    "A 60-foot-radius sphere of light spreads out from a point you choose within range. The sphere is bright light and sheds dim light for an additional 60 feet.",  
                    "If you chose a point on an object you are holding or one that isn't being worn or carried, the light shines from the object and moves with it. Completely covering the affected object with an opaque object, such as a bowl or a helm, blocks the light.",  
                    "If any of this spell's area overlaps with an area of darkness created by a spell of 3rd level or lower, the spell that created the darkness is dispelled."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 60  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/daylight",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "nondetection",  
            "name": "Nondetection",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "nondetection",  
                "name": "Nondetection",  
                "desc": [  
                    "For the duration, you hide a target that you touch from divination magic. The target can be a willing creature or a place or an object no larger than 10 feet in any dimension. The target can't be targeted by any divination magic or perceived through magical scrying sensors."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A pinch of diamond dust worth 25 gp sprinkled over the target, which the spell consumes.",  
                "ritual": false,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/nondetection",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "plant-growth",  
            "name": "Plant Growth",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "plant-growth",  
                "name": "Plant Growth",  
                "desc": [  
                    "This spell channels vitality into plants within a specific area. There are two possible uses for the spell, granting either immediate or long-term benefits.",  
                    "If you cast this spell using 1 action, choose a point within range. All normal plants in a 100-foot radius centered on that point become thick and overgrown. A creature moving through the area must spend 4 feet of movement for every 1 foot it moves.",  
                    "You can exclude one or more areas of any size within the spell's area from being affected.",  
                    "If you cast this spell over 8 hours, you enrich the land. All plants in a half-mile radius centered on a point within range become enriched for 1 year. The plants yield twice the normal amount of food when harvested."  
                ],  
                "range": "150 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/plant-growth",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "protection-from-energy",  
            "name": "Protection From Energy",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "protection-from-energy",  
                "name": "Protection From Energy",  
                "desc": [  
                    "For the duration, the willing creature you touch has resistance to one damage type of your choice: acid, cold, fire, lightning, or thunder."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/protection-from-energy",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "speak-with-plants",  
            "name": "Speak with Plants",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "speak-with-plants",  
                "name": "Speak with Plants",  
                "desc": [  
                    "You imbue plants within 30 feet of you with limited sentience and animation, giving them the ability to communicate with you and follow your simple commands. You can question plants about events in the spell's area within the past day, gaining information about creatures that have passed, weather, and other circumstances.",  
                    "You can also turn difficult terrain caused by plant growth (such as thickets and undergrowth) into ordinary terrain that lasts for the duration. Or you can turn ordinary terrain where plants are present into difficult terrain that lasts for the duration, causing vines and branches to hinder pursuers, for example.",  
                    "Plants might be able to perform other tasks on your behalf, at the GM's discretion. The spell doesn't enable plants to uproot themselves and move about, but they can freely move branches, tendrils, and stalks.",  
                    "If a plant creature is in the area, you can communicate with it as if you shared a common language, but you gain no magical ability to influence it.",  
                    "This spell can cause the plants created by the entangle spell to release a restrained creature."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "10 minutes",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/speak-with-plants",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "water-breathing",  
            "name": "Water Breathing",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "water-breathing",  
                "name": "Water Breathing",  
                "desc": [  
                    "This spell gives a maximum of ten willing creatures within range and you can see, the ability to breathe underwater until the end of its term. Affected creatures also retain their normal breathing pattern."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A short piece of reed or straw.",  
                "ritual": true,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/water-breathing",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "water-walk",  
            "name": "Water Walk",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "water-walk",  
                "name": "Water Walk",  
                "desc": [  
                    "This spell grants the ability to move across any liquid surface--such as water, acid, mud, snow, quicksand, or lava--as if it were harmless solid ground (creatures crossing molten lava can still take damage from the heat). Up to ten willing creatures you can see within range gain this ability for the duration.",  
                    "If you target a creature submerged in a liquid, the spell carries the target to the surface of the liquid at a rate of 60 feet per round."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A piece of cork.",  
                "ritual": true,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/water-walk",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "wind-wall",  
            "name": "Wind Wall",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "wind-wall",  
                "name": "Wind Wall",  
                "desc": [  
                    "A wall of strong wind rises from the ground at a point you choose within range. You can make the wall up to 50 feet long, 15 feet high, and 1 foot thick. You can shape the wall in any way you choose so long as it makes one continuous path along the ground. The wall lasts for the duration.",  
                    "When the wall appears, each creature within its area must make a strength saving throw. A creature takes 3d8 bludgeoning damage on a failed save, or half as much damage on a successful one.",  
                    "The strong wind keeps fog, smoke, and other gases at bay. Small or smaller flying creatures or objects can't pass through the wall. Loose, lightweight materials brought into the wall fly upward. Arrows, bolts, and other ordinary projectiles launched at targets behind the wall are deflected upward and automatically miss. (Boulders hurled by giants or siege engines, and similar projectiles, are unaffected.) Creatures in gaseous form can't pass through it."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A tiny fan and a feather of exotic origin.",  
                "ritual": false,  
                "duration": "Up to 1 minute",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "damage": {  
                    "damage_type": {  
                        "index": "bludgeoning",  
                        "name": "Bludgeoning",  
                        "url": "/api/2014/damage-types/bludgeoning"  
                    },  
                    "damage_at_slot_level": {  
                        "3": "3d8"  
                    }  
                },  
                "dc": {  
                    "dc_type": {  
                        "index": "str",  
                        "name": "STR",  
                        "url": "/api/2014/ability-scores/str"  
                    },  
                    "dc_success": "half"  
                },  
                "area_of_effect": {  
                    "type": "line",  
                    "size": 50  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/wind-wall",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "conjure-woodland-beings",  
            "name": "Conjure Woodland Beings",  
            "level": 4,  
            "details": {  
                "index": "conjure-woodland-beings",  
                "name": "Conjure Woodland Beings",  
                "desc": [  
                    "You summon fey creatures that appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:",  
                    "- One fey creature of challenge rating 2 or lower",  
                    "- Two fey creatures of challenge rating 1 or lower",  
                    "- Four fey creatures of challenge rating 1/2 or lower",  
                    "- Eight fey creatures of challenge rating 1/4 or lower",  
                    "A summoned creature disappears when it drops to 0 hit points or when the spell ends.",  
                    "The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which have their own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.",  
                    "The GM has the creatures' statistics."  
                ],  
                "higher_level": [  
                    "When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 6th-level slot and three times as many with an 8th-level slot."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "One holly berry per creature summoned.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/conjure-woodland-beings",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "freedom-of-movement",  
            "name": "Freedom of Movement",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "freedom-of-movement",  
                "name": "Freedom of Movement",  
                "desc": [  
                    "You touch a willing creature. For the duration, the target's movement is unaffected by difficult terrain, and spells and other magical effects can neither reduce the target's speed nor cause the target to be paralyzed or restrained.",  
                    "The target can also spend 5 feet of movement to automatically escape from nonmagical restraints, such as manacles or a creature that has it grappled. Finally, being underwater imposes no penalties on the target's movement or attacks."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A leather strap, bound around the arm or a similar appendage.",  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    },  
                    {  
                        "index": "devotion",  
                        "name": "Devotion",  
                        "url": "/api/2014/subclasses/devotion"  
                    }  
                ],  
                "url": "/api/2014/spells/freedom-of-movement",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-creature",  
            "name": "Locate Creature",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "locate-creature",  
                "name": "Locate Creature",  
                "desc": [  
                    "Describe or name a creature that is familiar to you. You sense the direction to the creature's location, as long as that creature is within 1,000 feet of you. If the creature is moving, you know the direction of its movement.",  
                    "The spell can locate a specific creature known to you, or the nearest creature of a specific kind (such as a human or a unicorn), so long as you have seen such a creature up close--within 30 feet--at least once. If the creature you described or named is in a different form, such as being under the effects of a polymorph spell, this spell doesn't locate the creature.",  
                    "This spell can't locate a creature if running water at least 10 feet wide blocks a direct path between you and the creature."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A bit of fur from a bloodhound.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-creature",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "stoneskin",  
            "name": "Stoneskin",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "stoneskin",  
                "name": "Stoneskin",  
                "desc": [  
                    "This spell turns the flesh of a willing creature you touch as hard as stone. Until the spell ends, the target has resistance to nonmagical bludgeoning, piercing, and slashing damage."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Diamond dust worth 100 gp, which the spell consumes.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/stoneskin",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "commune-with-nature",  
            "name": "Commune With Nature",  
            "level": 5,  
            "details": {  
                "higher_level": [],  
                "index": "commune-with-nature",  
                "name": "Commune With Nature",  
                "desc": [  
                    "You briefly become one with nature and gain knowledge of the surrounding territory. In the outdoors, the spell gives you knowledge of the land within 3 miles of you. In caves and other natural underground settings, the radius is limited to 300 feet. The spell doesn't function where nature has been replaced by construction, such as in dungeons and towns.",  
                    "You instantly gain knowledge of up to three facts of your choice about any of the following subjects as they relate to the area:",  
                    "- terrain and bodies of water",  
                    "- prevalent plants, minerals, animals, or peoples",  
                    "- powerful celestials, fey, fiends, elementals, or undead",  
                    "- influence from other planes of existence",  
                    "- buildings",  
                    "For example, you could determine the location of powerful undead in the area, the location of major sources of safe drinking water, and the location of any nearby towns."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 minute",  
                "level": 5,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/commune-with-nature",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "tree-stride",  
            "name": "Tree Stride",  
            "level": 5,  
            "details": {  
                "higher_level": [],  
                "index": "tree-stride",  
                "name": "Tree Stride",  
                "desc": [  
                    "You gain the ability to enter a tree and move from inside it to inside another tree of the same kind within 500 feet. Both trees must be living and at least the same size as you. You must use 5 feet of movement to enter a tree. You instantly know the location of all other trees of the same kind within 500 feet and, as part of the move used to enter the tree, can either pass into one of those trees or step out of the tree you're in. You appear in a spot of your choice within 5 feet of the destination tree, using another 5 feet of movement. If you have no movement left, you appear within 5 feet of the tree you entered.",  
                    "You can use this transportation ability once per round for the duration. You must end each turn outside a tree."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 minute",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 5,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/tree-stride",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        }  
    ]  
]  
"""  
  
sublcass_data:  
"""  
[  
    [  
        {  
            "index": "hunter",  
            "class": {  
                "index": "ranger",  
                "name": "Ranger",  
                "url": "/api/2014/classes/ranger"  
            },  
            "name": "Hunter",  
            "subclass_flavor": "Ranger Archetype",  
            "desc": [  
                "Emulating the Hunter archetype means accepting your place as a bulwark between civilization and the terrors of the wilderness. As you walk the Hunter's path, you learn specialized techniques for fighting the threats you face, from rampaging ogres and hordes of orcs to towering giants and terrifying dragons."  
            ],  
            "subclass_levels": [  
                {  
                    "level": 3,  
                    "features": [  
                        {  
                            "index": "hunters-prey",  
                            "name": "Hunter's Prey",  
                            "details": {  
                                "index": "hunters-prey",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Hunter's Prey",  
                                "level": 3,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 3rd level, you gain one of the following features of your choice.",  
                                    "Colossus Slayer",  
                                    "Giant Killer",  
                                    "Horde Breaker"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-colossus-slayer",  
                                                        "name": "Hunter's Prey: Colossus Slayer",  
                                                        "url": "/api/2014/features/hunters-prey-colossus-slayer"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-giant-killer",  
                                                        "name": "Hunter's Prey: Giant Killer",  
                                                        "url": "/api/2014/features/hunters-prey-giant-killer"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-horde-breaker",  
                                                        "name": "Hunter's Prey: Horde Breaker",  
                                                        "url": "/api/2014/features/hunters-prey-horde-breaker"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/hunters-prey",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/3",  
                    "index": "hunter-3",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 7,  
                    "features": [  
                        {  
                            "index": "defensive-tactics",  
                            "name": "Defensive Tactics",  
                            "details": {  
                                "index": "defensive-tactics",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Defensive Tactics",  
                                "level": 7,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 7th level, you gain one of the following features of your choice.",  
                                    "Escape the Horde",  
                                    "Multiattack Defense",  
                                    "Steel Will"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-escape-the-horde",  
                                                        "name": "Defensive Tactics: Escape the Horde",  
                                                        "url": "/api/2014/features/defensive-tactics-escape-the-horde"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-multiattack-defense",  
                                                        "name": "Defensive Tactics: Multiattack Defense",  
                                                        "url": "/api/2014/features/defensive-tactics-multiattack-defense"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-steel-will",  
                                                        "name": "Defensive Tactics: Steel Will",  
                                                        "url": "/api/2014/features/defensive-tactics-steel-will"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/defensive-tactics",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/7",  
                    "index": "hunter-7",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 11,  
                    "features": [  
                        {  
                            "index": "multiattack",  
                            "name": "Multiattack",  
                            "details": {  
                                "index": "multiattack",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Multiattack",  
                                "level": 11,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 11th level, you gain one of the following features of your choice.",  
                                    "Volley",  
                                    "Whirlwind Attack"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "multiattack-volley",  
                                                        "name": "Multiattack: Volley",  
                                                        "url": "/api/2014/features/multiattack-volley"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "multiattack-whirlwind-attack",  
                                                        "name": "Multiattack: Whirlwind Attack",  
                                                        "url": "/api/2014/features/multiattack-whirlwind-attack"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/multiattack",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/11",  
                    "index": "hunter-11",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 15,  
                    "features": [  
                        {  
                            "index": "superior-hunters-defense",  
                            "name": "Superior Hunter's Defense",  
                            "details": {  
                                "index": "superior-hunters-defense",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Superior Hunter's Defense",  
                                "level": 15,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 15th level, you gain one of the following features of your choice.",  
                                    "Evasion",  
                                    "Stand Against the Tide",  
                                    "Uncanny Dodge"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-evasion",  
                                                        "name": "Superior Hunter's Defense: Evasion",  
                                                        "url": "/api/2014/features/superior-hunters-defense-evasion"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-stand-against-the-tide",  
                                                        "name": "Superior Hunter's Defense: Stand Against the Tide",  
                                                        "url": "/api/2014/features/superior-hunters-defense-stand-against-the-tide"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-uncanny-dodge",  
                                                        "name": "Superior Hunter's Defense: Uncanny Dodge",  
                                                        "url": "/api/2014/features/superior-hunters-defense-uncanny-dodge"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/superior-hunters-defense",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/15",  
                    "index": "hunter-15",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                }  
            ],  
            "url": "/api/2014/subclasses/hunter",  
            "updated_at": "2025-04-08T21:14:17.800Z",  
            "spells": []  
        }  
    ]  
]  
"""  
```


# Robin Hood

## Mistral

>[!Warning] **Resume**:
>
>Mistral hatte gar keine probleme den Prompt anzunehmen. 
>Ich konnte den Text direckt in das Browserfenster eingeben und kurz darauf wurde der Character erstellt.
>
>Mein Resume ist daher: **A**


>[!Info]+ Analysed Data:
>**prompt_1** : 
>```
>Erstelle einen Robin Hood, aus Robin Hood. Level 10. ranger. Orientiere dich bei dem ragner an folgenden details: ["Robin Hood", "Level 10", "Bogenschütze", "Dieb", "Geschicklichkeit", "Tarnung"]
>```
>
>**prompt_2** :
>```
>Erstelle einen Robin Hood, aus Robin Hood. Level 10. rogue. Orientiere dich bei dem rogue an folgenden details: ["Robin Hood", "Level 10", "Bogenschütze", "Dieb", "Geschicklichkeit", "Tarnung"]
>```
>
>**prompt_3**: 
>```
>Erstelle einen Robin Hood, aus Robin Hood. Level 10. fighter. Orientiere dich bei dem fighter an folgenden details: ["Robin Hood", "Level 10", "Bogenschütze", "Dieb", "Geschicklichkeit", "Tarnung"]
>```
>


### CharacterGeneration

#### CharGenPrompt:
```
Du bist ein Dungeons and Dragons(DnD) Experte. Du erstellst DnD Charactere.  
Um einen Character zu erstellen erhälst du alle nötigen Informationen für eine Klasse im Json format, an diesen Prompt als json-file angehängt.  
Zusätzlich bekommst du Details zu dem Character, die den character noch einmal näher definieren.  
  
Ein beispiel für die Details ist:  
- Ein dunkler Magier Level 8, der tote beschwören kann und mit Feuermagie zaubert.  
In diesem Beispiel sollst du den DnD Character so erstellen, dass er viele Fähigkeiten hat, die in das Themengebiet 'Necromantie', 'dunkle Magie' und 'Feuermagie' fallen.  
Du wirst in den daten, die du erhälst immer wieder Fähgikeiten auswählen können. Wähle bei diesen auch so, dass die Auswhl den genannten Character Details entsprechen.  
  
Den erstellen Character sollst du im Json Format zurück geben.  
Hier ist ein Beispiel für einen DnD character der stufe 20:  
  
{  
    "name": "Cleric",    "level": 20,    "hit_points": 150,    "proficiency_bonus": 6,    "subclass": "Life Domain",    "attributes": {        "strength": 12,        "dexterity": 14,        "constitution": 14,        "intelligence": 10,        "wisdom": 20,        "charisma": 8    },    "attribute_proficiencys": {      "strength": false,        "dexterity": false,        "constitution": false,        "intelligence": false,        "wisdom": true,        "charisma": true    },    "saving_throws": {      "strength": 1,        "dexterity": 2,        "constitution": 2,        "intelligence": 0,        "wisdom": 11,        "charisma": 5    },  
    "armor_class": 18,    "attack_bonus": 8,    "spellcasting": {        "spellcasting_bonus": 11,        "spellcasting_dc": 19,        "spellcasting_attack_bonus": 11,        "cantrips_known": 5,        "spells_prepared": 25,        "spell_slots": {            "1st": 4,            "2nd": 4,            "3rd": 4,            "4th": 4,            "5th": 3,            "6th": 3,            "7th": 2,            "8th": 2,            "9th": 1        },        "known_spells": {            "cantrips": ["Guidance", "Light", "Sacred Flame", "Thaumaturgy", "Toll the Dead"],            "1st_level": ["Bless", "Cure Wounds", "Guiding Bolt", "Infestation", "Magic Stone"],            "2nd_level": ["Lesser Restoration", "Prayer of Healing", "Spiritual Weapon", "Warding Bond", "Zone of Truth"],            "3rd_level": ["Mass Healing Word", "Revivify", "Sending", "Spirit Guardians", "Water Walk"],            "4th_level": ["Banishment", "Control Water", "Death Ward", "Freedom of Movement", "Guardian of Faith"],            "5th_level": ["Circle of Power", "Contagion", "Flame Strike", "Geas", "Insect Plague"],            "6th_level": ["Blade Barrier", "Create Undead", "Harm", "Heal", "Heroes' Feast"],            "7th_level": ["Conjure Celestial", "Divine Word", "Etherealness", "Fire Storm", "Regenerate"],            "8th_level": ["Antimagic Field", "Control Weather", "Earthquake", "Holy Aura", "Sunburst"],            "9th_level": ["Astral Projection", "Gate", "Mass Heal", "True Resurrection", "Weird"]        },        "prepared_spells": {            "cantrips": ["Guidance (S)", "Sacred Flame (D)", "Thaumaturgy (S)", "Toll the Dead (D)"],            "1st_level": ["Bless (S)", "Cure Wounds (S)", "Guiding Bolt (D)", "Infestation (D)"],            "2nd_level": ["Lesser Restoration (S)", "Prayer of Healing (S)", "Spiritual Weapon (D)"],            "3rd_level": ["Mass Healing Word (S)", "Revivify (S)", "Spirit Guardians (D)"],            "4th_level": ["Banishment (D)", "Death Ward (S)", "Guardian of Faith (D)"],            "5th_level": ["Flame Strike (D)", "Insect Plague (D)"],            "6th_level": ["Harm (D)", "Heal (S)"],            "7th_level": ["Fire Storm (D)", "Regenerate (S)"],            "8th_level": ["Earthquake (D)", "Holy Aura (S)"],            "9th_level": ["Mass Heal (S)" ]        }    },    "skills": {        "strength_skills": {            "athletics": {"bonus": 9, "proficiency_bonus": true}        },        "dexterity_skills": {            "acrobatics": {"bonus": 5, "proficiency_bonus": false},            "sleight_of_hand": {"bonus": 5, "proficiency_bonus": false},            "stealth": {"bonus": 5, "proficiency_bonus": false}        },        "intelligence_skills": {            "arcana": {"bonus": 3, "proficiency_bonus": false},            "history": {"bonus": 3, "proficiency_bonus": false},            "investigation": {"bonus": 3, "proficiency_bonus": false},            "nature": {"bonus": 3, "proficiency_bonus": false},            "religion": {"bonus": 9, "proficiency_bonus": true}        },        "wisdom_skills": {            "animal_handling": {"bonus": 13, "proficiency_bonus": true},            "insight": {"bonus": 13, "proficiency_bonus": true},            "medicine": {"bonus": 13, "proficiency_bonus": true},            "perception": {"bonus": 13, "proficiency_bonus": true},            "survival": {"bonus": 13, "proficiency_bonus": true}        },        "charisma_skills": {            "deception": {"bonus": 1, "proficiency_bonus": false},            "intimidation": {"bonus": 1, "proficiency_bonus": false},            "performance": {"bonus": 1, "proficiency_bonus": false},            "persuasion": {"bonus": 7, "proficiency_bonus": true}        }    },  
    "features": [        "Spellcasting",        "Channel Divinity (2/short rest)",        "Destroy Undead (CR 3)",        "Divine Intervention (1/long rest)",        "Domain Spells",        "Blessed Healer",        "Divine Strike",        "Supreme Healing",        "Life Domain: Preserve Life",        "Life Domain: Blessed Healer"    ],    "special_abilities_and_traits": [        "Darkvision (60 ft)",        "Ritual Casting",        "Life Domain: Bonus Proficiency in Heavy Armor"    ],    "languages": ["Common", "Celestial", "Primordial"],    "equipment": [        "Mace",        "Scale mail armor",        "Light crossbow and 20 bolts",        "Dungeoneer's pack",        "A holy symbol"    ],    "additional_equipment": [        "Bedroll",        "Mess kit",        "10 ball bearings",        "10 feet of string",        "A belt pouch containing 10 GP"    ],    "money": {        "platinum": 0,        "gold": 100,        "electrum": 0,        "silver": 50,        "copper": 25    },    "weapons": {        "mace": {            "damage": "1d6 bludgeoning",            "attack_bonus": 8,            "properties": ["Light"]        },        "light_crossbow": {            "damage": "1d8 piercing",            "attack_bonus": 7,            "properties": ["Ammunition", "Loading", "Two-Handed"],            "range": "80/320 ft"        }    }}  
  
  
Geb nur den erstellen character in genau dieser struktur zurück, wie ich sie dir im beispiel gezeigt habe.  
Füge kein 'Json' kennzeichen. Nur den reinen text.  
  
Achte darauf, dass das Level der beispiel-struktur 20 ist. Nicht jeder Character soll auf level 20 erstellt werden!  
  
Wenn du in der Characterbeschreibung keine klar erkennbare Level-höhe herauslesen kannst,  
dann wähle ein level, dass zu den stärke-beschreibungen passt.  
Wenn z.B der Prompt lautet: 'Starker Krieger', dann kannst du das level ruhig auf 5-8 setzten.  
Wenn aber der Prompt ist: 'super starker Krieger', oder 'Heroischer Champion', dann setze das Level gern zwischen 10  und 14.  
Wenn das Wort 'gottgleich' oder andere extreme worte für die Mächtigkeit eines Characters fallen,  
dann kannst du das Level gern auf 18 - 20 setzten.  
  
Das gleiche gilt für schwache wörter.  
z.B 'schwacher Krieger', wäre eher Level 1-4.  
  
Falls keine dieser - oder andere - Schlagwörter für die Stärke eines Characters fallen, dann setzte das Level pauschal auf 5 - 8  
  
Als nächstes kommt die aufforderung den character zu erstellen, mit den KLassen daten und den character details.  
  
Das hier ist die Aufferderung den Character zu erstellen:  
'''  
Erstelle einen Robin Hood, aus Robin Hood. Level 10. ranger. Orientiere dich bei dem ragner an folgenden details: ["Robin Hood", "Level 10", "Bogenschütze", "Dieb", "Geschicklichkeit", "Tarnung"]
'''  
  
Jetzt kommen allen nötigen Klassendaten:  
'''  
Base_data_for_class:  
"""  
{  
        "index": "ranger",  
        "name": "Ranger",  
        "hit_die": 10,  
        "proficiency_choices": [  
            {  
                "desc": "Choose three from Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, and Survival",  
                "choose": 3,  
                "type": "proficiencies",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-animal-handling",  
                                "name": "Skill: Animal Handling",  
                                "url": "/api/2014/proficiencies/skill-animal-handling"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-athletics",  
                                "name": "Skill: Athletics",  
                                "url": "/api/2014/proficiencies/skill-athletics"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-insight",  
                                "name": "Skill: Insight",  
                                "url": "/api/2014/proficiencies/skill-insight"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-investigation",  
                                "name": "Skill: Investigation",  
                                "url": "/api/2014/proficiencies/skill-investigation"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-nature",  
                                "name": "Skill: Nature",  
                                "url": "/api/2014/proficiencies/skill-nature"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-perception",  
                                "name": "Skill: Perception",  
                                "url": "/api/2014/proficiencies/skill-perception"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-stealth",  
                                "name": "Skill: Stealth",  
                                "url": "/api/2014/proficiencies/skill-stealth"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-survival",  
                                "name": "Skill: Survival",  
                                "url": "/api/2014/proficiencies/skill-survival"  
                            }  
                        }  
                    ]  
                }  
            }  
        ],  
        "proficiencies": [  
            {  
                "index": "light-armor",  
                "name": "Light Armor",  
                "url": "/api/2014/proficiencies/light-armor"  
            },  
            {  
                "index": "medium-armor",  
                "name": "Medium Armor",  
                "url": "/api/2014/proficiencies/medium-armor"  
            },  
            {  
                "index": "shields",  
                "name": "Shields",  
                "url": "/api/2014/proficiencies/shields"  
            },  
            {  
                "index": "simple-weapons",  
                "name": "Simple Weapons",  
                "url": "/api/2014/proficiencies/simple-weapons"  
            },  
            {  
                "index": "martial-weapons",  
                "name": "Martial Weapons",  
                "url": "/api/2014/proficiencies/martial-weapons"  
            },  
            {  
                "index": "saving-throw-dex",  
                "name": "Saving Throw: DEX",  
                "url": "/api/2014/proficiencies/saving-throw-dex"  
            },  
            {  
                "index": "saving-throw-str",  
                "name": "Saving Throw: STR",  
                "url": "/api/2014/proficiencies/saving-throw-str"  
            }  
        ],  
        "saving_throws": [  
            {  
                "index": "str",  
                "name": "STR",  
                "url": "/api/2014/ability-scores/str"  
            },  
            {  
                "index": "dex",  
                "name": "DEX",  
                "url": "/api/2014/ability-scores/dex"  
            }  
        ],  
        "starting_equipment": [  
            {  
                "equipment": {  
                    "index": "longbow",  
                    "name": "Longbow",  
                    "url": "/api/2014/equipment/longbow"  
                },  
                "quantity": 1  
            },  
            {  
                "equipment": {  
                    "index": "arrow",  
                    "name": "Arrow",  
                    "url": "/api/2014/equipment/arrow"  
                },  
                "quantity": 20  
            }  
        ],  
        "starting_equipment_options": [  
            {  
                "desc": "(a) scale mail or (b) leather armor",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "scale-mail",  
                                "name": "Scale Mail",  
                                "url": "/api/2014/equipment/scale-mail"  
                            }  
                        },  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "leather-armor",  
                                "name": "Leather Armor",  
                                "url": "/api/2014/equipment/leather-armor"  
                            }  
                        }  
                    ]  
                }  
            },  
            {  
                "desc": "(a) two shortswords or (b) two simple melee weapons",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 2,  
                            "of": {  
                                "index": "shortsword",  
                                "name": "Shortsword",  
                                "url": "/api/2014/equipment/shortsword"  
                            }  
                        },  
                        {  
                            "option_type": "choice",  
                            "choice": {  
                                "desc": "two simple melee weapons",  
                                "choose": 2,  
                                "type": "equipment",  
                                "from": {  
                                    "option_set_type": "equipment_category",  
                                    "equipment_category": {  
                                        "index": "simple-melee-weapons",  
                                        "name": "Simple Melee Weapons",  
                                        "url": "/api/2014/equipment-categories/simple-melee-weapons"  
                                    }  
                                }  
                            }  
                        }  
                    ]  
                }  
            },  
            {  
                "desc": "(a) a dungeoneer\u2019s pack or (b) an explorer\u2019s pack",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "dungeoneers-pack",  
                                "name": "Dungeoneer's Pack",  
                                "url": "/api/2014/equipment/dungeoneers-pack"  
                            }  
                        },  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "explorers-pack",  
                                "name": "Explorer's Pack",  
                                "url": "/api/2014/equipment/explorers-pack"  
                            }  
                        }  
                    ]  
                }  
            }  
        ],  
        "class_levels": "/api/2014/classes/ranger/levels",  
        "multi_classing": {  
            "prerequisites": [  
                {  
                    "ability_score": {  
                        "index": "dex",  
                        "name": "DEX",  
                        "url": "/api/2014/ability-scores/dex"  
                    },  
                    "minimum_score": 13  
                },  
                {  
                    "ability_score": {  
                        "index": "wis",  
                        "name": "WIS",  
                        "url": "/api/2014/ability-scores/wis"  
                    },  
                    "minimum_score": 13  
                }  
            ],  
            "proficiencies": [  
                {  
                    "index": "light-armor",  
                    "name": "Light Armor",  
                    "url": "/api/2014/proficiencies/light-armor"  
                },  
                {  
                    "index": "medium-armor",  
                    "name": "Medium Armor",  
                    "url": "/api/2014/proficiencies/medium-armor"  
                },  
                {  
                    "index": "shields",  
                    "name": "Shields",  
                    "url": "/api/2014/proficiencies/shields"  
                },  
                {  
                    "index": "simple-weapons",  
                    "name": "Simple Weapons",  
                    "url": "/api/2014/proficiencies/simple-weapons"  
                },  
                {  
                    "index": "martial-weapons",  
                    "name": "Martial Weapons",  
                    "url": "/api/2014/proficiencies/martial-weapons"  
                }  
            ],  
            "proficiency_choices": [  
                {  
                    "choose": 1,  
                    "type": "proficiencies",  
                    "from": {  
                        "option_set_type": "options_array",  
                        "options": [  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-animal-handling",  
                                    "name": "Skill: Animal Handling",  
                                    "url": "/api/2014/proficiencies/skill-animal-handling"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-athletics",  
                                    "name": "Skill: Athletics",  
                                    "url": "/api/2014/proficiencies/skill-athletics"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-insight",  
                                    "name": "Skill: Insight",  
                                    "url": "/api/2014/proficiencies/skill-insight"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-investigation",  
                                    "name": "Skill: Investigation",  
                                    "url": "/api/2014/proficiencies/skill-investigation"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-nature",  
                                    "name": "Skill: Nature",  
                                    "url": "/api/2014/proficiencies/skill-nature"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-perception",  
                                    "name": "Skill: Perception",  
                                    "url": "/api/2014/proficiencies/skill-perception"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-stealth",  
                                    "name": "Skill: Stealth",  
                                    "url": "/api/2014/proficiencies/skill-stealth"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-survival",  
                                    "name": "Skill: Survival",  
                                    "url": "/api/2014/proficiencies/skill-survival"  
                                }  
                            }  
                        ]  
                    }  
                }  
            ]  
        },  
        "subclasses": [  
            {  
                "index": "hunter",  
                "name": "Hunter",  
                "url": "/api/2014/subclasses/hunter"  
            }  
        ],  
        "spellcasting": {  
            "level": 2,  
            "spellcasting_ability": {  
                "index": "wis",  
                "name": "WIS",  
                "url": "/api/2014/ability-scores/wis"  
            },  
            "info": [  
                {  
                    "name": "Spell Slots",  
                    "desc": [  
                        "The Ranger table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.",  
                        "For example, if you know the 1st-level spell animal friendship and have a 1st-level and a 2nd-level spell slot available, you can cast animal friendship using either slot."  
                    ]  
                },  
                {  
                    "name": "Spells Known of 1st Level and Higher",  
                    "desc": [  
                        "You know two 1st-level spells of your choice from the ranger spell list.",  
                        "The Spells Known column of the Ranger table shows when you learn more ranger spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 5th level in this class, you can learn one new spell of 1st or 2nd level.",  
                        "Additionally, when you gain a level in this class, you can choose one of the ranger spells you know and replace it with another spell from the ranger spell list, which also must be of a level for which you have spell slots."  
                    ]  
                },  
                {  
                    "name": "Spellcasting Ability",  
                    "desc": [  
                        "Wisdom is your spellcasting ability for your ranger spells, since your magic draws on your attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a ranger spell you cast and when making an attack roll with one.",  
                        "Spell save DC = 8 + your proficiency bonus + your Wisdom modifier.",  
                        "Spell attack modifier = your proficiency bonus + your Wisdom modifier."  
                    ]  
                }  
            ]  
        },  
        "spells": "/api/2014/classes/ranger/spells",  
        "url": "/api/2014/classes/ranger"  
    }  
"""  
      
  
level_features:  
"""  
[  
    [  
        {  
            "level": 1,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "favored-enemy-1-type",  
                    "name": "Favored Enemy (1 type)",  
                    "details": {  
                        "index": "favored-enemy-1-type",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (1 type)",  
                        "level": 1,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-1-type",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "natural-explorer-1-terrain-type",  
                    "name": "Natural Explorer (1 terrain type)",  
                    "details": {  
                        "index": "natural-explorer-1-terrain-type",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (1 terrain type)",  
                        "level": 1,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-1-terrain-type",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 0,  
                "spell_slots_level_1": 0,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-1"  
        },  
        {  
            "level": 2,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-fighting-style",  
                    "name": "Fighting Style",  
                    "details": {  
                        "index": "ranger-fighting-style",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Fighting Style",  
                        "level": 2,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 2nd level, you adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again."  
                        ],  
                        "feature_specific": {  
                            "subfeature_options": {  
                                "choose": 1,  
                                "type": "feature",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-archery",  
                                                "name": "Fighting Style: Archery",  
                                                "url": "/api/2014/features/ranger-fighting-style-archery"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-defense",  
                                                "name": "Fighting Style: Defense",  
                                                "url": "/api/2014/features/ranger-fighting-style-defense"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-dueling",  
                                                "name": "Fighting Style: Dueling",  
                                                "url": "/api/2014/features/ranger-fighting-style-dueling"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-two-weapon-fighting",  
                                                "name": "Fighting Style: Two-Weapon Fighting",  
                                                "url": "/api/2014/features/ranger-fighting-style-two-weapon-fighting"  
                                            }  
                                        }  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/ranger-fighting-style",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "spellcasting-ranger",  
                    "name": "Spellcasting: Ranger",  
                    "details": {  
                        "index": "spellcasting-ranger",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Spellcasting: Ranger",  
                        "level": 2,  
                        "prerequisites": [],  
                        "desc": [  
                            "By the time you reach 2nd level, you have learned to use the magical essence of nature to cast spells, much as a druid does."  
                        ],  
                        "reference": "/api/2014/classes/ranger/spellcasting",  
                        "url": "/api/2014/features/spellcasting-ranger",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 2,  
                "spell_slots_level_1": 2,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-2"  
        },  
        {  
            "level": 3,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-archetype",  
                    "name": "Ranger Archetype",  
                    "details": {  
                        "index": "ranger-archetype",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ranger Archetype",  
                        "level": 3,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 3rd level, you choose an archetype that you strive to emulate, such as the Hunter. Your choice grants you features at 3rd level and again at 7th, 11th, and 15th level."  
                        ],  
                        "url": "/api/2014/features/ranger-archetype",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "primeval-awareness",  
                    "name": "Primeval Awareness",  
                    "details": {  
                        "index": "primeval-awareness",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Primeval Awareness",  
                        "level": 3,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 3rd level, you can use your action and expend one ranger spell slot to focus your awareness on the region around you. For 1 minute per level of the spell slot you expend, you can sense whether the following types of creatures are present within 1 mile of you (or within up to 6 miles if you are in your favored terrain): aberrations, celestials, dragons, elementals, fey, fiends, and undead. This feature doesn't reveal the creatures' location or number."  
                        ],  
                        "url": "/api/2014/features/primeval-awareness",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 3,  
                "spell_slots_level_1": 3,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-3"  
        },  
        {  
            "level": 4,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-1",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-1",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 4,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-1",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 3,  
                "spell_slots_level_1": 3,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-4"  
        },  
        {  
            "level": 5,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "ranger-extra-attack",  
                    "name": "Extra Attack",  
                    "details": {  
                        "index": "ranger-extra-attack",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Extra Attack",  
                        "level": 5,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."  
                        ],  
                        "url": "/api/2014/features/ranger-extra-attack",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 4,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 2,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-5"  
        },  
        {  
            "level": 6,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "favored-enemy-2-types",  
                    "name": "Favored Enemy (2 types)",  
                    "details": {  
                        "index": "favored-enemy-2-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (2 types)",  
                        "level": 6,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-2-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "natural-explorer-2-terrain-types",  
                    "name": "Natural Explorer (2 terrain types)",  
                    "details": {  
                        "index": "natural-explorer-2-terrain-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (2 terrain types)",  
                        "level": 6,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-2-terrain-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 4,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 2,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-6"  
        },  
        {  
            "level": 7,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 5,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-7"  
        },  
        {  
            "level": 8,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-2",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-2",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 8,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-2",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "ranger-lands-stride",  
                    "name": "Land's Stride",  
                    "details": {  
                        "index": "ranger-lands-stride",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Land's Stride",  
                        "level": 8,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 8th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.",  
                            "In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such those created by the entangle spell."  
                        ],  
                        "url": "/api/2014/features/ranger-lands-stride",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 5,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-8"  
        },  
        {  
            "level": 9,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 6,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 2,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-9"  
        },  
        {  
            "level": 10,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [  
                {  
                    "index": "natural-explorer-3-terrain-types",  
                    "name": "Natural Explorer (3 terrain types)",  
                    "details": {  
                        "index": "natural-explorer-3-terrain-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (3 terrain types)",  
                        "level": 10,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-3-terrain-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "hide-in-plain-sight",  
                    "name": "Hide in Plain Sight",  
                    "details": {  
                        "index": "hide-in-plain-sight",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Hide in Plain Sight",  
                        "level": 10,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 10th level, you can spend 1 minute creating camouflage for yourself. You must have access to fresh mud, dirt, plants, soot, and other naturally occurring materials with which to create your camouflage.",  
                            "Once you are camouflaged in this way, you can try to hide by pressing yourself up against a solid surface, such as a tree or wall, that is at least as tall and wide as you are. You gain a +10 bonus to Dexterity (Stealth) checks as long as you remain there without moving or taking actions. Once you move or take an action or a reaction, you must camouflage yourself again to gain this benefit."  
                        ],  
                        "url": "/api/2014/features/hide-in-plain-sight",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 6,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 2,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-10"  
        },  
        {  
            "level": 11,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 7,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-11"  
        },  
        {  
            "level": 12,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 4,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-3",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-3",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 12,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-3",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 7,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-12"  
        },  
        {  
            "level": 13,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 8,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 1,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-13"  
        },  
        {  
            "level": 14,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [  
                {  
                    "index": "favored-enemy-3-enemies",  
                    "name": "Favored Enemy (3 enemies)",  
                    "details": {  
                        "index": "favored-enemy-3-enemies",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (3 enemies)",  
                        "level": 14,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-3-enemies",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "vanish",  
                    "name": "Vanish",  
                    "details": {  
                        "index": "vanish",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Vanish",  
                        "level": 14,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 14th level, you can use the Hide action as a bonus action on your turn. Also, you can't be tracked by nonmagical means, unless you choose to leave a trail."  
                        ],  
                        "url": "/api/2014/features/vanish",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 8,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 1,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-14"  
        },  
        {  
            "level": 15,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 9,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 2,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-15"  
        },  
        {  
            "level": 16,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 5,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-4",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-4",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 16,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-4",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 9,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 2,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-16"  
        },  
        {  
            "level": 17,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 6,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 10,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 1  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-17"  
        },  
        {  
            "level": 18,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "feral-senses",  
                    "name": "Feral Senses",  
                    "details": {  
                        "index": "feral-senses",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Feral Senses",  
                        "level": 18,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 18th level, you gain preternatural senses that help you fight creatures you can't see. When you attack a creature you can't see, your inability to see it doesn't impose disadvantage on your attack rolls against it.",  
                            "You are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn't hidden from you and you aren't blinded or deafened."  
                        ],  
                        "url": "/api/2014/features/feral-senses",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 10,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 1  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-18"  
        },  
        {  
            "level": 19,  
            "ability_score_bonuses": 5,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-5",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-5",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 19,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-5",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 11,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 2  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-19"  
        },  
        {  
            "level": 20,  
            "ability_score_bonuses": 5,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "foe-slayer",  
                    "name": "Foe Slayer",  
                    "details": {  
                        "index": "foe-slayer",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Foe Slayer",  
                        "level": 20,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 20th level, you become an unparalleled hunter of your enemies. Once on each of your turns, you can add your Wisdom modifier to the attack roll or the damage roll of an attack you make against one of your favored enemies. You can choose to use this feature before or after the roll, but before any effects of the roll are applied."  
                        ],  
                        "url": "/api/2014/features/foe-slayer",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 11,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 2  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-20"  
        }  
    ]  
]  
"""  
  
spells:  
"""  
[  
    [  
        {  
            "index": "alarm",  
            "name": "Alarm",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "alarm",  
                "name": "Alarm",  
                "desc": [  
                    "You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area. When you cast the spell, you can designate creatures that won't set off the alarm. You also choose whether the alarm is mental or audible.",  
                    "A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping.",  
                    "An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A tiny bell and a piece of fine silver wire.",  
                "ritual": true,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 minute",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "cube",  
                    "size": 20  
                },  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/alarm",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "animal-friendship",  
            "name": "Animal Friendship",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "animal-friendship",  
                "name": "Animal Friendship",  
                "desc": [  
                    "This spell lets you convince a beast that you mean it no harm. Choose a beast that you can see within range. It must see and hear you. If the beast's Intelligence is 4 or higher, the spell fails. Otherwise, the beast must succeed on a wisdom saving throw or be charmed by you for the spell's duration. If you or one of your companions harms the target, the spells ends."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A morsel of food.",  
                "ritual": false,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "dc": {  
                    "dc_type": {  
                        "index": "wis",  
                        "name": "WIS",  
                        "url": "/api/2014/ability-scores/wis"  
                    },  
                    "dc_success": "none"  
                },  
                "school": {  
                    "index": "enchantment",  
                    "name": "Enchantment",  
                    "url": "/api/2014/magic-schools/enchantment"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/animal-friendship",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "cure-wounds",  
            "name": "Cure Wounds",  
            "level": 1,  
            "details": {  
                "index": "cure-wounds",  
                "name": "Cure Wounds",  
                "desc": [  
                    "A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d8 for each slot level above 1st."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "heal_at_slot_level": {  
                    "1": "1d8 + MOD",  
                    "2": "2d8 + MOD",  
                    "3": "3d8 + MOD",  
                    "4": "4d8 + MOD",  
                    "5": "5d8 + MOD",  
                    "6": "6d8 + MOD",  
                    "7": "7d8 + MOD",  
                    "8": "8d8 + MOD",  
                    "9": "9d8 + MOD"  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "life",  
                        "name": "Life",  
                        "url": "/api/2014/subclasses/life"  
                    }  
                ],  
                "url": "/api/2014/spells/cure-wounds",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "detect-magic",  
            "name": "Detect Magic",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "detect-magic",  
                "name": "Detect Magic",  
                "desc": [  
                    "For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic, and you learn its school of magic, if any.",  
                    "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/detect-magic",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "detect-poison-and-disease",  
            "name": "Detect Poison and Disease",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "detect-poison-and-disease",  
                "name": "Detect Poison and Disease",  
                "desc": [  
                    "For the duration, you can sense the presence and location of poisons, poisonous creatures, and diseases within 30 feet of you. You also identify the kind of poison, poisonous creature, or disease in each case.",  
                    "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A yew leaf.",  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/detect-poison-and-disease",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "fog-cloud",  
            "name": "Fog Cloud",  
            "level": 1,  
            "details": {  
                "index": "fog-cloud",  
                "name": "Fog Cloud",  
                "desc": [  
                    "You create a 20-foot-radius sphere of fog centered on a point within range. The sphere spreads around corners, and its area is heavily obscured. It lasts for the duration or until a wind of moderate or greater speed (at least 10 miles per hour) disperses it."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, the radius of the fog increases by 20 feet for each slot level above 1st."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 20  
                },  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/fog-cloud",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "goodberry",  
            "name": "Goodberry",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "goodberry",  
                "name": "Goodberry",  
                "desc": [  
                    "Up to ten berries appear in your hand and are infused with magic for the duration. A creature can use its action to eat one berry. Eating a berry restores 1 hit point, and the berry provides enough nourishment to sustain a creature for a day.",  
                    "The berries lose their potency if they have not been consumed within 24 hours of the casting of this spell."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A sprig of mistletoe.",  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/goodberry",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "hunters-mark",  
            "name": "Hunter's Mark",  
            "level": 1,  
            "details": {  
                "index": "hunters-mark",  
                "name": "Hunter's Mark",  
                "desc": [  
                    "You choose a creature you can see within range and mystically mark it as your quarry. Until the spell ends, you deal an extra 1d6 damage to the target whenever you hit it with a weapon attack, and you have advantage on any Wisdom (Perception) or Wisdom (Survival) check you make to find it. If the target drops to 0 hit points before this spell ends, you can use a bonus action on a subsequent turn of yours to mark a new creature."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 3rd or 4th level, you can maintain your concentration on the spell for up to 8 hours. When you use a spell slot of 5th level or higher, you can maintain your concentration on the spell for up to 24 hours."  
                ],  
                "range": "90 feet",  
                "components": [  
                    "V"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 bonus action",  
                "level": 1,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/hunters-mark",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "jump",  
            "name": "Jump",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "jump",  
                "name": "Jump",  
                "desc": [  
                    "You touch a creature. The creature's jump distance is tripled until the spell ends."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A grasshopper's hind leg.",  
                "ritual": false,  
                "duration": "1 minute",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/jump",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "longstrider",  
            "name": "Longstrider",  
            "level": 1,  
            "details": {  
                "index": "longstrider",  
                "name": "Longstrider",  
                "desc": [  
                    "You touch a creature. The target's speed increases by 10 feet until the spell ends."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each spell slot above 1st."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A pinch of dirt.",  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/longstrider",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "speak-with-animals",  
            "name": "Speak with Animals",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "speak-with-animals",  
                "name": "Speak with Animals",  
                "desc": [  
                    "You gain the ability to comprehend and verbally communicate with beasts for the duration. The knowledge and awareness of many beasts is limited by their intelligence, but at a minimum, beasts can give you information about nearby locations and monsters, including whatever they can perceive or have perceived within the past day. You might be able to persuade a beast to perform a small favor for you, at the GM's discretion."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "10 minutes",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/speak-with-animals",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "animal-messenger",  
            "name": "Animal Messenger",  
            "level": 2,  
            "details": {  
                "index": "animal-messenger",  
                "name": "Animal Messenger",  
                "desc": [  
                    "By means of this spell, you use an animal to deliver a message. Choose a Tiny beast you can see within range, such as a squirrel, a blue jay, or a bat. You specify a location, which you must have visited, and a recipient who matches a general description, such as \"a man or woman dressed in the uniform of the town guard\" or \"a red-haired dwarf wearing a pointed hat.\" You also speak a message of up to twenty-five words. The target beast travels for the duration of the spell toward the specified location, covering about 50 miles per 24 hours for a flying messenger, or 25 miles for other animals.",  
                    "When the messenger arrives, it delivers your message to the creature that you described, replicating the sound of your voice. The messenger speaks only to a creature matching the description you gave. If the messenger doesn't reach its destination before the spell ends, the message is lost, and the beast makes its way back to where you cast this spell."  
                ],  
                "higher_level": [  
                    "If you cast this spell using a spell slot of 3nd level or higher, the duration of the spell increases by 48 hours for each slot level above 2nd."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A morsel of food.",  
                "ritual": true,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "enchantment",  
                    "name": "Enchantment",  
                    "url": "/api/2014/magic-schools/enchantment"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/animal-messenger",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "barkskin",  
            "name": "Barkskin",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "barkskin",  
                "name": "Barkskin",  
                "desc": [  
                    "You touch a willing creature. Until the spell ends, the target's skin has a rough, bark-like appearance, and the target's AC can't be less than 16, regardless of what kind of armor it is wearing."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A handful of oak bark.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/barkskin",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "darkvision",  
            "name": "Darkvision",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "darkvision",  
                "name": "Darkvision",  
                "desc": [  
                    "You touch a willing creature to grant it the ability to see in the dark. For the duration, that creature has darkvision out to a range of 60 feet."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Either a pinch of dried carrot or an agate.",  
                "ritual": false,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/darkvision",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "find-traps",  
            "name": "Find Traps",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "find-traps",  
                "name": "Find Traps",  
                "desc": [  
                    "You sense the presence of any trap within range that is within line of sight. A trap, for the purpose of this spell, includes anything that would inflict a sudden or unexpected effect you consider harmful or undesirable, which was specifically intended as such by its creator. Thus, the spell would sense an area affected by the alarm spell, a glyph of warding, or a mechanical pit trap, but it would not reveal a natural weakness in the floor, an unstable ceiling, or a hidden sinkhole.",  
                    "This spell merely reveals that a trap is present. You don't learn the location of each trap, but you do learn the general nature of the danger posed by a trap you sense."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/find-traps",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "lesser-restoration",  
            "name": "Lesser Restoration",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "lesser-restoration",  
                "name": "Lesser Restoration",  
                "desc": [  
                    "You touch a creature and can end either one disease or one condition afflicting it. The condition can be blinded, deafened, paralyzed, or poisoned."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "life",  
                        "name": "Life",  
                        "url": "/api/2014/subclasses/life"  
                    },  
                    {  
                        "index": "devotion",  
                        "name": "Devotion",  
                        "url": "/api/2014/subclasses/devotion"  
                    }  
                ],  
                "url": "/api/2014/spells/lesser-restoration",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-animals-or-plants",  
            "name": "Locate Animals or Plants",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "locate-animals-or-plants",  
                "name": "Locate Animals or Plants",  
                "desc": [  
                    "Describe or name a specific kind of beast or plant. Concentrating on the voice of nature in your surroundings, you learn the direction and distance to the closest creature or plant of that kind within 5 miles, if any are present."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A bit of fur from a bloodhound.",  
                "ritual": true,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-animals-or-plants",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-object",  
            "name": "Locate Object",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "locate-object",  
                "name": "Locate Object",  
                "desc": [  
                    "Describe or name an object that is familiar to you. You sense the direction to the object's location, as long as that object is within 1,000 feet of you. If the object is in motion, you know the direction of its movement.",  
                    "The spell can locate a specific object known to you, as long as you have seen it up close--within 30 feet--at least once. Alternatively, the spell can locate the nearest object of a particular kind, such as a certain kind of apparel, jewelry, furniture, tool, or weapon.",  
                    "This spell can't locate an object if any thickness of lead, even a thin sheet, blocks a direct path between you and the object."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A forked twig.",  
                "ritual": false,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-object",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "pass-without-trace",  
            "name": "Pass Without Trace",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "pass-without-trace",  
                "name": "Pass Without Trace",  
                "desc": [  
                    "A veil of shadows and silence radiates from you, masking you and your companions from detection. For the duration, each creature you choose within 30 feet of you (including you) has a +10 bonus to Dexterity (Stealth) checks and can't be tracked except by magical means. A creature that receives this bonus leaves behind no tracks or other traces of its passage."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Ashes from a burned leaf of mistletoe and a sprig of spruce.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/pass-without-trace",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "protection-from-poison",  
            "name": "Protection from Poison",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "protection-from-poison",  
                "name": "Protection from Poison",  
                "desc": [  
                    "You touch a creature. If it is poisoned, you neutralize the poison. If more than one poison afflicts the target, you neutralize one poison that you know is present, or you neutralize one at random.",  
                    "For the duration, the target has advantage on saving throws against being poisoned, and it has resistance to poison damage."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/protection-from-poison",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "silence",  
            "name": "Silence",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "silence",  
                "name": "Silence",  
                "desc": [  
                    "For the duration, no sound can be created within or pass through a 20-foot-radius sphere centered on a point you choose within range. Any creature or object entirely inside the sphere is immune to thunder damage, and creatures are deafened while entirely inside it.",  
                    "Casting a spell that includes a verbal component is impossible there."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 20  
                },  
                "school": {  
                    "index": "illusion",  
                    "name": "Illusion",  
                    "url": "/api/2014/magic-schools/illusion"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/silence",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "spike-growth",  
            "name": "Spike Growth",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "spike-growth",  
                "name": "Spike Growth",  
                "desc": [  
                    "The ground in a 20-foot radius centered on a point within range twists and sprouts hard spikes and thorns. The area becomes difficult terrain for the duration. When a creature moves into or within the area, it takes 2d4 piercing damage for every 5 feet it travels.",  
                    "The transformation of the ground is camouflaged to look natural. Any creature that can't see the area at the time the spell is cast can make a Wisdom (Perception) check against your spell save DC to recognize the terrain as hazardous before entering it."  
                ],  
                "range": "150 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Seven sharp thorns or seven small twigs, each sharpened to a point.",  
                "ritual": false,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "area_of_effect": {  
                    "type": "cylinder",  
                    "size": 20  
                },  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/spike-growth",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "conjure-animals",  
            "name": "Conjure Animals",  
            "level": 3,  
            "details": {  
                "index": "conjure-animals",  
                "name": "Conjure Animals",  
                "desc": [  
                    "You summon fey spirits that take the form of beasts and appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:",  
                    "- One beast of challenge rating 2 or lower",  
                    "- Two beasts of challenge rating 1 or lower",  
                    "- Four beasts of challenge rating 1/2 or lower",  
                    "- Eight beasts of challenge rating 1/4 or lower",  
                    "- Each beast is also considered fey, and it disappears when it drops to 0 hit points or when the spell ends.",  
                    "The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which has its own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.",  
                    "The GM has the creatures' statistics."  
                ],  
                "higher_level": [  
                    "When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 5th-level slot, three times as many with a 7th-level."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/conjure-animals",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "daylight",  
            "name": "Daylight",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "daylight",  
                "name": "Daylight",  
                "desc": [  
                    "A 60-foot-radius sphere of light spreads out from a point you choose within range. The sphere is bright light and sheds dim light for an additional 60 feet.",  
                    "If you chose a point on an object you are holding or one that isn't being worn or carried, the light shines from the object and moves with it. Completely covering the affected object with an opaque object, such as a bowl or a helm, blocks the light.",  
                    "If any of this spell's area overlaps with an area of darkness created by a spell of 3rd level or lower, the spell that created the darkness is dispelled."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 60  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/daylight",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "nondetection",  
            "name": "Nondetection",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "nondetection",  
                "name": "Nondetection",  
                "desc": [  
                    "For the duration, you hide a target that you touch from divination magic. The target can be a willing creature or a place or an object no larger than 10 feet in any dimension. The target can't be targeted by any divination magic or perceived through magical scrying sensors."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A pinch of diamond dust worth 25 gp sprinkled over the target, which the spell consumes.",  
                "ritual": false,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/nondetection",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "plant-growth",  
            "name": "Plant Growth",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "plant-growth",  
                "name": "Plant Growth",  
                "desc": [  
                    "This spell channels vitality into plants within a specific area. There are two possible uses for the spell, granting either immediate or long-term benefits.",  
                    "If you cast this spell using 1 action, choose a point within range. All normal plants in a 100-foot radius centered on that point become thick and overgrown. A creature moving through the area must spend 4 feet of movement for every 1 foot it moves.",  
                    "You can exclude one or more areas of any size within the spell's area from being affected.",  
                    "If you cast this spell over 8 hours, you enrich the land. All plants in a half-mile radius centered on a point within range become enriched for 1 year. The plants yield twice the normal amount of food when harvested."  
                ],  
                "range": "150 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/plant-growth",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "protection-from-energy",  
            "name": "Protection From Energy",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "protection-from-energy",  
                "name": "Protection From Energy",  
                "desc": [  
                    "For the duration, the willing creature you touch has resistance to one damage type of your choice: acid, cold, fire, lightning, or thunder."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/protection-from-energy",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "speak-with-plants",  
            "name": "Speak with Plants",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "speak-with-plants",  
                "name": "Speak with Plants",  
                "desc": [  
                    "You imbue plants within 30 feet of you with limited sentience and animation, giving them the ability to communicate with you and follow your simple commands. You can question plants about events in the spell's area within the past day, gaining information about creatures that have passed, weather, and other circumstances.",  
                    "You can also turn difficult terrain caused by plant growth (such as thickets and undergrowth) into ordinary terrain that lasts for the duration. Or you can turn ordinary terrain where plants are present into difficult terrain that lasts for the duration, causing vines and branches to hinder pursuers, for example.",  
                    "Plants might be able to perform other tasks on your behalf, at the GM's discretion. The spell doesn't enable plants to uproot themselves and move about, but they can freely move branches, tendrils, and stalks.",  
                    "If a plant creature is in the area, you can communicate with it as if you shared a common language, but you gain no magical ability to influence it.",  
                    "This spell can cause the plants created by the entangle spell to release a restrained creature."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "10 minutes",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/speak-with-plants",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "water-breathing",  
            "name": "Water Breathing",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "water-breathing",  
                "name": "Water Breathing",  
                "desc": [  
                    "This spell gives a maximum of ten willing creatures within range and you can see, the ability to breathe underwater until the end of its term. Affected creatures also retain their normal breathing pattern."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A short piece of reed or straw.",  
                "ritual": true,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/water-breathing",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "water-walk",  
            "name": "Water Walk",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "water-walk",  
                "name": "Water Walk",  
                "desc": [  
                    "This spell grants the ability to move across any liquid surface--such as water, acid, mud, snow, quicksand, or lava--as if it were harmless solid ground (creatures crossing molten lava can still take damage from the heat). Up to ten willing creatures you can see within range gain this ability for the duration.",  
                    "If you target a creature submerged in a liquid, the spell carries the target to the surface of the liquid at a rate of 60 feet per round."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A piece of cork.",  
                "ritual": true,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/water-walk",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "wind-wall",  
            "name": "Wind Wall",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "wind-wall",  
                "name": "Wind Wall",  
                "desc": [  
                    "A wall of strong wind rises from the ground at a point you choose within range. You can make the wall up to 50 feet long, 15 feet high, and 1 foot thick. You can shape the wall in any way you choose so long as it makes one continuous path along the ground. The wall lasts for the duration.",  
                    "When the wall appears, each creature within its area must make a strength saving throw. A creature takes 3d8 bludgeoning damage on a failed save, or half as much damage on a successful one.",  
                    "The strong wind keeps fog, smoke, and other gases at bay. Small or smaller flying creatures or objects can't pass through the wall. Loose, lightweight materials brought into the wall fly upward. Arrows, bolts, and other ordinary projectiles launched at targets behind the wall are deflected upward and automatically miss. (Boulders hurled by giants or siege engines, and similar projectiles, are unaffected.) Creatures in gaseous form can't pass through it."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A tiny fan and a feather of exotic origin.",  
                "ritual": false,  
                "duration": "Up to 1 minute",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "damage": {  
                    "damage_type": {  
                        "index": "bludgeoning",  
                        "name": "Bludgeoning",  
                        "url": "/api/2014/damage-types/bludgeoning"  
                    },  
                    "damage_at_slot_level": {  
                        "3": "3d8"  
                    }  
                },  
                "dc": {  
                    "dc_type": {  
                        "index": "str",  
                        "name": "STR",  
                        "url": "/api/2014/ability-scores/str"  
                    },  
                    "dc_success": "half"  
                },  
                "area_of_effect": {  
                    "type": "line",  
                    "size": 50  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/wind-wall",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "conjure-woodland-beings",  
            "name": "Conjure Woodland Beings",  
            "level": 4,  
            "details": {  
                "index": "conjure-woodland-beings",  
                "name": "Conjure Woodland Beings",  
                "desc": [  
                    "You summon fey creatures that appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:",  
                    "- One fey creature of challenge rating 2 or lower",  
                    "- Two fey creatures of challenge rating 1 or lower",  
                    "- Four fey creatures of challenge rating 1/2 or lower",  
                    "- Eight fey creatures of challenge rating 1/4 or lower",  
                    "A summoned creature disappears when it drops to 0 hit points or when the spell ends.",  
                    "The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which have their own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.",  
                    "The GM has the creatures' statistics."  
                ],  
                "higher_level": [  
                    "When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 6th-level slot and three times as many with an 8th-level slot."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "One holly berry per creature summoned.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/conjure-woodland-beings",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "freedom-of-movement",  
            "name": "Freedom of Movement",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "freedom-of-movement",  
                "name": "Freedom of Movement",  
                "desc": [  
                    "You touch a willing creature. For the duration, the target's movement is unaffected by difficult terrain, and spells and other magical effects can neither reduce the target's speed nor cause the target to be paralyzed or restrained.",  
                    "The target can also spend 5 feet of movement to automatically escape from nonmagical restraints, such as manacles or a creature that has it grappled. Finally, being underwater imposes no penalties on the target's movement or attacks."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A leather strap, bound around the arm or a similar appendage.",  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    },  
                    {  
                        "index": "devotion",  
                        "name": "Devotion",  
                        "url": "/api/2014/subclasses/devotion"  
                    }  
                ],  
                "url": "/api/2014/spells/freedom-of-movement",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-creature",  
            "name": "Locate Creature",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "locate-creature",  
                "name": "Locate Creature",  
                "desc": [  
                    "Describe or name a creature that is familiar to you. You sense the direction to the creature's location, as long as that creature is within 1,000 feet of you. If the creature is moving, you know the direction of its movement.",  
                    "The spell can locate a specific creature known to you, or the nearest creature of a specific kind (such as a human or a unicorn), so long as you have seen such a creature up close--within 30 feet--at least once. If the creature you described or named is in a different form, such as being under the effects of a polymorph spell, this spell doesn't locate the creature.",  
                    "This spell can't locate a creature if running water at least 10 feet wide blocks a direct path between you and the creature."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A bit of fur from a bloodhound.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-creature",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "stoneskin",  
            "name": "Stoneskin",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "stoneskin",  
                "name": "Stoneskin",  
                "desc": [  
                    "This spell turns the flesh of a willing creature you touch as hard as stone. Until the spell ends, the target has resistance to nonmagical bludgeoning, piercing, and slashing damage."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Diamond dust worth 100 gp, which the spell consumes.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/stoneskin",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "commune-with-nature",  
            "name": "Commune With Nature",  
            "level": 5,  
            "details": {  
                "higher_level": [],  
                "index": "commune-with-nature",  
                "name": "Commune With Nature",  
                "desc": [  
                    "You briefly become one with nature and gain knowledge of the surrounding territory. In the outdoors, the spell gives you knowledge of the land within 3 miles of you. In caves and other natural underground settings, the radius is limited to 300 feet. The spell doesn't function where nature has been replaced by construction, such as in dungeons and towns.",  
                    "You instantly gain knowledge of up to three facts of your choice about any of the following subjects as they relate to the area:",  
                    "- terrain and bodies of water",  
                    "- prevalent plants, minerals, animals, or peoples",  
                    "- powerful celestials, fey, fiends, elementals, or undead",  
                    "- influence from other planes of existence",  
                    "- buildings",  
                    "For example, you could determine the location of powerful undead in the area, the location of major sources of safe drinking water, and the location of any nearby towns."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 minute",  
                "level": 5,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/commune-with-nature",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "tree-stride",  
            "name": "Tree Stride",  
            "level": 5,  
            "details": {  
                "higher_level": [],  
                "index": "tree-stride",  
                "name": "Tree Stride",  
                "desc": [  
                    "You gain the ability to enter a tree and move from inside it to inside another tree of the same kind within 500 feet. Both trees must be living and at least the same size as you. You must use 5 feet of movement to enter a tree. You instantly know the location of all other trees of the same kind within 500 feet and, as part of the move used to enter the tree, can either pass into one of those trees or step out of the tree you're in. You appear in a spot of your choice within 5 feet of the destination tree, using another 5 feet of movement. If you have no movement left, you appear within 5 feet of the tree you entered.",  
                    "You can use this transportation ability once per round for the duration. You must end each turn outside a tree."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 minute",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 5,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/tree-stride",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        }  
    ]  
]  
"""  
  
sublcass_data:  
"""  
[  
    [  
        {  
            "index": "hunter",  
            "class": {  
                "index": "ranger",  
                "name": "Ranger",  
                "url": "/api/2014/classes/ranger"  
            },  
            "name": "Hunter",  
            "subclass_flavor": "Ranger Archetype",  
            "desc": [  
                "Emulating the Hunter archetype means accepting your place as a bulwark between civilization and the terrors of the wilderness. As you walk the Hunter's path, you learn specialized techniques for fighting the threats you face, from rampaging ogres and hordes of orcs to towering giants and terrifying dragons."  
            ],  
            "subclass_levels": [  
                {  
                    "level": 3,  
                    "features": [  
                        {  
                            "index": "hunters-prey",  
                            "name": "Hunter's Prey",  
                            "details": {  
                                "index": "hunters-prey",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Hunter's Prey",  
                                "level": 3,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 3rd level, you gain one of the following features of your choice.",  
                                    "Colossus Slayer",  
                                    "Giant Killer",  
                                    "Horde Breaker"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-colossus-slayer",  
                                                        "name": "Hunter's Prey: Colossus Slayer",  
                                                        "url": "/api/2014/features/hunters-prey-colossus-slayer"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-giant-killer",  
                                                        "name": "Hunter's Prey: Giant Killer",  
                                                        "url": "/api/2014/features/hunters-prey-giant-killer"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-horde-breaker",  
                                                        "name": "Hunter's Prey: Horde Breaker",  
                                                        "url": "/api/2014/features/hunters-prey-horde-breaker"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/hunters-prey",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/3",  
                    "index": "hunter-3",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 7,  
                    "features": [  
                        {  
                            "index": "defensive-tactics",  
                            "name": "Defensive Tactics",  
                            "details": {  
                                "index": "defensive-tactics",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Defensive Tactics",  
                                "level": 7,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 7th level, you gain one of the following features of your choice.",  
                                    "Escape the Horde",  
                                    "Multiattack Defense",  
                                    "Steel Will"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-escape-the-horde",  
                                                        "name": "Defensive Tactics: Escape the Horde",  
                                                        "url": "/api/2014/features/defensive-tactics-escape-the-horde"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-multiattack-defense",  
                                                        "name": "Defensive Tactics: Multiattack Defense",  
                                                        "url": "/api/2014/features/defensive-tactics-multiattack-defense"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-steel-will",  
                                                        "name": "Defensive Tactics: Steel Will",  
                                                        "url": "/api/2014/features/defensive-tactics-steel-will"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/defensive-tactics",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/7",  
                    "index": "hunter-7",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 11,  
                    "features": [  
                        {  
                            "index": "multiattack",  
                            "name": "Multiattack",  
                            "details": {  
                                "index": "multiattack",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Multiattack",  
                                "level": 11,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 11th level, you gain one of the following features of your choice.",  
                                    "Volley",  
                                    "Whirlwind Attack"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "multiattack-volley",  
                                                        "name": "Multiattack: Volley",  
                                                        "url": "/api/2014/features/multiattack-volley"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "multiattack-whirlwind-attack",  
                                                        "name": "Multiattack: Whirlwind Attack",  
                                                        "url": "/api/2014/features/multiattack-whirlwind-attack"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/multiattack",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/11",  
                    "index": "hunter-11",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 15,  
                    "features": [  
                        {  
                            "index": "superior-hunters-defense",  
                            "name": "Superior Hunter's Defense",  
                            "details": {  
                                "index": "superior-hunters-defense",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Superior Hunter's Defense",  
                                "level": 15,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 15th level, you gain one of the following features of your choice.",  
                                    "Evasion",  
                                    "Stand Against the Tide",  
                                    "Uncanny Dodge"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-evasion",  
                                                        "name": "Superior Hunter's Defense: Evasion",  
                                                        "url": "/api/2014/features/superior-hunters-defense-evasion"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-stand-against-the-tide",  
                                                        "name": "Superior Hunter's Defense: Stand Against the Tide",  
                                                        "url": "/api/2014/features/superior-hunters-defense-stand-against-the-tide"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-uncanny-dodge",  
                                                        "name": "Superior Hunter's Defense: Uncanny Dodge",  
                                                        "url": "/api/2014/features/superior-hunters-defense-uncanny-dodge"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/superior-hunters-defense",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/15",  
                    "index": "hunter-15",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                }  
            ],  
            "url": "/api/2014/subclasses/hunter",  
            "updated_at": "2025-04-08T21:14:17.800Z",  
            "spells": []  
        }  
    ]  
]  
"""  
'''
Hier noch mal das format in dem du die antwort zurück geben sollst.

Rückgabeformat: text  
Verbotene formate: Markdwon  
vorboteneer inhalt: ```json, ```
```
#### Character:
```
{
    "name": "Robin Hood",
    "level": 10,
    "hit_points": 85,
    "proficiency_bonus": 4,
    "subclass": "Hunter",
    "attributes": {
        "strength": 12,
        "dexterity": 20,
        "constitution": 14,
        "intelligence": 10,
        "wisdom": 16,
        "charisma": 14
    },
    "attribute_proficiencies": {
        "strength": false,
        "dexterity": true,
        "constitution": false,
        "intelligence": false,
        "wisdom": true,
        "charisma": false
    },
    "saving_throws": {
        "strength": 7,
        "dexterity": 11,
        "constitution": 7,
        "intelligence": 5,
        "wisdom": 9,
        "charisma": 7
    },
    "armor_class": 17,
    "attack_bonus": 8,
    "spellcasting": {
        "spellcasting_bonus": 5,
        "spellcasting_dc": 15,
        "spellcasting_attack_bonus": 7,
        "cantrips_known": 0,
        "spells_prepared": 6,
        "spell_slots": {
            "1st": 4,
            "2nd": 3,
            "3rd": 2,
            "4th": 0,
            "5th": 0
        },
        "known_spells": {
            "1st_level": [
                "Hunter's Mark",
                "Longstrider",
                "Cure Wounds",
                "Detect Magic"
            ],
            "2nd_level": [
                "Pass Without Trace",
                "Barkskin",
                "Silence"
            ],
            "3rd_level": [
                "Conjure Animals",
                "Wind Wall"
            ]
        },
        "prepared_spells": {
            "1st_level": [
                "Hunter's Mark (D)",
                "Longstrider (D)",
                "Cure Wounds (S)"
            ],
            "2nd_level": [
                "Pass Without Trace (D)",
                "Barkskin (S)"
            ],
            "3rd_level": [
                "Conjure Animals (D)"
            ]
        }
    },
    "skills": {
        "strength_skills": {
            "athletics": {
                "bonus": 1,
                "proficiency_bonus": false
            }
        },
        "dexterity_skills": {
            "acrobatics": {
                "bonus": 10,
                "proficiency_bonus": true
            },
            "sleight_of_hand": {
                "bonus": 10,
                "proficiency_bonus": true
            },
            "stealth": {
                "bonus": 14,
                "proficiency_bonus": true
            }
        },
        "intelligence_skills": {
            "arcana": {
                "bonus": 0,
                "proficiency_bonus": false
            },
            "history": {
                "bonus": 0,
                "proficiency_bonus": false
            },
            "investigation": {
                "bonus": 0,
                "proficiency_bonus": false
            },
            "nature": {
                "bonus": 6,
                "proficiency_bonus": true
            },
            "religion": {
                "bonus": 0,
                "proficiency_bonus": false
            }
        },
        "wisdom_skills": {
            "animal_handling": {
                "bonus": 8,
                "proficiency_bonus": true
            },
            "insight": {
                "bonus": 8,
                "proficiency_bonus": true
            },
            "medicine": {
                "bonus": 3,
                "proficiency_bonus": false
            },
            "perception": {
                "bonus": 10,
                "proficiency_bonus": true
            },
            "survival": {
                "bonus": 10,
                "proficiency_bonus": true
            }
        },
        "charisma_skills": {
            "deception": {
                "bonus": 2,
                "proficiency_bonus": false
            },
            "intimidation": {
                "bonus": 2,
                "proficiency_bonus": false
            },
            "performance": {
                "bonus": 6,
                "proficiency_bonus": true
            },
            "persuasion": {
                "bonus": 6,
                "proficiency_bonus": true
            }
        }
    },
    "features": [
        "Favored Enemy (Humanoids)",
        "Natural Explorer (Forest)",
        "Fighting Style: Archery",
        "Spellcasting",
        "Primeval Awareness",
        "Extra Attack",
        "Land's Stride",
        "Hide in Plain Sight",
        "Hunter's Prey: Horde Breaker",
        "Defensive Tactics: Escape the Horde"
    ],
    "special_abilities_and_traits": [
        "Darkvision (60 ft)",
        "Fey Ancestry",
        "Trance",
        "Mask of the Wild"
    ],
    "languages": [
        "Common",
        "Elvish",
        "Sylvan"
    ],
    "equipment": [
        "Longbow",
        "Quiver with 20 arrows",
        "Leather armor",
        "Two shortswords",
        "Explorer's pack",
        "A hooded cloak",
        "A hunting trap",
        "A trophy from an animal killed by you"
    ],
    "additional_equipment": [
        "Bedroll",
        "Mess kit",
        "Tinderbox",
        "10 torches",
        "10 days of rations",
        "Waterskin",
        "50 feet of hempen rope",
        "A belt pouch containing 10 GP"
    ],
    "money": {
        "platinum": 0,
        "gold": 50,
        "electrum": 0,
        "silver": 20,
        "copper": 50
    },
    "weapons": {
        "longbow": {
            "damage": "1d8 piercing",
            "attack_bonus": 8,
            "properties": [
                "Ammunition",
                "Heavy",
                "Two-Handed"
            ],
            "range": "150/600 ft"
        },
        "shortsword": {
            "damage": "1d6 piercing",
            "attack_bonus": 8,
            "properties": [
                "Finesse",
                "Light"
            ]
        }
    }
}

```

## Gemini 2.5 Flash

>[!Warning] **Resume:**
>
>Prompt_lenght: `191562`
>Gemini ist komplett durchgefallen. 
>Gemini konnte weder den Prompt direkt ausführen, da er zu groß war; noch konnte Gemini den Prompt als file oder gesplitted in 11 kleinere files, verarbeiten. 
>
>die Antwort von Gemini auf die 11 angehängten files war: 
>```
>The provided files contain information about Dungeons and Dragons (D&D) classes and spells in JSON format, along with details for creating a character. I will act as a D&D expert to create a character based on this information.
>
>My task is to construct a D&D character, selecting abilities and spells that align with the themes of 'Necromancy', 'dark magic', and 'fire magic' as described in the character details example. The final character will be returned in JSON format.
>
I have successfully retrieved the content from all the provided files:
>
>- `gemini_texts_1.txt`
  >  
>- `gemini_texts_2.txt`
mini_texts_3.txt`
  >  
>- `gemini_texts_4.txt`
  >  
>- `gemini_texts_5.txt`
  >  
>- `gemini_texts_6.txt`
  >  
>- `gemini_texts_7.txt`
  >  
>- `gemini_texts_8.txt`
  >  
>- `gemini_texts_9.txt`
  >  
>- `gemini_texts_10.txt`
  >  
>
Now I will proceed to combine and parse the content to generate the character.
>```
>
>Mein Resume ist daher: **F**

>[!Info]+ Analysed Data:
>**prompt_1** : 
>```
>Erstelle einen Robin Hood als Ranger, Level 10.. Orientiere dich bei dem ranger an folgenden details: ["Robin Hood", "Dieb", "Bogenschütze", "gerecht"]
>```
>
>**prompt_2** :
>```
>Erstelle einen Robin Hood als Rogue, Level 10.. Orientiere dich bei dem rogue an folgenden details: ["Robin Hood", "Dieb", "Bogenschütze", "gerecht"]
>```
>
>**prompt_3**: 
>```
>Erstelle einen Robin Hood als Fighter, Level 10.. Orientiere dich bei dem fighter an folgenden details: ["Robin Hood", "Dieb", "Bogenschütze", "gerecht"]
>```


### CharacterGeneration

#### CharGenPrompt:
```
Du bist ein Dungeons and Dragons(DnD) Experte. Du erstellst DnD Charactere.  
Um einen Character zu erstellen erhälst du alle nötigen Informationen für eine Klasse im Json format, an diesen Prompt als json-file angehängt.  
Zusätzlich bekommst du Details zu dem Character, die den character noch einmal näher definieren.  
  
Ein beispiel für die Details ist:  
- Ein dunkler Magier Level 8, der tote beschwören kann und mit Feuermagie zaubert.  
In diesem Beispiel sollst du den DnD Character so erstellen, dass er viele Fähigkeiten hat, die in das Themengebiet 'Necromantie', 'dunkle Magie' und 'Feuermagie' fallen.  
Du wirst in den daten, die du erhälst immer wieder Fähgikeiten auswählen können. Wähle bei diesen auch so, dass die Auswhl den genannten Character Details entsprechen.  
  
Den erstellen Character sollst du im Json Format zurück geben.  
Hier ist ein Beispiel für einen DnD character der stufe 20:  
  
{  
    "name": "Cleric",    "level": 20,    "hit_points": 150,    "proficiency_bonus": 6,    "subclass": "Life Domain",    "attributes": {        "strength": 12,        "dexterity": 14,        "constitution": 14,        "intelligence": 10,        "wisdom": 20,        "charisma": 8    },    "attribute_proficiencys": {      "strength": false,        "dexterity": false,        "constitution": false,        "intelligence": false,        "wisdom": true,        "charisma": true    },    "saving_throws": {      "strength": 1,        "dexterity": 2,        "constitution": 2,        "intelligence": 0,        "wisdom": 11,        "charisma": 5    },  
    "armor_class": 18,    "attack_bonus": 8,    "spellcasting": {        "spellcasting_bonus": 11,        "spellcasting_dc": 19,        "spellcasting_attack_bonus": 11,        "cantrips_known": 5,        "spells_prepared": 25,        "spell_slots": {            "1st": 4,            "2nd": 4,            "3rd": 4,            "4th": 4,            "5th": 3,            "6th": 3,            "7th": 2,            "8th": 2,            "9th": 1        },        "known_spells": {            "cantrips": ["Guidance", "Light", "Sacred Flame", "Thaumaturgy", "Toll the Dead"],            "1st_level": ["Bless", "Cure Wounds", "Guiding Bolt", "Infestation", "Magic Stone"],            "2nd_level": ["Lesser Restoration", "Prayer of Healing", "Spiritual Weapon", "Warding Bond", "Zone of Truth"],            "3rd_level": ["Mass Healing Word", "Revivify", "Sending", "Spirit Guardians", "Water Walk"],            "4th_level": ["Banishment", "Control Water", "Death Ward", "Freedom of Movement", "Guardian of Faith"],            "5th_level": ["Circle of Power", "Contagion", "Flame Strike", "Geas", "Insect Plague"],            "6th_level": ["Blade Barrier", "Create Undead", "Harm", "Heal", "Heroes' Feast"],            "7th_level": ["Conjure Celestial", "Divine Word", "Etherealness", "Fire Storm", "Regenerate"],            "8th_level": ["Antimagic Field", "Control Weather", "Earthquake", "Holy Aura", "Sunburst"],            "9th_level": ["Astral Projection", "Gate", "Mass Heal", "True Resurrection", "Weird"]        },        "prepared_spells": {            "cantrips": ["Guidance (S)", "Sacred Flame (D)", "Thaumaturgy (S)", "Toll the Dead (D)"],            "1st_level": ["Bless (S)", "Cure Wounds (S)", "Guiding Bolt (D)", "Infestation (D)"],            "2nd_level": ["Lesser Restoration (S)", "Prayer of Healing (S)", "Spiritual Weapon (D)"],            "3rd_level": ["Mass Healing Word (S)", "Revivify (S)", "Spirit Guardians (D)"],            "4th_level": ["Banishment (D)", "Death Ward (S)", "Guardian of Faith (D)"],            "5th_level": ["Flame Strike (D)", "Insect Plague (D)"],            "6th_level": ["Harm (D)", "Heal (S)"],            "7th_level": ["Fire Storm (D)", "Regenerate (S)"],            "8th_level": ["Earthquake (D)", "Holy Aura (S)"],            "9th_level": ["Mass Heal (S)" ]        }    },    "skills": {        "strength_skills": {            "athletics": {"bonus": 9, "proficiency_bonus": true}        },        "dexterity_skills": {            "acrobatics": {"bonus": 5, "proficiency_bonus": false},            "sleight_of_hand": {"bonus": 5, "proficiency_bonus": false},            "stealth": {"bonus": 5, "proficiency_bonus": false}        },        "intelligence_skills": {            "arcana": {"bonus": 3, "proficiency_bonus": false},            "history": {"bonus": 3, "proficiency_bonus": false},            "investigation": {"bonus": 3, "proficiency_bonus": false},            "nature": {"bonus": 3, "proficiency_bonus": false},            "religion": {"bonus": 9, "proficiency_bonus": true}        },        "wisdom_skills": {            "animal_handling": {"bonus": 13, "proficiency_bonus": true},            "insight": {"bonus": 13, "proficiency_bonus": true},            "medicine": {"bonus": 13, "proficiency_bonus": true},            "perception": {"bonus": 13, "proficiency_bonus": true},            "survival": {"bonus": 13, "proficiency_bonus": true}        },        "charisma_skills": {            "deception": {"bonus": 1, "proficiency_bonus": false},            "intimidation": {"bonus": 1, "proficiency_bonus": false},            "performance": {"bonus": 1, "proficiency_bonus": false},            "persuasion": {"bonus": 7, "proficiency_bonus": true}        }    },  
    "features": [        "Spellcasting",        "Channel Divinity (2/short rest)",        "Destroy Undead (CR 3)",        "Divine Intervention (1/long rest)",        "Domain Spells",        "Blessed Healer",        "Divine Strike",        "Supreme Healing",        "Life Domain: Preserve Life",        "Life Domain: Blessed Healer"    ],    "special_abilities_and_traits": [        "Darkvision (60 ft)",        "Ritual Casting",        "Life Domain: Bonus Proficiency in Heavy Armor"    ],    "languages": ["Common", "Celestial", "Primordial"],    "equipment": [        "Mace",        "Scale mail armor",        "Light crossbow and 20 bolts",        "Dungeoneer's pack",        "A holy symbol"    ],    "additional_equipment": [        "Bedroll",        "Mess kit",        "10 ball bearings",        "10 feet of string",        "A belt pouch containing 10 GP"    ],    "money": {        "platinum": 0,        "gold": 100,        "electrum": 0,        "silver": 50,        "copper": 25    },    "weapons": {        "mace": {            "damage": "1d6 bludgeoning",            "attack_bonus": 8,            "properties": ["Light"]        },        "light_crossbow": {            "damage": "1d8 piercing",            "attack_bonus": 7,            "properties": ["Ammunition", "Loading", "Two-Handed"],            "range": "80/320 ft"        }    }}  
  
  
Geb nur den erstellen character in genau dieser struktur zurück, wie ich sie dir im beispiel gezeigt habe.  
Füge kein 'Json' kennzeichen. Nur den reinen text.  
  
Achte darauf, dass das Level der beispiel-struktur 20 ist. Nicht jeder Character soll auf level 20 erstellt werden!  
  
Wenn du in der Characterbeschreibung keine klar erkennbare Level-höhe herauslesen kannst,  
dann wähle ein level, dass zu den stärke-beschreibungen passt.  
Wenn z.B der Prompt lautet: 'Starker Krieger', dann kannst du das level ruhig auf 5-8 setzten.  
Wenn aber der Prompt ist: 'super starker Krieger', oder 'Heroischer Champion', dann setze das Level gern zwischen 10  und 14.  
Wenn das Wort 'gottgleich' oder andere extreme worte für die Mächtigkeit eines Characters fallen,  
dann kannst du das Level gern auf 18 - 20 setzten.  
  
Das gleiche gilt für schwache wörter.  
z.B 'schwacher Krieger', wäre eher Level 1-4.  
  
Falls keine dieser - oder andere - Schlagwörter für die Stärke eines Characters fallen, dann setzte das Level pauschal auf 5 - 8  
  
Als nächstes kommt die aufforderung den character zu erstellen, mit den KLassen daten und den character details.  
  
Das hier ist die Aufferderung den Character zu erstellen:  
'''  
Erstelle einen Robin Hood als Ranger, Level 10.. Orientiere dich bei dem ranger an folgenden details: ["Robin Hood", "Dieb", "Bogenschütze", "gerecht"]
'''  
  
Jetzt kommen allen nötigen Klassendaten:  
'''  
Base_data_for_class:  
"""  
{  
        "index": "ranger",  
        "name": "Ranger",  
        "hit_die": 10,  
        "proficiency_choices": [  
            {  
                "desc": "Choose three from Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, and Survival",  
                "choose": 3,  
                "type": "proficiencies",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-animal-handling",  
                                "name": "Skill: Animal Handling",  
                                "url": "/api/2014/proficiencies/skill-animal-handling"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-athletics",  
                                "name": "Skill: Athletics",  
                                "url": "/api/2014/proficiencies/skill-athletics"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-insight",  
                                "name": "Skill: Insight",  
                                "url": "/api/2014/proficiencies/skill-insight"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-investigation",  
                                "name": "Skill: Investigation",  
                                "url": "/api/2014/proficiencies/skill-investigation"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-nature",  
                                "name": "Skill: Nature",  
                                "url": "/api/2014/proficiencies/skill-nature"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-perception",  
                                "name": "Skill: Perception",  
                                "url": "/api/2014/proficiencies/skill-perception"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-stealth",  
                                "name": "Skill: Stealth",  
                                "url": "/api/2014/proficiencies/skill-stealth"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-survival",  
                                "name": "Skill: Survival",  
                                "url": "/api/2014/proficiencies/skill-survival"  
                            }  
                        }  
                    ]  
                }  
            }  
        ],  
        "proficiencies": [  
            {  
                "index": "light-armor",  
                "name": "Light Armor",  
                "url": "/api/2014/proficiencies/light-armor"  
            },  
            {  
                "index": "medium-armor",  
                "name": "Medium Armor",  
                "url": "/api/2014/proficiencies/medium-armor"  
            },  
            {  
                "index": "shields",  
                "name": "Shields",  
                "url": "/api/2014/proficiencies/shields"  
            },  
            {  
                "index": "simple-weapons",  
                "name": "Simple Weapons",  
                "url": "/api/2014/proficiencies/simple-weapons"  
            },  
            {  
                "index": "martial-weapons",  
                "name": "Martial Weapons",  
                "url": "/api/2014/proficiencies/martial-weapons"  
            },  
            {  
                "index": "saving-throw-dex",  
                "name": "Saving Throw: DEX",  
                "url": "/api/2014/proficiencies/saving-throw-dex"  
            },  
            {  
                "index": "saving-throw-str",  
                "name": "Saving Throw: STR",  
                "url": "/api/2014/proficiencies/saving-throw-str"  
            }  
        ],  
        "saving_throws": [  
            {  
                "index": "str",  
                "name": "STR",  
                "url": "/api/2014/ability-scores/str"  
            },  
            {  
                "index": "dex",  
                "name": "DEX",  
                "url": "/api/2014/ability-scores/dex"  
            }  
        ],  
        "starting_equipment": [  
            {  
                "equipment": {  
                    "index": "longbow",  
                    "name": "Longbow",  
                    "url": "/api/2014/equipment/longbow"  
                },  
                "quantity": 1  
            },  
            {  
                "equipment": {  
                    "index": "arrow",  
                    "name": "Arrow",  
                    "url": "/api/2014/equipment/arrow"  
                },  
                "quantity": 20  
            }  
        ],  
        "starting_equipment_options": [  
            {  
                "desc": "(a) scale mail or (b) leather armor",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "scale-mail",  
                                "name": "Scale Mail",  
                                "url": "/api/2014/equipment/scale-mail"  
                            }  
                        },  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "leather-armor",  
                                "name": "Leather Armor",  
                                "url": "/api/2014/equipment/leather-armor"  
                            }  
                        }  
                    ]  
                }  
            },  
            {  
                "desc": "(a) two shortswords or (b) two simple melee weapons",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 2,  
                            "of": {  
                                "index": "shortsword",  
                                "name": "Shortsword",  
                                "url": "/api/2014/equipment/shortsword"  
                            }  
                        },  
                        {  
                            "option_type": "choice",  
                            "choice": {  
                                "desc": "two simple melee weapons",  
                                "choose": 2,  
                                "type": "equipment",  
                                "from": {  
                                    "option_set_type": "equipment_category",  
                                    "equipment_category": {  
                                        "index": "simple-melee-weapons",  
                                        "name": "Simple Melee Weapons",  
                                        "url": "/api/2014/equipment-categories/simple-melee-weapons"  
                                    }  
                                }  
                            }  
                        }  
                    ]  
                }  
            },  
            {  
                "desc": "(a) a dungeoneer\u2019s pack or (b) an explorer\u2019s pack",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "dungeoneers-pack",  
                                "name": "Dungeoneer's Pack",  
                                "url": "/api/2014/equipment/dungeoneers-pack"  
                            }  
                        },  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "explorers-pack",  
                                "name": "Explorer's Pack",  
                                "url": "/api/2014/equipment/explorers-pack"  
                            }  
                        }  
                    ]  
                }  
            }  
        ],  
        "class_levels": "/api/2014/classes/ranger/levels",  
        "multi_classing": {  
            "prerequisites": [  
                {  
                    "ability_score": {  
                        "index": "dex",  
                        "name": "DEX",  
                        "url": "/api/2014/ability-scores/dex"  
                    },  
                    "minimum_score": 13  
                },  
                {  
                    "ability_score": {  
                        "index": "wis",  
                        "name": "WIS",  
                        "url": "/api/2014/ability-scores/wis"  
                    },  
                    "minimum_score": 13  
                }  
            ],  
            "proficiencies": [  
                {  
                    "index": "light-armor",  
                    "name": "Light Armor",  
                    "url": "/api/2014/proficiencies/light-armor"  
                },  
                {  
                    "index": "medium-armor",  
                    "name": "Medium Armor",  
                    "url": "/api/2014/proficiencies/medium-armor"  
                },  
                {  
                    "index": "shields",  
                    "name": "Shields",  
                    "url": "/api/2014/proficiencies/shields"  
                },  
                {  
                    "index": "simple-weapons",  
                    "name": "Simple Weapons",  
                    "url": "/api/2014/proficiencies/simple-weapons"  
                },  
                {  
                    "index": "martial-weapons",  
                    "name": "Martial Weapons",  
                    "url": "/api/2014/proficiencies/martial-weapons"  
                }  
            ],  
            "proficiency_choices": [  
                {  
                    "choose": 1,  
                    "type": "proficiencies",  
                    "from": {  
                        "option_set_type": "options_array",  
                        "options": [  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-animal-handling",  
                                    "name": "Skill: Animal Handling",  
                                    "url": "/api/2014/proficiencies/skill-animal-handling"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-athletics",  
                                    "name": "Skill: Athletics",  
                                    "url": "/api/2014/proficiencies/skill-athletics"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-insight",  
                                    "name": "Skill: Insight",  
                                    "url": "/api/2014/proficiencies/skill-insight"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-investigation",  
                                    "name": "Skill: Investigation",  
                                    "url": "/api/2014/proficiencies/skill-investigation"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-nature",  
                                    "name": "Skill: Nature",  
                                    "url": "/api/2014/proficiencies/skill-nature"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-perception",  
                                    "name": "Skill: Perception",  
                                    "url": "/api/2014/proficiencies/skill-perception"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-stealth",  
                                    "name": "Skill: Stealth",  
                                    "url": "/api/2014/proficiencies/skill-stealth"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-survival",  
                                    "name": "Skill: Survival",  
                                    "url": "/api/2014/proficiencies/skill-survival"  
                                }  
                            }  
                        ]  
                    }  
                }  
            ]  
        },  
        "subclasses": [  
            {  
                "index": "hunter",  
                "name": "Hunter",  
                "url": "/api/2014/subclasses/hunter"  
            }  
        ],  
        "spellcasting": {  
            "level": 2,  
            "spellcasting_ability": {  
                "index": "wis",  
                "name": "WIS",  
                "url": "/api/2014/ability-scores/wis"  
            },  
            "info": [  
                {  
                    "name": "Spell Slots",  
                    "desc": [  
                        "The Ranger table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.",  
                        "For example, if you know the 1st-level spell animal friendship and have a 1st-level and a 2nd-level spell slot available, you can cast animal friendship using either slot."  
                    ]  
                },  
                {  
                    "name": "Spells Known of 1st Level and Higher",  
                    "desc": [  
                        "You know two 1st-level spells of your choice from the ranger spell list.",  
                        "The Spells Known column of the Ranger table shows when you learn more ranger spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 5th level in this class, you can learn one new spell of 1st or 2nd level.",  
                        "Additionally, when you gain a level in this class, you can choose one of the ranger spells you know and replace it with another spell from the ranger spell list, which also must be of a level for which you have spell slots."  
                    ]  
                },  
                {  
                    "name": "Spellcasting Ability",  
                    "desc": [  
                        "Wisdom is your spellcasting ability for your ranger spells, since your magic draws on your attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a ranger spell you cast and when making an attack roll with one.",  
                        "Spell save DC = 8 + your proficiency bonus + your Wisdom modifier.",  
                        "Spell attack modifier = your proficiency bonus + your Wisdom modifier."  
                    ]  
                }  
            ]  
        },  
        "spells": "/api/2014/classes/ranger/spells",  
        "url": "/api/2014/classes/ranger"  
    }  
"""  
      
  
level_features:  
"""  
[  
    [  
        {  
            "level": 1,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "favored-enemy-1-type",  
                    "name": "Favored Enemy (1 type)",  
                    "details": {  
                        "index": "favored-enemy-1-type",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (1 type)",  
                        "level": 1,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-1-type",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "natural-explorer-1-terrain-type",  
                    "name": "Natural Explorer (1 terrain type)",  
                    "details": {  
                        "index": "natural-explorer-1-terrain-type",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (1 terrain type)",  
                        "level": 1,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-1-terrain-type",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 0,  
                "spell_slots_level_1": 0,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-1"  
        },  
        {  
            "level": 2,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-fighting-style",  
                    "name": "Fighting Style",  
                    "details": {  
                        "index": "ranger-fighting-style",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Fighting Style",  
                        "level": 2,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 2nd level, you adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again."  
                        ],  
                        "feature_specific": {  
                            "subfeature_options": {  
                                "choose": 1,  
                                "type": "feature",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-archery",  
                                                "name": "Fighting Style: Archery",  
                                                "url": "/api/2014/features/ranger-fighting-style-archery"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-defense",  
                                                "name": "Fighting Style: Defense",  
                                                "url": "/api/2014/features/ranger-fighting-style-defense"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-dueling",  
                                                "name": "Fighting Style: Dueling",  
                                                "url": "/api/2014/features/ranger-fighting-style-dueling"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-two-weapon-fighting",  
                                                "name": "Fighting Style: Two-Weapon Fighting",  
                                                "url": "/api/2014/features/ranger-fighting-style-two-weapon-fighting"  
                                            }  
                                        }  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/ranger-fighting-style",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "spellcasting-ranger",  
                    "name": "Spellcasting: Ranger",  
                    "details": {  
                        "index": "spellcasting-ranger",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Spellcasting: Ranger",  
                        "level": 2,  
                        "prerequisites": [],  
                        "desc": [  
                            "By the time you reach 2nd level, you have learned to use the magical essence of nature to cast spells, much as a druid does."  
                        ],  
                        "reference": "/api/2014/classes/ranger/spellcasting",  
                        "url": "/api/2014/features/spellcasting-ranger",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 2,  
                "spell_slots_level_1": 2,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-2"  
        },  
        {  
            "level": 3,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-archetype",  
                    "name": "Ranger Archetype",  
                    "details": {  
                        "index": "ranger-archetype",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ranger Archetype",  
                        "level": 3,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 3rd level, you choose an archetype that you strive to emulate, such as the Hunter. Your choice grants you features at 3rd level and again at 7th, 11th, and 15th level."  
                        ],  
                        "url": "/api/2014/features/ranger-archetype",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "primeval-awareness",  
                    "name": "Primeval Awareness",  
                    "details": {  
                        "index": "primeval-awareness",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Primeval Awareness",  
                        "level": 3,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 3rd level, you can use your action and expend one ranger spell slot to focus your awareness on the region around you. For 1 minute per level of the spell slot you expend, you can sense whether the following types of creatures are present within 1 mile of you (or within up to 6 miles if you are in your favored terrain): aberrations, celestials, dragons, elementals, fey, fiends, and undead. This feature doesn't reveal the creatures' location or number."  
                        ],  
                        "url": "/api/2014/features/primeval-awareness",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 3,  
                "spell_slots_level_1": 3,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-3"  
        },  
        {  
            "level": 4,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-1",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-1",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 4,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-1",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 3,  
                "spell_slots_level_1": 3,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-4"  
        },  
        {  
            "level": 5,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "ranger-extra-attack",  
                    "name": "Extra Attack",  
                    "details": {  
                        "index": "ranger-extra-attack",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Extra Attack",  
                        "level": 5,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."  
                        ],  
                        "url": "/api/2014/features/ranger-extra-attack",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 4,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 2,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-5"  
        },  
        {  
            "level": 6,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "favored-enemy-2-types",  
                    "name": "Favored Enemy (2 types)",  
                    "details": {  
                        "index": "favored-enemy-2-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (2 types)",  
                        "level": 6,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-2-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "natural-explorer-2-terrain-types",  
                    "name": "Natural Explorer (2 terrain types)",  
                    "details": {  
                        "index": "natural-explorer-2-terrain-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (2 terrain types)",  
                        "level": 6,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-2-terrain-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 4,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 2,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-6"  
        },  
        {  
            "level": 7,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 5,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-7"  
        },  
        {  
            "level": 8,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-2",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-2",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 8,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-2",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "ranger-lands-stride",  
                    "name": "Land's Stride",  
                    "details": {  
                        "index": "ranger-lands-stride",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Land's Stride",  
                        "level": 8,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 8th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.",  
                            "In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such those created by the entangle spell."  
                        ],  
                        "url": "/api/2014/features/ranger-lands-stride",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 5,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-8"  
        },  
        {  
            "level": 9,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 6,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 2,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-9"  
        },  
        {  
            "level": 10,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [  
                {  
                    "index": "natural-explorer-3-terrain-types",  
                    "name": "Natural Explorer (3 terrain types)",  
                    "details": {  
                        "index": "natural-explorer-3-terrain-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (3 terrain types)",  
                        "level": 10,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-3-terrain-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "hide-in-plain-sight",  
                    "name": "Hide in Plain Sight",  
                    "details": {  
                        "index": "hide-in-plain-sight",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Hide in Plain Sight",  
                        "level": 10,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 10th level, you can spend 1 minute creating camouflage for yourself. You must have access to fresh mud, dirt, plants, soot, and other naturally occurring materials with which to create your camouflage.",  
                            "Once you are camouflaged in this way, you can try to hide by pressing yourself up against a solid surface, such as a tree or wall, that is at least as tall and wide as you are. You gain a +10 bonus to Dexterity (Stealth) checks as long as you remain there without moving or taking actions. Once you move or take an action or a reaction, you must camouflage yourself again to gain this benefit."  
                        ],  
                        "url": "/api/2014/features/hide-in-plain-sight",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 6,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 2,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-10"  
        },  
        {  
            "level": 11,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 7,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-11"  
        },  
        {  
            "level": 12,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 4,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-3",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-3",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 12,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-3",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 7,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-12"  
        },  
        {  
            "level": 13,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 8,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 1,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-13"  
        },  
        {  
            "level": 14,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [  
                {  
                    "index": "favored-enemy-3-enemies",  
                    "name": "Favored Enemy (3 enemies)",  
                    "details": {  
                        "index": "favored-enemy-3-enemies",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (3 enemies)",  
                        "level": 14,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-3-enemies",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "vanish",  
                    "name": "Vanish",  
                    "details": {  
                        "index": "vanish",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Vanish",  
                        "level": 14,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 14th level, you can use the Hide action as a bonus action on your turn. Also, you can't be tracked by nonmagical means, unless you choose to leave a trail."  
                        ],  
                        "url": "/api/2014/features/vanish",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 8,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 1,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-14"  
        },  
        {  
            "level": 15,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 9,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 2,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-15"  
        },  
        {  
            "level": 16,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 5,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-4",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-4",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 16,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-4",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 9,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 2,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-16"  
        },  
        {  
            "level": 17,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 6,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 10,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 1  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-17"  
        },  
        {  
            "level": 18,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "feral-senses",  
                    "name": "Feral Senses",  
                    "details": {  
                        "index": "feral-senses",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Feral Senses",  
                        "level": 18,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 18th level, you gain preternatural senses that help you fight creatures you can't see. When you attack a creature you can't see, your inability to see it doesn't impose disadvantage on your attack rolls against it.",  
                            "You are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn't hidden from you and you aren't blinded or deafened."  
                        ],  
                        "url": "/api/2014/features/feral-senses",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 10,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 1  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-18"  
        },  
        {  
            "level": 19,  
            "ability_score_bonuses": 5,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-5",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-5",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 19,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-5",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 11,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 2  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-19"  
        },  
        {  
            "level": 20,  
            "ability_score_bonuses": 5,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "foe-slayer",  
                    "name": "Foe Slayer",  
                    "details": {  
                        "index": "foe-slayer",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Foe Slayer",  
                        "level": 20,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 20th level, you become an unparalleled hunter of your enemies. Once on each of your turns, you can add your Wisdom modifier to the attack roll or the damage roll of an attack you make against one of your favored enemies. You can choose to use this feature before or after the roll, but before any effects of the roll are applied."  
                        ],  
                        "url": "/api/2014/features/foe-slayer",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 11,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 2  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-20"  
        }  
    ]  
]  
"""  
  
spells:  
"""  
[  
    [  
        {  
            "index": "alarm",  
            "name": "Alarm",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "alarm",  
                "name": "Alarm",  
                "desc": [  
                    "You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area. When you cast the spell, you can designate creatures that won't set off the alarm. You also choose whether the alarm is mental or audible.",  
                    "A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping.",  
                    "An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A tiny bell and a piece of fine silver wire.",  
                "ritual": true,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 minute",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "cube",  
                    "size": 20  
                },  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/alarm",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "animal-friendship",  
            "name": "Animal Friendship",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "animal-friendship",  
                "name": "Animal Friendship",  
                "desc": [  
                    "This spell lets you convince a beast that you mean it no harm. Choose a beast that you can see within range. It must see and hear you. If the beast's Intelligence is 4 or higher, the spell fails. Otherwise, the beast must succeed on a wisdom saving throw or be charmed by you for the spell's duration. If you or one of your companions harms the target, the spells ends."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A morsel of food.",  
                "ritual": false,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "dc": {  
                    "dc_type": {  
                        "index": "wis",  
                        "name": "WIS",  
                        "url": "/api/2014/ability-scores/wis"  
                    },  
                    "dc_success": "none"  
                },  
                "school": {  
                    "index": "enchantment",  
                    "name": "Enchantment",  
                    "url": "/api/2014/magic-schools/enchantment"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/animal-friendship",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "cure-wounds",  
            "name": "Cure Wounds",  
            "level": 1,  
            "details": {  
                "index": "cure-wounds",  
                "name": "Cure Wounds",  
                "desc": [  
                    "A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d8 for each slot level above 1st."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "heal_at_slot_level": {  
                    "1": "1d8 + MOD",  
                    "2": "2d8 + MOD",  
                    "3": "3d8 + MOD",  
                    "4": "4d8 + MOD",  
                    "5": "5d8 + MOD",  
                    "6": "6d8 + MOD",  
                    "7": "7d8 + MOD",  
                    "8": "8d8 + MOD",  
                    "9": "9d8 + MOD"  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "life",  
                        "name": "Life",  
                        "url": "/api/2014/subclasses/life"  
                    }  
                ],  
                "url": "/api/2014/spells/cure-wounds",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "detect-magic",  
            "name": "Detect Magic",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "detect-magic",  
                "name": "Detect Magic",  
                "desc": [  
                    "For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic, and you learn its school of magic, if any.",  
                    "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/detect-magic",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "detect-poison-and-disease",  
            "name": "Detect Poison and Disease",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "detect-poison-and-disease",  
                "name": "Detect Poison and Disease",  
                "desc": [  
                    "For the duration, you can sense the presence and location of poisons, poisonous creatures, and diseases within 30 feet of you. You also identify the kind of poison, poisonous creature, or disease in each case.",  
                    "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A yew leaf.",  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/detect-poison-and-disease",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "fog-cloud",  
            "name": "Fog Cloud",  
            "level": 1,  
            "details": {  
                "index": "fog-cloud",  
                "name": "Fog Cloud",  
                "desc": [  
                    "You create a 20-foot-radius sphere of fog centered on a point within range. The sphere spreads around corners, and its area is heavily obscured. It lasts for the duration or until a wind of moderate or greater speed (at least 10 miles per hour) disperses it."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, the radius of the fog increases by 20 feet for each slot level above 1st."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 20  
                },  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/fog-cloud",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "goodberry",  
            "name": "Goodberry",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "goodberry",  
                "name": "Goodberry",  
                "desc": [  
                    "Up to ten berries appear in your hand and are infused with magic for the duration. A creature can use its action to eat one berry. Eating a berry restores 1 hit point, and the berry provides enough nourishment to sustain a creature for a day.",  
                    "The berries lose their potency if they have not been consumed within 24 hours of the casting of this spell."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A sprig of mistletoe.",  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/goodberry",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "hunters-mark",  
            "name": "Hunter's Mark",  
            "level": 1,  
            "details": {  
                "index": "hunters-mark",  
                "name": "Hunter's Mark",  
                "desc": [  
                    "You choose a creature you can see within range and mystically mark it as your quarry. Until the spell ends, you deal an extra 1d6 damage to the target whenever you hit it with a weapon attack, and you have advantage on any Wisdom (Perception) or Wisdom (Survival) check you make to find it. If the target drops to 0 hit points before this spell ends, you can use a bonus action on a subsequent turn of yours to mark a new creature."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 3rd or 4th level, you can maintain your concentration on the spell for up to 8 hours. When you use a spell slot of 5th level or higher, you can maintain your concentration on the spell for up to 24 hours."  
                ],  
                "range": "90 feet",  
                "components": [  
                    "V"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 bonus action",  
                "level": 1,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/hunters-mark",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "jump",  
            "name": "Jump",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "jump",  
                "name": "Jump",  
                "desc": [  
                    "You touch a creature. The creature's jump distance is tripled until the spell ends."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A grasshopper's hind leg.",  
                "ritual": false,  
                "duration": "1 minute",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/jump",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "longstrider",  
            "name": "Longstrider",  
            "level": 1,  
            "details": {  
                "index": "longstrider",  
                "name": "Longstrider",  
                "desc": [  
                    "You touch a creature. The target's speed increases by 10 feet until the spell ends."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each spell slot above 1st."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A pinch of dirt.",  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/longstrider",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "speak-with-animals",  
            "name": "Speak with Animals",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "speak-with-animals",  
                "name": "Speak with Animals",  
                "desc": [  
                    "You gain the ability to comprehend and verbally communicate with beasts for the duration. The knowledge and awareness of many beasts is limited by their intelligence, but at a minimum, beasts can give you information about nearby locations and monsters, including whatever they can perceive or have perceived within the past day. You might be able to persuade a beast to perform a small favor for you, at the GM's discretion."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "10 minutes",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/speak-with-animals",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "animal-messenger",  
            "name": "Animal Messenger",  
            "level": 2,  
            "details": {  
                "index": "animal-messenger",  
                "name": "Animal Messenger",  
                "desc": [  
                    "By means of this spell, you use an animal to deliver a message. Choose a Tiny beast you can see within range, such as a squirrel, a blue jay, or a bat. You specify a location, which you must have visited, and a recipient who matches a general description, such as \"a man or woman dressed in the uniform of the town guard\" or \"a red-haired dwarf wearing a pointed hat.\" You also speak a message of up to twenty-five words. The target beast travels for the duration of the spell toward the specified location, covering about 50 miles per 24 hours for a flying messenger, or 25 miles for other animals.",  
                    "When the messenger arrives, it delivers your message to the creature that you described, replicating the sound of your voice. The messenger speaks only to a creature matching the description you gave. If the messenger doesn't reach its destination before the spell ends, the message is lost, and the beast makes its way back to where you cast this spell."  
                ],  
                "higher_level": [  
                    "If you cast this spell using a spell slot of 3nd level or higher, the duration of the spell increases by 48 hours for each slot level above 2nd."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A morsel of food.",  
                "ritual": true,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "enchantment",  
                    "name": "Enchantment",  
                    "url": "/api/2014/magic-schools/enchantment"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/animal-messenger",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "barkskin",  
            "name": "Barkskin",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "barkskin",  
                "name": "Barkskin",  
                "desc": [  
                    "You touch a willing creature. Until the spell ends, the target's skin has a rough, bark-like appearance, and the target's AC can't be less than 16, regardless of what kind of armor it is wearing."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A handful of oak bark.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/barkskin",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "darkvision",  
            "name": "Darkvision",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "darkvision",  
                "name": "Darkvision",  
                "desc": [  
                    "You touch a willing creature to grant it the ability to see in the dark. For the duration, that creature has darkvision out to a range of 60 feet."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Either a pinch of dried carrot or an agate.",  
                "ritual": false,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/darkvision",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "find-traps",  
            "name": "Find Traps",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "find-traps",  
                "name": "Find Traps",  
                "desc": [  
                    "You sense the presence of any trap within range that is within line of sight. A trap, for the purpose of this spell, includes anything that would inflict a sudden or unexpected effect you consider harmful or undesirable, which was specifically intended as such by its creator. Thus, the spell would sense an area affected by the alarm spell, a glyph of warding, or a mechanical pit trap, but it would not reveal a natural weakness in the floor, an unstable ceiling, or a hidden sinkhole.",  
                    "This spell merely reveals that a trap is present. You don't learn the location of each trap, but you do learn the general nature of the danger posed by a trap you sense."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/find-traps",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "lesser-restoration",  
            "name": "Lesser Restoration",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "lesser-restoration",  
                "name": "Lesser Restoration",  
                "desc": [  
                    "You touch a creature and can end either one disease or one condition afflicting it. The condition can be blinded, deafened, paralyzed, or poisoned."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "life",  
                        "name": "Life",  
                        "url": "/api/2014/subclasses/life"  
                    },  
                    {  
                        "index": "devotion",  
                        "name": "Devotion",  
                        "url": "/api/2014/subclasses/devotion"  
                    }  
                ],  
                "url": "/api/2014/spells/lesser-restoration",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-animals-or-plants",  
            "name": "Locate Animals or Plants",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "locate-animals-or-plants",  
                "name": "Locate Animals or Plants",  
                "desc": [  
                    "Describe or name a specific kind of beast or plant. Concentrating on the voice of nature in your surroundings, you learn the direction and distance to the closest creature or plant of that kind within 5 miles, if any are present."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A bit of fur from a bloodhound.",  
                "ritual": true,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-animals-or-plants",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-object",  
            "name": "Locate Object",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "locate-object",  
                "name": "Locate Object",  
                "desc": [  
                    "Describe or name an object that is familiar to you. You sense the direction to the object's location, as long as that object is within 1,000 feet of you. If the object is in motion, you know the direction of its movement.",  
                    "The spell can locate a specific object known to you, as long as you have seen it up close--within 30 feet--at least once. Alternatively, the spell can locate the nearest object of a particular kind, such as a certain kind of apparel, jewelry, furniture, tool, or weapon.",  
                    "This spell can't locate an object if any thickness of lead, even a thin sheet, blocks a direct path between you and the object."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A forked twig.",  
                "ritual": false,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-object",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "pass-without-trace",  
            "name": "Pass Without Trace",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "pass-without-trace",  
                "name": "Pass Without Trace",  
                "desc": [  
                    "A veil of shadows and silence radiates from you, masking you and your companions from detection. For the duration, each creature you choose within 30 feet of you (including you) has a +10 bonus to Dexterity (Stealth) checks and can't be tracked except by magical means. A creature that receives this bonus leaves behind no tracks or other traces of its passage."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Ashes from a burned leaf of mistletoe and a sprig of spruce.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/pass-without-trace",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "protection-from-poison",  
            "name": "Protection from Poison",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "protection-from-poison",  
                "name": "Protection from Poison",  
                "desc": [  
                    "You touch a creature. If it is poisoned, you neutralize the poison. If more than one poison afflicts the target, you neutralize one poison that you know is present, or you neutralize one at random.",  
                    "For the duration, the target has advantage on saving throws against being poisoned, and it has resistance to poison damage."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/protection-from-poison",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "silence",  
            "name": "Silence",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "silence",  
                "name": "Silence",  
                "desc": [  
                    "For the duration, no sound can be created within or pass through a 20-foot-radius sphere centered on a point you choose within range. Any creature or object entirely inside the sphere is immune to thunder damage, and creatures are deafened while entirely inside it.",  
                    "Casting a spell that includes a verbal component is impossible there."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 20  
                },  
                "school": {  
                    "index": "illusion",  
                    "name": "Illusion",  
                    "url": "/api/2014/magic-schools/illusion"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/silence",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "spike-growth",  
            "name": "Spike Growth",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "spike-growth",  
                "name": "Spike Growth",  
                "desc": [  
                    "The ground in a 20-foot radius centered on a point within range twists and sprouts hard spikes and thorns. The area becomes difficult terrain for the duration. When a creature moves into or within the area, it takes 2d4 piercing damage for every 5 feet it travels.",  
                    "The transformation of the ground is camouflaged to look natural. Any creature that can't see the area at the time the spell is cast can make a Wisdom (Perception) check against your spell save DC to recognize the terrain as hazardous before entering it."  
                ],  
                "range": "150 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Seven sharp thorns or seven small twigs, each sharpened to a point.",  
                "ritual": false,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "area_of_effect": {  
                    "type": "cylinder",  
                    "size": 20  
                },  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/spike-growth",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "conjure-animals",  
            "name": "Conjure Animals",  
            "level": 3,  
            "details": {  
                "index": "conjure-animals",  
                "name": "Conjure Animals",  
                "desc": [  
                    "You summon fey spirits that take the form of beasts and appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:",  
                    "- One beast of challenge rating 2 or lower",  
                    "- Two beasts of challenge rating 1 or lower",  
                    "- Four beasts of challenge rating 1/2 or lower",  
                    "- Eight beasts of challenge rating 1/4 or lower",  
                    "- Each beast is also considered fey, and it disappears when it drops to 0 hit points or when the spell ends.",  
                    "The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which has its own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.",  
                    "The GM has the creatures' statistics."  
                ],  
                "higher_level": [  
                    "When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 5th-level slot, three times as many with a 7th-level."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/conjure-animals",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "daylight",  
            "name": "Daylight",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "daylight",  
                "name": "Daylight",  
                "desc": [  
                    "A 60-foot-radius sphere of light spreads out from a point you choose within range. The sphere is bright light and sheds dim light for an additional 60 feet.",  
                    "If you chose a point on an object you are holding or one that isn't being worn or carried, the light shines from the object and moves with it. Completely covering the affected object with an opaque object, such as a bowl or a helm, blocks the light.",  
                    "If any of this spell's area overlaps with an area of darkness created by a spell of 3rd level or lower, the spell that created the darkness is dispelled."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 60  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/daylight",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "nondetection",  
            "name": "Nondetection",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "nondetection",  
                "name": "Nondetection",  
                "desc": [  
                    "For the duration, you hide a target that you touch from divination magic. The target can be a willing creature or a place or an object no larger than 10 feet in any dimension. The target can't be targeted by any divination magic or perceived through magical scrying sensors."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A pinch of diamond dust worth 25 gp sprinkled over the target, which the spell consumes.",  
                "ritual": false,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/nondetection",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "plant-growth",  
            "name": "Plant Growth",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "plant-growth",  
                "name": "Plant Growth",  
                "desc": [  
                    "This spell channels vitality into plants within a specific area. There are two possible uses for the spell, granting either immediate or long-term benefits.",  
                    "If you cast this spell using 1 action, choose a point within range. All normal plants in a 100-foot radius centered on that point become thick and overgrown. A creature moving through the area must spend 4 feet of movement for every 1 foot it moves.",  
                    "You can exclude one or more areas of any size within the spell's area from being affected.",  
                    "If you cast this spell over 8 hours, you enrich the land. All plants in a half-mile radius centered on a point within range become enriched for 1 year. The plants yield twice the normal amount of food when harvested."  
                ],  
                "range": "150 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/plant-growth",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "protection-from-energy",  
            "name": "Protection From Energy",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "protection-from-energy",  
                "name": "Protection From Energy",  
                "desc": [  
                    "For the duration, the willing creature you touch has resistance to one damage type of your choice: acid, cold, fire, lightning, or thunder."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/protection-from-energy",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "speak-with-plants",  
            "name": "Speak with Plants",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "speak-with-plants",  
                "name": "Speak with Plants",  
                "desc": [  
                    "You imbue plants within 30 feet of you with limited sentience and animation, giving them the ability to communicate with you and follow your simple commands. You can question plants about events in the spell's area within the past day, gaining information about creatures that have passed, weather, and other circumstances.",  
                    "You can also turn difficult terrain caused by plant growth (such as thickets and undergrowth) into ordinary terrain that lasts for the duration. Or you can turn ordinary terrain where plants are present into difficult terrain that lasts for the duration, causing vines and branches to hinder pursuers, for example.",  
                    "Plants might be able to perform other tasks on your behalf, at the GM's discretion. The spell doesn't enable plants to uproot themselves and move about, but they can freely move branches, tendrils, and stalks.",  
                    "If a plant creature is in the area, you can communicate with it as if you shared a common language, but you gain no magical ability to influence it.",  
                    "This spell can cause the plants created by the entangle spell to release a restrained creature."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "10 minutes",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/speak-with-plants",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "water-breathing",  
            "name": "Water Breathing",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "water-breathing",  
                "name": "Water Breathing",  
                "desc": [  
                    "This spell gives a maximum of ten willing creatures within range and you can see, the ability to breathe underwater until the end of its term. Affected creatures also retain their normal breathing pattern."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A short piece of reed or straw.",  
                "ritual": true,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/water-breathing",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "water-walk",  
            "name": "Water Walk",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "water-walk",  
                "name": "Water Walk",  
                "desc": [  
                    "This spell grants the ability to move across any liquid surface--such as water, acid, mud, snow, quicksand, or lava--as if it were harmless solid ground (creatures crossing molten lava can still take damage from the heat). Up to ten willing creatures you can see within range gain this ability for the duration.",  
                    "If you target a creature submerged in a liquid, the spell carries the target to the surface of the liquid at a rate of 60 feet per round."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A piece of cork.",  
                "ritual": true,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/water-walk",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "wind-wall",  
            "name": "Wind Wall",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "wind-wall",  
                "name": "Wind Wall",  
                "desc": [  
                    "A wall of strong wind rises from the ground at a point you choose within range. You can make the wall up to 50 feet long, 15 feet high, and 1 foot thick. You can shape the wall in any way you choose so long as it makes one continuous path along the ground. The wall lasts for the duration.",  
                    "When the wall appears, each creature within its area must make a strength saving throw. A creature takes 3d8 bludgeoning damage on a failed save, or half as much damage on a successful one.",  
                    "The strong wind keeps fog, smoke, and other gases at bay. Small or smaller flying creatures or objects can't pass through the wall. Loose, lightweight materials brought into the wall fly upward. Arrows, bolts, and other ordinary projectiles launched at targets behind the wall are deflected upward and automatically miss. (Boulders hurled by giants or siege engines, and similar projectiles, are unaffected.) Creatures in gaseous form can't pass through it."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A tiny fan and a feather of exotic origin.",  
                "ritual": false,  
                "duration": "Up to 1 minute",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "damage": {  
                    "damage_type": {  
                        "index": "bludgeoning",  
                        "name": "Bludgeoning",  
                        "url": "/api/2014/damage-types/bludgeoning"  
                    },  
                    "damage_at_slot_level": {  
                        "3": "3d8"  
                    }  
                },  
                "dc": {  
                    "dc_type": {  
                        "index": "str",  
                        "name": "STR",  
                        "url": "/api/2014/ability-scores/str"  
                    },  
                    "dc_success": "half"  
                },  
                "area_of_effect": {  
                    "type": "line",  
                    "size": 50  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/wind-wall",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "conjure-woodland-beings",  
            "name": "Conjure Woodland Beings",  
            "level": 4,  
            "details": {  
                "index": "conjure-woodland-beings",  
                "name": "Conjure Woodland Beings",  
                "desc": [  
                    "You summon fey creatures that appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:",  
                    "- One fey creature of challenge rating 2 or lower",  
                    "- Two fey creatures of challenge rating 1 or lower",  
                    "- Four fey creatures of challenge rating 1/2 or lower",  
                    "- Eight fey creatures of challenge rating 1/4 or lower",  
                    "A summoned creature disappears when it drops to 0 hit points or when the spell ends.",  
                    "The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which have their own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.",  
                    "The GM has the creatures' statistics."  
                ],  
                "higher_level": [  
                    "When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 6th-level slot and three times as many with an 8th-level slot."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "One holly berry per creature summoned.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/conjure-woodland-beings",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "freedom-of-movement",  
            "name": "Freedom of Movement",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "freedom-of-movement",  
                "name": "Freedom of Movement",  
                "desc": [  
                    "You touch a willing creature. For the duration, the target's movement is unaffected by difficult terrain, and spells and other magical effects can neither reduce the target's speed nor cause the target to be paralyzed or restrained.",  
                    "The target can also spend 5 feet of movement to automatically escape from nonmagical restraints, such as manacles or a creature that has it grappled. Finally, being underwater imposes no penalties on the target's movement or attacks."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A leather strap, bound around the arm or a similar appendage.",  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    },  
                    {  
                        "index": "devotion",  
                        "name": "Devotion",  
                        "url": "/api/2014/subclasses/devotion"  
                    }  
                ],  
                "url": "/api/2014/spells/freedom-of-movement",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-creature",  
            "name": "Locate Creature",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "locate-creature",  
                "name": "Locate Creature",  
                "desc": [  
                    "Describe or name a creature that is familiar to you. You sense the direction to the creature's location, as long as that creature is within 1,000 feet of you. If the creature is moving, you know the direction of its movement.",  
                    "The spell can locate a specific creature known to you, or the nearest creature of a specific kind (such as a human or a unicorn), so long as you have seen such a creature up close--within 30 feet--at least once. If the creature you described or named is in a different form, such as being under the effects of a polymorph spell, this spell doesn't locate the creature.",  
                    "This spell can't locate a creature if running water at least 10 feet wide blocks a direct path between you and the creature."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A bit of fur from a bloodhound.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-creature",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "stoneskin",  
            "name": "Stoneskin",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "stoneskin",  
                "name": "Stoneskin",  
                "desc": [  
                    "This spell turns the flesh of a willing creature you touch as hard as stone. Until the spell ends, the target has resistance to nonmagical bludgeoning, piercing, and slashing damage."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Diamond dust worth 100 gp, which the spell consumes.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/stoneskin",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "commune-with-nature",  
            "name": "Commune With Nature",  
            "level": 5,  
            "details": {  
                "higher_level": [],  
                "index": "commune-with-nature",  
                "name": "Commune With Nature",  
                "desc": [  
                    "You briefly become one with nature and gain knowledge of the surrounding territory. In the outdoors, the spell gives you knowledge of the land within 3 miles of you. In caves and other natural underground settings, the radius is limited to 300 feet. The spell doesn't function where nature has been replaced by construction, such as in dungeons and towns.",  
                    "You instantly gain knowledge of up to three facts of your choice about any of the following subjects as they relate to the area:",  
                    "- terrain and bodies of water",  
                    "- prevalent plants, minerals, animals, or peoples",  
                    "- powerful celestials, fey, fiends, elementals, or undead",  
                    "- influence from other planes of existence",  
                    "- buildings",  
                    "For example, you could determine the location of powerful undead in the area, the location of major sources of safe drinking water, and the location of any nearby towns."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 minute",  
                "level": 5,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/commune-with-nature",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "tree-stride",  
            "name": "Tree Stride",  
            "level": 5,  
            "details": {  
                "higher_level": [],  
                "index": "tree-stride",  
                "name": "Tree Stride",  
                "desc": [  
                    "You gain the ability to enter a tree and move from inside it to inside another tree of the same kind within 500 feet. Both trees must be living and at least the same size as you. You must use 5 feet of movement to enter a tree. You instantly know the location of all other trees of the same kind within 500 feet and, as part of the move used to enter the tree, can either pass into one of those trees or step out of the tree you're in. You appear in a spot of your choice within 5 feet of the destination tree, using another 5 feet of movement. If you have no movement left, you appear within 5 feet of the tree you entered.",  
                    "You can use this transportation ability once per round for the duration. You must end each turn outside a tree."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 minute",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 5,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/tree-stride",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        }  
    ]  
]  
"""  
  
sublcass_data:  
"""  
[  
    [  
        {  
            "index": "hunter",  
            "class": {  
                "index": "ranger",  
                "name": "Ranger",  
                "url": "/api/2014/classes/ranger"  
            },  
            "name": "Hunter",  
            "subclass_flavor": "Ranger Archetype",  
            "desc": [  
                "Emulating the Hunter archetype means accepting your place as a bulwark between civilization and the terrors of the wilderness. As you walk the Hunter's path, you learn specialized techniques for fighting the threats you face, from rampaging ogres and hordes of orcs to towering giants and terrifying dragons."  
            ],  
            "subclass_levels": [  
                {  
                    "level": 3,  
                    "features": [  
                        {  
                            "index": "hunters-prey",  
                            "name": "Hunter's Prey",  
                            "details": {  
                                "index": "hunters-prey",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Hunter's Prey",  
                                "level": 3,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 3rd level, you gain one of the following features of your choice.",  
                                    "Colossus Slayer",  
                                    "Giant Killer",  
                                    "Horde Breaker"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-colossus-slayer",  
                                                        "name": "Hunter's Prey: Colossus Slayer",  
                                                        "url": "/api/2014/features/hunters-prey-colossus-slayer"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-giant-killer",  
                                                        "name": "Hunter's Prey: Giant Killer",  
                                                        "url": "/api/2014/features/hunters-prey-giant-killer"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-horde-breaker",  
                                                        "name": "Hunter's Prey: Horde Breaker",  
                                                        "url": "/api/2014/features/hunters-prey-horde-breaker"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/hunters-prey",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/3",  
                    "index": "hunter-3",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 7,  
                    "features": [  
                        {  
                            "index": "defensive-tactics",  
                            "name": "Defensive Tactics",  
                            "details": {  
                                "index": "defensive-tactics",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Defensive Tactics",  
                                "level": 7,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 7th level, you gain one of the following features of your choice.",  
                                    "Escape the Horde",  
                                    "Multiattack Defense",  
                                    "Steel Will"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-escape-the-horde",  
                                                        "name": "Defensive Tactics: Escape the Horde",  
                                                        "url": "/api/2014/features/defensive-tactics-escape-the-horde"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-multiattack-defense",  
                                                        "name": "Defensive Tactics: Multiattack Defense",  
                                                        "url": "/api/2014/features/defensive-tactics-multiattack-defense"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-steel-will",  
                                                        "name": "Defensive Tactics: Steel Will",  
                                                        "url": "/api/2014/features/defensive-tactics-steel-will"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/defensive-tactics",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/7",  
                    "index": "hunter-7",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 11,  
                    "features": [  
                        {  
                            "index": "multiattack",  
                            "name": "Multiattack",  
                            "details": {  
                                "index": "multiattack",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Multiattack",  
                                "level": 11,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 11th level, you gain one of the following features of your choice.",  
                                    "Volley",  
                                    "Whirlwind Attack"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "multiattack-volley",  
                                                        "name": "Multiattack: Volley",  
                                                        "url": "/api/2014/features/multiattack-volley"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "multiattack-whirlwind-attack",  
                                                        "name": "Multiattack: Whirlwind Attack",  
                                                        "url": "/api/2014/features/multiattack-whirlwind-attack"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/multiattack",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/11",  
                    "index": "hunter-11",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 15,  
                    "features": [  
                        {  
                            "index": "superior-hunters-defense",  
                            "name": "Superior Hunter's Defense",  
                            "details": {  
                                "index": "superior-hunters-defense",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Superior Hunter's Defense",  
                                "level": 15,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 15th level, you gain one of the following features of your choice.",  
                                    "Evasion",  
                                    "Stand Against the Tide",  
                                    "Uncanny Dodge"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-evasion",  
                                                        "name": "Superior Hunter's Defense: Evasion",  
                                                        "url": "/api/2014/features/superior-hunters-defense-evasion"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-stand-against-the-tide",  
                                                        "name": "Superior Hunter's Defense: Stand Against the Tide",  
                                                        "url": "/api/2014/features/superior-hunters-defense-stand-against-the-tide"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-uncanny-dodge",  
                                                        "name": "Superior Hunter's Defense: Uncanny Dodge",  
                                                        "url": "/api/2014/features/superior-hunters-defense-uncanny-dodge"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/superior-hunters-defense",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/15",  
                    "index": "hunter-15",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                }  
            ],  
            "url": "/api/2014/subclasses/hunter",  
            "updated_at": "2025-04-08T21:14:17.800Z",  
            "spells": []  
        }  
    ]  
]  
"""  
'''
Hier noch mal das format in dem du die antwort zurück geben sollst.

Rückgabeformat: text  
Verbotene formate: Markdwon  
vorboteneer inhalt: ```json, ```
```
#### Character:
```
{
    "name": "Robin Hood",
    "level": 10,
    "hit_points": 85,
    "proficiency_bonus": 4,
    "subclass": "Hunter",
    "attributes": {
        "strength": 12,
        "dexterity": 20,
        "constitution": 14,
        "intelligence": 10,
        "wisdom": 16,
        "charisma": 14
    },
    "attribute_proficiencies": {
        "strength": false,
        "dexterity": true,
        "constitution": false,
        "intelligence": false,
        "wisdom": true,
        "charisma": false
    },
    "saving_throws": {
        "strength": 7,
        "dexterity": 11,
        "constitution": 7,
        "intelligence": 5,
        "wisdom": 9,
        "charisma": 7
    },
    "armor_class": 17,
    "attack_bonus": 8,
    "spellcasting": {
        "spellcasting_bonus": 5,
        "spellcasting_dc": 15,
        "spellcasting_attack_bonus": 7,
        "cantrips_known": 0,
        "spells_prepared": 6,
        "spell_slots": {
            "1st": 4,
            "2nd": 3,
            "3rd": 2,
            "4th": 0,
            "5th": 0
        },
        "known_spells": {
            "1st_level": [
                "Hunter's Mark",
                "Longstrider",
                "Cure Wounds",
                "Detect Magic"
            ],
            "2nd_level": [
                "Pass Without Trace",
                "Barkskin",
                "Silence"
            ],
            "3rd_level": [
                "Conjure Animals",
                "Wind Wall"
            ]
        },
        "prepared_spells": {
            "1st_level": [
                "Hunter's Mark (D)",
                "Longstrider (D)",
                "Cure Wounds (S)"
            ],
            "2nd_level": [
                "Pass Without Trace (D)",
                "Barkskin (S)"
            ],
            "3rd_level": [
                "Conjure Animals (D)"
            ]
        }
    },
    "skills": {
        "strength_skills": {
            "athletics": {
                "bonus": 1,
                "proficiency_bonus": false
            }
        },
        "dexterity_skills": {
            "acrobatics": {
                "bonus": 10,
                "proficiency_bonus": true
            },
            "sleight_of_hand": {
                "bonus": 10,
                "proficiency_bonus": true
            },
            "stealth": {
                "bonus": 14,
                "proficiency_bonus": true
            }
        },
        "intelligence_skills": {
            "arcana": {
                "bonus": 0,
                "proficiency_bonus": false
            },
            "history": {
                "bonus": 0,
                "proficiency_bonus": false
            },
            "investigation": {
                "bonus": 0,
                "proficiency_bonus": false
            },
            "nature": {
                "bonus": 6,
                "proficiency_bonus": true
            },
            "religion": {
                "bonus": 0,
                "proficiency_bonus": false
            }
        },
        "wisdom_skills": {
            "animal_handling": {
                "bonus": 8,
                "proficiency_bonus": true
            },
            "insight": {
                "bonus": 8,
                "proficiency_bonus": true
            },
            "medicine": {
                "bonus": 3,
                "proficiency_bonus": false
            },
            "perception": {
                "bonus": 10,
                "proficiency_bonus": true
            },
            "survival": {
                "bonus": 10,
                "proficiency_bonus": true
            }
        },
        "charisma_skills": {
            "deception": {
                "bonus": 2,
                "proficiency_bonus": false
            },
            "intimidation": {
                "bonus": 2,
                "proficiency_bonus": false
            },
            "performance": {
                "bonus": 6,
                "proficiency_bonus": true
            },
            "persuasion": {
                "bonus": 6,
                "proficiency_bonus": true
            }
        }
    },
    "features": [
        "Favored Enemy (Humanoids)",
        "Natural Explorer (Forest)",
        "Fighting Style: Archery",
        "Spellcasting",
        "Primeval Awareness",
        "Extra Attack",
        "Land's Stride",
        "Hide in Plain Sight",
        "Hunter's Prey: Horde Breaker",
        "Defensive Tactics: Escape the Horde"
    ],
    "special_abilities_and_traits": [
        "Darkvision (60 ft)",
        "Fey Ancestry",
        "Trance",
        "Mask of the Wild"
    ],
    "languages": [
        "Common",
        "Elvish",
        "Sylvan"
    ],
    "equipment": [
        "Longbow",
        "Quiver with 20 arrows",
        "Leather armor",
        "Two shortswords",
        "Explorer's pack",
        "A hooded cloak",
        "A hunting trap",
        "A trophy from an animal killed by you"
    ],
    "additional_equipment": [
        "Bedroll",
        "Mess kit",
        "Tinderbox",
        "10 torches",
        "10 days of rations",
        "Waterskin",
        "50 feet of hempen rope",
        "A belt pouch containing 10 GP"
    ],
    "money": {
        "platinum": 0,
        "gold": 50,
        "electrum": 0,
        "silver": 20,
        "copper": 50
    },
    "weapons": {
        "longbow": {
            "damage": "1d8 piercing",
            "attack_bonus": 8,
            "properties": [
                "Ammunition",
                "Heavy",
                "Two-Handed"
            ],
            "range": "150/600 ft"
        },
        "shortsword": {
            "damage": "1d6 piercing",
            "attack_bonus": 8,
            "properties": [
                "Finesse",
                "Light"
            ]
        }
    }
}

```


## ChatGpt

>[!Warning] **Resume:**
>ChatGPT konnte den Prompt zwar nicht direckt von der Textleiste übernehmen, aber ein großes File wurde von ChatGpt gelesen.
>
>Der Erstellte Character ist nicht ganz vollständig. Es fehlen: 
>- Prepared_spells
>- skills
>  
> Das fehlen der skills ist ein großer Malus. Ohne diese ist der Character unspielbar.
> 
>Mein Resume ist daher: **D**


>[!Info]+ Analysed Data:
>**prompt_1** : 
>```
>Erstelle einen Robin Hood, ein ranger auf Level 10. Orientiere dich bei dem ranger an folgenden details: ["Robin Hood", "Bogenschütze", "Wald", "Dieb", "Geschicklichkeit", "Heimlichkeit", "Gerechtigkeit"]
>```
>
>**prompt_2** :
>```
>Erstelle einen Robin Hood, ein rogue auf Level 10. Orientiere dich bei dem rogue an folgenden details: ["Robin Hood", "Bogenschütze", "Wald", "Dieb", "Geschicklichkeit", "Heimlichkeit", "Gerechtigkeit"]
>```
>
>prompt_3: 
>```
>Erstelle einen Robin Hood, ein fighter auf Level 10. Orientiere dich bei dem fighter an folgenden details: ["Robin Hood", "Bogenschütze", "Wald", "Dieb", "Geschicklichkeit", "Heimlichkeit", "Gerechtigkeit"]
>```


### CharacterGeneration

#### CharGenPrompt:
```
Du bist ein Dungeons and Dragons(DnD) Experte. Du erstellst DnD Charactere.  
Um einen Character zu erstellen erhälst du alle nötigen Informationen für eine Klasse im Json format, an diesen Prompt als json-file angehängt.  
Zusätzlich bekommst du Details zu dem Character, die den character noch einmal näher definieren.  
  
Ein beispiel für die Details ist:  
- Ein dunkler Magier Level 8, der tote beschwören kann und mit Feuermagie zaubert.  
In diesem Beispiel sollst du den DnD Character so erstellen, dass er viele Fähigkeiten hat, die in das Themengebiet 'Necromantie', 'dunkle Magie' und 'Feuermagie' fallen.  
Du wirst in den daten, die du erhälst immer wieder Fähgikeiten auswählen können. Wähle bei diesen auch so, dass die Auswhl den genannten Character Details entsprechen.  
  
Den erstellen Character sollst du im Json Format zurück geben.  
Hier ist ein Beispiel für einen DnD character der stufe 20:  
  
{  
    "name": "Cleric",    "level": 20,    "hit_points": 150,    "proficiency_bonus": 6,    "subclass": "Life Domain",    "attributes": {        "strength": 12,        "dexterity": 14,        "constitution": 14,        "intelligence": 10,        "wisdom": 20,        "charisma": 8    },    "attribute_proficiencys": {      "strength": false,        "dexterity": false,        "constitution": false,        "intelligence": false,        "wisdom": true,        "charisma": true    },    "saving_throws": {      "strength": 1,        "dexterity": 2,        "constitution": 2,        "intelligence": 0,        "wisdom": 11,        "charisma": 5    },  
    "armor_class": 18,    "attack_bonus": 8,    "spellcasting": {        "spellcasting_bonus": 11,        "spellcasting_dc": 19,        "spellcasting_attack_bonus": 11,        "cantrips_known": 5,        "spells_prepared": 25,        "spell_slots": {            "1st": 4,            "2nd": 4,            "3rd": 4,            "4th": 4,            "5th": 3,            "6th": 3,            "7th": 2,            "8th": 2,            "9th": 1        },        "known_spells": {            "cantrips": ["Guidance", "Light", "Sacred Flame", "Thaumaturgy", "Toll the Dead"],            "1st_level": ["Bless", "Cure Wounds", "Guiding Bolt", "Infestation", "Magic Stone"],            "2nd_level": ["Lesser Restoration", "Prayer of Healing", "Spiritual Weapon", "Warding Bond", "Zone of Truth"],            "3rd_level": ["Mass Healing Word", "Revivify", "Sending", "Spirit Guardians", "Water Walk"],            "4th_level": ["Banishment", "Control Water", "Death Ward", "Freedom of Movement", "Guardian of Faith"],            "5th_level": ["Circle of Power", "Contagion", "Flame Strike", "Geas", "Insect Plague"],            "6th_level": ["Blade Barrier", "Create Undead", "Harm", "Heal", "Heroes' Feast"],            "7th_level": ["Conjure Celestial", "Divine Word", "Etherealness", "Fire Storm", "Regenerate"],            "8th_level": ["Antimagic Field", "Control Weather", "Earthquake", "Holy Aura", "Sunburst"],            "9th_level": ["Astral Projection", "Gate", "Mass Heal", "True Resurrection", "Weird"]        },        "prepared_spells": {            "cantrips": ["Guidance (S)", "Sacred Flame (D)", "Thaumaturgy (S)", "Toll the Dead (D)"],            "1st_level": ["Bless (S)", "Cure Wounds (S)", "Guiding Bolt (D)", "Infestation (D)"],            "2nd_level": ["Lesser Restoration (S)", "Prayer of Healing (S)", "Spiritual Weapon (D)"],            "3rd_level": ["Mass Healing Word (S)", "Revivify (S)", "Spirit Guardians (D)"],            "4th_level": ["Banishment (D)", "Death Ward (S)", "Guardian of Faith (D)"],            "5th_level": ["Flame Strike (D)", "Insect Plague (D)"],            "6th_level": ["Harm (D)", "Heal (S)"],            "7th_level": ["Fire Storm (D)", "Regenerate (S)"],            "8th_level": ["Earthquake (D)", "Holy Aura (S)"],            "9th_level": ["Mass Heal (S)" ]        }    },    "skills": {        "strength_skills": {            "athletics": {"bonus": 9, "proficiency_bonus": true}        },        "dexterity_skills": {            "acrobatics": {"bonus": 5, "proficiency_bonus": false},            "sleight_of_hand": {"bonus": 5, "proficiency_bonus": false},            "stealth": {"bonus": 5, "proficiency_bonus": false}        },        "intelligence_skills": {            "arcana": {"bonus": 3, "proficiency_bonus": false},            "history": {"bonus": 3, "proficiency_bonus": false},            "investigation": {"bonus": 3, "proficiency_bonus": false},            "nature": {"bonus": 3, "proficiency_bonus": false},            "religion": {"bonus": 9, "proficiency_bonus": true}        },        "wisdom_skills": {            "animal_handling": {"bonus": 13, "proficiency_bonus": true},            "insight": {"bonus": 13, "proficiency_bonus": true},            "medicine": {"bonus": 13, "proficiency_bonus": true},            "perception": {"bonus": 13, "proficiency_bonus": true},            "survival": {"bonus": 13, "proficiency_bonus": true}        },        "charisma_skills": {            "deception": {"bonus": 1, "proficiency_bonus": false},            "intimidation": {"bonus": 1, "proficiency_bonus": false},            "performance": {"bonus": 1, "proficiency_bonus": false},            "persuasion": {"bonus": 7, "proficiency_bonus": true}        }    },  
    "features": [        "Spellcasting",        "Channel Divinity (2/short rest)",        "Destroy Undead (CR 3)",        "Divine Intervention (1/long rest)",        "Domain Spells",        "Blessed Healer",        "Divine Strike",        "Supreme Healing",        "Life Domain: Preserve Life",        "Life Domain: Blessed Healer"    ],    "special_abilities_and_traits": [        "Darkvision (60 ft)",        "Ritual Casting",        "Life Domain: Bonus Proficiency in Heavy Armor"    ],    "languages": ["Common", "Celestial", "Primordial"],    "equipment": [        "Mace",        "Scale mail armor",        "Light crossbow and 20 bolts",        "Dungeoneer's pack",        "A holy symbol"    ],    "additional_equipment": [        "Bedroll",        "Mess kit",        "10 ball bearings",        "10 feet of string",        "A belt pouch containing 10 GP"    ],    "money": {        "platinum": 0,        "gold": 100,        "electrum": 0,        "silver": 50,        "copper": 25    },    "weapons": {        "mace": {            "damage": "1d6 bludgeoning",            "attack_bonus": 8,            "properties": ["Light"]        },        "light_crossbow": {            "damage": "1d8 piercing",            "attack_bonus": 7,            "properties": ["Ammunition", "Loading", "Two-Handed"],            "range": "80/320 ft"        }    }}  
  
  
Geb nur den erstellen character in genau dieser struktur zurück, wie ich sie dir im beispiel gezeigt habe.  
Füge kein 'Json' kennzeichen. Nur den reinen text.  
  
Achte darauf, dass das Level der beispiel-struktur 20 ist. Nicht jeder Character soll auf level 20 erstellt werden!  
  
Wenn du in der Characterbeschreibung keine klar erkennbare Level-höhe herauslesen kannst,  
dann wähle ein level, dass zu den stärke-beschreibungen passt.  
Wenn z.B der Prompt lautet: 'Starker Krieger', dann kannst du das level ruhig auf 5-8 setzten.  
Wenn aber der Prompt ist: 'super starker Krieger', oder 'Heroischer Champion', dann setze das Level gern zwischen 10  und 14.  
Wenn das Wort 'gottgleich' oder andere extreme worte für die Mächtigkeit eines Characters fallen,  
dann kannst du das Level gern auf 18 - 20 setzten.  
  
Das gleiche gilt für schwache wörter.  
z.B 'schwacher Krieger', wäre eher Level 1-4.  
  
Falls keine dieser - oder andere - Schlagwörter für die Stärke eines Characters fallen, dann setzte das Level pauschal auf 5 - 8  
  
Als nächstes kommt die aufforderung den character zu erstellen, mit den KLassen daten und den character details.  
  
Das hier ist die Aufferderung den Character zu erstellen:  
'''  
Erstelle einen Robin Hood, ein ranger auf Level 10. Orientiere dich bei dem ranger an folgenden details: ["Robin Hood", "Bogenschütze", "Wald", "Dieb", "Geschicklichkeit", "Heimlichkeit", "Gerechtigkeit"]
'''  
  
Jetzt kommen allen nötigen Klassendaten:  
'''  
Base_data_for_class:  
"""  
{  
        "index": "ranger",  
        "name": "Ranger",  
        "hit_die": 10,  
        "proficiency_choices": [  
            {  
                "desc": "Choose three from Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, and Survival",  
                "choose": 3,  
                "type": "proficiencies",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-animal-handling",  
                                "name": "Skill: Animal Handling",  
                                "url": "/api/2014/proficiencies/skill-animal-handling"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-athletics",  
                                "name": "Skill: Athletics",  
                                "url": "/api/2014/proficiencies/skill-athletics"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-insight",  
                                "name": "Skill: Insight",  
                                "url": "/api/2014/proficiencies/skill-insight"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-investigation",  
                                "name": "Skill: Investigation",  
                                "url": "/api/2014/proficiencies/skill-investigation"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-nature",  
                                "name": "Skill: Nature",  
                                "url": "/api/2014/proficiencies/skill-nature"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-perception",  
                                "name": "Skill: Perception",  
                                "url": "/api/2014/proficiencies/skill-perception"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-stealth",  
                                "name": "Skill: Stealth",  
                                "url": "/api/2014/proficiencies/skill-stealth"  
                            }  
                        },  
                        {  
                            "option_type": "reference",  
                            "item": {  
                                "index": "skill-survival",  
                                "name": "Skill: Survival",  
                                "url": "/api/2014/proficiencies/skill-survival"  
                            }  
                        }  
                    ]  
                }  
            }  
        ],  
        "proficiencies": [  
            {  
                "index": "light-armor",  
                "name": "Light Armor",  
                "url": "/api/2014/proficiencies/light-armor"  
            },  
            {  
                "index": "medium-armor",  
                "name": "Medium Armor",  
                "url": "/api/2014/proficiencies/medium-armor"  
            },  
            {  
                "index": "shields",  
                "name": "Shields",  
                "url": "/api/2014/proficiencies/shields"  
            },  
            {  
                "index": "simple-weapons",  
                "name": "Simple Weapons",  
                "url": "/api/2014/proficiencies/simple-weapons"  
            },  
            {  
                "index": "martial-weapons",  
                "name": "Martial Weapons",  
                "url": "/api/2014/proficiencies/martial-weapons"  
            },  
            {  
                "index": "saving-throw-dex",  
                "name": "Saving Throw: DEX",  
                "url": "/api/2014/proficiencies/saving-throw-dex"  
            },  
            {  
                "index": "saving-throw-str",  
                "name": "Saving Throw: STR",  
                "url": "/api/2014/proficiencies/saving-throw-str"  
            }  
        ],  
        "saving_throws": [  
            {  
                "index": "str",  
                "name": "STR",  
                "url": "/api/2014/ability-scores/str"  
            },  
            {  
                "index": "dex",  
                "name": "DEX",  
                "url": "/api/2014/ability-scores/dex"  
            }  
        ],  
        "starting_equipment": [  
            {  
                "equipment": {  
                    "index": "longbow",  
                    "name": "Longbow",  
                    "url": "/api/2014/equipment/longbow"  
                },  
                "quantity": 1  
            },  
            {  
                "equipment": {  
                    "index": "arrow",  
                    "name": "Arrow",  
                    "url": "/api/2014/equipment/arrow"  
                },  
                "quantity": 20  
            }  
        ],  
        "starting_equipment_options": [  
            {  
                "desc": "(a) scale mail or (b) leather armor",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "scale-mail",  
                                "name": "Scale Mail",  
                                "url": "/api/2014/equipment/scale-mail"  
                            }  
                        },  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "leather-armor",  
                                "name": "Leather Armor",  
                                "url": "/api/2014/equipment/leather-armor"  
                            }  
                        }  
                    ]  
                }  
            },  
            {  
                "desc": "(a) two shortswords or (b) two simple melee weapons",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 2,  
                            "of": {  
                                "index": "shortsword",  
                                "name": "Shortsword",  
                                "url": "/api/2014/equipment/shortsword"  
                            }  
                        },  
                        {  
                            "option_type": "choice",  
                            "choice": {  
                                "desc": "two simple melee weapons",  
                                "choose": 2,  
                                "type": "equipment",  
                                "from": {  
                                    "option_set_type": "equipment_category",  
                                    "equipment_category": {  
                                        "index": "simple-melee-weapons",  
                                        "name": "Simple Melee Weapons",  
                                        "url": "/api/2014/equipment-categories/simple-melee-weapons"  
                                    }  
                                }  
                            }  
                        }  
                    ]  
                }  
            },  
            {  
                "desc": "(a) a dungeoneer\u2019s pack or (b) an explorer\u2019s pack",  
                "choose": 1,  
                "type": "equipment",  
                "from": {  
                    "option_set_type": "options_array",  
                    "options": [  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "dungeoneers-pack",  
                                "name": "Dungeoneer's Pack",  
                                "url": "/api/2014/equipment/dungeoneers-pack"  
                            }  
                        },  
                        {  
                            "option_type": "counted_reference",  
                            "count": 1,  
                            "of": {  
                                "index": "explorers-pack",  
                                "name": "Explorer's Pack",  
                                "url": "/api/2014/equipment/explorers-pack"  
                            }  
                        }  
                    ]  
                }  
            }  
        ],  
        "class_levels": "/api/2014/classes/ranger/levels",  
        "multi_classing": {  
            "prerequisites": [  
                {  
                    "ability_score": {  
                        "index": "dex",  
                        "name": "DEX",  
                        "url": "/api/2014/ability-scores/dex"  
                    },  
                    "minimum_score": 13  
                },  
                {  
                    "ability_score": {  
                        "index": "wis",  
                        "name": "WIS",  
                        "url": "/api/2014/ability-scores/wis"  
                    },  
                    "minimum_score": 13  
                }  
            ],  
            "proficiencies": [  
                {  
                    "index": "light-armor",  
                    "name": "Light Armor",  
                    "url": "/api/2014/proficiencies/light-armor"  
                },  
                {  
                    "index": "medium-armor",  
                    "name": "Medium Armor",  
                    "url": "/api/2014/proficiencies/medium-armor"  
                },  
                {  
                    "index": "shields",  
                    "name": "Shields",  
                    "url": "/api/2014/proficiencies/shields"  
                },  
                {  
                    "index": "simple-weapons",  
                    "name": "Simple Weapons",  
                    "url": "/api/2014/proficiencies/simple-weapons"  
                },  
                {  
                    "index": "martial-weapons",  
                    "name": "Martial Weapons",  
                    "url": "/api/2014/proficiencies/martial-weapons"  
                }  
            ],  
            "proficiency_choices": [  
                {  
                    "choose": 1,  
                    "type": "proficiencies",  
                    "from": {  
                        "option_set_type": "options_array",  
                        "options": [  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-animal-handling",  
                                    "name": "Skill: Animal Handling",  
                                    "url": "/api/2014/proficiencies/skill-animal-handling"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-athletics",  
                                    "name": "Skill: Athletics",  
                                    "url": "/api/2014/proficiencies/skill-athletics"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-insight",  
                                    "name": "Skill: Insight",  
                                    "url": "/api/2014/proficiencies/skill-insight"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-investigation",  
                                    "name": "Skill: Investigation",  
                                    "url": "/api/2014/proficiencies/skill-investigation"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-nature",  
                                    "name": "Skill: Nature",  
                                    "url": "/api/2014/proficiencies/skill-nature"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-perception",  
                                    "name": "Skill: Perception",  
                                    "url": "/api/2014/proficiencies/skill-perception"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-stealth",  
                                    "name": "Skill: Stealth",  
                                    "url": "/api/2014/proficiencies/skill-stealth"  
                                }  
                            },  
                            {  
                                "option_type": "reference",  
                                "item": {  
                                    "index": "skill-survival",  
                                    "name": "Skill: Survival",  
                                    "url": "/api/2014/proficiencies/skill-survival"  
                                }  
                            }  
                        ]  
                    }  
                }  
            ]  
        },  
        "subclasses": [  
            {  
                "index": "hunter",  
                "name": "Hunter",  
                "url": "/api/2014/subclasses/hunter"  
            }  
        ],  
        "spellcasting": {  
            "level": 2,  
            "spellcasting_ability": {  
                "index": "wis",  
                "name": "WIS",  
                "url": "/api/2014/ability-scores/wis"  
            },  
            "info": [  
                {  
                    "name": "Spell Slots",  
                    "desc": [  
                        "The Ranger table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.",  
                        "For example, if you know the 1st-level spell animal friendship and have a 1st-level and a 2nd-level spell slot available, you can cast animal friendship using either slot."  
                    ]  
                },  
                {  
                    "name": "Spells Known of 1st Level and Higher",  
                    "desc": [  
                        "You know two 1st-level spells of your choice from the ranger spell list.",  
                        "The Spells Known column of the Ranger table shows when you learn more ranger spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 5th level in this class, you can learn one new spell of 1st or 2nd level.",  
                        "Additionally, when you gain a level in this class, you can choose one of the ranger spells you know and replace it with another spell from the ranger spell list, which also must be of a level for which you have spell slots."  
                    ]  
                },  
                {  
                    "name": "Spellcasting Ability",  
                    "desc": [  
                        "Wisdom is your spellcasting ability for your ranger spells, since your magic draws on your attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a ranger spell you cast and when making an attack roll with one.",  
                        "Spell save DC = 8 + your proficiency bonus + your Wisdom modifier.",  
                        "Spell attack modifier = your proficiency bonus + your Wisdom modifier."  
                    ]  
                }  
            ]  
        },  
        "spells": "/api/2014/classes/ranger/spells",  
        "url": "/api/2014/classes/ranger"  
    }  
"""  
      
  
level_features:  
"""  
[  
    [  
        {  
            "level": 1,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "favored-enemy-1-type",  
                    "name": "Favored Enemy (1 type)",  
                    "details": {  
                        "index": "favored-enemy-1-type",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (1 type)",  
                        "level": 1,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-1-type",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "natural-explorer-1-terrain-type",  
                    "name": "Natural Explorer (1 terrain type)",  
                    "details": {  
                        "index": "natural-explorer-1-terrain-type",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (1 terrain type)",  
                        "level": 1,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-1-terrain-type",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 0,  
                "spell_slots_level_1": 0,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-1"  
        },  
        {  
            "level": 2,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-fighting-style",  
                    "name": "Fighting Style",  
                    "details": {  
                        "index": "ranger-fighting-style",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Fighting Style",  
                        "level": 2,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 2nd level, you adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again."  
                        ],  
                        "feature_specific": {  
                            "subfeature_options": {  
                                "choose": 1,  
                                "type": "feature",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-archery",  
                                                "name": "Fighting Style: Archery",  
                                                "url": "/api/2014/features/ranger-fighting-style-archery"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-defense",  
                                                "name": "Fighting Style: Defense",  
                                                "url": "/api/2014/features/ranger-fighting-style-defense"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-dueling",  
                                                "name": "Fighting Style: Dueling",  
                                                "url": "/api/2014/features/ranger-fighting-style-dueling"  
                                            }  
                                        },  
                                        {  
                                            "option_type": "reference",  
                                            "item": {  
                                                "index": "ranger-fighting-style-two-weapon-fighting",  
                                                "name": "Fighting Style: Two-Weapon Fighting",  
                                                "url": "/api/2014/features/ranger-fighting-style-two-weapon-fighting"  
                                            }  
                                        }  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/ranger-fighting-style",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "spellcasting-ranger",  
                    "name": "Spellcasting: Ranger",  
                    "details": {  
                        "index": "spellcasting-ranger",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Spellcasting: Ranger",  
                        "level": 2,  
                        "prerequisites": [],  
                        "desc": [  
                            "By the time you reach 2nd level, you have learned to use the magical essence of nature to cast spells, much as a druid does."  
                        ],  
                        "reference": "/api/2014/classes/ranger/spellcasting",  
                        "url": "/api/2014/features/spellcasting-ranger",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 2,  
                "spell_slots_level_1": 2,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-2"  
        },  
        {  
            "level": 3,  
            "ability_score_bonuses": 0,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-archetype",  
                    "name": "Ranger Archetype",  
                    "details": {  
                        "index": "ranger-archetype",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ranger Archetype",  
                        "level": 3,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 3rd level, you choose an archetype that you strive to emulate, such as the Hunter. Your choice grants you features at 3rd level and again at 7th, 11th, and 15th level."  
                        ],  
                        "url": "/api/2014/features/ranger-archetype",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "primeval-awareness",  
                    "name": "Primeval Awareness",  
                    "details": {  
                        "index": "primeval-awareness",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Primeval Awareness",  
                        "level": 3,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 3rd level, you can use your action and expend one ranger spell slot to focus your awareness on the region around you. For 1 minute per level of the spell slot you expend, you can sense whether the following types of creatures are present within 1 mile of you (or within up to 6 miles if you are in your favored terrain): aberrations, celestials, dragons, elementals, fey, fiends, and undead. This feature doesn't reveal the creatures' location or number."  
                        ],  
                        "url": "/api/2014/features/primeval-awareness",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 3,  
                "spell_slots_level_1": 3,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-3"  
        },  
        {  
            "level": 4,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 2,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-1",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-1",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 4,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-1",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 3,  
                "spell_slots_level_1": 3,  
                "spell_slots_level_2": 0,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-4"  
        },  
        {  
            "level": 5,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "ranger-extra-attack",  
                    "name": "Extra Attack",  
                    "details": {  
                        "index": "ranger-extra-attack",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Extra Attack",  
                        "level": 5,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."  
                        ],  
                        "url": "/api/2014/features/ranger-extra-attack",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 4,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 2,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 1,  
                "favored_terrain": 1  
            },  
            "index": "ranger-5"  
        },  
        {  
            "level": 6,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "favored-enemy-2-types",  
                    "name": "Favored Enemy (2 types)",  
                    "details": {  
                        "index": "favored-enemy-2-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (2 types)",  
                        "level": 6,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-2-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "natural-explorer-2-terrain-types",  
                    "name": "Natural Explorer (2 terrain types)",  
                    "details": {  
                        "index": "natural-explorer-2-terrain-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (2 terrain types)",  
                        "level": 6,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-2-terrain-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 4,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 2,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-6"  
        },  
        {  
            "level": 7,  
            "ability_score_bonuses": 1,  
            "prof_bonus": 3,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 5,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-7"  
        },  
        {  
            "level": 8,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 3,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-2",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-2",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 8,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-2",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "ranger-lands-stride",  
                    "name": "Land's Stride",  
                    "details": {  
                        "index": "ranger-lands-stride",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Land's Stride",  
                        "level": 8,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 8th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.",  
                            "In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such those created by the entangle spell."  
                        ],  
                        "url": "/api/2014/features/ranger-lands-stride",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 5,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 0,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-8"  
        },  
        {  
            "level": 9,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 6,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 2,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 2  
            },  
            "index": "ranger-9"  
        },  
        {  
            "level": 10,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [  
                {  
                    "index": "natural-explorer-3-terrain-types",  
                    "name": "Natural Explorer (3 terrain types)",  
                    "details": {  
                        "index": "natural-explorer-3-terrain-types",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Natural Explorer (3 terrain types)",  
                        "level": 10,  
                        "prerequisites": [],  
                        "desc": [  
                            "You are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, or swamp. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.",  
                            "While traveling for an hour or more in your favored terrain, you gain the following benefits:",  
                            "- Difficult terrain doesn't slow your group's travel.",  
                            "- Your group can't become lost except by magical means.",  
                            "- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.",  
                            "- If you are traveling alone, you can move stealthily at a normal pace.",  
                            "- When you forage, you find twice as much food as you normally would.",  
                            "- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",  
                            "You choose additional favored terrain types at 6th and 10th level."  
                        ],  
                        "feature_specific": {  
                            "terrain_type_options": {  
                                "desc": "one terrain type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "arctic",  
                                        "coast",  
                                        "desert",  
                                        "forest",  
                                        "grassland",  
                                        "mountain",  
                                        "swamp"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/natural-explorer-3-terrain-types",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "hide-in-plain-sight",  
                    "name": "Hide in Plain Sight",  
                    "details": {  
                        "index": "hide-in-plain-sight",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Hide in Plain Sight",  
                        "level": 10,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 10th level, you can spend 1 minute creating camouflage for yourself. You must have access to fresh mud, dirt, plants, soot, and other naturally occurring materials with which to create your camouflage.",  
                            "Once you are camouflaged in this way, you can try to hide by pressing yourself up against a solid surface, such as a tree or wall, that is at least as tall and wide as you are. You gain a +10 bonus to Dexterity (Stealth) checks as long as you remain there without moving or taking actions. Once you move or take an action or a reaction, you must camouflage yourself again to gain this benefit."  
                        ],  
                        "url": "/api/2014/features/hide-in-plain-sight",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 6,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 2,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-10"  
        },  
        {  
            "level": 11,  
            "ability_score_bonuses": 2,  
            "prof_bonus": 4,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 7,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-11"  
        },  
        {  
            "level": 12,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 4,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-3",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-3",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 12,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-3",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 7,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 0,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-12"  
        },  
        {  
            "level": 13,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 8,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 1,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 2,  
                "favored_terrain": 3  
            },  
            "index": "ranger-13"  
        },  
        {  
            "level": 14,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [  
                {  
                    "index": "favored-enemy-3-enemies",  
                    "name": "Favored Enemy (3 enemies)",  
                    "details": {  
                        "index": "favored-enemy-3-enemies",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Favored Enemy (3 enemies)",  
                        "level": 14,  
                        "prerequisites": [],  
                        "desc": [  
                            "Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.",  
                            "Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.",  
                            "You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.",  
                            "When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.",  
                            "You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures."  
                        ],  
                        "feature_specific": {  
                            "enemy_type_options": {  
                                "desc": "one enemy type",  
                                "choose": 1,  
                                "type": "string",  
                                "from": {  
                                    "option_set_type": "options_array",  
                                    "options": [  
                                        "aberrations",  
                                        "beasts",  
                                        "celestials",  
                                        "constructs",  
                                        "dragons",  
                                        "elementals",  
                                        "fey",  
                                        "fiends",  
                                        "giants",  
                                        "monstrosities",  
                                        "oozes",  
                                        "plants",  
                                        "undead",  
                                        "humanoids"  
                                    ]  
                                }  
                            },  
                            "invocations": []  
                        },  
                        "url": "/api/2014/features/favored-enemy-3-enemies",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                },  
                {  
                    "index": "vanish",  
                    "name": "Vanish",  
                    "details": {  
                        "index": "vanish",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Vanish",  
                        "level": 14,  
                        "prerequisites": [],  
                        "desc": [  
                            "Starting at 14th level, you can use the Hide action as a bonus action on your turn. Also, you can't be tracked by nonmagical means, unless you choose to leave a trail."  
                        ],  
                        "url": "/api/2014/features/vanish",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 8,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 1,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-14"  
        },  
        {  
            "level": 15,  
            "ability_score_bonuses": 3,  
            "prof_bonus": 5,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 9,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 2,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-15"  
        },  
        {  
            "level": 16,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 5,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-4",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-4",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 16,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-4",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 9,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 2,  
                "spell_slots_level_5": 0  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-16"  
        },  
        {  
            "level": 17,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 6,  
            "features": [],  
            "spellcasting": {  
                "spells_known": 10,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 1  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-17"  
        },  
        {  
            "level": 18,  
            "ability_score_bonuses": 4,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "feral-senses",  
                    "name": "Feral Senses",  
                    "details": {  
                        "index": "feral-senses",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Feral Senses",  
                        "level": 18,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 18th level, you gain preternatural senses that help you fight creatures you can't see. When you attack a creature you can't see, your inability to see it doesn't impose disadvantage on your attack rolls against it.",  
                            "You are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn't hidden from you and you aren't blinded or deafened."  
                        ],  
                        "url": "/api/2014/features/feral-senses",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 10,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 1  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-18"  
        },  
        {  
            "level": 19,  
            "ability_score_bonuses": 5,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "ranger-ability-score-improvement-5",  
                    "name": "Ability Score Improvement",  
                    "details": {  
                        "index": "ranger-ability-score-improvement-5",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Ability Score Improvement",  
                        "level": 19,  
                        "prerequisites": [],  
                        "desc": [  
                            "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."  
                        ],  
                        "url": "/api/2014/features/ranger-ability-score-improvement-5",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 11,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 2  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-19"  
        },  
        {  
            "level": 20,  
            "ability_score_bonuses": 5,  
            "prof_bonus": 6,  
            "features": [  
                {  
                    "index": "foe-slayer",  
                    "name": "Foe Slayer",  
                    "details": {  
                        "index": "foe-slayer",  
                        "class": {  
                            "index": "ranger",  
                            "name": "Ranger",  
                            "url": "/api/2014/classes/ranger"  
                        },  
                        "name": "Foe Slayer",  
                        "level": 20,  
                        "prerequisites": [],  
                        "desc": [  
                            "At 20th level, you become an unparalleled hunter of your enemies. Once on each of your turns, you can add your Wisdom modifier to the attack roll or the damage roll of an attack you make against one of your favored enemies. You can choose to use this feature before or after the roll, but before any effects of the roll are applied."  
                        ],  
                        "url": "/api/2014/features/foe-slayer",  
                        "updated_at": "2025-04-08T21:14:01.855Z"  
                    }  
                }  
            ],  
            "spellcasting": {  
                "spells_known": 11,  
                "spell_slots_level_1": 4,  
                "spell_slots_level_2": 3,  
                "spell_slots_level_3": 3,  
                "spell_slots_level_4": 3,  
                "spell_slots_level_5": 2  
            },  
            "class_specific": {  
                "favored_enemies": 3,  
                "favored_terrain": 3  
            },  
            "index": "ranger-20"  
        }  
    ]  
]  
"""  
  
spells:  
"""  
[  
    [  
        {  
            "index": "alarm",  
            "name": "Alarm",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "alarm",  
                "name": "Alarm",  
                "desc": [  
                    "You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area. When you cast the spell, you can designate creatures that won't set off the alarm. You also choose whether the alarm is mental or audible.",  
                    "A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping.",  
                    "An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A tiny bell and a piece of fine silver wire.",  
                "ritual": true,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 minute",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "cube",  
                    "size": 20  
                },  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/alarm",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "animal-friendship",  
            "name": "Animal Friendship",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "animal-friendship",  
                "name": "Animal Friendship",  
                "desc": [  
                    "This spell lets you convince a beast that you mean it no harm. Choose a beast that you can see within range. It must see and hear you. If the beast's Intelligence is 4 or higher, the spell fails. Otherwise, the beast must succeed on a wisdom saving throw or be charmed by you for the spell's duration. If you or one of your companions harms the target, the spells ends."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A morsel of food.",  
                "ritual": false,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "dc": {  
                    "dc_type": {  
                        "index": "wis",  
                        "name": "WIS",  
                        "url": "/api/2014/ability-scores/wis"  
                    },  
                    "dc_success": "none"  
                },  
                "school": {  
                    "index": "enchantment",  
                    "name": "Enchantment",  
                    "url": "/api/2014/magic-schools/enchantment"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/animal-friendship",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "cure-wounds",  
            "name": "Cure Wounds",  
            "level": 1,  
            "details": {  
                "index": "cure-wounds",  
                "name": "Cure Wounds",  
                "desc": [  
                    "A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d8 for each slot level above 1st."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "heal_at_slot_level": {  
                    "1": "1d8 + MOD",  
                    "2": "2d8 + MOD",  
                    "3": "3d8 + MOD",  
                    "4": "4d8 + MOD",  
                    "5": "5d8 + MOD",  
                    "6": "6d8 + MOD",  
                    "7": "7d8 + MOD",  
                    "8": "8d8 + MOD",  
                    "9": "9d8 + MOD"  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "life",  
                        "name": "Life",  
                        "url": "/api/2014/subclasses/life"  
                    }  
                ],  
                "url": "/api/2014/spells/cure-wounds",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "detect-magic",  
            "name": "Detect Magic",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "detect-magic",  
                "name": "Detect Magic",  
                "desc": [  
                    "For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic, and you learn its school of magic, if any.",  
                    "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/detect-magic",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "detect-poison-and-disease",  
            "name": "Detect Poison and Disease",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "detect-poison-and-disease",  
                "name": "Detect Poison and Disease",  
                "desc": [  
                    "For the duration, you can sense the presence and location of poisons, poisonous creatures, and diseases within 30 feet of you. You also identify the kind of poison, poisonous creature, or disease in each case.",  
                    "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A yew leaf.",  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/detect-poison-and-disease",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "fog-cloud",  
            "name": "Fog Cloud",  
            "level": 1,  
            "details": {  
                "index": "fog-cloud",  
                "name": "Fog Cloud",  
                "desc": [  
                    "You create a 20-foot-radius sphere of fog centered on a point within range. The sphere spreads around corners, and its area is heavily obscured. It lasts for the duration or until a wind of moderate or greater speed (at least 10 miles per hour) disperses it."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, the radius of the fog increases by 20 feet for each slot level above 1st."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 1,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 20  
                },  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/fog-cloud",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "goodberry",  
            "name": "Goodberry",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "goodberry",  
                "name": "Goodberry",  
                "desc": [  
                    "Up to ten berries appear in your hand and are infused with magic for the duration. A creature can use its action to eat one berry. Eating a berry restores 1 hit point, and the berry provides enough nourishment to sustain a creature for a day.",  
                    "The berries lose their potency if they have not been consumed within 24 hours of the casting of this spell."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A sprig of mistletoe.",  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/goodberry",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "hunters-mark",  
            "name": "Hunter's Mark",  
            "level": 1,  
            "details": {  
                "index": "hunters-mark",  
                "name": "Hunter's Mark",  
                "desc": [  
                    "You choose a creature you can see within range and mystically mark it as your quarry. Until the spell ends, you deal an extra 1d6 damage to the target whenever you hit it with a weapon attack, and you have advantage on any Wisdom (Perception) or Wisdom (Survival) check you make to find it. If the target drops to 0 hit points before this spell ends, you can use a bonus action on a subsequent turn of yours to mark a new creature."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 3rd or 4th level, you can maintain your concentration on the spell for up to 8 hours. When you use a spell slot of 5th level or higher, you can maintain your concentration on the spell for up to 24 hours."  
                ],  
                "range": "90 feet",  
                "components": [  
                    "V"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 bonus action",  
                "level": 1,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/hunters-mark",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "jump",  
            "name": "Jump",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "jump",  
                "name": "Jump",  
                "desc": [  
                    "You touch a creature. The creature's jump distance is tripled until the spell ends."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A grasshopper's hind leg.",  
                "ritual": false,  
                "duration": "1 minute",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/jump",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "longstrider",  
            "name": "Longstrider",  
            "level": 1,  
            "details": {  
                "index": "longstrider",  
                "name": "Longstrider",  
                "desc": [  
                    "You touch a creature. The target's speed increases by 10 feet until the spell ends."  
                ],  
                "higher_level": [  
                    "When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each spell slot above 1st."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A pinch of dirt.",  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/longstrider",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "speak-with-animals",  
            "name": "Speak with Animals",  
            "level": 1,  
            "details": {  
                "higher_level": [],  
                "index": "speak-with-animals",  
                "name": "Speak with Animals",  
                "desc": [  
                    "You gain the ability to comprehend and verbally communicate with beasts for the duration. The knowledge and awareness of many beasts is limited by their intelligence, but at a minimum, beasts can give you information about nearby locations and monsters, including whatever they can perceive or have perceived within the past day. You might be able to persuade a beast to perform a small favor for you, at the GM's discretion."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "10 minutes",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 1,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/speak-with-animals",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "animal-messenger",  
            "name": "Animal Messenger",  
            "level": 2,  
            "details": {  
                "index": "animal-messenger",  
                "name": "Animal Messenger",  
                "desc": [  
                    "By means of this spell, you use an animal to deliver a message. Choose a Tiny beast you can see within range, such as a squirrel, a blue jay, or a bat. You specify a location, which you must have visited, and a recipient who matches a general description, such as \"a man or woman dressed in the uniform of the town guard\" or \"a red-haired dwarf wearing a pointed hat.\" You also speak a message of up to twenty-five words. The target beast travels for the duration of the spell toward the specified location, covering about 50 miles per 24 hours for a flying messenger, or 25 miles for other animals.",  
                    "When the messenger arrives, it delivers your message to the creature that you described, replicating the sound of your voice. The messenger speaks only to a creature matching the description you gave. If the messenger doesn't reach its destination before the spell ends, the message is lost, and the beast makes its way back to where you cast this spell."  
                ],  
                "higher_level": [  
                    "If you cast this spell using a spell slot of 3nd level or higher, the duration of the spell increases by 48 hours for each slot level above 2nd."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A morsel of food.",  
                "ritual": true,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "enchantment",  
                    "name": "Enchantment",  
                    "url": "/api/2014/magic-schools/enchantment"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/animal-messenger",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "barkskin",  
            "name": "Barkskin",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "barkskin",  
                "name": "Barkskin",  
                "desc": [  
                    "You touch a willing creature. Until the spell ends, the target's skin has a rough, bark-like appearance, and the target's AC can't be less than 16, regardless of what kind of armor it is wearing."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A handful of oak bark.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/barkskin",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "darkvision",  
            "name": "Darkvision",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "darkvision",  
                "name": "Darkvision",  
                "desc": [  
                    "You touch a willing creature to grant it the ability to see in the dark. For the duration, that creature has darkvision out to a range of 60 feet."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Either a pinch of dried carrot or an agate.",  
                "ritual": false,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/darkvision",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "find-traps",  
            "name": "Find Traps",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "find-traps",  
                "name": "Find Traps",  
                "desc": [  
                    "You sense the presence of any trap within range that is within line of sight. A trap, for the purpose of this spell, includes anything that would inflict a sudden or unexpected effect you consider harmful or undesirable, which was specifically intended as such by its creator. Thus, the spell would sense an area affected by the alarm spell, a glyph of warding, or a mechanical pit trap, but it would not reveal a natural weakness in the floor, an unstable ceiling, or a hidden sinkhole.",  
                    "This spell merely reveals that a trap is present. You don't learn the location of each trap, but you do learn the general nature of the danger posed by a trap you sense."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/find-traps",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "lesser-restoration",  
            "name": "Lesser Restoration",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "lesser-restoration",  
                "name": "Lesser Restoration",  
                "desc": [  
                    "You touch a creature and can end either one disease or one condition afflicting it. The condition can be blinded, deafened, paralyzed, or poisoned."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "life",  
                        "name": "Life",  
                        "url": "/api/2014/subclasses/life"  
                    },  
                    {  
                        "index": "devotion",  
                        "name": "Devotion",  
                        "url": "/api/2014/subclasses/devotion"  
                    }  
                ],  
                "url": "/api/2014/spells/lesser-restoration",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-animals-or-plants",  
            "name": "Locate Animals or Plants",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "locate-animals-or-plants",  
                "name": "Locate Animals or Plants",  
                "desc": [  
                    "Describe or name a specific kind of beast or plant. Concentrating on the voice of nature in your surroundings, you learn the direction and distance to the closest creature or plant of that kind within 5 miles, if any are present."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A bit of fur from a bloodhound.",  
                "ritual": true,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-animals-or-plants",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-object",  
            "name": "Locate Object",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "locate-object",  
                "name": "Locate Object",  
                "desc": [  
                    "Describe or name an object that is familiar to you. You sense the direction to the object's location, as long as that object is within 1,000 feet of you. If the object is in motion, you know the direction of its movement.",  
                    "The spell can locate a specific object known to you, as long as you have seen it up close--within 30 feet--at least once. Alternatively, the spell can locate the nearest object of a particular kind, such as a certain kind of apparel, jewelry, furniture, tool, or weapon.",  
                    "This spell can't locate an object if any thickness of lead, even a thin sheet, blocks a direct path between you and the object."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A forked twig.",  
                "ritual": false,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-object",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "pass-without-trace",  
            "name": "Pass Without Trace",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "pass-without-trace",  
                "name": "Pass Without Trace",  
                "desc": [  
                    "A veil of shadows and silence radiates from you, masking you and your companions from detection. For the duration, each creature you choose within 30 feet of you (including you) has a +10 bonus to Dexterity (Stealth) checks and can't be tracked except by magical means. A creature that receives this bonus leaves behind no tracks or other traces of its passage."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Ashes from a burned leaf of mistletoe and a sprig of spruce.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/pass-without-trace",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "protection-from-poison",  
            "name": "Protection from Poison",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "protection-from-poison",  
                "name": "Protection from Poison",  
                "desc": [  
                    "You touch a creature. If it is poisoned, you neutralize the poison. If more than one poison afflicts the target, you neutralize one poison that you know is present, or you neutralize one at random.",  
                    "For the duration, the target has advantage on saving throws against being poisoned, and it has resistance to poison damage."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 2,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/protection-from-poison",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "silence",  
            "name": "Silence",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "silence",  
                "name": "Silence",  
                "desc": [  
                    "For the duration, no sound can be created within or pass through a 20-foot-radius sphere centered on a point you choose within range. Any creature or object entirely inside the sphere is immune to thunder damage, and creatures are deafened while entirely inside it.",  
                    "Casting a spell that includes a verbal component is impossible there."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 20  
                },  
                "school": {  
                    "index": "illusion",  
                    "name": "Illusion",  
                    "url": "/api/2014/magic-schools/illusion"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/silence",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "spike-growth",  
            "name": "Spike Growth",  
            "level": 2,  
            "details": {  
                "higher_level": [],  
                "index": "spike-growth",  
                "name": "Spike Growth",  
                "desc": [  
                    "The ground in a 20-foot radius centered on a point within range twists and sprouts hard spikes and thorns. The area becomes difficult terrain for the duration. When a creature moves into or within the area, it takes 2d4 piercing damage for every 5 feet it travels.",  
                    "The transformation of the ground is camouflaged to look natural. Any creature that can't see the area at the time the spell is cast can make a Wisdom (Perception) check against your spell save DC to recognize the terrain as hazardous before entering it."  
                ],  
                "range": "150 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Seven sharp thorns or seven small twigs, each sharpened to a point.",  
                "ritual": false,  
                "duration": "Up to 10 minutes",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 2,  
                "area_of_effect": {  
                    "type": "cylinder",  
                    "size": 20  
                },  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/spike-growth",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "conjure-animals",  
            "name": "Conjure Animals",  
            "level": 3,  
            "details": {  
                "index": "conjure-animals",  
                "name": "Conjure Animals",  
                "desc": [  
                    "You summon fey spirits that take the form of beasts and appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:",  
                    "- One beast of challenge rating 2 or lower",  
                    "- Two beasts of challenge rating 1 or lower",  
                    "- Four beasts of challenge rating 1/2 or lower",  
                    "- Eight beasts of challenge rating 1/4 or lower",  
                    "- Each beast is also considered fey, and it disappears when it drops to 0 hit points or when the spell ends.",  
                    "The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which has its own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.",  
                    "The GM has the creatures' statistics."  
                ],  
                "higher_level": [  
                    "When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 5th-level slot, three times as many with a 7th-level."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/conjure-animals",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "daylight",  
            "name": "Daylight",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "daylight",  
                "name": "Daylight",  
                "desc": [  
                    "A 60-foot-radius sphere of light spreads out from a point you choose within range. The sphere is bright light and sheds dim light for an additional 60 feet.",  
                    "If you chose a point on an object you are holding or one that isn't being worn or carried, the light shines from the object and moves with it. Completely covering the affected object with an opaque object, such as a bowl or a helm, blocks the light.",  
                    "If any of this spell's area overlaps with an area of darkness created by a spell of 3rd level or lower, the spell that created the darkness is dispelled."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 60  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/daylight",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "nondetection",  
            "name": "Nondetection",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "nondetection",  
                "name": "Nondetection",  
                "desc": [  
                    "For the duration, you hide a target that you touch from divination magic. The target can be a willing creature or a place or an object no larger than 10 feet in any dimension. The target can't be targeted by any divination magic or perceived through magical scrying sensors."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A pinch of diamond dust worth 25 gp sprinkled over the target, which the spell consumes.",  
                "ritual": false,  
                "duration": "8 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/nondetection",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "plant-growth",  
            "name": "Plant Growth",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "plant-growth",  
                "name": "Plant Growth",  
                "desc": [  
                    "This spell channels vitality into plants within a specific area. There are two possible uses for the spell, granting either immediate or long-term benefits.",  
                    "If you cast this spell using 1 action, choose a point within range. All normal plants in a 100-foot radius centered on that point become thick and overgrown. A creature moving through the area must spend 4 feet of movement for every 1 foot it moves.",  
                    "You can exclude one or more areas of any size within the spell's area from being affected.",  
                    "If you cast this spell over 8 hours, you enrich the land. All plants in a half-mile radius centered on a point within range become enriched for 1 year. The plants yield twice the normal amount of food when harvested."  
                ],  
                "range": "150 feet",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/plant-growth",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "protection-from-energy",  
            "name": "Protection From Energy",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "protection-from-energy",  
                "name": "Protection From Energy",  
                "desc": [  
                    "For the duration, the willing creature you touch has resistance to one damage type of your choice: acid, cold, fire, lightning, or thunder."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/protection-from-energy",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "speak-with-plants",  
            "name": "Speak with Plants",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "speak-with-plants",  
                "name": "Speak with Plants",  
                "desc": [  
                    "You imbue plants within 30 feet of you with limited sentience and animation, giving them the ability to communicate with you and follow your simple commands. You can question plants about events in the spell's area within the past day, gaining information about creatures that have passed, weather, and other circumstances.",  
                    "You can also turn difficult terrain caused by plant growth (such as thickets and undergrowth) into ordinary terrain that lasts for the duration. Or you can turn ordinary terrain where plants are present into difficult terrain that lasts for the duration, causing vines and branches to hinder pursuers, for example.",  
                    "Plants might be able to perform other tasks on your behalf, at the GM's discretion. The spell doesn't enable plants to uproot themselves and move about, but they can freely move branches, tendrils, and stalks.",  
                    "If a plant creature is in the area, you can communicate with it as if you shared a common language, but you gain no magical ability to influence it.",  
                    "This spell can cause the plants created by the entangle spell to release a restrained creature."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "10 minutes",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "area_of_effect": {  
                    "type": "sphere",  
                    "size": 30  
                },  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/speak-with-plants",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "water-breathing",  
            "name": "Water Breathing",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "water-breathing",  
                "name": "Water Breathing",  
                "desc": [  
                    "This spell gives a maximum of ten willing creatures within range and you can see, the ability to breathe underwater until the end of its term. Affected creatures also retain their normal breathing pattern."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A short piece of reed or straw.",  
                "ritual": true,  
                "duration": "24 hours",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/water-breathing",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "water-walk",  
            "name": "Water Walk",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "water-walk",  
                "name": "Water Walk",  
                "desc": [  
                    "This spell grants the ability to move across any liquid surface--such as water, acid, mud, snow, quicksand, or lava--as if it were harmless solid ground (creatures crossing molten lava can still take damage from the heat). Up to ten willing creatures you can see within range gain this ability for the duration.",  
                    "If you target a creature submerged in a liquid, the spell carries the target to the surface of the liquid at a rate of 60 feet per round."  
                ],  
                "range": "30 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A piece of cork.",  
                "ritual": true,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 3,  
                "school": {  
                    "index": "transmutation",  
                    "name": "Transmutation",  
                    "url": "/api/2014/magic-schools/transmutation"  
                },  
                "classes": [  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    },  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/water-walk",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "wind-wall",  
            "name": "Wind Wall",  
            "level": 3,  
            "details": {  
                "higher_level": [],  
                "index": "wind-wall",  
                "name": "Wind Wall",  
                "desc": [  
                    "A wall of strong wind rises from the ground at a point you choose within range. You can make the wall up to 50 feet long, 15 feet high, and 1 foot thick. You can shape the wall in any way you choose so long as it makes one continuous path along the ground. The wall lasts for the duration.",  
                    "When the wall appears, each creature within its area must make a strength saving throw. A creature takes 3d8 bludgeoning damage on a failed save, or half as much damage on a successful one.",  
                    "The strong wind keeps fog, smoke, and other gases at bay. Small or smaller flying creatures or objects can't pass through the wall. Loose, lightweight materials brought into the wall fly upward. Arrows, bolts, and other ordinary projectiles launched at targets behind the wall are deflected upward and automatically miss. (Boulders hurled by giants or siege engines, and similar projectiles, are unaffected.) Creatures in gaseous form can't pass through it."  
                ],  
                "range": "120 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A tiny fan and a feather of exotic origin.",  
                "ritual": false,  
                "duration": "Up to 1 minute",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 3,  
                "damage": {  
                    "damage_type": {  
                        "index": "bludgeoning",  
                        "name": "Bludgeoning",  
                        "url": "/api/2014/damage-types/bludgeoning"  
                    },  
                    "damage_at_slot_level": {  
                        "3": "3d8"  
                    }  
                },  
                "dc": {  
                    "dc_type": {  
                        "index": "str",  
                        "name": "STR",  
                        "url": "/api/2014/ability-scores/str"  
                    },  
                    "dc_success": "half"  
                },  
                "area_of_effect": {  
                    "type": "line",  
                    "size": 50  
                },  
                "school": {  
                    "index": "evocation",  
                    "name": "Evocation",  
                    "url": "/api/2014/magic-schools/evocation"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "lore",  
                        "name": "Lore",  
                        "url": "/api/2014/subclasses/lore"  
                    }  
                ],  
                "url": "/api/2014/spells/wind-wall",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "conjure-woodland-beings",  
            "name": "Conjure Woodland Beings",  
            "level": 4,  
            "details": {  
                "index": "conjure-woodland-beings",  
                "name": "Conjure Woodland Beings",  
                "desc": [  
                    "You summon fey creatures that appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:",  
                    "- One fey creature of challenge rating 2 or lower",  
                    "- Two fey creatures of challenge rating 1 or lower",  
                    "- Four fey creatures of challenge rating 1/2 or lower",  
                    "- Eight fey creatures of challenge rating 1/4 or lower",  
                    "A summoned creature disappears when it drops to 0 hit points or when the spell ends.",  
                    "The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which have their own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.",  
                    "The GM has the creatures' statistics."  
                ],  
                "higher_level": [  
                    "When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 6th-level slot and three times as many with an 8th-level slot."  
                ],  
                "range": "60 feet",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "One holly berry per creature summoned.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [],  
                "url": "/api/2014/spells/conjure-woodland-beings",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "freedom-of-movement",  
            "name": "Freedom of Movement",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "freedom-of-movement",  
                "name": "Freedom of Movement",  
                "desc": [  
                    "You touch a willing creature. For the duration, the target's movement is unaffected by difficult terrain, and spells and other magical effects can neither reduce the target's speed nor cause the target to be paralyzed or restrained.",  
                    "The target can also spend 5 feet of movement to automatically escape from nonmagical restraints, such as manacles or a creature that has it grappled. Finally, being underwater imposes no penalties on the target's movement or attacks."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A leather strap, bound around the arm or a similar appendage.",  
                "ritual": false,  
                "duration": "1 hour",  
                "concentration": false,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    },  
                    {  
                        "index": "devotion",  
                        "name": "Devotion",  
                        "url": "/api/2014/subclasses/devotion"  
                    }  
                ],  
                "url": "/api/2014/spells/freedom-of-movement",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "locate-creature",  
            "name": "Locate Creature",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "locate-creature",  
                "name": "Locate Creature",  
                "desc": [  
                    "Describe or name a creature that is familiar to you. You sense the direction to the creature's location, as long as that creature is within 1,000 feet of you. If the creature is moving, you know the direction of its movement.",  
                    "The spell can locate a specific creature known to you, or the nearest creature of a specific kind (such as a human or a unicorn), so long as you have seen such a creature up close--within 30 feet--at least once. If the creature you described or named is in a different form, such as being under the effects of a polymorph spell, this spell doesn't locate the creature.",  
                    "This spell can't locate a creature if running water at least 10 feet wide blocks a direct path between you and the creature."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "A bit of fur from a bloodhound.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "bard",  
                        "name": "Bard",  
                        "url": "/api/2014/classes/bard"  
                    },  
                    {  
                        "index": "cleric",  
                        "name": "Cleric",  
                        "url": "/api/2014/classes/cleric"  
                    },  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "paladin",  
                        "name": "Paladin",  
                        "url": "/api/2014/classes/paladin"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/locate-creature",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "stoneskin",  
            "name": "Stoneskin",  
            "level": 4,  
            "details": {  
                "higher_level": [],  
                "index": "stoneskin",  
                "name": "Stoneskin",  
                "desc": [  
                    "This spell turns the flesh of a willing creature you touch as hard as stone. Until the spell ends, the target has resistance to nonmagical bludgeoning, piercing, and slashing damage."  
                ],  
                "range": "Touch",  
                "components": [  
                    "V",  
                    "S",  
                    "M"  
                ],  
                "material": "Diamond dust worth 100 gp, which the spell consumes.",  
                "ritual": false,  
                "duration": "Up to 1 hour",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 4,  
                "school": {  
                    "index": "abjuration",  
                    "name": "Abjuration",  
                    "url": "/api/2014/magic-schools/abjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    {  
                        "index": "sorcerer",  
                        "name": "Sorcerer",  
                        "url": "/api/2014/classes/sorcerer"  
                    },  
                    {  
                        "index": "wizard",  
                        "name": "Wizard",  
                        "url": "/api/2014/classes/wizard"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/stoneskin",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "commune-with-nature",  
            "name": "Commune With Nature",  
            "level": 5,  
            "details": {  
                "higher_level": [],  
                "index": "commune-with-nature",  
                "name": "Commune With Nature",  
                "desc": [  
                    "You briefly become one with nature and gain knowledge of the surrounding territory. In the outdoors, the spell gives you knowledge of the land within 3 miles of you. In caves and other natural underground settings, the radius is limited to 300 feet. The spell doesn't function where nature has been replaced by construction, such as in dungeons and towns.",  
                    "You instantly gain knowledge of up to three facts of your choice about any of the following subjects as they relate to the area:",  
                    "- terrain and bodies of water",  
                    "- prevalent plants, minerals, animals, or peoples",  
                    "- powerful celestials, fey, fiends, elementals, or undead",  
                    "- influence from other planes of existence",  
                    "- buildings",  
                    "For example, you could determine the location of powerful undead in the area, the location of major sources of safe drinking water, and the location of any nearby towns."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": true,  
                "duration": "Instantaneous",  
                "concentration": false,  
                "casting_time": "1 minute",  
                "level": 5,  
                "school": {  
                    "index": "divination",  
                    "name": "Divination",  
                    "url": "/api/2014/magic-schools/divination"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/commune-with-nature",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        },  
        {  
            "index": "tree-stride",  
            "name": "Tree Stride",  
            "level": 5,  
            "details": {  
                "higher_level": [],  
                "index": "tree-stride",  
                "name": "Tree Stride",  
                "desc": [  
                    "You gain the ability to enter a tree and move from inside it to inside another tree of the same kind within 500 feet. Both trees must be living and at least the same size as you. You must use 5 feet of movement to enter a tree. You instantly know the location of all other trees of the same kind within 500 feet and, as part of the move used to enter the tree, can either pass into one of those trees or step out of the tree you're in. You appear in a spot of your choice within 5 feet of the destination tree, using another 5 feet of movement. If you have no movement left, you appear within 5 feet of the tree you entered.",  
                    "You can use this transportation ability once per round for the duration. You must end each turn outside a tree."  
                ],  
                "range": "Self",  
                "components": [  
                    "V",  
                    "S"  
                ],  
                "ritual": false,  
                "duration": "Up to 1 minute",  
                "concentration": true,  
                "casting_time": "1 action",  
                "level": 5,  
                "school": {  
                    "index": "conjuration",  
                    "name": "Conjuration",  
                    "url": "/api/2014/magic-schools/conjuration"  
                },  
                "classes": [  
                    {  
                        "index": "druid",  
                        "name": "Druid",  
                        "url": "/api/2014/classes/druid"  
                    },  
                    {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    }  
                ],  
                "subclasses": [  
                    {  
                        "index": "land",  
                        "name": "Land",  
                        "url": "/api/2014/subclasses/land"  
                    }  
                ],  
                "url": "/api/2014/spells/tree-stride",  
                "updated_at": "2025-04-08T21:14:16.147Z"  
            }  
        }  
    ]  
]  
"""  
  
sublcass_data:  
"""  
[  
    [  
        {  
            "index": "hunter",  
            "class": {  
                "index": "ranger",  
                "name": "Ranger",  
                "url": "/api/2014/classes/ranger"  
            },  
            "name": "Hunter",  
            "subclass_flavor": "Ranger Archetype",  
            "desc": [  
                "Emulating the Hunter archetype means accepting your place as a bulwark between civilization and the terrors of the wilderness. As you walk the Hunter's path, you learn specialized techniques for fighting the threats you face, from rampaging ogres and hordes of orcs to towering giants and terrifying dragons."  
            ],  
            "subclass_levels": [  
                {  
                    "level": 3,  
                    "features": [  
                        {  
                            "index": "hunters-prey",  
                            "name": "Hunter's Prey",  
                            "details": {  
                                "index": "hunters-prey",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Hunter's Prey",  
                                "level": 3,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 3rd level, you gain one of the following features of your choice.",  
                                    "Colossus Slayer",  
                                    "Giant Killer",  
                                    "Horde Breaker"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-colossus-slayer",  
                                                        "name": "Hunter's Prey: Colossus Slayer",  
                                                        "url": "/api/2014/features/hunters-prey-colossus-slayer"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-giant-killer",  
                                                        "name": "Hunter's Prey: Giant Killer",  
                                                        "url": "/api/2014/features/hunters-prey-giant-killer"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "hunters-prey-horde-breaker",  
                                                        "name": "Hunter's Prey: Horde Breaker",  
                                                        "url": "/api/2014/features/hunters-prey-horde-breaker"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/hunters-prey",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/3",  
                    "index": "hunter-3",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 7,  
                    "features": [  
                        {  
                            "index": "defensive-tactics",  
                            "name": "Defensive Tactics",  
                            "details": {  
                                "index": "defensive-tactics",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Defensive Tactics",  
                                "level": 7,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 7th level, you gain one of the following features of your choice.",  
                                    "Escape the Horde",  
                                    "Multiattack Defense",  
                                    "Steel Will"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-escape-the-horde",  
                                                        "name": "Defensive Tactics: Escape the Horde",  
                                                        "url": "/api/2014/features/defensive-tactics-escape-the-horde"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-multiattack-defense",  
                                                        "name": "Defensive Tactics: Multiattack Defense",  
                                                        "url": "/api/2014/features/defensive-tactics-multiattack-defense"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "defensive-tactics-steel-will",  
                                                        "name": "Defensive Tactics: Steel Will",  
                                                        "url": "/api/2014/features/defensive-tactics-steel-will"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/defensive-tactics",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/7",  
                    "index": "hunter-7",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 11,  
                    "features": [  
                        {  
                            "index": "multiattack",  
                            "name": "Multiattack",  
                            "details": {  
                                "index": "multiattack",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Multiattack",  
                                "level": 11,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 11th level, you gain one of the following features of your choice.",  
                                    "Volley",  
                                    "Whirlwind Attack"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "multiattack-volley",  
                                                        "name": "Multiattack: Volley",  
                                                        "url": "/api/2014/features/multiattack-volley"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "multiattack-whirlwind-attack",  
                                                        "name": "Multiattack: Whirlwind Attack",  
                                                        "url": "/api/2014/features/multiattack-whirlwind-attack"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/multiattack",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/11",  
                    "index": "hunter-11",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                },  
                {  
                    "level": 15,  
                    "features": [  
                        {  
                            "index": "superior-hunters-defense",  
                            "name": "Superior Hunter's Defense",  
                            "details": {  
                                "index": "superior-hunters-defense",  
                                "class": {  
                                    "index": "ranger",  
                                    "name": "Ranger",  
                                    "url": "/api/2014/classes/ranger"  
                                },  
                                "subclass": {  
                                    "index": "hunter",  
                                    "name": "Hunter",  
                                    "url": "/api/2014/subclasses/hunter"  
                                },  
                                "name": "Superior Hunter's Defense",  
                                "level": 15,  
                                "prerequisites": [],  
                                "desc": [  
                                    "At 15th level, you gain one of the following features of your choice.",  
                                    "Evasion",  
                                    "Stand Against the Tide",  
                                    "Uncanny Dodge"  
                                ],  
                                "feature_specific": {  
                                    "subfeature_options": {  
                                        "choose": 1,  
                                        "type": "feature",  
                                        "from": {  
                                            "option_set_type": "options_array",  
                                            "options": [  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-evasion",  
                                                        "name": "Superior Hunter's Defense: Evasion",  
                                                        "url": "/api/2014/features/superior-hunters-defense-evasion"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-stand-against-the-tide",  
                                                        "name": "Superior Hunter's Defense: Stand Against the Tide",  
                                                        "url": "/api/2014/features/superior-hunters-defense-stand-against-the-tide"  
                                                    }  
                                                },  
                                                {  
                                                    "option_type": "reference",  
                                                    "item": {  
                                                        "index": "superior-hunters-defense-uncanny-dodge",  
                                                        "name": "Superior Hunter's Defense: Uncanny Dodge",  
                                                        "url": "/api/2014/features/superior-hunters-defense-uncanny-dodge"  
                                                    }  
                                                }  
                                            ]  
                                        }  
                                    },  
                                    "invocations": []  
                                },  
                                "url": "/api/2014/features/superior-hunters-defense",  
                                "updated_at": "2025-04-08T21:14:01.855Z"  
                            }  
                        }  
                    ],  
                    "class": {  
                        "index": "ranger",  
                        "name": "Ranger",  
                        "url": "/api/2014/classes/ranger"  
                    },  
                    "subclass": {  
                        "index": "hunter",  
                        "name": "Hunter",  
                        "url": "/api/2014/subclasses/hunter"  
                    },  
                    "url": "/api/2014/subclasses/hunter/levels/15",  
                    "index": "hunter-15",  
                    "updated_at": "2025-04-08T21:14:04.101Z"  
                }  
            ],  
            "url": "/api/2014/subclasses/hunter",  
            "updated_at": "2025-04-08T21:14:17.800Z",  
            "spells": []  
        }  
    ]  
]  
"""  
'''
Hier noch mal das format in dem du die antwort zurück geben sollst.

Rückgabeformat: text  
Verbotene formate: Markdwon  
vorboteneer inhalt: ```json, ```
```
#### Character:
```
{
  "name": "Robin Hood",
  "level": 10,
  "hit_points": 85,
  "proficiency_bonus": 4,
  "subclass": "Hunter",
  "attributes": {
    "strength": 10,
    "dexterity": 18,
    "constitution": 14,
    "intelligence": 12,
    "wisdom": 16,
    "charisma": 13
  },
  "attribute_proficiencys": {
    "strength": false,
    "dexterity": true,
    "constitution": false,
    "intelligence": false,
    "wisdom": true,
    "charisma": false
  },
  "saving_throws": {
    "strength": 0,
    "dexterity": 8,
    "constitution": 2,
    "intelligence": 1,
    "wisdom": 7,
    "charisma": 1
  },
  "armor_class": 16,
  "attack_bonus": 8,
  "spellcasting": {
    "spellcasting_bonus": 3,
    "spellcasting_dc": 15,
    "spellcasting_attack_bonus": 7,
    "cantrips_known": 0,
    "spells_prepared": 6,
    "spell_slots": {
      "1st": 4,
      "2nd": 3,
      "3rd": 2,
      "4th": 0,
      "5th": 0
    },
    "known_spells": {
      "1st_level": ["Hunter's Mark", "Speak with Animals"],
      "2nd_level": ["Pass Without Trace", "Spike Growth"],
      "3rd_level": ["Conjure Animals", "Lightning Arrow"]
    }
  },
  "features": [
    "Favored Enemy (2 types)",
    "Natural Explorer (3 terrains)",
    "Fighting Style: Archery",
    "Spellcasting",
    "Primeval Awareness",
    "Hunter's Prey: Colossus Slayer",
    "Extra Attack",
    "Land's Stride",
    "Hide in Plain Sight"
  ],
  "special_abilities_and_traits": [
    "Expert Tracker",
    "Stealth Master",
    "Forest Camouflage",
    "Robin Hood’s Code: Steals from the rich, gives to the poor"
  ],
  "languages": ["Common", "Elvish", "Thieves' Cant"],
  "equipment": [
    "Longbow and 20 arrows",
    "Shortsword",
    "Leather armor",
    "Explorer’s pack",
    "Cloak of Elvenkind"
  ],
  "additional_equipment": [
    "Thieves’ tools",
    "Rope (50 feet)",
    "Signal whistle",
    "Map of local area",
    "Pouch with 15 GP"
  ],
  "money": {
    "platinum": 0,
    "gold": 15,
    "electrum": 0,
    "silver": 20,
    "copper": 50
  },
  "weapons": {
    "longbow": {
      "damage": "1d8 piercing",
      "attack_bonus": 8,
      "properties": ["Ammunition", "Heavy", "Two-Handed"],
      "range": "150/600 ft"
    },
    "shortsword": {
      "damage": "1d6 piercing",
      "attack_bonus": 6,
      "properties": ["Finesse", "Light"]
    }
  }
}


```
