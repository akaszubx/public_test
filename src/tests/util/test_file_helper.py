#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
INTEL CONFIDENTIAL
Copyright 2022 Intel Corporation.
This software and the related documents are Intel copyrighted materials, and
your use of them is governed by the express license under which they were
provided to you (License).Unless the License provides otherwise, you may not
use, modify, copy, publish, distribute, disclose or transmit this software or
the related documents without Intel's prior written permission.

This software and the related documents are provided as is, with no express or
implied warranties, other than those that are expressly stated in the License.
"""


import pytest

from util.file_helper import FileHelper


class TestFileHelper:

    @pytest.mark.parametrize('path',
                             ['test.ext', 'test.dot.ext', '/testdir/testing.ext' 'testdir/test.ext', 'c:/dir/test.ext'])
    def test_validate_file_extension(self, path):
        extension = '.ext'
        assert FileHelper.validate_file_extension(path, extension) == True


