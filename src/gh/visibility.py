from github import Github
from github import Auth

def set_visibility(auth_token: str, org_name: str, repo_prefix: str, private: bool):
    g = Github(auth=Auth.Token(auth_token))
    org = g.get_organization(org_name)

    for repo in org.get_repos():
        if repo.name.startswith(repo_prefix):
            print(f"change visibility for repo {repo.name} to {'private' if private else 'public'}")
            repo.edit(private=private)
    g.close()