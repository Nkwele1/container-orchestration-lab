# Container Orchestration & DevSecOps Lab

## Overview
This project builds a complete container orchestration and DevSecOps pipeline from 
scratch, covering Docker, Kubernetes, Prometheus monitoring, GitLab CI/CD automation, 
and Ansible security hardening. Every phase maps directly to real world cloud 
engineering responsibilities in production DevSecOps environments.

## Architecture Overview

### Phase 1: Docker and Containerization

**Explain like I'm 5:**
Imagine you built a useful robot. You want to run copies of that robot anywhere 
without rebuilding it from scratch every time. So you pack the robot into a box with 
everything it needs to work. That box runs the same way on any computer. This phase 
builds that box from scratch using a Dockerfile and runs it locally.

**What was built:**
A Python web application containerized from scratch using Docker best practices. The 
app serves system information as a JSON response and demonstrates core containerization 
principles including non-root user execution, health checks, and environment variable 
configuration.

- Python web server built without external frameworks
- Dockerfile written from scratch with security best practices
- Non-root user execution to minimize container attack surface
- Built-in health check for container orchestration compatibility
- Environment variable configuration for portability across environments

### Phase 2: Kubernetes Deployment and Self-Healing

**Explain like I'm 5:**
Now that you have your robot box you want to run 3 copies of it at the same time and 
have a manager who automatically replaces any box that breaks. Kubernetes is that 
manager. This phase deploys 3 copies of the app and proves Kubernetes automatically 
replaces them when they fail.

**What was built:**
Deployed the containerized app to a local Kubernetes cluster using Minikube with 3 
replicas, a NodePort service for traffic routing, and demonstrated Kubernetes 
self-healing by deleting a pod and watching it automatically restart.

- Kubernetes Deployment with 3 replicas maintaining desired state
- Resource requests and limits enforcing compute boundaries per pod
- Liveness and readiness probes for health-based traffic routing
- NodePort service exposing the app within the cluster
- Self-healing demonstration — deleted pod replaced within seconds
- Load balancing across replicas verified via hostname changes

### Phase 3: Prometheus and Grafana Monitoring

**Explain like I'm 5:**
Now that your robots are running you need someone to watch them and report back on 
how they are doing. Prometheus is like a health monitor that checks every container 
every few seconds and records the results. Grafana is the dashboard that shows all 
that data in a visual way. This phase sets up real time monitoring for the entire 
cluster.

**What was built:**
Deployed the full kube-prometheus-stack using Helm, providing cluster wide monitoring 
with pre-built dashboards showing real time CPU usage, memory utilization, and pod 
health across all namespaces.

- Helm-based deployment of kube-prometheus-stack
- Prometheus scraping metrics from all cluster components
- Grafana dashboards showing live cluster resource utilization
- Container Insights across default, monitoring, and kube-system namespaces
- CPU and memory metrics per namespace and per pod

### Phase 4: GitLab CI/CD Pipeline

**Explain like I'm 5:**
Every time you update your code an automatic inspector shows up and checks everything 
before anyone can use it. The inspector lints your Dockerfile, validates your 
Kubernetes files, builds your container, tests it, and scans it for security 
vulnerabilities. If anything fails the inspector flags it immediately. This phase 
builds that automatic inspector using GitLab CI/CD.

**What was built:**
A complete GitLab CI/CD pipeline with 4 stages that runs automatically on every push. 
The pipeline validates infrastructure code, builds and tests the container, and scans 
for security vulnerabilities using Trivy.

- validate stage: Dockerfile linting with hadolint and Kubernetes manifest validation
- build stage: Docker image build tagged with git commit SHA for traceability
- test stage: Container health check in isolated environment
- security stage: Trivy vulnerability scan against known CVEs
- Pipeline triggers automatically on every push to main branch
- All stages use allow_failure for graceful degradation

### Phase 5: Ansible Security Hardening

**Explain like I'm 5:**
Imagine you need to set up 100 servers all exactly the same secure way. Without 
Ansible you would have to log into each one and manually run the same commands 100 
times. With Ansible you write a recipe once and it automatically configures all 100 
servers at the same time. This phase writes that recipe for security hardening.

**What was built:**
An Ansible playbook that automatically applies a security baseline to Linux servers. 
The playbook installs security tools, configures firewall rules, hardens authentication, 
and enables audit logging — all in a single automated run.

- Automated package updates to latest security patches
- fail2ban installation and configuration blocking brute force after 3 attempts
- UFW firewall with deny-by-default inbound rules
- Automatic security updates enabled for ongoing patch management
- Password policy enforcement with minimum 14 character length
- SSH hardening disabling root login and password authentication
- auditd configuration for system level audit logging
- Idempotent design — safe to run multiple times without side effects

## Technologies Used
- Python 3.11
- Docker
- Kubernetes (Minikube)
- Helm
- Prometheus
- Grafana
- GitLab CI/CD
- Ansible
- Trivy
- hadolint
- Bash scripting
- Git / GitHub / GitLab

## Repository Structure
container-orchestration-lab/
├── app.py                    # Python web application
├── Dockerfile                # Container image definition
├── deployment.yaml           # Kubernetes deployment manifest
├── service.yaml              # Kubernetes service manifest
├── .gitlab-ci.yml            # GitLab CI/CD pipeline
├── ansible/
│   ├── inventory.ini         # Ansible inventory file
│   └── security-hardening.yml # Security hardening playbook
└── README.md

## Prerequisites
- Docker Desktop
- Minikube
- kubectl
- Helm
- Ansible (via WSL on Windows)
- GitLab account

## How to Run

**Build and run the Docker container:**

    docker build -t swooplab:v1.0 .
    docker run -d -p 8080:8080 swooplab:v1.0

**Deploy to Kubernetes:**

    minikube start --driver=docker
    minikube image load swooplab:v1.0
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    minikube service swooplab-service --url

**Deploy Prometheus monitoring:**

    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update
    kubectl create namespace monitoring
    helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring

**Run Ansible security hardening:**

    cd ansible
    ansible-playbook -i inventory.ini security-hardening.yml

## Compliance Alignment
- NIST 800-53 CM-6 — Configuration Settings
- NIST 800-53 AC-6 — Least Privilege
- NIST 800-53 AU-2 — Audit Events
- NIST 800-53 SI-2 — Flaw Remediation
- CIS Benchmark hardening principles
- Zero Trust Architecture principles

## Skills Demonstrated
- Docker containerization from scratch
- Kubernetes deployment and orchestration
- Container self-healing and replica management
- Prometheus and Grafana monitoring stack deployment
- GitLab CI/CD pipeline design and configuration
- Ansible playbook development for security hardening
- Linux security baseline configuration
- DevSecOps pipeline integration
- Infrastructure as Code principles
- Security scanning and vulnerability management