# 🚀 End-to-End MLOps Capstone Project

<div align="center">

![MLOps](https://img.shields.io/badge/MLOps-Production%20Ready-brightgreen?style=for-the-badge)
![AWS](https://img.shields.io/badge/AWS-EKS%20%7C%20ECR-orange?style=for-the-badge&logo=amazon-aws)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?style=for-the-badge&logo=github)

**A production-grade Machine Learning Operations pipeline showcasing industry best practices**

[Features](#-key-features) • [Architecture](#-architecture) • [Setup](#-quick-start) • [Deployment](#-deployment) • [Monitoring](#-monitoring)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [Workflow](#-detailed-workflow)
- [Deployment](#-deployment)
- [Monitoring](#-monitoring)
- [API Endpoints](#-api-endpoints)
- [Learnings](#-key-learnings)
- [Connect](#-connect-with-me)

---

## 🌟 Overview

This project demonstrates a **complete MLOps pipeline** — from experiment tracking and version control to containerization, CI/CD automation, cloud deployment, and real-time monitoring. Built with industry-standard tools and practices, it showcases how to take ML models from development to production seamlessly.

### What Makes This Special?

- 🎯 **Production-Ready**: Fully automated CI/CD pipeline with zero-downtime deployments
- 📊 **Experiment Tracking**: Complete model lineage and versioning with MLflow
- 🔄 **Reproducibility**: DVC ensures consistent data and model versions across environments
- ☁️ **Cloud-Native**: Deployed on AWS EKS with auto-scaling capabilities
- 📈 **Observable**: Real-time monitoring with Prometheus and Grafana dashboards

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### Development & Tracking

- ✅ Cookiecutter Data Science structure
- ✅ MLFlow + DagsHub integration
- ✅ DVC for data/model versioning
- ✅ AWS S3 remote storage
- ✅ Parameterized pipelines

</td>
<td width="50%">

### Deployment & Operations

- ✅ Flask REST API
- ✅ Docker containerization
- ✅ GitHub Actions CI/CD
- ✅ AWS ECR + EKS deployment
- ✅ Prometheus & Grafana monitoring

</td>
</tr>
</table>

---

## 🏗️ Architecture

```
┌─────────────────┐      ┌──────────────┐      ┌─────────────────┐
│   Development   │──────▶│   GitHub     │──────▶│   CI/CD        │
│   (Local)       │      │   Repository │      │   (Actions)     │
└─────────────────┘      └──────────────┘      └─────────────────┘
        │                                               │
        │                                               ▼
        ▼                                      ┌─────────────────┐
┌─────────────────┐                           │   AWS ECR       │
│   MLflow        │                           │   (Container    │
│   + DagsHub     │                           │    Registry)    │
└─────────────────┘                           └─────────────────┘
        │                                               │
        │                                               ▼
        ▼                                      ┌─────────────────┐
┌─────────────────┐                           │   AWS EKS       │
│   DVC + S3      │                           │   (Kubernetes)  │
│   (Versioning)  │                           └─────────────────┘
└─────────────────┘                                    │
                                                       ▼
                                              ┌─────────────────┐
                                              │  Monitoring     │
                                              │  Prometheus +   │
                                              │  Grafana        │
                                              └─────────────────┘
```

---

## 🛠️ Tech Stack

<table>
<tr>
<td align="center" width="20%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="48" height="48" alt="Python"/>
<br><strong>Python</strong>
</td>
<td align="center" width="20%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="48" height="48" alt="Docker"/>
<br><strong>Docker</strong>
</td>
<td align="center" width="20%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg" width="48" height="48" alt="AWS"/>
<br><strong>AWS</strong>
</td>
<td align="center" width="20%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg" width="48" height="48" alt="Kubernetes"/>
<br><strong>Kubernetes</strong>
</td>
<td align="center" width="20%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="48" height="48" alt="GitHub Actions"/>
<br><strong>CI/CD</strong>
</td>
</tr>
</table>

| **Category**         | **Technologies**              |
| -------------------- | ----------------------------- |
| **ML & Tracking**    | MLflow, DagsHub, Scikit-learn |
| **Version Control**  | Git, GitHub, DVC              |
| **Storage**          | AWS S3                        |
| **API**              | Flask, REST                   |
| **Containerization** | Docker                        |
| **Orchestration**    | AWS EKS, kubectl, eksctl      |
| **CI/CD**            | GitHub Actions                |
| **Monitoring**       | Prometheus, Grafana           |
| **Infrastructure**   | AWS CLI, IAM                  |

---

## 🚀 Quick Start

### Prerequisites

```bash
# Required installations
- Python 3.10+
- Docker
- AWS CLI
- kubectl
- eksctl
- Git
```

### Installation

1️⃣ **Clone the repository**

```bash
git clone https://github.com/brij26/MLOPS-Capstone-proj.git
cd MLOPS-Capstone-proj
```

2️⃣ **Create virtual environment**

```bash
conda create -n atlas python=3.10
conda activate atlas
pip install -r requirements.txt
```

3️⃣ **Configure DVC and AWS**

```bash
# Initialize DVC
dvc init

# Configure AWS credentials
aws configure

# Add S3 remote
dvc remote add -d myremote s3://<your-bucket-name>
```

4️⃣ **Run the pipeline**

```bash
dvc repro
```

5️⃣ **Start Flask app locally**

```bash
python flask_app/app.py
```

---

## 📖 Detailed Workflow

### 1. Project Initialization

Set up a clean, modular project structure using Cookiecutter Data Science template.

```bash
cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
```

### 2. Experiment Tracking with MLflow & DagsHub

Track experiments, log metrics, parameters, and artifacts:

```python
import dagshub
import mlflow

dagshub.init(repo_name="MLOPS-Capstone-proj", mlflow=True)

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("model.pkl")
```

### 3. Data Version Control with DVC

Create reproducible ML pipelines:

```yaml
# dvc.yaml
stages:
  data_ingestion:
    cmd: python src/data/load_data.py
    deps:
      - src/data/load_data.py
    outs:
      - data/raw

  preprocessing:
    cmd: python src/features/preprocess.py
    deps:
      - data/raw
    outs:
      - data/processed
```

### 4. Dockerization

Build consistent, portable containers:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "flask_app/app.py"]
```

Build and run:

```bash
docker build -t capstone-app:latest .
docker run -p 8888:5000 -e CAPSTONE_PROJ=<token> capstone-app:latest
```

### 5. CI/CD Pipeline

GitHub Actions automate the entire deployment:

- ✅ Code checkout
- ✅ Dependency installation
- ✅ Testing with pytest
- ✅ Docker image build
- ✅ Push to AWS ECR
- ✅ Deploy to EKS

---

## ☁️ Deployment

### AWS EKS Setup

1️⃣ **Create EKS Cluster**

```bash
eksctl create cluster \
  --name flask-app-cluster \
  --region us-east-1 \
  --node-type t3.small \
  --nodes 1 \
  --managed
```

2️⃣ **Verify Cluster**

```bash
kubectl get nodes
kubectl get svc
```

3️⃣ **Deploy Application**

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

4️⃣ **Access Application**

```bash
kubectl get svc flask-app-service
# Access via LoadBalancer URL
```

### GitHub Secrets Required

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
ECR_REPOSITORY
AWS_ACCOUNT_ID
CAPSTONE_PROJ
```

---

## 📊 Monitoring

### Prometheus Setup

Monitor application metrics in real-time:

```yaml
# prometheus.yml
scrape_configs:
  - job_name: "flask-app"
    static_configs:
      - targets: ["<load-balancer-url>:5000"]
```

**Access**: `http://<prometheus-ec2-ip>:9090`

### Grafana Dashboards

Visualize metrics with custom dashboards:

1. Add Prometheus as data source
2. Create dashboards for:
   - Request rate
   - Response time
   - Error rate
   - Resource utilization

**Access**: `http://<grafana-ec2-ip>:3000`

---

## 🔌 API Endpoints

### Health Check

```bash
GET /health
```

### Prediction

```bash
POST /predict
Content-Type: application/json

{
  "features": [...]
}
```

### Metrics

```bash
GET /metrics
```

---

## 🎓 Key Learnings

This project provided hands-on experience with:

- 🔄 **End-to-end ML automation** from training to deployment
- ☁️ **Cloud-native deployment** on AWS with EKS
- 📦 **Container orchestration** using Kubernetes
- 🔍 **Model versioning** and experiment tracking
- 📈 **Production monitoring** and observability
- 🚀 **CI/CD best practices** with GitHub Actions
- 🎯 **Reproducible ML pipelines** with DVC

---

## 🌐 Live Demo

🚀 **Application**: `http://a123b8a3751df4bd8ae72212bbfd34b6-1071991751.us-east-1.elb.amazonaws.com:5000`

📊 **Grafana Dashboard**: `http://<grafana-ip>:3000`

🎯 **Prometheus Metrics**: `http://<prometheus-ip>:9090`

---

## 📚 Documentation

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [DVC Documentation](https://dvc.org/doc)
- [AWS EKS Guide](https://docs.aws.amazon.com/eks/)
- [Prometheus Guide](https://prometheus.io/docs/)

---

## 🤝 Connect With Me

<div align="center">

[![Email](https://img.shields.io/badge/Email-brijrpatel076%40gmail.com-red?style=for-the-badge&logo=gmail)](mailto:brijrpatel076@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Brij%20R%20Patel-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/brij-r-patel-800a41256/)
[![GitHub](https://img.shields.io/badge/GitHub-brij26-black?style=for-the-badge&logo=github)](https://github.com/brij26)

</div>

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### ⭐ If you found this project helpful, please give it a star!

**Made with ❤️ and ☕ by [Brij R Patel](https://github.com/brij26)**

</div>
