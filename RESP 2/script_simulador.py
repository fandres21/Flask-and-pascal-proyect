import random as RA
from time import sleep
import requests as r


def Data_MP25(nType):
    if nType == 'N' : return [RA.randint(5,15) for i in range(20)    ]
    if nType == 'A' : return [RA.randint(16,50) for i in range(20)   ] 
    if nType == 'P' : return [RA.randint(51,100) for i in range(20)  ]
    if nType == 'E' : return [RA.randint(101,150) for i in range(20) ]

def Data_MP10(nType):
    if nType == 'N' : return [RA.randint(1,50) for i in range(20)    ]
    if nType == 'A' : return [RA.randint(51,100) for i in range(20)  ] 
    if nType == 'P' : return [RA.randint(101,150) for i in range(20) ]
    if nType == 'E' : return [RA.randint(151,200) for i in range(20) ]


def Get_DD():
    dD = {
        'EA': RA.choice(['E1','E2','E3']),
        '25': Data_MP25(RA.choice(['N','A','P','E'])),
        '10': Data_MP10(RA.choice(['N','A','P','E']))
    }
    return dD

URL = "http://127.0.0.1:4000/data"

while 1:
    res = r.post(URL, json =  Get_DD())
    print('Status: ',res.status_code)
    sleep(5)