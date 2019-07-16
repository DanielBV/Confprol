# Confprol

Confprol is a programming language interpreted with a python program. The language will be designed to be as confusing as possible by tweaking common
programming keywords and changing expected behaviours.

Right now the syntax isn't twisted to facilitate the development of the core language.  


### Prerequisites

* Python 3.7
* ANTLR4


### Installing ANTLR4
* Ubuntu
```
sudo apt-get install antlr4
```
* Fedora
```
sudo dnf --refresh install antlr4
```

* Other:
https://www.antlr.org/download.html

### Generate the ANTLR4 Parser
```
antlr4 -Dlanguage=Python3 confprol.g4 -o ./generated_antlr4/  -visitor -no-listener
```

### Running a confprol program
```
cd src
python main.py programFile
```

### Running the tests


```
pytest .\tests\
```
