import time

import schedule, csv
from easysnmp import Session


def poll(host, com, ver, mib):
    # Create an SNMP session to be used for all our requests
    session = Session(hostname=host, community=com, version=ver)
    # You may retrieve an individual OID using an SNMP GET
    if mib is not None:
        output = session.get(mib)
    print("Hello")
    print(output)
    #
    # # You may also specify the OID as a tuple (name, index)
    # # Note: the index is specified as a string as it can be of other types than
    # # just a regular integer
    # contact = session.get(('sysContact', '0'))
    #
    # # And of course, you may use the numeric OID too
    # description = session.get('.1.3.6.1.2.1.1.1.0')
    #
    # # Set a variable using an SNMP SET
    # session.set('sysLocation.0', 'The SNMP Lab')
    #
    # # Perform an SNMP walk
    # system_items = session.walk('system')
    #
    # # Each returned item can be used normally as its related type (str or int)
    # # but also has several extended attributes with SNMP-specific information
    # for item in system_items:
    #     print
    #     '{oid}.{oid_index} {snmp_type} = {value}'.format(
    #         oid=item.oid,
    #         oid_index=item.oid_index,
    #         snmp_type=item.snmp_type,
    #         value=item.value
    #     )


with open('inventory.csv') as inventory:
    invcsv = csv.reader(inventory)
    for row in invcsv:
        host = row[0]
        freq = int(row[1])
        com = row[2]
        ver = int(row[3])
        for mib in row[4:]:
            schedule.every(freq).seconds.do(poll, host, com, ver, mib)

while True:
    schedule.run_pending()
    time.sleep(1)
