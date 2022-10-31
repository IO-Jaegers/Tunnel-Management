#!/usr/bin/env python3
from typing \
    import Final


var_endpoint = 'Endpoint'
var_allowed_ips = 'AllowedIPs'

var_public_key = 'PublicKey'
var_shared_key = 'PresharedKey'

var_persistent_keepalive = 'PersistentKeepalive'


class configuration_peer_variables:
    def __init__(self):
        global var_endpoint, \
            var_allowed_ips, \
            var_public_key, \
            var_shared_key, \
            var_persistent_keepalive
        
        self.endpoint: Final   = var_endpoint
        
        self.allowedIps: Final = var_allowed_ips

        self.publicKey: Final  = var_public_key
        self.sharedKey: Final  = var_shared_key
        self.keepAlive: Final  = var_persistent_keepalive
        


var_private_key = 'PrivateKey'
var_save_config = 'SaveConfig'
var_listen_ports = 'ListenPort'

var_post_up = 'PostUp'
var_post_down = 'PostDown'

var_addr = 'Address'
var_dns = 'DNS'


class configuration_interface_variables:
    def __init__( self ):
        global var_private_key, \
            var_listen_ports, \
            var_save_config, \
            var_post_up, \
            var_post_down, \
            var_addr, \
            var_dns    

        self.address: Final = var_addr
        self.dns: Final = var_dns

        self.privateKey: Final = var_private_key
        self.listenPort: Final = var_listen_ports
        
        self.saveConfig: Final = var_save_config

        self.postUp: Final = var_post_up
        self.postDown: Final = var_post_down


##
class configuration_variables:
    def __init__( self ):
        self.peer = configuration_peer_variables()
        self.interface = configuration_interface_variables()

var_attribute_peer = '[Peer]'
var_attribute_interface = '[Interface]'


class configuration_attributes:
    def __init__( self ):
        global var_attribute_peer, \
            var_attribute_interface

        self.peer: Final = var_attribute_peer
        self.interface: Final = var_attribute_interface

    def get_peer( self ):
        return self.peer

    def get_interface( self ):
        return self.interface



# Main
class configuration:
    def __init__( self ):
        self.attributes = configuration_attributes()
        self.variables = configuration_variables()
    
    def get_attributes( self ):
        return self.attributes

    def get_variables( self ):
        return self.variables
    