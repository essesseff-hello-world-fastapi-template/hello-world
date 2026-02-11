# hello-world Application (FastAPI)

Python FastAPI implementation with trunk-based development and GitOps-driven deployments via Argo CD to Kubernetes (see related repositories), with *optional* process orchestration, reporting, etc. via the essesseff DevOps platform available on a per essesseff app subscription.

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

## Develop, Build and Deploy 

* **Branch Strategy**: Single `main` branch (trunk-based)
* **Auto-Build**: GitHub Actions image build runs on code push to `main` branch
* **Auto-Deploy**: DEV CI/CD deployment subsequent to successful image build (via essesseff deployment orchestration)
* **ClickOps Promote/Deploy/Re-Deploy/Rollback**: DEV, QA, STAGING, PROD (via essesseff UX)
* **GitOps Deploy**: DEV, QA, STAGING, PROD (managed by Argo CD by updating config-env Chart.yaml/values.yaml)
* **API Promote/Deploy**: DEV, QA, STAGING, PROD (via essesseff public API)

## Golden Path App Template Architecture Diagram

![Golden Path App Template Diagram](https://www.essesseff.com/images/architecture/essesseff-app-template-minus-subscription-light-mode.svg)

*Note: GitHub and K8s Licensed and Hosted Separately. This diagram shows an example of three K8s-deployed apps following the build-once-deploy-many "essesseff app" model, each app with its own Source and Helm-config-env GitHub repos (and Argo CD GitHub repos (not shown)), and with deployments distributed across as few or as many K8s clusters as desired, both on an env-specific basis as well as on a one-or-many deployments per environment basis. The essesseff app templates easily support and provide standardized configuration and automation OOTB for all of the above.*

## Onboarding

**If an essesseff subscriber**, it is highly recommended that you use the [essesseff onboarding utility](https://www.essesseff.com/docs/deployment/essesseff-onboarding-utility) from a shell terminal with kubectl access to your K8s cluster(s) to onboard to essesseff, GitHub, Argo CD and K8s typically in under 5 minutes per essesseff app, or otherwise similarly make use of the [essesseff public API](https://www.essesseff.com/docs/api) for onboarding.  Otherwise, the essesseff UX and shell terminal with kubectl access to your K8s cluster(s), in combination with onboarding scripts in your essesseff app argocd-env repos, may also be used to onboard your essesseff app(s) to essesseff, GitHub, Argo CD and K8s.

**If not an essesseff subscriber**, you can still freely use all of the repos in this golden path template, edit app name and namespace labels according to your needs (typically via global string replacements in the file names and contents), and then run the onboarding scripts included in each of your argocd-env repos from a shell terminal with kubectl access to you K8s cluster(s) to get fully onboarded to GitHub, Argo CD and K8s in about ~20 minutes.

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

# 5. *If an essesseff subscriber*, upon successful build completion, Helm config-dev Chart.yaml and values.yaml will be automatically updated with the newly built image tag, triggering Argo CD DEV (see argocd-dev repo) to trigger automated deployment to DEV Kubernetes.

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

The application is built automatically and ready to deploy to DEV environment after changes are merged to `main` branch and automatic code build succeeds. If an essesseff subscriber, essesseff updates the Helm config-dev Chart.yaml and values.yaml with the newly built image tag, triggering Argo CD DEV (see argocd-dev repo) to deploy the image and DEV config to Kubernetes DEV.  Promotion to QA, STAGING, and PROD environments is managed through the essesseff platform.

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
