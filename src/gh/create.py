from github import Github
from github import Auth

def create_repos(auth_token: str, org_name: str, repos: list[str]):
    g = Github(auth=Auth.Token(auth_token))
    org = g.get_organization(org_name)

    for repo in repos:
        print(f"creating repo: {repo}")
        org.create_repo(repo, private=True)
    g.close()