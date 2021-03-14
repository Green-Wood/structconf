from structconf import StructConf
import pytest
from pydantic.error_wrappers import ValidationError


class SimpleConf(StructConf):
    a: int = 1
    b: str = "b"


prefix = './tests/yaml/simple'


def test_simple():
    conf = SimpleConf.load(f'{prefix}/simple.yaml')
    assert conf.a == 2
    assert conf.b == '123'


def test_simple_default():
    conf = SimpleConf.load(f'{prefix}/simple_default.yaml')
    assert conf.a == 2
    assert conf.b == "b"


def test_simple_error():
    with pytest.raises(ValidationError):
        conf = SimpleConf.load(f'{prefix}/simple_error.yaml')
