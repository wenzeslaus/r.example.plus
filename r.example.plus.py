#!/usr/bin/env python3

"""
MODULE:    r.example.plus

AUTHOR(S): Vaclav Petras <wenzeslaus gmail com>

PURPOSE:   Add two raster maps (an example of a module in Python)

COPYRIGHT: (C) 2018-2020 by Vaclav Petras and the GRASS Development Team

This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS
for details.
"""

#%module
#% description: Adds the values of two rasters (A + B)
#% keyword: raster
#% keyword: algebra
#% keyword: sum
#%end
#%option G_OPT_R_INPUT
#% key: a_input
#% label: Name of input raster A in an expression A + B
#%end
#%option G_OPT_R_INPUT
#% key: b_input
#% label: Name of input raster B in an expression A + B
#%end
#%option G_OPT_R_OUTPUT
#% label: Name of result of an expression A + B
#%end


import sys

import grass.script as gs


def main():
    """Contains the main processing and executes all other functions"""
    # Get the parsed parameters as dictionaries
    # We are using unused_ for flags to tell Pylint that we know this variable
    # is unused (our modules does not have any flags).
    options, unused_flags = gs.parser()
    # Put parameter values into variables
    # This is not necessary, but advantageous for longer code as the variable
    # name can be better checked than a dictionary key.
    # The names don't have to be the same as the parameter names.
    a_input = options["a_input"]
    b_input = options["b_input"]
    output = options["output"]

    gs.mapcalc("{r} = {a} + {b}".format(r=output, a=a_input, b=b_input))

    return 0


if __name__ == "__main__":
    sys.exit(main())
