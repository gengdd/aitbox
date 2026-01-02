#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File        : machine.py
Project     : aitbox
Author      : gdd
Created     : 2026-01-02
Description :
"""

from dataclasses import dataclass

from aitbox.config.base import ConfigBase


@dataclass(init=False)
class GPUInfo(ConfigBase):
    """ """

    name: str
    cuda: bool = True


@dataclass(init=False)
class CPUInfo(ConfigBase):
    """ """

    name: str = "intel"
    num: int = 1


@dataclass(init=False)
class Machine(ConfigBase):
    """ """

    gpu: GPUInfo
    cpu: CPUInfo
    name: str = "HP"


if __name__ == "__main__":
    pass
