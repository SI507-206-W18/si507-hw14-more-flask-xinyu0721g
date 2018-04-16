import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []


def init(app):
    global entries
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []


def get_entries():
    global entries
    return entries


def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    id_lst = list(int(i['id']) for i in entries)
    if len(id_lst) != 0:
        next_id = max(id_lst) + 1
    else:
        next_id = 0
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    entries.insert(0, entry)  # add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def delete_entry(delete_id):
    global entries, GUESTBOOK_ENTRIES_FILE
    for i in entries:
        if i["id"] == delete_id:
            entries.remove(i)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def edit_entry(edit_id, new_text):
    global entries, GUESTBOOK_ENTRIES_FILE
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    for i in entries:
        if i["id"] == edit_id:
            i['timestamp'] = time_string
            i['text'] = new_text
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
