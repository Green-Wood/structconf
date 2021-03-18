# StructConf

[![PyPI](https://img.shields.io/pypi/v/structconf?color=blue)](https://pypi.org/project/structconf/)

Config your project with yaml and validation.

Enjoy wirting your code with IDEs python **type hint**

## Simple Usage

1. Define your configuration class, with attribute type and default value

```python
from structconf import StructConf

class SimpleConf(StructConf):
    a: int = 1
    b: str = "b"
```

2. write your yaml config file (e.g simple.yaml)

```yaml
a: 2
b: "123"
```

3. load yaml config file to your struct class

```python
conf = SimpleConf.load("simple.yaml")
assert conf.a == 2
assert conf.b == "123"
```



## Advanced Usage

StructConf use [pydantic](https://github.com/samuelcolvin/pydantic) to validate your yaml and python class. So we can use recursive modelto build complex configuration.

```python
from structconf import StructConf

class AConf(StructConf):
    a: int = 1


class BConf(StructConf):
    b: int = 2


class ComplexConf(StructConf):
    aconf: AConf = AConf()
    bconf: BConf = BConf()
```