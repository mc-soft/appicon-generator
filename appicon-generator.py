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

import os, sys, argparse
from PIL import Image

# Icon sizes taken from:
# https://developer.apple.com/library/content/qa/qa1686/_index.html

# Icon size/scales for modern iOS versions.
icons = {
    # iPhone
    '20pt': (20, [1, 2, 3]),
    '29pt': (29, [1, 2, 3]),
    '40pt': (40, [1, 2, 3]),
    '60pt': (60, [2, 3]),
    '76pt': (76, [1, 2]),
    '83.5pt': (83.5, [2]),
    '1024pt': (1024, [1]),

    # iPad
    'iTunesArtwork': (512, [1, 2]),
}

# Icon size/scales for versions of iOS 6.1 and earlier.
old_icons = {
    # iPhone / iPad
    '57pt': (57, [1, 2]),
    '72pt': (72, [1, 2]),
    '50pt': (50, [1, 2])
}


def parse_args():
    print_banner()

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
                        help="You can change the name of the output icons."
                             "(Example: {NAME}20pt@1x.png) [Default: AppIcon]",
                        required=False)

    parser.add_argument("-a", "--all",
                        help="By default only icon sizes required for iOS 6.2 and later are generated, if you wish "
                             "to generate icons for iOS 6.1 and earlier you need to set this.",
                        action="store_true", required=False)

    args = parser.parse_args()
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(1)
    else:
        if not os.path.isfile(args.image):
            print("[ERROR] The master image you specifed doesn't seem to exist?")
            sys.exit(1)

    process(args)


def icons_generator(array):
    for variation, icon_details in array.items():
        size = icon_details[0]
        scales = icon_details[1]

        for scale in scales:
            yield variation, size, scale


def get_destination(output_dir, name, variation, scale):
    scale_str = "@%dx" % scale
    return '%s/%s-%s%s.png' % (output_dir, name, variation, scale_str)


def generate_variations(master, output_dir, name, generator):
    for variation, size, scale in generator:
        image_size = int(size * scale)
        image = master.resize((image_size, image_size), Image.ANTIALIAS)
        dest = get_destination(output_dir, name, variation, scale)

        sys.stdout.write("Saving %s -> " % dest)
        image.save(dest)
        print("Done!")


def print_banner():
    print("########################################################\n")
    print("\tappicon-generator.py\t\t\t\t\tv1.0\n")
    print("\tMatthew Croston")
    print("\thttps://github.com/mc-soft/appicon-generator\n")
    print("########################################################\n")


def process(args):
    # Load our master image.
    master = Image.open(args.image)

    # Prep our vars.
    output_dir = 'output' if args.output is None else args.output
    name = 'AppIcon' if args.name is None else args.name

    # Attempt to create our directory if it doesn't exist.
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

        if not os.path.isdir(output_dir):
            print("[ERROR] An error occured creating your output directory (%s)" % output_dir)
            sys.exit(1)

    # Generate our variations.
    generate_variations(master, output_dir, name, icons_generator(icons))

    if args.all:
        print("\n[INFO] -all option has been specified, generating additional images.\n")
        generate_variations(master, output_dir, name, icons_generator(old_icons))


if __name__ == "__main__":
    parse_args()
