#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File        : track
Project     : aitbox
Author      : gdd
Created     : 2026/1/5
Description :
"""
from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple

import pandas as pd
import polars as pl


class CoordinateType(Enum):
    """ """

    EUCLIDEAN = auto()
    WGS84 = auto()
    BD09 = auto()


@dataclass(frozen=True)
class CoordinateSpec:
    columns: Tuple[str, str, str, str]
    unit: str
    description: str
    epsg: int | None = None


COORDINATE_SPECS = {
    CoordinateType.EUCLIDEAN: CoordinateSpec(
        columns=("track_id", "x", "y", "time"),
        unit="meter",
        description="Local 2D Cartesian coordinate",
        epsg=None,
    ),
    CoordinateType.WGS84: CoordinateSpec(
        columns=("track_id", "lon", "lat", "time"),
        unit="degree",
        description="WGS84 geographic coordinate",
        epsg=4326,
    ),
    CoordinateType.BD09: CoordinateSpec(
        columns=("track_id", "lon", "lat", "time"),
        unit="degree",
        description="Baidu BD09 coordinate",
        epsg=None,
    ),
}


@dataclass
class TrackBase:
    """ """
    data: pd.DataFrame | pl.DataFrame
    coord_type: CoordinateType
    time_format: str | None = None

    @abstractmethod
    def __post_init__(self):
        """ """
        ...

    @property
    def required_columns(self) -> tuple:
        """ """
        return COORDINATE_SPECS[self.coord_type].columns

    @property
    def coordinate_specs(self) -> CoordinateSpec:
        """ """
        return COORDINATE_SPECS[self.coord_type]


@dataclass
class TrackPd(TrackBase):
    """ """

    def __post_init__(self):
        pass


@dataclass
class TrackPl(TrackBase):
    """ """

    def __post_init__(self):
        self._validate_columns()

    def _validate_columns(self):
        """ """
        required = set(self.required_columns)
        existing = set(self.data.columns)

        missing = required - existing
        if missing:
            raise ValueError(
                f"Missing required columns: {sorted(missing)}"
            )


TRACK_BACKEND = {
    "pandas": TrackPd,
    "polars": TrackPl,
}
BACKEND = "pandas"


def set_track_backend(backend):
    """ """
    global BACKEND
    BACKEND = backend


def Track(data, coord_type=None):
    """ """
    global BACKEND, TRACK_BACKEND
    if coord_type is None:
        coord_type = CoordinateType.EUCLIDEAN
    return TRACK_BACKEND[BACKEND](data, coord_type)
