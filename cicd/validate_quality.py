from github import Github

import os
token = os.getenv('GITHUB_TOKEN')
print("token:", repr(token))

g = Github(token)

org = g.get_organization('TeliaSoneraNorge')
print('org', repr(org))
repo = org.get_repo('dss_project_pr_experiment')
print("repo:", repr(repo))
pr = repo.get_pull(1)
print("pr:", repr(pr))

print("End PR comment")