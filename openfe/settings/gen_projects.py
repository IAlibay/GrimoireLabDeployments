import argparse
import json
import os
from github import Github


def gen_json(orgname: str) -> None:
    """
    Generate a basic grimorelab json file
    """
    git = Github(os.environ['GH_API_TOKEN'])
    org = git.get_organization(orgname)

    # we filter out all the forks by default
    repo_urls = [r.clone_url for r in org.get_repos() if not r.fork]

    gml_data = {orgname: {'meta': {'title': orgname}, 'git': repo_urls}}

    with open('projects.json', 'w') as f:
        f.write(json.dumps(gml_data, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--orgname',
        help="name of the Github Organization to generate json for")
    args = parser.parse_args()
    gen_json(args.orgname)
