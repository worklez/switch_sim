switch_sim
==========
This is a dumb L1 switch simulator, written in Python/Django.  It supports a few (most basic) L1 switch operations, such as
* listing the ports
* listing the port mappings
* map 2 ports
* unmap 2 ports
* clear all port mappings

It also has a few basic managment operations, such as 
* get a list of simulated switches
* for a particular switch, show me the details
* for a particular switch, add/delete a bunch of ports

### Installation
1.  clone a copy of the whole project form github: https://github.com/ahmay98/switch_sim
2.  modify the <INSTALL_DIR>/src/switch_sim/settings.py, and update the sqlite DB's absolute path -- the path should be your <INSTALL_DIR>/src/sqlite.db
3.  make sure you have python 2.7.x and django installed
4.  'cd' to your <INSTALL_DIR>/src
5.  'python manage.py runserver'
5a.  btw, default port is 8000
6.  bring up a browser, and hit 'http://localhost:8000/sim'

### Operations
This is a complete REST WS interface...most of the operations will return some sort of JSON object as the response, (with one exception).

#### Swich List

<code>http://localhost:8000/sim</code>

No further HTTP request parameters needed.  This request will return a JSON object describing the 
* (switch) count
* a list of switch simulations

<code>
{
    "count": 1, 
    "switches": [
        {
            "description": "blah blah blah", 
            "id": 1, 
            "name": "MRV 1", 
            "port_count": 144, 
            "status": "online"
        }
    ]
}
</code>

#### Swtich Detail

<code>http://localhost:8000/sim/\<switch_id\></code>

\<switch_id\> -- switch ID one can read from the switch listing result

No additional HTTP request parameters needed.  This request will return a JSON object describing the details of a switch, including all the ports for this switch.

<code>
{
    "description": "blah blah blah", 
    "id": "1", 
    "name": "MRV 1", 
    "ports": [
        {
            "is_cabled": true, 
            "is_mapped": true, 
            "name": "1.1.1"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.2"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.3"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": true, 
            "name": "1.1.4"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.5"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.6"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.7"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.8"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.9"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.10"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.11"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.12"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.13"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.14"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.15"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.16"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.17"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.18"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.19"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.20"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.21"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.22"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.23"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.24"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.25"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.26"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.27"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.28"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.29"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.30"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.31"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.32"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.33"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.34"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.35"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.36"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.37"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.38"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.39"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.40"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.41"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.42"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.43"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.44"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.45"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.46"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.47"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.48"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.49"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.50"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.51"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.52"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.53"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.54"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.55"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.56"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.57"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.58"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.59"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.60"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.61"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.62"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.63"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.64"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.65"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.66"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.67"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.68"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.69"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.70"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.71"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.72"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.73"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.74"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.75"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.76"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.77"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.78"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.79"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.80"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.81"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.82"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.83"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.84"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.85"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.86"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.87"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.88"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.89"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.90"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.91"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.92"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.93"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.94"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.95"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.96"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.97"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.98"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.99"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.100"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.101"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.102"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.103"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.104"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.105"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.106"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.107"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.108"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.109"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.110"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.111"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.112"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.113"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.114"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.115"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.116"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.117"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.118"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.119"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.120"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.121"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.122"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.123"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.124"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.125"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.126"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.127"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.128"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.129"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.130"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.131"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.132"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.133"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.134"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.135"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.136"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.137"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.138"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.139"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.140"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.141"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.142"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.143"
        }, 
        {
            "is_cabled": true, 
            "is_mapped": false, 
            "name": "1.1.144"
        }
    ], 
    "status": "online"
}
</code>

