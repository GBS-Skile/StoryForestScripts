import json
import os
import re

from os import path
from simplethoth.transcript import transcripter

SCRIPTS_DIR = 'scripts'
SCENARIOS_DIR = 'scenarios'

pattern = re.compile(r'^(.+?)(\.[^.]+)?$')

if not path.exists(SCENARIOS_DIR):
    os.mkdir(SCENARIOS_DIR)

for filename in os.listdir(SCRIPTS_DIR):
    with open(path.join(SCRIPTS_DIR, filename), encoding='utf-8') as f_in:
        scenario = transcripter.transcript(f_in)

        if scenario:
            filename = pattern.match(filename).group(1) + ".json"
            with open(path.join(SCENARIOS_DIR, filename), 'w', encoding='utf-8') as f_out:
                json.dump(scenario, f_out, ensure_ascii=False, indent=2)


