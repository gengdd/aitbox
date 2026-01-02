#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File        : config.py
Project     : aitbox
Author      : gdd
Created     : 2025-12-27
Description :
"""
import pytest

from aitbox.config.config import set_yaml_path
from tests.config.machine import GPUInfo


@pytest.fixture(scope="function")
def config():
    """
    每个 test 前都会重新加载 yaml, 避免全局状态互相污染
    """
    return set_yaml_path("tests/config/machine.yaml")


def test_config_basic(config):
    """
    测试 yaml 是否被正确加载成 config 对象
    """
    assert config is not None

    assert config.name is not None

    assert config.gpu is not None
    assert config.gpu.name is not None

    assert config.cpu is not None
    assert config.cpu.name is not None
    assert isinstance(config.cpu.num, int)


def test_gpu_info_from_yaml(config):
    """
    不传参时, GPUInfo 应该从 yaml 读取配置
    """
    gpu = GPUInfo()

    assert gpu.name == config.gpu.name
    assert isinstance(gpu.cuda, bool)


def test_gpu_info_init_override(config):
    """
    传 init 参数时，应优先使用构造参数，
    而不是被 yaml 覆盖
    """
    gpu = GPUInfo("ascend")
    assert gpu.name == "ascend"
