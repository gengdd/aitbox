#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File        : track
Project     : aitbox
Author      : gdd
Created     : 2026/1/5
Description :
"""

from dataclasses import dataclass
from enum import Enum, auto


class CoordinateType(Enum):
    """ """

    EUCLIDEAN = auto()
    WGS84 = auto()
    BD09 = auto()


@dataclass
class Track:
    """ """
    pass
