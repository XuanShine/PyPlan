#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3

from cx_Freeze import setup, Executable

setup(
    name = "pyPlan",
    version = "1",
    description = "Organiser les plannings du doodle",
    executables = [Executable("pyPlan.py")],
)
