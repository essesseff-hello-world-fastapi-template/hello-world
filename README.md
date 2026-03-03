# hello-world Application (FastAPI)

Python FastAPI implementation with trunk-based development and GitOps-driven deployments via Argo CD to Kubernetes (see related repositories), with *optional* process orchestration, reporting, etc. via the [essesseff DevOps platform](https://essesseff.com) available on a per essesseff app subscription.  

Setup **GitHub → Argo CD → K8s** in *less than 5 minutes* with the [essesseff onboarding utility](https://www.essesseff.com/docs/deployment/essesseff-onboarding-utility) *(absolutely free -- no essesseff subscription required)*.  

*Please Note:*

*essesseff™ is an independent DevOps ALM PaaS-as-SaaS and is in no way affiliated with, endorsed by, sponsored by, or otherwise connected to GitHub® or The Linux Foundation®.* 

*essesseff™ and the essesseff™ logo design are trademarks of essesseff LLC.*

*GITHUB®, the GITHUB® logo design and the INVERTOCAT logo design are trademarks of GitHub, Inc., registered in the United States and other countries.*

*Argo®, Helm®, Kubernetes® and K8s® are registered trademarks of The Linux Foundation.*

## essesseff App GitHub Repository Structure 

* Source: [hello-world (this repo)](https://github.com/essesseff-hello-world-fastapi-template/hello-world)
* Helm Config DEV: [hello-world-config-dev](https://github.com/essesseff-hello-world-fastapi-template/hello-world-config-dev)
* Helm Config QA: [hello-world-config-qa](https://github.com/essesseff-hello-world-fastapi-template/hello-world-config-qa)
* Helm Config STAGING: [hello-world-config-staging](https://github.com/essesseff-hello-world-fastapi-template/hello-world-config-staging)
* Helm Config PROD: [hello-world-config-prod](https://github.com/essesseff-hello-world-fastapi-template/hello-world-config-prod)
* Argo CD Config DEV: [hello-world-argocd-dev](https://github.com/essesseff-hello-world-fastapi-template/hello-world-argocd-dev)
* Argo CD Config QA: [hello-world-argocd-qa](https://github.com/essesseff-hello-world-fastapi-template/hello-world-argocd-qa)
* Argo CD Config STAGING: [hello-world-argocd-staging](https://github.com/essesseff-hello-world-fastapi-template/hello-world-argocd-staging)
* Argo CD Config PROD: [hello-world-argocd-prod](https://github.com/essesseff-hello-world-fastapi-template/hello-world-argocd-prod)

### Why so many repos?

essesseff favors simplicity and clear boundaries over a single repo with many rules.:

#### Simpler RBAC: 

Each repo is one permission boundary.  essesseff roles map directly to GitHub repo access (e.g. who can push to config-prod).  There are no path-based approval rules, CODEOWNERS, or branch policies to maintain—just straightforward repo-level permissions, i.e.:
  - Developer ~ DEV
  - QA Engineer ~ QA
  - Release Engineer ~ STAGING and PROD
  - DevOps Engineer ~ all of the above

#### Distinct change history and audit trail: 

Each environment has its own git history.  "What changed in prod?" means opening the prod config repo and reading the log.  No filtering a monorepo by path or digging through unrelated commits.  Blame, compliance, and rollbacks stay scoped to the environment.

#### Simplicity via separation: 

We chose "more repos, each with a single concern and simple rules" over "one repo with complex conventions to get the same isolation."  For a golden path and role-based control, that trade keeps the model easy to explain and operate.

*That said, if you prefer more of a DRY than WET approach to managing your Helm configs, this template does provide a fairly WET starting point only.  One way that you could take a more DRY approach while still retaining the benefits of the template as designed would be to separate the Helm Chart and any default values out from the app-/env-specific context(s) into other repo(s) (such as at an org or global context), and then also update your Argo CD config to first reference these as defaults and subsequently reference your app-/env-specific values.yaml.*

## Develop, Build and Deploy 

* **Branch Strategy**: Single `main` branch (trunk-based)
* **Auto-Build**: GitHub Actions image build runs on code push to `main` branch
* **Auto-Deploy**: DEV CI/CD deployment subsequent to successful image build (via [essesseff](https://essesseff.com) deployment orchestration)
* **ClickOps Promote/Deploy/Re-Deploy/Rollback**: DEV, QA, STAGING, PROD (via [essesseff](https://essesseff.com) UX)
* **GitOps Deploy**: DEV, QA, STAGING, PROD (managed by Argo CD by updating config-env values.yaml)
* **API Promote/Deploy**: DEV, QA, STAGING, PROD (via [essesseff public API](https://www.essesseff.com/docs/api))
* **K8s Namespace**: this template assumes a mapping of GitHub organization ~ K8s namespace i.e. string replace essesseff-hello-world-fastapi-template with your K8s namespace (or if an [essesseff](https://essesseff.com) subscriber, simply create an app from this template to have that standard convention enforced automatically)

## Golden Path App Template Architecture Diagram

![Golden Path App Template Diagram](https://www.essesseff.com/images/architecture/essesseff-app-template-minus-subscription-light-mode.svg)

*Note: GitHub and K8s Licensed and Hosted Separately. This diagram shows an example of three K8s-deployed apps following the build-once-deploy-many "essesseff app" model, each app with its own Source and Helm-config-env GitHub repos (and Argo CD GitHub repos (not shown)), and with deployments distributed across as few or as many K8s clusters as desired, both on an env-specific basis as well as on a one-or-many deployments per environment basis. The essesseff app templates easily support and provide standardized configuration and automation OOTB for all of the above.*

## Onboarding

### For essesseff subscribers

It is highly recommended that you use the [essesseff onboarding utility](https://www.essesseff.com/docs/deployment/essesseff-onboarding-utility) from a shell terminal with kubectl access to your K8s cluster(s) to onboard to essesseff, GitHub, Argo CD and K8s *typically in under 5 minutes* per essesseff app

Otherwise, you may similarly make use of the [essesseff public API](https://www.essesseff.com/docs/api) for onboarding and/or use the essesseff UX and shell terminal with kubectl access to your K8s cluster(s), in combination with onboarding scripts in your essesseff app argocd-env repos, to onboard your essesseff app(s) to essesseff, GitHub, Argo CD and K8s.

### If not an essesseff subscriber

It is highly recommended that you use the [essesseff onboarding utility](https://www.essesseff.com/docs/deployment/essesseff-onboarding-utility) in `--non-essesseff-subscriber-mode` from a shell terminal with kubectl access to your K8s cluster(s) to onboard to GitHub, Argo CD and K8s *typically in under 5 minutes* per essesseff app.  

Otherwise, you can still freely use all of the repos in this golden path template, edit app name and namespace labels according to your needs (typically via global string replacements in the file names and contents), and then run the onboarding scripts included in each of your argocd-env repos from a shell terminal with kubectl access to you K8s cluster(s) to get fully onboarded to GitHub, Argo CD and K8s in about ~20 minutes.

## Development Workflow

```bash
# 1. Create feature branch
git checkout -b feature/my-feature

# 2. Make changes and commit
git commit -am "Add feature"

# 3. Push and create PR
git push origin feature/my-feature

# 4. After review, merge to main
# This triggers automatic build

# 5. *If an essesseff subscriber*, upon successful build completion, Helm config-dev values.yaml will be automatically updated with the newly built image tag, triggering Argo CD DEV (see argocd-dev repo) to trigger automated deployment to DEV Kubernetes.

# 6. Use essesseff UI for promotions:
#    - Developer declares Release Candidate
#    - QA accepts RC → deploys to QA (or alternatively rejects the promotion of the RC to QA)
#    - QA marks as Stable (or alternatively rejects the promotion to Stable)
#    - Release Engineer deploys from Stable Release to STAGING/PROD
```

## Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Or run with uvicorn
uvicorn app:app --host 0.0.0.0 --port 8080 --workers 2
```

## Docker

```bash
# Build container
docker build -t hello-world-fastapi:local .

# Run container
docker run -p 8080:8080 hello-world-fastapi:local
```

## Endpoints

* `/` - Main page with version information
* `/health` - Health check (returns JSON)
* `/ready` - Readiness check (returns JSON)
* `/docs` - Interactive API documentation (Swagger UI)
* `/redoc` - Alternative API documentation (ReDoc)

## Environment Variables

* `PORT` - Port to run the application on (default: 8080)

## Project Structure

```
.
├── app.py              # Main FastAPI application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container definition
├── semver.txt         # Version tracking
├── .gitignore         # Git ignore patterns
└── README.md          # This file
```

## Testing

```bash
# Test health endpoint
curl http://localhost:8080/health

# Test readiness endpoint
curl http://localhost:8080/ready

# Test main page
curl http://localhost:8080/

# Interactive API docs
open http://localhost:8080/docs
```

## Deployment

The application is built automatically and ready to deploy to DEV environment after changes are merged to `main` branch and automatic code build succeeds. If an essesseff subscriber, essesseff updates the Helm config-dev values.yaml with the newly built image tag, triggering Argo CD DEV (see argocd-dev repo) to deploy the image and DEV config to Kubernetes DEV.  Promotion to QA, STAGING, and PROD environments is managed through the essesseff platform.

### Container Image Tags

Container images are tagged with the format:
```
{semver}-{git-hash}-{timestamp}
```

Example: `1.0.0-a1b2c3d-20231201T120000Z`

## CI/CD

GitHub Actions workflow (`.github/workflows/build.yml`) handles:
* Building the Docker image
* Pushing to GitHub Container Registry
* Generating build metadata
* Triggering essesseff deployment to DEV

## Health Checks

The application includes health check endpoints that can be used by:
* Kubernetes liveness/readiness probes
* Load balancers
* Monitoring systems

## Disclaimer
This software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

Use at your own risk. The maintainers of this project make no guarantees about its functionality, security, or suitability for any purpose.
