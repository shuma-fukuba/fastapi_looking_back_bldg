import os
import subprocess

COLOR_GREEN = '\033[92m'
COLOR_END = '\033[0m'

root_dir = os.path.dirname(__file__)
migration_files_dir = os.path.join(root_dir, 'migrations', 'versions', '*')

cmds = ['alembic downgrade base',
        f'rm -rf {migration_files_dir}',
        'alembic revision --autogenerate',
        'alembic upgrade head']

for cmd in cmds:
    print(f'{COLOR_GREEN}=> {cmd}{COLOR_END}')
    subprocess.call(cmd, shell=True)
