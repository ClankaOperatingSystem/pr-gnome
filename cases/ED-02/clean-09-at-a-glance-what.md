title: Withdraw every name that pointed at a destroyed droplet
expect: 
why: states the problem and why the fix is by address rather than by name.
commit: Withdraw every name that pointed at a destroyed droplet
file: cloudlab/destroy.yml +38 -14
file: cloudlab/guard_test.py +18 -0
---
Destroy removed the host's own DNS record and nothing else, so a route label a project had published kept resolving to an address the provider had taken back. It now asks the zone what points at the droplet's address and withdraws all of it. By address rather than by name: it needs no map from projects to hosts, and a record somebody published by hand is caught too.
