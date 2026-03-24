import sys
import subprocess

version = None

with open('changelog.txt', 'r') as f:
    for line in f.readlines():
        if line.startswith('202'):
            version = line.split(':', 1)[-1].strip()

if version == None:
    print('No version found in changelog.txt')
    sys.exit(1)

print(f'Using version: {version}')

date = subprocess.check_output(['date', '-R'], text=True).strip()

print(f'Using date: {date}')

def specialize(path):
    with open(f'{path}.template', 'r') as f:
        template = f.read()

    content = template.replace('{{{version}}}', version).replace('{{{date}}}', date)

    with open(path, 'w') as f:
        f.write(content)


specialize('setup.py')
specialize('tinkerforge_util/__init__.py')
specialize('debian/changelog')
