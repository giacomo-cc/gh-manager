from github import Github
from github import Auth
from dotenv import load_dotenv
import os

load_dotenv()

org_name = "its-biomedicale"
repo_prefix = "da-mod3-"
auth = Auth.Token(os.getenv("GH_TOKEN"))

def set_read_to_all(new_permissions):
    g = Github(auth=auth)
    current_user = g.get_user().login
    org = g.get_organization(org_name)

    for repo in org.get_repos():
        if not repo.archived and repo.name.startswith(repo_prefix):
            for collab in repo.get_collaborators():
                if collab.login != current_user:
                    print(f"set permissions for {collab.login} on {repo.name} to {new_permissions}")
                    repo.add_to_collaborators(collab.login, new_permissions)
    g.close()

def monitor_invitations_in_repos():
    g = Github(auth=auth)
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

def create_repos(repos):
    g = Github(auth=auth)
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

def main():
    monitor_invitations_in_repos()

if __name__ == "__main__":
    main()