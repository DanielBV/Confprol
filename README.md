# Confprol

Confprol is a dynamically typed language that tweaks common programming concepts and behaviours to make them more confusing. 
It is parsed and executed with a python interpreter.

### Prerequisites

* Python 3.7
* antlr4-python3-runtime library

```buildoutcfg
pip install antlr4-python3-runtime
```


### Running a confprol program
```
cd src
python main.py programFile
```

#### Examples:
```
python main.py ./examples/GoodbyeWorld.conf
```
```
python main.py ./examples/Factorial.conf
```
```
python main.py ./examples/Context.conf
```
### Running the tests


```
pytest .\tests\
```

### Documentation
[https://github.com/DanielBV/Confprol/wiki](https://github.com/DanielBV/Confprol/wiki)




### Generate the ANTLR4 Parser (optional)

#### Installing ANTLR4
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

### Generate the Parser:
```
antlr4 -Dlanguage=Python3 confprol.g4 -o ./src/generated_antlr4/  -visitor -no-listener
```

