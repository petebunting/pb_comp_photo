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
# Purpose:  Command line tool to generate HDR photo
#
# Author: Pete Bunting
# Email: petebunting@mac.com
# Date: 08/04/2023
# Version: 1.0
#
# History:
# Version 1.0 - Created.
##########################################################################

import argparse
import sys

import pb_comp_photo
import pb_comp_photo.hdr
import pb_comp_photo.io
import pb_comp_photo.utils

if __name__ == "__main__":
    """
    The command line user interface
    """
    if len(sys.argv) == 1:
        print("Hello World")
    else:
        parser = argparse.ArgumentParser(
            prog="pbpc_hdr.py",
            description="Calculate HDR photo",
        )

        parser.add_argument(
            "-i",
            "--images",
            type=str,
            nargs="+",
            required=True,
            help="Provide a list of input images",
        )
        parser.add_argument(
            "-o",
            "--output",
            type=str,
            required=True,
            help="The output image (JPG)",
        )
        parser.add_argument(
            "-m",
            "--method",
            type=str,
            choices=pb_comp_photo.PBCP_HDR_METHODS,
            default="MERTENS",
            help="Select the method used to generate the HDR image",
        )
        parser.add_argument(
            "-g",
            "--gamma",
            type=float,
            default=1.8,
            help="Gamma value used for tonal mapping for debevec and robertson methods",
        )

        # Call the parser to parse the arguments.
        args = parser.parse_args()

        cv_img_objs, img_meta_lst = pb_comp_photo.io.read_img_opencv(args.images)
        exposure_times = list()
        for img_meta in img_meta_lst:
            ev100 = pb_comp_photo.utils.calc_ev_iso100(
                fnumber=img_meta["FNumber"],
                exposure_time=img_meta["ExposureTime"],
                iso=img_meta["ISO"],
            )
            exp_time = pb_comp_photo.utils.calc_exposure_time(5, ev100)
            exposure_times.append(exp_time)

        if args.method == "MERTENS":
            pb_comp_photo.hdr.create_hdr_mertens_img(
                cv_img_objs, output_img=args.output
            )
        elif args.method == "DEBEVEC":
            pb_comp_photo.hdr.create_hdr_debevec_img(
                cv_img_objs, exposure_times, output_img=args.output, gamma=args.gamma
            )
        elif args.method == "ROBERTSON":
            pb_comp_photo.hdr.create_hdr_robertson_img(
                cv_img_objs, exposure_times, output_img=args.output, gamma=args.gamma
            )
        else:
            raise Exception("Method for HDR generation is not recognised.")
