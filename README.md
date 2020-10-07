# tld-scanner
## Installation
```
pipenv --three shell
pipenv sync
```

## Use
```
pipenv shell
python tld-scanner.py <domain without .com or .ch or .de ...>
```

## Example Output for hacking-lab
```
python tld-scanner.py -d hacking-lab

hacking-lab.CH,"ns2.compass-security.com. ns1.compass-security.com."
hacking-lab.CLUB,"ns.udag.net. ns.udag.de. ns.udag.org."
hacking-lab.COM,"ns1.compass-security.COM. ns2.compass-security.COM."
hacking-lab.DE,"ns1.compass-security.com. ns2.compass-security.com."
hacking-lab.EU,"d.ns14.net. a.ns14.net. c.ns14.net. b.ns14.net."
hacking-lab.INFO,"ns1.compass-security.com. ns2.compass-security.com."
hacking-lab.IO,"c.ns14.net. d.ns14.net. b.ns14.net. a.ns14.net."
hacking-lab.NET,"ns2.compass-security.com. ns1.compass-security.com."
hacking-lab.ONLINE,"ns22.worldnic.com. ns21.worldnic.com."
hacking-lab.XN--KPRW13D,"hacking-lab.xn--kpry57d. xn--kpry57d."
```

The domain `hacking-lab.com` is served by `ns1.compass-security.com`. Other domains are registered but not in the hands of Compass Security. 





