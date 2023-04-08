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
# Purpose:  Utilities for module
#
# Author: Pete Bunting
# Email: petebunting@mac.com
# Date: 08/04/2023
# Version: 1.0
#
# History:
# Version 1.0 - Created.
##########################################################################

import math

def calc_ev(fnumber:float, exposure_time:float):
    """
    Calculate the exposure value (EV) for a given ISO based on the
    f-stop and shutter time.

    :param fnumber: the f-number for the photo
    :param exposure_time: the exposure time (secs) for the photo.
    :return: the exposure value (EV)

    """
    return math.log2((fnumber*fnumber)/exposure_time)


def calc_ev_iso100(fnumber:float, exposure_time:float, iso:float):
    """
    Calculate exposure value (EV) standardised to ISO 100 based
    on the f-stop, shutter time and ISO for the photo.

    :param fnumber: the f-number for the photo
    :param exposure_time: the exposure time (secs) for the photo.
    :param iso: the ISO for the photo.
    :return: exposure value (EV) normalised to ISO 100

    """
    ev = calc_ev(fnumber, exposure_time)
    return ev - math.log2(iso/100)

def calc_exposure_time(fnumber:float, ev:float):
    """
    Calculate an exposure time for a given exposure value (EV) and f-stop.

    :param fnumber: the f-stop used for the photo
    :param ev: the exposure value (EV) for a given ISO (i.e., 100)
    :return: exposure time in seconds

    """
    return (fnumber*fnumber) / math.pow(2, ev)
