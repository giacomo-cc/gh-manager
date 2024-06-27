from github import Github
from github import Auth

def archive_repos(auth_token: str, org_name: str, repo_prefix: str):
    g = Github(auth=Auth.Token(auth_token))
    org = g.get_organization(org_name)

    for repo in org.get_repos():
        if not repo.archived and repo.name.startswith(repo_prefix):
            print("archiving repo: " + repo.name)
            repo.edit(archived=True)
    g.close()