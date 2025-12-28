#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File        : log.py
Project     : aitbox
Author      : gdd
Created     : 2025-12-28
Description :
"""

import sys
import loguru


class Log:
    """ """

    logger = loguru.logger
    format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{file}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    )
    level = "INFO"
    logger.remove()
    logger.add(sys.stdout, format=format, level=level)

    @classmethod
    def _log(cls, level, message, *args, depth=2, **kwargs):
        """ """
        cls.logger.opt(depth=depth).log(level, message, *args, **kwargs)

    @classmethod
    def info(cls, message, *args, **kwargs):
        """ """
        cls._log("INFO", message, *args, **kwargs)

    @classmethod
    def warning(cls, message, *args, **kwargs):
        """ """
        cls._log("WARNING", message, *args, **kwargs)

    @classmethod
    def error(cls, message, *args, **kwargs):
        """ """
        cls._log("ERROR", message, *args, **kwargs)

    @classmethod
    def debug(cls, message, *args, **kwargs):
        """ """
        cls._log("DEBUG", message, *args, **kwargs)

    @classmethod
    def exception(cls, message, *args, **kwargs):
        """ """
        cls.logger.opt(depth=2).exception(message, *args, **kwargs)

    @classmethod
    def remove(cls):
        """ """
        cls.logger.remove()

    @classmethod
    def add_filename(
        cls,
        filename: str,
        level: str = "INFO",
        rotation: str = "10 MB",
        retention: str = "7 days",
        compression: str = "zip",
        enqueue: bool = True,
    ):
        """ """
        return cls.logger.add(
            filename,
            level=level,
            format=cls.format,
            rotation=rotation,
            retention=retention,
            compression=compression,
            enqueue=enqueue,
            colorize=False,
        )


class Logger:
    """"""

    def __init__(
        self,
        name: str | None = None,
        level: str = "INFO",
        format: str | None = None,
        stdout: bool = True,
    ):
        """ """
        self.level = level
        self.format = format or (
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{file}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        )

        self.logger = loguru.logger.bind(name=name)

        if stdout:
            self.logger.add(
                sys.stdout,
                level=self.level,
                format=self.format,
                colorize=True,
            )

    def _log(self, level, message, *args, depth=2, **kwargs):
        """ """
        self.logger.opt(depth=depth).log(level, message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        """ """
        self._log("INFO", message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        """ """
        self._log("WARNING", message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        """ """
        self._log("ERROR", message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        """ """
        self._log("DEBUG", message, *args, **kwargs)

    def exception(self, message, *args, **kwargs):
        """ """
        self.logger.opt(depth=2).exception(message, *args, **kwargs)

    def remove(self):
        """"""
        self.logger.remove()

    def add_filename(
        self,
        filename: str,
        level: str | None = None,
        rotation: str = "10 MB",
        retention: str = "7 days",
        compression: str = "zip",
        enqueue: bool = True,
    ):
        """"""
        return self.logger.add(
            filename,
            level=level or self.level,
            format=self.format,
            rotation=rotation,
            retention=retention,
            compression=compression,
            enqueue=enqueue,
            colorize=False,
        )


if __name__ == "__main__":
    pass
