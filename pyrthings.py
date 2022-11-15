'''A set of random things.'''
import random


def random_mac():
    '''Create a random MAC address.'''
    mac = [ random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]
    return ':'.join(['%02x' % m for m in mac])


def random_asset_tag():
    '''Create a random, zero padded, 6 digit number.'''
    return '{0:06d}'.format(random.randint(1, 999999))


def random_ports(port_prefix='eth', amount=5):
    '''create a random amount of ethernet port names between 2 and option,
    amount.

    '''
    ports_to_create = []
    no_of_ports = random.randint(2, amount)
    for port in range(1, no_of_ports):
        if port != None:
            ports_to_create.append(port_prefix + str(port))
    return ports_to_create


if __name__ == '__main__':
    print(f'Random MAC: {random_mac()}')
    print(f'Random Asset Tag: {random_asset_tag()}')
    print(f'Random Ports: {",".join(random_ports())}')
