wget "https://raw.githubusercontent.com/volexity/threat-intel/main/2022/2022-02-03%20Operation%20EmailThief/indicators/iocs.csv" |

-> file:bytes

for $line in $lib.axon.readlines(:sha256) {
    ($valu, $type, $desc) = $line.split(",")
    switch $type {
        entity_type: {} // skip the header
        
        hostname: {
            [ inet:fqdn=$valu ]
        }
        ipaddress: {
            [ inet:ipv4=$valu ]
        }
        *: { $lib.print("Missing type: {type}", type=$type) }
    }
}
