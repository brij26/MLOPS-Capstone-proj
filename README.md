````markdown
# 🚀 End-to-End MLOps Capstone Project

### 🧠 Machine Learning | 🧩 DVC | ☁️ AWS (ECR + EKS) | 🧰 CI/CD (GitHub Actions) | 📊 Monitoring with Prometheus & Grafana

---

## 📖 Overview

This project represents a **complete MLOps pipeline** — from experiment tracking and version control to containerization, CI/CD automation, cloud deployment, and monitoring.

It demonstrates **industry-standard practices** for managing the ML lifecycle using **MLFlow, DVC, Docker, AWS ECR/EKS, Prometheus, and Grafana**.

---

---

## ⚙️ Major Features

✅ **Cookiecutter Data Science Template** — for clean, modular project organization
✅ **MLFlow + Dagshub** — experiment tracking and model registry and model serving
✅ **DVC (Data Version Control)** — tracks dataset and model versioning
✅ **AWS S3 Remote Storage** — stores data and model artifacts securely
✅ **Flask App** — deployable ML inference API
✅ **Dockerized Application** — consistent and portable environment
✅ **CI/CD with GitHub Actions** — automated build, test, and deployment pipeline
✅ **AWS ECR + EKS** — production-grade container orchestration
✅ **Prometheus & Grafana** — real-time monitoring and visualization

---

## 🧩 Step-by-Step Workflow

### 🏗️ 1. Project Setup

1. Initialize repo locally using Cookiecutter Data Science:
   ```bash
   conda create -n atlas python=3.10
   conda activate atlas
   pip install cookiecutter
   cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
   ```
````

````

2. Setup source folders (`src/`), rename `models` → `model`.
3. Initialize git and push to GitHub.

---

### 🧪 2. MLFlow Tracking with DagsHub

- Created DagsHub repository and connected it with GitHub.
- Installed `dagshub` and `mlflow` for experiment tracking.
- Logged metrics, parameters, and artifacts using MLFlow UI.

```python
import dagshub
dagshub.init(repo_name="MLOPS-Capstone-proj", mlflow=True)
```

---

### 📦 3. Data Versioning with DVC

- Initialized DVC:

  ```bash
  dvc init
  dvc remote add -d mylocal local_s3
  ```

- Added pipeline stages in `dvc.yaml`:

  - Data ingestion → preprocessing → feature engineering → model training → evaluation

- Configured `params.yaml` for tunable parameters.

- Linked AWS S3 as remote:

  ```bash
  aws configure
  dvc remote add -d myremote s3://<bucket-name>
  ```

---

### 🔥 4. Flask Application

- Developed a lightweight Flask app (`flask_app/app.py`) for model inference.
- Integrated ML model artifact loading and endpoint testing.
- Ran locally:

  ```bash
  python app.py
  ```

---

### 🐳 5. Dockerization

- Installed `pipreqs` to auto-generate dependencies:

  ```bash
  pipreqs . --force
  ```

- Built and ran Docker image:

  ```bash
  docker build -t capstone-app:latest .
  docker run -p 8888:5000 -e CAPSTONE_PROJ=<token> capstone-app:latest
  ```

- (Optional) Pushed image to DockerHub.

---

### ⚡ 6. CI/CD with GitHub Actions

- Configured `.github/workflows/ci.yaml` to automate:

  - Dependency installation
  - Code testing (`pytest`)
  - Docker image build
  - Push image to AWS ECR
  - Deploy to EKS

- Added GitHub secrets for:

  ```
  AWS_ACCESS_KEY_ID
  AWS_SECRET_ACCESS_KEY
  AWS_REGION
  ECR_REPOSITORY
  AWS_ACCOUNT_ID
  CAPSTONE_PROJ
  ```

---

### ☁️ 7. AWS EKS Deployment

- Installed & configured:

  - **AWS CLI**, **kubectl**, **eksctl**

- Created EKS Cluster:

  ```bash
  eksctl create cluster \
    --name flask-app-cluster \
    --region us-east-1 \
    --node-type t3.small \
    --nodes 1 --managed
  ```

- Verified:

  ```bash
  kubectl get nodes
  kubectl get svc
  ```

- Exposed LoadBalancer service:

  ```bash
  kubectl get svc flask-app-service
  ```

- Accessed app via:

  ```
  http://a123b8a3751df4bd8ae72212bbfd34b6-1071991751.us-east-1.elb.amazonaws.com:5000
  ```

---

### 📈 8. Monitoring with Prometheus & Grafana

#### 🧭 Prometheus

- Installed on Ubuntu EC2 (port `9090`)
- Configured targets to scrape metrics from Flask app:

  ```yaml
  scrape_configs:
    - job_name: "flask-app"
      static_configs:
        - targets:
            [
              "a123b8a3751df4bd8ae72212bbfd34b6-1071991751.us-east-1.elb.amazonaws.com:5000",
            ]
  ```

#### 📊 Grafana

- Installed on another EC2 (port `3000`)
- Connected Prometheus as a data source.
- Built real-time dashboards for app health and performance.

---

## 🧰 Tech Stack

| Layer                      | Tools                    |
| -------------------------- | ------------------------ |
| **Version Control**        | Git, GitHub              |
| **Experiment Tracking**    | MLflow, Dagshub          |
| **Data Versioning**        | DVC                      |
| **Storage**                | AWS S3                   |
| **Containerization**       | Docker                   |
| **CI/CD**                  | GitHub Actions           |
| **Orchestration**          | AWS EKS                  |
| **Monitoring**             | Prometheus, Grafana      |
| **Backend API**            | Flask                    |
| **Infrastructure as Code** | eksctl, kubectl, AWS CLI |

---

## 🧠 Learnings & Highlights

- Implemented **end-to-end automation** for ML workflows.
- Hands-on experience with **AWS Cloud deployment** using ECR & EKS.
- Learned **model versioning, experiment tracking**, and **pipeline orchestration** using DVC.
- Built **observability dashboards** with Prometheus & Grafana.
- Designed a **production-ready CI/CD pipeline** integrated with GitHub Actions.

---

## 🪄 Final Output

Once deployed successfully, your app will be available at:

> 🌐 `http://a123b8a3751df4bd8ae72212bbfd34b6-1071991751.us-east-1.elb.amazonaws.com::5000`

You can view real-time metrics in:

> 📊 Grafana Dashboard → `http://<Grafana-EC2-IP>:3000`

and

> 🧭 Prometheus UI → `http://<Prometheus-EC2-IP>:9090`

## 🤝 Connect with Me

📧 **Email:** [brijrpatel076@gmail.com]
💼 **LinkedIn:** [https://www.linkedin.com/in/brij-r-patel-800a41256/]
💻 **GitHub:** [https://github.com/brij26]

---

⭐ _If you like this project, don’t forget to give it a star!_ ⭐

```

---


```
````
