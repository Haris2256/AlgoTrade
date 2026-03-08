from abc import ABC
from dataclasses import dataclass


class Action(ABC):
    """An action taken by a Bot"""
    pass

@dataclass
class Buy(Action):
    """Buy a security"""
    symbol: str
    amount: float

@dataclass
class Sell(Action):
    """Sell a security"""
    symbol: str
    amount: float