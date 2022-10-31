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
        
        endpoint: Final   = var_endpoint
        
        allowedIps: Final = var_allowed_ips

        publicKey: Final  = var_public_key
        sharedKey: Final  = var_shared_key
        keepAlive: Final  = var_persistent_keepalive
        


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
        address: Final = var_addr
        dns: Final = var_dns

        privateKey: Final = var_private_key
        listenPort: Final = var_listen_ports
        
        saveConfig: Final = var_save_config

        postUp: Final = var_post_up
        postDown: Final = var_post_down


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

        peer: Final = var_attribute_peer
        interface: Final = var_attribute_interface


# Main
class configuration:
    def __init__( self ):
        self.attributes = configuration_attributes()
        self.variables = configuration_variables()

    