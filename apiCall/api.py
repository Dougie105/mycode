#!/usr/bin/env python3
import requests, json

def main():
    location = requests.get('http://api.open-notify.org/iss-now.json')
    
    results = location.json()
    
    longitude = results['iss_position']['longitude']
    latitude = results['iss_position']['latitude']


    print(results)
    print('Was successful?:', results['message'])
    print()

    print('Timestamp:', results['timestamp'])
    print()

    print('Full Location:', results['iss_position'])
    print()

    print('longitude:', longitude)
    print()

    print('latitude:', latitude)
    print()






if __name__ == "__main__":
    # execute only if run as a script
    main()
