#!/usr/bin/env python3
from typing import Final

var_extension_name = '.conf'

class variables:
    def __init__( self ):
        global var_extension_name
        extension_name: Final = var_extension_name


# generates a generic template that has to be filled out by a user.
# gives a nice starting point.
def generic( name ):
    defaults = variables()

    