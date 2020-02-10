# r.example.plus: GRASS GIS module example in Python

[![GRASS GIS module](https://img.shields.io/badge/GRASS%20GIS-module-%23009000)](https://grass.osgeo.org/)
[![CI](https://github.com/wenzeslaus/r.example.plus/workflows/CI/badge.svg)](https://github.com/wenzeslaus/r.example.plus/actions?query=workflow%3A%22CI%22)
[![Code quality check](https://github.com/wenzeslaus/r.example.plus/workflows/Code%20quality%20check/badge.svg)](https://github.com/wenzeslaus/r.example.plus/actions?query=workflow%3A%22Code%20quality%20check%22)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Black code style check](https://github.com/wenzeslaus/r.example.plus/workflows/Black%20code%20style%20check/badge.svg)](https://github.com/wenzeslaus/r.example.plus/actions?query=workflow%3A%22Black%20code%20style%20check%22)
[![Deploy online documentation](https://github.com/wenzeslaus/r.example.plus/workflows/Deploy%20online%20documentation/badge.svg)](https://github.com/wenzeslaus/r.example.plus/actions?query=workflow%3A%22Deploy%20online%20documentation%22)

This is an example of a GRASS GIS module for processing rasters in Python,
it is showing:
* which files to include,
* how to script raster map processing,
* how to handle parameters,
* how to publish documentation as a website, and
* how to describe everything.

## How to use this project

### Start by using this as a template

GitHub has a mechanism how to use this repository as a template:

* On GitHub, press *Use this template*.
* Name the project and provide other repository info.
* Clone the project using Git.

### Start by Get the copy

Alternatively, e.g., when not using GitHub, you can get the files in
a standard way:

* Just download the files as ZIP or clone the repository using Git.
* Copy them to your new project directory.

### Rename

Once you have the files in place, you need to do some renaming:

* Rename files to fit the name of your new module.
* Search all the content of all files for r.example.plus and
  r_example_plus and replace that with your module name.

### Renaming protip

You will probably replace the names in the files as you are adding your
functionality, but if you are using Bash, you may want to try these
commands (do it before you make any changes to the files, so you can
review the changes with git):

```
FILES="Makefile *.* */*.* .github/*/*.*"
sed -i 's/r\.example\.plus/r.minus/g' $FILES
sed -i 's/r_example_plus/r_minus/g' $FILES
```

### Getting the GitHub Actions work

If you have the repository on GitHub, you can also reuse the GitHub
Actions defined in the repository (under `.github`). Initially, most of
them will fail, but once you do the renaming, most of them should start
working.

For the workflow uploading documentation to GitHub Pages to
work, you will need you to
[set up Deploy key and a Secret](https://github.com/marketplace/actions/github-pages-action#1-add-ssh-deploy-key)
for your repository. Once the keys are in place, the online documentation
will be published as GitHub Pages website automatically.
The URL for the website is available in the Settings of your repository.

## Files which usually are not part of a module

These are the files in this repository which usually are not part of
a GRASS GIS module source code, but are useful for a standalone repository.

* README (README.md) is very useful for a standalone repository,
  but is not required for a GRASS GIS module because installation,
  code contributions, etc. are already described in the main repository.
* LICENSE file makes it easier to identify the license (even when the
  license is specified elsewhere). It is not required for the modules
  in the main repository as there is a license file already included.
* Files in .github/ directory for GitHub Actions, Continuous Integration, etc.

## What is next

Consider contributing the your module to the
[GRASS GIS Addons repository](https://grass.osgeo.org/development/code-submission/)
through pull request on GitHub.
This comes with several advantages such as maintenance support
from the core team and easier distribution to users.
At the same time, you can still keep using
repository like this one for development and release the
code to the Addons when ready. This is especially suitable for
for larger projects with multiple contributors.
For smaller projects, it may be more suitable to do initial
development separately, but after maturing, move the code Addons.

## How to contribute to this repository

Fork the project and submit a pull request or open an issue.
