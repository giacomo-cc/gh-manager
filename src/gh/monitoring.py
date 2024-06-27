from github import Github
from github import Auth

def monitor_invitations_in_repos(auth_token: str, org_name: str, repo_prefix: str):
    g = Github(auth=Auth.Token(auth_token))
    org = g.get_organization(org_name)

    for repo in org.get_repos():
        if not repo.archived and repo.name.startswith(repo_prefix):
            print("REPOSITORY: " + repo.name)
            for collab in repo.get_collaborators():
                if collab.login != "giacomo-cc":
                    print(f"+ {collab.login} ({collab.permissions})")
                    if collab.permissions.push:
                        print("- - - - - - Attenzione!!! - - - - -")
            print()

    g.close()