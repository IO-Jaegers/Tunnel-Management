#!/usr/bin/env python3
from os \
    import walk, path


def listConfiguration( path_to_wireguard_configuration ):
    retVal = []

    if( isinstance( path_to_wireguard_configuration, str ) ):
        for ( dirpath, dirnames, files ) \
            in walk( path_to_wireguard_configuration ):

            for fname in files:
                pathTo = path.join( dirpath, fname )
                name, ext = path.splitext( fname )

                if ext == '.conf':
                    print( pathTo )
                    retVal.append( pathTo )
                pass
            
        pass

    return retVal