from datetime import datetime, timedelta
from git import Repo
import random
import os

# commits per day range
COMMITS_PER_DAY = (1, 5)

START_DATE = '2025-01-01'
END_DATE = '2025-09-02'

date = datetime.strptime(START_DATE, "%Y-%m-%d")
sd = date.strftime("%Y-%m-%d %H:%M:%S")

repo = Repo(os.getcwd())
origin = repo.remote(name='origin')

while date.strftime("%Y-%m-%d") < END_DATE:
    for _ in range(random.randint(COMMITS_PER_DAY[0], COMMITS_PER_DAY[1])):
        file = open('data.txt', 'w+')
        file.write(sd)

        os.environ['GIT_AUTHOR_DATE'] = sd
        os.environ['GIT_COMMITTER_DATE'] = sd

        repo.index.add(['data.txt'])
        repo.index.commit(f'Update data.txt at {sd}')

    date += timedelta(days=1)
    sd = date.strftime("%Y-%m-%d %H:%M:%S")

origin.push()