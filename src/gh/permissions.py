from github import Github
from github import Auth

def set_read_to_all(auth_token: str, org_name: str, repo_prefix: str, new_permissions: str):
    g = Github(auth=Auth.Token(auth_token))
    current_user = g.get_user().login
    org = g.get_organization(org_name)

    for repo in org.get_repos():
        if not repo.archived and repo.name.startswith(repo_prefix):
            for collab in repo.get_collaborators():
                if collab.login != current_user:
                    print(f"set permissions for {collab.login} on {repo.name} to {new_permissions}")
                    repo.add_to_collaborators(collab.login, new_permissions)
    g.close()

def check_permissions(auth_token: str, org_name: str, repo_prefix: str):
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