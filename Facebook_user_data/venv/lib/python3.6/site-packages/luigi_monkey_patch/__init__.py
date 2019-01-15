# -*- coding: utf-8 -*-
#
# Copyright 2016-2020 Zenix Huang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import httplib
from socket import error as SocketError
from luigi.s3 import ReadableS3File


def _patched_s3_close(self):
    try:
        self.s3_key.close()
    except Exception:
        self.s3_key.close(fast=True)
    self.closed = True


def _patched_s3_iterator(self):
    key_iter = self.s3_key.__iter__()
    has_next = True
    index = 0
    while has_next:
        try:
            # grad the next chunk
            chunk = ''
            while True:
                try:
                    chunk = next(key_iter)
                    break
                except (httplib.IncompleteRead, SocketError) as e:
                    self.s3_key.close(fast=True)
                    self.s3_key.open(mode='r', headers={
                        'Range': 'bytes=%d-' % index
                        })
                    key_iter = self.s3_key.__iter__()
            index += len(chunk)

            # split on newlines, preserving the newline
            for line in chunk.splitlines(True):

                if not line.endswith(os.linesep):
                    # no newline, so store in buffer
                    self._add_to_buffer(line)
                else:
                    # newline found, send it out
                    if self.buffer:
                        self._add_to_buffer(line)
                        yield self._flush_buffer()
                    else:
                        yield line
        except StopIteration:
            # send out anything we have left in the buffer
            output = self._flush_buffer()
            if output:
                yield output
            has_next = False
    self.close()

def patch():
    ReadableS3File.close = _patched_s3_close
    ReadableS3File.__iter__ = _patched_s3_iterator

patch()
