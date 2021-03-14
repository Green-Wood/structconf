from structconf import StructConf
from pydantic.error_wrappers import ValidationError
import pytest


class AConf(StructConf):
    a: int = 1


class BConf(StructConf):
    b: int = 2


class ComplexConf(StructConf):
    aconf: AConf = AConf()
    bconf: BConf = BConf()


prefix = "./tests/yaml/complex"


def test_complex():
    conf = ComplexConf.load(f"{prefix}/complex.yaml")
    assert conf.aconf.a == 10
    assert conf.bconf.b == 100


def test_default():
    conf = ComplexConf.load(f"{prefix}/complex_default.yaml")
    assert conf.aconf.a == 1
    assert conf.bconf.b == 2


def test_error():
    with pytest.raises(ValidationError):
        conf = ComplexConf.load(f"{prefix}/complex_error.yaml")
