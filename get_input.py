#!/usr/bin/python3
import argparse
import subprocess
import sys
import os
from dotenv import load_dotenv
load_dotenv()

SESSION = os.environ.get("SESSION")
useragent = 'br3nr'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2023)
parser.add_argument('--day', type=int, default=2)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}" -A {useragent}'
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)
