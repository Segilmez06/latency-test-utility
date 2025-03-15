# Latency Test Utility
Latency Test Utility is a simple tool for sending pings to list of targets, then visualizing the results.

## Requirements

Depends on Python 3. Make sure to install `pyyaml` and `rich` packages.

## Usage

Modify the configuration file. Specify source list file, ping count and time limit value. Then, run the script.

## List files

List files has simple syntax.

```
<Address> <Name or Description>
<Address> <Name or Description>
...
```

Create a file, add your targets. Then modify the config file to use this source file. There are some example files inside [latency-test-utility/lists](/lists) directory. You can use DNS server list to have a quick start

## Screenshot
Not really a screenshot but, still does the job. 😃
```
Latency Test Utility by Segilmez06
Test started at 15 March 2025 22:02:46

Reading config...
Reading server list...
Testing servers... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Fetching results...

                        Test Results
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Name        ┃ Address         ┃ Average ┃ Graph          ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ Loopback    │ 127.0.0.1       │ 0ms     │ Instant        │
│ Router      │ 192.168.1.1     │ 0ms     │ Instant        │
│ Control D   │ 76.76.2.0       │ 6ms     │ ######         │
│ Control D   │ 76.76.10.0      │ 6ms     │ ######         │
│ AdGuard DNS │ 94.140.15.15    │ 6ms     │ ######         │
│ Flash Start │ 185.236.104.104 │ 6ms     │ ######         │
│ Flash Start │ 185.236.105.105 │ 6ms     │ ######         │
│ AdGuard DNS │ 94.140.14.14    │ 7ms     │ #######        │
│ DNSFilter   │ 103.247.37.37   │ 7ms     │ #######        │
│ Cloudflare  │ 1.0.0.1         │ 8ms     │ ########       │
│ Cloudflare  │ 1.1.1.1         │ 10ms    │ ##########     │
│ Google      │ 8.8.4.4         │ 13ms    │ #############  │
│ Google      │ 8.8.8.8         │ 14ms    │ ############## │
└─────────────┴─────────────────┴─────────┴────────────────┘

                                 Response after Timeout
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Name           ┃ Address         ┃ Average ┃ Graph                                    ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ UltraDNS       │ 64.6.65.6       │ 38ms    │ ###                                      │
│ SafeDNS        │ 195.46.39.39    │ 42ms    │ ###                                      │
│ SafeDNS        │ 195.46.39.40    │ 42ms    │ ###                                      │
│ NextDNS DNS0EU │ 185.253.5.0     │ 42ms    │ ###                                      │
│ UltraDNS       │ 64.6.64.6       │ 46ms    │ ####                                     │
│ NextDNS DNS0EU │ 193.110.81.0    │ 46ms    │ ####                                     │
│ OpenDNS Home   │ 208.67.220.220  │ 54ms    │ #####                                    │
│ Cisco Umbrella │ 208.67.220.220  │ 54ms    │ #####                                    │
│ OpenDNS Home   │ 208.67.222.222  │ 55ms    │ ######                                   │
│ Cisco Umbrella │ 208.67.222.222  │ 55ms    │ ######                                   │
│ CleanBrowsing  │ 185.228.169.9   │ 64ms    │ #######                                  │
│ Quad9          │ 9.9.9.9         │ 71ms    │ ########                                 │
│ Quad9          │ 149.112.112.112 │ 71ms    │ ########                                 │
│ Gcore Free     │ 95.85.95.85     │ 72ms    │ #########                                │
│ Gcore Free     │ 2.56.220.2      │ 73ms    │ #########                                │
│ CleanBrowsing  │ 185.228.168.9   │ 77ms    │ ##########                               │
│ DNSFilter      │ 103.247.36.36   │ 248ms   │ ######################################## │
└────────────────┴─────────────────┴─────────┴──────────────────────────────────────────┘

          Failed
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Name      ┃ Address     ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ No Server │ 192.168.1.0 │
└───────────┴─────────────┘

Test finished at 15 March 2025 22:02:50
```

## Contributing

Any PR and issue is really appreciated. You can show your support by ⭐ starring the repo.

## Credits

Created and maintained by [@Segilmez06](https://github.com/Segilmez06).
