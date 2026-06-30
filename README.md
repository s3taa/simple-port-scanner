# Port Scanner

A multi-threaded port scanner built in Python as a learning project. 
Scans a target IP across a port range and identifies which ports are open, 
what service they're likely running, and exports results to JSON.

## Features
- Command-line interface using argparse (no interactive prompts — run it like a real tool)
- Threading for speed — scans hundreds of ports concurrently instead of one at a time
- Common service identification (HTTP, SSH, SMB, RDP, etc.)
- JSON export of results
- Input validation and error handling

## How to run
```bash
python simple_port_scanner.py 127.0.0.1 --start 1 --end 1000 --output results.json
```

## What it taught me
This project deepened my understanding of how networks and ports actually work,
not just how to use a tool that scans them. Implementing threading taught me how
concurrency speeds up I/O-bound tasks like network requests. Adding argparse
showed me how real command-line tools are structured, rather than relying on
interactive input(). Overall this project pushed my core Python ability and
problem-solving further than anything I'd built before.
