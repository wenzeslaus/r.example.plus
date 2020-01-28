# r.example.plus: GRASS GIS module example in Python

![CI](https://github.com/wenzeslaus/r.example.plus/workflows/CI/badge.svg)
![Code quality](https://github.com/wenzeslaus/r.example.plus/workflows/Code%20quality/badge.svg)
![Black code style](https://github.com/wenzeslaus/r.example.plus/workflows/Black%20code%20style/badge.svg)

This is an example of a GRASS GIS module for processing rasters in Python,
it is showing:
* which files to include,
* how to script raster map processing,
* how to handle parameters,
* how to publish documentation as a website, and
* how to describe everything.

## How to use this project

* Just download the files or clone the repository using Git.
* Copy them to your new project directory.

Alternatively, if you are thinking about forking it on GitHub and starting from there,
it is possible.
However, the only way how to remove the fork relationship is cloning locally, deleting the fork
on GitHub, creating a new project and pushing into it.

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
