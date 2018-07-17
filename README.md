# Oracle Touch the Cloud Project

## Project Overview
I am an avid Pokemon player and wanted to create a project that would help me and other Pokemon fans in their Pokemon battles and adventures. The program benefits from the cloud as clients and customers can receive fast information when playing in high-action fast-paced competitions across the globe. The project is split into two parts: a Virtual Pokedex that performs queries and a personal Pokemon database containing a player's favorite Pokemon.

## Part 1: Virtual Pokedex

Using a Kaggle Pokemon dataset csv file, I wanted to create a personal pokedex that performed simple and complex queries. 

**Figure 1. Pokemon Dataset Column and Associated Attribute**

| Column Number     | Attribute  | Type | 
| :-------------: |:-------------:| :-------------: |
| 0  | # | int |
| 1 | Name  |  string |
| 2 | Type 1| string |
|3 | Type 2| string |
|4 | Total| int |
|5 | HP| int |
|6 | Attack| int |
|7 | Defense| int |
|8 | Special Atk| int|
|9 | Special Def| int|
|10| Speed| int|
|11| Generation| int |
|12| Legendary| boolean |

A Pokemon's type(s) and stats are very important to the gameplay and often determine victory. There are 18 different Pokemon types, and (for the purpose of this demo) each can be super effective, normally effective, or not effective against another type. When Pokemon have multiple types type matchup values are multiplied against each other using the type matrix.

### Functions

Users could use the pokedex to perform the following queries: 
* **type_search** - returns a list Pokemon of a given type
* **stat_search** - returns a set of Pokemon with values greater than or equal to the given value for any given stat
* **legend_search** - returns a list of legendary Pokemon
* **pokemon_search** - given a Pokemon name, returns all known statistics and information
* **number_search** - given a number entry, returns all known statistics and information
* **image_search** - given a Pokemon name, opens corresponding png sprite image
* **stronger_type_search** - returns a list of types that are super effective against a given pokemon
* **stronger_stat_search** - returns a list of Pokemon that are stronger than a given Pokemon based on stats
* **weaker_stat_search** - returns a list of Pokemon that are weaker than a given Pokemon based on stats
* **stronger_pokemon_search** - returns a list of Pokemon that are stronger than a given Pokemon based on stats AND type matchup

## Part 2: Personal Pokemon PC

In the Pokemon RPG video game, a trainer's Pokemon are placed in storage containers called PCs. I wanted to create the same thing using an Oracle cloud database application container using Python. 

Using Python, I created a database where users could add, update, get, and delete their Pokemon. 

Each Pokemon was an entry with the following attributes: 
	NAME VARCHAR(255),
    LEVEL VARCHAR(255),
	TYPE1 VARCHAR(255),
	TYPE2 VARCHAR(255),
	ABILITY VARCHAR(255),
	MOVE VARCHAR(255)
with the name as the primary key.

Using curl GET, POST, and DELETE methods, we could upload, view, update, and delete any Pokemon entry in the Cloud database.

## Challenges
The actual upload to the Oracle Cloud services did not work for either part 1 or part 2.
For part 1, while the test python applciation was able to run, I was not able to interpret the logfiles of the pokedex and was not sure how to troubleshoot from there. 

For part 2, I had originally tried to use PHP/MySQL for my database of trainers; however, there were several installation package issues particularly with NetBean and Laravel. Instead, I was able to translate and adjust into Python, an even simpler language to create data TABLES. While the Python methods and Oracle database initialization were successfully completed, I was not able to run the Python program in the Oracle Cloud. 

Ideally, I would've liked to use Oracle Analytics Cloud to make visualizations based off of my data inputs.

## Conclusions
This project was intended to show my technical skills particularly in database systems and data processing. Given more time, I would've loved to add more features and integration with the Oracle Cloud Services. I enjoyed programming this project as it is something I am passionate about. 

## References
[Oracle Python Tutorial](https://docs.oracle.com/en/cloud/paas/app-container-cloud/create-sample-python-applications.html)

[Pokemon Dataset](https://www.kaggle.com/abcsds/pokemon)



