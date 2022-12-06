from datetime import datetime
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

REPORT = {
    'pelican': {
        'user': 'surfer1234',
        'timestamp': get_timestamp(),
        'contents': 'surf is a couple feet with moderate cross shore/onshore winds. Mostly late breakers and bigger closeouts'
    },
    'hightower': {
        'user': 'wiverider35',
        'timestamp': get_timestamp(),
        'contents': 'weak surf and kinda windy'
    },
    'petden': {
        'user': 'soulsurfer',
        'timestamp': get_timestamp(),
        'contents': 'not very good'
    },
}

def read_all():
    return list(REPORT.values())