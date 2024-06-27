from dotenv import load_dotenv
import os
import gh.visibility

load_dotenv()

org_name = "its-biomedicale"
auth_token = os.getenv("GH_TOKEN")

def main():
    gh.visibility.set_visibility(auth_token, org_name, "da-mod3-python-db", True)
    gh.visibility.set_visibility(auth_token, org_name, "da-mod2-correzione", True)

if __name__ == "__main__":
    main()