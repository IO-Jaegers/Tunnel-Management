#!/usr/bin/env python3
from typing \
    import Final

from var \
    import configuration


var_extension_name = '.conf'

class variables:
    def __init__( self ):
        global var_extension_name

        self.extension_name: Final = var_extension_name
        self.configuration = configuration()
    
    def get_configuration( self ):
        return self.configuration

    def get_extension_name( self ):
        return self.extension_name


# generates a generic template that has to be filled out by a user.
# gives a nice starting point.
def generic( name, n ):
    if isinstance( name, str ):
        return _generic_make( name, n )


def _generic_make( name, n ):
    defaults = variables()
    filename = _combine_filename( name, defaults.extension_name )
    returnConfig = \
        {          \
            "file" : filename, \
            "interface": None, \
            "peers":[]         \
        }
    
    returnConfig[ "interface" ] = _template_interface( defaults )
    returnConfig[ "peers" ] = _template_peers( defaults, returnConfig[ "peers" ], n )

    return returnConfig


def _template_interface( vars ):

    if isinstance( vars.get_configuration(), configuration ):
        returnPeer = {}
        returnPeer[ "entry" ] = vars.get_configuration().get_attributes().get_interface()


        return returnPeer
        

def _template_peers( vars, peers, n ):
    base = peers

    if( base == None ):
        base = []

    if isinstance( vars.get_configuration(), configuration ):
        for idx in range( 0, n ):
            returnPeer = {}
            returnPeer[ "entry" ] = vars.get_configuration().get_attributes().get_peer()
            
            base.append( returnPeer )

    return base
    
    

    

def _combine_filename( filename, ext ): 
    return str( filename + ext )


if __name__ == '__main__':
    print( generic( 'test', 4 ) )