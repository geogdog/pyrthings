'''A set of random things.'''
from __future__ import print_function
from random import randint
from struct import unpack_from
from os import urandom
import netaddr


def random_mac():
    '''Create a random MAC address.'''
    return '{0:02x}:{1:02x}:{2:02x}:{3:02x}:{4:02x}:{5:02x}'.format(
        *unpack_from('BBBBBB',urandom(20)))

def random_asset_tag():
    '''Create a random, zero padded, 6 digit number.'''
    return ('%06d' % randint(100000, 999999))

def random_ports(port_prefix='eth', amount=4):
    '''create a random amount of ethernet port names between 2 and option,
    amount.

    '''
    ports_to_create = []
    no_of_ports = randint(1, amount)
    for port in xrange(0, no_of_ports):
        if port != None:
            ports_to_create.append(port_prefix + str(port))
    return ports_to_create

def random_ip_in_network(network):
    network = netaddr.IPNetwork(network)
    return network[randint(0, len(network))]

def random_ip_in_range(start, end):
    range = netaddr.IPRange(start, end)
    return range[randint(0, len(range))]


if __name__ == '__main__':
    print('Random MAC: %s' % random_mac())
    print('Random Asset Tag: %s' % random_asset_tag())
    print('Random Ports: %s' % ', '.join(random_ports()))
    print('Random IP in 10.0.0.0/8 network: {0}'.format(
        random_ip_in_network(network='10.0.0.0/8')))
    print('Random IP between 192.168.1.3 and 192.168.3.87: {0}'.format(
        random_ip_in_range('192.168.1.3', '192.168.3.87')))
