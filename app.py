from flask import Flask
import time
import schedule, csv
from easysnmp import Session


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
    while True:
        schedule.run_pending()
        time.sleep(1)


def poll(host,com,ver,mib):
    # Create an SNMP session to be used for all our requests
    session = Session(hostname=host, community=com, version=ver)
    # You may retrieve an individual OID using an SNMP GET
    output = session.get(mib)
    print(output)


with open('inventory.csv') as inventory:
    invcsv = csv.reader(inventory)
    for row in invcsv:
        host = row[0]
        freq = int(row[1])
        com = row[2]
        ver = int(row[3])
        for mib in row[4:]:
            schedule.every(freq).seconds.do(poll, host=host, com=com, ver=ver, mib=mib)





