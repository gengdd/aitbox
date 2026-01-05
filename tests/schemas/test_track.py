#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File        : test_track
Project     : aitbox
Author      : gdd
Created     : 2026/1/5
Description :
"""
import pandas as pd
import polars as pl

from aitbox.schemas.track import CoordinateType, TrackPd, Track, TrackPl, set_track_backend


def test_track_pd():
    """ """
    track = Track(
        data=pd.DataFrame(
            {
                "time": [0, 1, 2],
                "x": [0.0, 1.0, 2.0],
                "y": [0.0, 1.0, 2.0],
            }
        ),
        coord_type=CoordinateType.EUCLIDEAN,
    )

    assert isinstance(track, TrackPd)
    assert track.coord_type == CoordinateType.EUCLIDEAN


def test_track_pl():
    """ """
    set_track_backend("polars")

    track = Track(
        data=pl.DataFrame(
            {
                "time": [0, 1, 2],
                "x": [0.0, 1.0, 2.0],
                "y": [0.0, 1.0, 2.0],
            }
        ),
        coord_type=CoordinateType.EUCLIDEAN,
    )

    assert isinstance(track, TrackPl)
    assert track.coord_type == CoordinateType.EUCLIDEAN
