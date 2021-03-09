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
            repoRequest = requests.get("https://api.github.com/repos/{}/{}/commits".format(userID, repo["name"]))
            commits = repoRequest.json()
            repocommits.append("Repo: {} Number of commits: {}".format(repo["name"]), len(commits))
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
    
    
    
