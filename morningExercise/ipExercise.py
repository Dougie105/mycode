#!/usr/bin/env python3

import argparse
import requests

def main():

    resp =  requests.get(f'http://ip-api.com/json/{ipToLookUp}')

if __name__ == '__main__':
    parser = argparsse.ArgumentParser('Allows lookup from http://ip-api.com/json/')
    parser.add_argument('ipToLookUp', help='The IP address to look up via the API service')

    main()
