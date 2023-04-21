import json
from pprint import pprint
from urllib.parse import urljoin
import bioblend.galaxy
import bioblend.galaxy.objects

import os
import sys
import requests

server = 'https://gat-10.eu.galaxy.training/'
api_key = os.getenv('GAPI')
base_url = urljoin(server, 'api')

def bio():
    print("""
    gi = bioblend.galaxy.GalaxyInstance(url=server, key=api_key)
    pprint(gi.histories.get_histories())
    """)
    input("")
    gi = bioblend.galaxy.GalaxyInstance(url=server, key=api_key)
    pprint(gi.histories.get_histories())

    print("""
    new_hist = gi.histories.create_history(name='BioBlend test')
    pprint(new_hist)
    """)
    input("")
    new_hist = gi.histories.create_history(name='BioBlend test')
    pprint(new_hist)

    print("""
    input("")
    pprint(gi.histories.get_histories(name='BioBlend test'))
    """)
    input("")
    pprint(gi.histories.get_histories(name='BioBlend test'))

    print("""
    hist_id = new_hist["id"]
    pprint(gi.tools.upload_file("test-data/1.txt", hist_id))
    """)
    input("")
    hist_id = new_hist["id"]
    pprint(gi.tools.upload_file("test-data/1.txt", hist_id))

    print("""
    pprint(gi.histories.show_history(history_id=hist_id))
    """)
    input("")
    pprint(gi.histories.show_history(history_id=hist_id))

    print("""
    hdas = gi.histories.show_history(history_id=hist_id, contents=True)
    pprint(hdas)
    """)
    input("")
    hdas = gi.histories.show_history(history_id=hist_id, contents=True)
    pprint(hdas)

    print("""
    hda0_id = hdas[0]['id']
    print(hda0_id)
    pprint(gi.datasets.show_dataset(hda0_id))
    """)
    input("")
    hda0_id = hdas[0]['id']
    print(hda0_id)
    pprint(gi.datasets.show_dataset(hda0_id))

    print("""
    pprint(gi.histories.update_history(new_hist['id'], name='Updated history'))
    """)
    input("")
    pprint(gi.histories.update_history(new_hist['id'], name='Updated history'))

    print("""
    pprint(gi.histories.delete_history(new_hist['id']))
    """)
    input("")
    pprint(gi.histories.delete_history(new_hist['id']))

def api():
    print("""
    headers = {"Content-Type": "application/json", "x-api-key": api_key}
    r = requests.get(base_url + "/histories", headers=headers)
    print(r.text)
    hists = r.json()
    """)
    input("")
    headers = {"Content-Type": "application/json", "x-api-key": api_key}
    r = requests.get(base_url + "/histories", headers=headers)
    print(r.text)
    hists = r.json()
    pprint(hists)

    print("""
    pprint([_ for _ in hists if _['name'] == 'Unnamed history'])
    """)
    input("")
    pprint([_ for _ in hists if _['name'] == 'Unnamed history'])

    
    print("""
    hist0_id = hists[0]['id']
    print(hist0_id)
    r = requests.get(base_url + "/histories/" + hist0_id, headers=headers)
    pprint(r.json())
    """)
    input("")
    hist0_id = hists[0]['id']
    print(hist0_id)
    r = requests.get(base_url + "/histories/" + hist0_id, headers=headers)
    pprint(r.json())

    print("""
    r = requests.get(base_url + "/histories/" + hist0_id + "/contents", headers=headers)
    hdas = r.json()
    pprint(hdas)
    """)
    input("")
    r = requests.get(base_url + "/histories/" + hist0_id + "/contents", headers=headers)
    hdas = r.json()
    pprint(hdas)

    print("""
    hda0_id = hdas[0]['id']
    print(hda0_id)
    r = requests.get(base_url + "/datasets/" + hda0_id, headers=headers)
    pprint(r.json())
    """)
    input("")
    hda0_id = hdas[0]['id']
    print(hda0_id)
    r = requests.get(base_url + "/datasets/" + hda0_id, headers=headers)
    pprint(r.json())

    print("""
    data = {'name': 'New history'}
    r = requests.post(base_url + "/histories", data=json.dumps(data), headers=headers)
    new_hist = r.json()
    pprint(new_hist)
    """)
    input("")
    data = {'name': 'New history'}
    r = requests.post(base_url + "/histories", data=json.dumps(data), headers=headers)
    new_hist = r.json()
    pprint(new_hist)

    print("""
    data = {'name': 'Updated history'}
    r = requests.put(base_url + "/histories/" + new_hist["id"], json.dumps(data), headers=headers)
    print(r.status_code)
    pprint(r.json())
    """)
    input("")
    data = {'name': 'Updated history'}
    r = requests.put(base_url + "/histories/" + new_hist["id"], json.dumps(data), headers=headers)
    print(r.status_code)
    pprint(r.json())

    print("""
    r = requests.delete(base_url + "/histories/" + new_hist["id"], headers=headers)
    print(r.status_code)
    """)
    input("")
    r = requests.delete(base_url + "/histories/" + new_hist["id"], headers=headers)
    print(r.status_code)

def obj():
    print("""
    gi = bioblend.galaxy.objects.GalaxyInstance(url=server, api_key=api_key)
    pprint(gi.histories.get_previews())
    """)
    input("")
    gi = bioblend.galaxy.objects.GalaxyInstance(url=server, api_key=api_key)
    pprint(gi.histories.get_previews())

    print("""
    new_hist = gi.histories.create(name='BioBlend test')
    pprint(new_hist)
    """)
    input("")
    new_hist = gi.histories.create(name='BioBlend test')
    pprint(new_hist)

    print("""
    pprint(gi.histories.list(name='BioBlend test'))
    """)
    input("")
    pprint(gi.histories.list(name='BioBlend test'))

    print("""
    hda = new_hist.upload_file("test-data/1.txt")
    pprint(hda)
    """)
    input("")
    hda = new_hist.upload_file("test-data/1.txt")
    pprint(hda)

    print("""
    gi.histories.get(new_hist.id)
    """)
    input("")
    gi.histories.get(new_hist.id)

    print("""
    pprint(new_hist.content_infos)
    """)
    input("")
    pprint(new_hist.content_infos)

    print("""
    new_hist.get_dataset(hda.id)
    """)
    input("")
    new_hist.get_dataset(hda.id)

    print("""
    new_hist.update(name='Updated history')
    """)
    input("")
    new_hist.update(name='Updated history')

    print("""
    new_hist.delete()
    """)
    input("")
    new_hist.delete()

def main():
    args = sys.argv[1]
    if args == 'bioblend':
        bio()
    elif args == 'api':
        api()
    elif args == 'obj':
        obj()


if __name__ == '__main__':
    main()
