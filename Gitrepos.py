'''
Created on Mar 8, 2021

@author: Steven Santiago
'''

import requests
import json

def gitrepo(userID):
        repocommits = []
        request = requests.get("https://api.github.com/users/{}/repos".format(userID))
        repos = request.json()
        for repo in repos:
            name = repo['name']
            repoRequest = requests.get("https://api.github.com/repos/{}/{}/commits".format(userID, name))
            commits = repoRequest.json()
            count = 0
            for obj in commits:
                if obj["commit"]:
                     count += 1
            repocommits.append("Repo: {} Number of commits: {}".format(name), count)
        return repocommits
if __name__ == '__main__':
    userID = input("Enter Github user ID:")
    try:
        repos = gitrepo(userID)
    except:
        repos = []
    if repos == [] :
        print("not a valid user ID")
    for repo in repos:
        print(repo)
    
    
    
