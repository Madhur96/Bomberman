# BomberMan

Implementation of Bomberman game using OOP Principles without using pygame and curses library.


## Getting Started

To operate the game run 'python main.py' in the folder where the file is located ensuring other modules (bomber.py, bomb.py, enemy.py, suplement.py) are also there in same folder.


### Prerequisites

Things you need to install the software and instructions to install them:

* You should have python3 and pip3 installed:

First check if python3 is intstalled by using the command:

```
python3 -V
```

```
Output:
Python 3.5.3
```

If not installed then type the following:

```
sudo apt-get update
sudo apt-get -y update
```

* Instructions for installing pip

```
sudo apt-get install python3-pip
```

* You should have termcolor installed.

If not then type the following:

```
sudo pip3 install termcolor
```


## Controls

After starting the game you can move the character by :
| Keys          | Movement      |
| ------------- |:-------------:|
| W             | Move Up       |
| A             | Move Left     |
| S             | Move Down     |
| D             | Move Right    |

Press 'b' key in order to plant a bomb.


The enemies move randomly per frame or per second(which so comes first)
Kill enemies using bombs and increase your score.
A bomb has a potential to kill enemy as well as the bomberman.

Press 'q' key in order to quit.


## Instructions

Kill both enemies to win the game  (game quits after that)

You lose if you die twice (game quits after that)


## Running the Game

On running main.py file you will see a prompt like this :


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXBBBB                                                    ////                XX
XXBBBB                                                    ////                XX
XX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XX
XX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XX
XXEEEE                ////                    ////                            XX
XXEEEE                ////                    ////                            XX
XX    XXXX    XXXX    XXXX    XXXX////XXXX    XXXX    XXXX    XXXX////XXXX    XX
XX    XXXX    XXXX    XXXX    XXXX////XXXX    XXXX    XXXX    XXXX////XXXX    XX
XX    EEEE    ////                                                ////        XX
XX    EEEE    ////                                                ////        XX
XX////XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX////XX
XX////XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX////XX
XX            ////                                                            XX
XX            ////                                                            XX
XX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XX
XX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XX
XX    ////                                                                ////XX
XX    ////                                                                ////XX
XX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XX
XX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XX
XX            ////                                                            XX
XX            ////                                                            XX
XX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX////XX
XX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX////XX
XX                                            ////                    ////    XX
XX                                            ////                    ////    XX
XX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX////XXXX    XX
XX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX////XXXX    XX
XX////                                                                        XX
XX////                                                                        XX
XX    XXXX////XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XX
XX    XXXX////XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XX
XX                ////        ////                                            XX
XX                ////        ////                                            XX
XX    XXXX    XXXX    XXXX////XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XX
XX    XXXX    XXXX    XXXX////XXXX    XXXX    XXXX    XXXX    XXXX    XXXX    XX
XX                                                                            XX
XX                                                                            XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Lives :  2
score :  0


The character with 'B' sybomls is bomberman and will be in blue 
The character with 'E' symbols is the enemy and will be in red
The character with '/' symbols is the bricks and will be in yellow (can be destroyed by bomb)
The character with 'X' symbols is the walls and will be in white (cannot be destroyed by bomb)


## Built With

* [Python](https://www.python.org/)

## Authors

* **Anurag Mehta** - **20161016**

