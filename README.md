# appicon-generator
A simple python script that can be used to generate all the iOS AppIcons sizes requried when developing within XCode.

## Getting Started

Simply clone the git repository to your computer.

### Prerequisites

In order to use this script you require Python 3 which can be downloaded from:

```
https://www.python.org/downloads/
```

You will also need to install the Python Imaging Library which can be done using PIP with the following command:

```
pip install pillow
```

## Usage

appicon-generator has been created to be as user friendly as possible. At it's most basic you simply need to provide a master image (1024x1024) and issue the following command:

```console
foo@bar:~$ ./appicon-generator.py -i master.png
```

This will generate create a folder in the working directory called output where all your iOS app icons will be saved.

### Additional arguments

Below I will cover the main script arguments, if at anytime you wish to view the full list of arguments you can do so by executing the script with the help (-h, --help) argument.

```console
foo@bar:~$ ./appicon-generator.py -h
```

#### Custom Output Directory

You can specify a custom out directory (relative or absolute path) by executing the script with the output (-o, --output) argument. You should be aware that this directory will be created if it does not currently exist.

```console
foo@bar:~$ ./appicon-generator.py -i master.png -o custom-dir
```

#### Custom File Name

By default, the file name structure for a 29pt image at 2x scale is:

*AppIcon-29pt@2x*

If you wish to change this to something custom such as:

*MyCustomName-29pt@2x*

This can be done by executing the script with the name (-n, --name) argument.

```console
foo@bar:~$ ./appicon-generator.py -i master.png -n MyCustomName
```

#### iOS 6.1 and earlier sizes

As per the documentation (found at the link below), the default AppIcon sizes changed for iOS version later than 6.1.

```
https://developer.apple.com/library/content/qa/qa1686/_index.html
```

By default, appicon-generator only generates the latest AppIcon sizes, if you are generating icons for a project that is using iOS 6.1 or earlier you will need to generate the icons using the all (-a, --all) argument.

```console
foo@bar:~$ ./appicon-generator.py -i master.png -a
```

## Authors

* **Matthew Croston** - *Original Developer* - [mc-soft](https://github.com/mc-soft)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

