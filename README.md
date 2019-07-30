# Confprol

Confprol is a dynamically typed language that tweaks common programming concepts and behaviours to make them more confusing. 
It is parsed and executed with a python interpreter.

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


### Documentation
[https://github.com/DanielBV/Confprol/wiki](https://github.com/DanielBV/Confprol/wiki)
