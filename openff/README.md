# Running GrimoireLab for OpenFE

## Getting started

### 1. Some pre-reqs

1. Get a GitHub API token
2. Add the token to the various `api-token` entries of ./settings/setup.cfg
3. Export your API token to an environment variable named `GH_API_TOKEN`
4. Set up a Python environment with `PyGithub` installed.
5. Make sure you have docker-compose and a machine with at least 8 GB of available RAM, see the [GrimoireLab docs](https://chaoss.github.io/grimoirelab-tutorial/docs/getting-started/setup/#requirements) for more information.

### 2. Generate the projects.json

1. Go to `settings`.
2. Execute the `gen_projects.py` for OpenFE: `python gen_projects.py --orgname OpenFreeEnergy`

## Starting up docker-compose

Now you can go ahead and set up docker-compose!

1. Call `sudo docker-compose up -d`
2. Open up a browser with the url http://localhost:5601/
3. Get lost in the data.
