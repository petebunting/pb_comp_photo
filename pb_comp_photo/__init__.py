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
# Purpose:  Version and General Info
#
# Author: Pete Bunting
# Email: petebunting@mac.com
# Date: 08/04/2023
# Version: 1.0
#
# History:
# Version 1.0 - Created.
##########################################################################

from distutils.version import LooseVersion

PB_COMP_PHOTO_VERSION_MAJOR = 0
PB_COMP_PHOTO_VERSION_MINOR = 0
PB_COMP_PHOTO_VERSION_PATCH = 1

PB_COMP_PHOTO_VERSION = (
    f"{PB_COMP_PHOTO_VERSION_MAJOR}."
    f"{PB_COMP_PHOTO_VERSION_MINOR}."
    f"{PB_COMP_PHOTO_VERSION_PATCH}"
)
PB_COMP_PHOTO_VERSION_OBJ = LooseVersion(PB_COMP_PHOTO_VERSION)
__version__ = PB_COMP_PHOTO_VERSION

PB_COMP_PHOTO_COPYRIGHT_YEAR = "2023"
PB_COMP_PHOTO_COPYRIGHT_NAMES = "Pete Bunting"

PBCP_HDR_METHODS = ["DEBEVEC", "MERTENS", "ROBERTSON"]
