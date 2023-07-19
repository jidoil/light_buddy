# -*- coding: utf-8 -*-

name = "vfx_pipeline_api"

version = "1.0.0"

authors = [
        "jidoil"
]

requires = [
        "python"
        ]

format_version = 1

description = \
        """
        Python-based vfx pipeline api pacakge
        """

variants = [
        ['platform-linux', 'python']
]

def commands():
    env.PYTHONPATH.append("{root}/python"),
    env.PYTHONPATH.prepend("{root}/python")
