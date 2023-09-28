
import os
import requests
import pandas as pd
import numpy as np
import csv
import seaborn as sns
sns.set_theme()


personal_token = "USE YOUR OWN TOKEN"
token = os.getenv('GITHUB_TOKEN', personal_token)
headers = {'Authorization': f'token {token}'}

def getCommitTablebyProject(projectfullname, updateissuetablename):
    theCommitQuery = f"https://api.github.com/repos/{projectfullname}/commits"
    theProjectQuery = f"https://api.github.com/repos/{projectfullname}"
    p_search = requests.get(theProjectQuery, headers=headers)
    project_info = p_search.json()
    print(project_info)
    project_id = project_info['id']
    params = {'per_page': 100}
    page = 1
    commit_features = ['project_id', 'commit_sha', 'author_email', 'author_date']
    with open(updateissuetablename, 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(commit_features)
    while 1 == 1:
        params['page'] = page
        print(page)
        print(projectfullname + ' ' + 'page ' + str(page))
        theResult = requests.get(theCommitQuery, headers=headers, params=params)
        theItemListPerPage = theResult.json()
        if len(theItemListPerPage) == 0:
            break
        else:
            print(len(theItemListPerPage))
            for item in theItemListPerPage:
                commititem = {}
                commititem['project_id'] = project_id
                commititem['commit_sha'] = item['sha']
                try:
                    commititem['author_email'] = item['commit']['author']['email']
                except:
                    commititem['author_email'] = np.NaN
                commititem['author_date'] = item['commit']['author']['date']
                with open(updateissuetablename, 'a', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    writer.writerow([commititem[x] for x in commit_features])
            page = page + 1

getCommitTablebyProject("pallets/flask", 'stats.csv')
