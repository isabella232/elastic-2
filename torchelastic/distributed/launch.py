#!/usr/bin/env/python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from torch.distributed.elastic_launch import parse_args, run


def main(args=None):
    args = parse_args(args)
    run(args)


if __name__ == "__main__":
    main()
