#!/usr/bin/env python3
"""jaihnsing-python-6oje."""
import sys,argparse
from utils import timestamp
def main():
    p=argparse.ArgumentParser(description="jaihnsing-python-6oje")
    p.add_argument("--version",action="version",version="1.0.0")
    p.add_argument("-v","--verbose",action="store_true")
    a=p.parse_args()
    if a.verbose:print(f"[{timestamp()}] jaihnsing-python-6oje v1.0.0")
    print(f"Hello from jaihnsing-python-6oje!")
    return 0
if __name__=="__main__":sys.exit(main())
