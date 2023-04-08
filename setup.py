#!/usr/bin/env python
##########################################################################
# Copyright 2023 Pete Bunting
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##########################################################################
#
# Purpose:  Module installation
#
# Author: Pete Bunting
# Email: petebunting@mac.com
# Date: 08/04/2023
# Version: 1.0
#
# History:
# Version 1.0 - Created.
##########################################################################

from setuptools import setup
import glob

import pb_comp_photo

setup(
    name="pb_comp_photo",
    version=pb_comp_photo.PB_COMP_PHOTO_VERSION,
    description="PBs Computational Photography Modules",
    author="Pete Bunting",
    author_email="petebunting@mac.com",
    scripts=glob.glob("bin/*.py"),
    packages=["pb_comp_photo"],
    license="LICENSE",
    url="https://github.com/petebunting/pb_comp_photo",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Photographers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
