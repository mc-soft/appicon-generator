#!/usr/bin/python

# Copyright (c) 2018 Matthew Croston

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys, argparse

icons = {
    '20pt': (20, [1, 2, 3]),
    '29pt': (29, [1, 2, 3]),
    '40pt': (40, [1, 2, 3]),
    '60pt': (60, [2, 3]),
    '76pt': (76, [1, 2]),
    '83.5pt': (83.5, [2]),
    '1024pt': (1024, [1])
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Quickly and easily creates all the AppIcons required during iOS development.",
        epilog="Please report any bugs at https://github.com/mc-soft/appicon-generator"
    )

    required = parser.add_argument_group("required arguments")
    required.add_argument("-i", "--image",
                          help="The master image that will be used to create the icons (1024x1024 pixels)",
                          required=True)

    parser.add_argument("-o", "--output",
                        help="The output directory to save the icons to. [Default: /output]",
                        required=False)

    parser.add_argument("-n", "--name",
                        help="You can change the name of the output icons. (Example: {NAME}20pt@1x.png) [Default: AppIcon]",
                        required=False)

    args = parser.parse_args()
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(1)

    process(args)


def process(args):
    print(args)


if __name__ == "__main__":
    parse_args()