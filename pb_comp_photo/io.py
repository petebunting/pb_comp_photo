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
# Purpose:  Module functions for I/O
#
# Author: Pete Bunting
# Email: petebunting@mac.com
# Date: 08/04/2023
# Version: 1.0
#
# History:
# Version 1.0 - Created.
##########################################################################

import os

import exifread


def read_img_opencv(input_imgs: list[str], read_meta: bool = True):
    """

    :param input_imgs:
    :param read_meta:
    :return:
    """
    import cv2

    img_obj_lst = list()
    exif_table = list()
    for img_file in input_imgs:
        print(f"Reading {img_file}...")
        if not os.path.exists(img_file):
            raise Exception(f"Image file does not exist - check path: {img_file}")
        img_obj_lst.append(cv2.imread(img_file, cv2.IMREAD_COLOR))

        if read_meta:
            lcl_exif_table = dict()
            lcl_exif_table["image file"] = img_file
            exif_img_obj = open(img_file, "rb")
            tags = exifread.process_file(exif_img_obj)
            for tag in tags.keys():
                if tag not in (
                    "JPEGThumbnail",
                    "TIFFThumbnail",
                    "Filename",
                    "EXIF MakerNote",
                ):
                    if "ISOSpeedRatings" in tag:
                        lcl_exif_table["ISO"] = int(f"{tags[tag]}")
                    elif "ExposureTime" in tag:
                        lcl_exif_table["ExposureTime"] = eval(f"{tags[tag]}")
                    elif "FNumber" in tag:
                        lcl_exif_table["FNumber"] = eval(f"{tags[tag]}")
                    elif "Image DateTime" in tag:
                        lcl_exif_table["DateTime"] = f"{tags[tag]}"
            exif_table.append(lcl_exif_table)

    return img_obj_lst, exif_table
