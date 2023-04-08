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
# Purpose:  Functions for HDR photography
#
# Author: Pete Bunting
# Email: petebunting@mac.com
# Date: 08/04/2023
# Version: 1.0
#
# History:
# Version 1.0 - Created.
##########################################################################

import cv2
import numpy

def create_hdr_debevec_img(cv_img_objs, exposure_times, output_img, gamma=1.8):
    """

    :param cv_img_objs:
    :param exposure_times:
    :param output_img:
    :param gamma:
    :return:
    """
    exposure_times_arr = numpy.array(exposure_times)

    merge_debevec = cv2.createMergeDebevec()
    hdr_debevec = merge_debevec.process(cv_img_objs, times=exposure_times_arr.copy())

    # Tonemap HDR image
    tone_map = cv2.createTonemap(gamma=gamma)
    res_debevec = tone_map.process(hdr_debevec.copy())

    res_debevec_8bit = numpy.clip(res_debevec * 255, 0, 255).astype('uint8')
    cv2.imwrite(output_img, res_debevec_8bit)


def create_hdr_robertson_img(cv_img_objs, exposure_times, output_img, gamma=1.8):
    exposure_times_arr = numpy.array(exposure_times)

    merge_robertson = cv2.createMergeRobertson()
    hdr_robertson = merge_robertson.process(cv_img_objs, times=exposure_times_arr.copy())

    # Tonemap HDR image
    tone_map = cv2.createTonemap(gamma=gamma)
    res_robertson = tone_map.process(hdr_robertson.copy())

    res_robertson_8bit = numpy.clip(res_robertson * 255, 0, 255).astype('uint8')
    cv2.imwrite(output_img, res_robertson_8bit)

def create_hdr_mertens_img(cv_img_objs, output_img):
    merge_mertens = cv2.createMergeMertens()
    res_mertens = merge_mertens.process(cv_img_objs)

    res_mertens_8bit = numpy.clip(res_mertens*255, 0, 255).astype('uint8')
    cv2.imwrite(output_img, res_mertens_8bit)
