from typing import Type, TypeVar
from pydantic import BaseModel
import yaml

T = TypeVar("T")


class StructConf(BaseModel):
    @classmethod
    def load(cls: Type[T], path: str) -> T:
        """load yaml file to structured class

        Parameters
        ----------
        cls : Type[T]
            structured class type
        path : str
            path to yaml file

        Returns
        -------
        T
            structured class
        """
        with open(path, 'r') as f:
            conf = yaml.safe_load(f)
        if conf is not None:
            model = cls(**conf)
        else:
            model = cls()
        return model
