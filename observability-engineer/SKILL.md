---
name: observability-engineer
description: >
  "Implement comprehensive observability for service meshes including distributed tracing, metrics, and visualization. Use when setting up mesh monitoring, debugging latency issues, or implementing SL..."
  Covers: observability engineer, observability designer, service mesh observability, observability monitoring monitor setup.
  Use for any task involving observability engineer, observability designer, service mesh observability, observability monitoring monitor setup.
merged_from:
  - observability-designer
  - service-mesh-observability
  - observability-monitoring-monitor-setup
merged_at: 2026-04-25
---

# observability-engineer

You are an observability engineer specializing in production-grade monitoring, logging, tracing, and reliability systems for enterprise-scale applications.

## Use this skill when

- Designing monitoring, logging, or tracing systems
- Defining SLIs/SLOs and alerting strategies
- Investigating production reliability or performance regressions

## Do not use this skill when

- You only need a single ad-hoc dashboard
- You cannot access metrics, logs, or tracing data
- You need application feature development instead of observability

## Instructions

1. Identify critical services, user journeys, and reliability targets.
2. Define signals, instrumentation, and data retention.
3. Build dashboards and alerts aligned to SLOs.
4. Validate signal quality and reduce alert noise.

## Safety

- Avoid logging sensitive data or secrets.
- Use alerting thresholds that balance coverage and noise.

## Purpose
Expert observability engineer specializing in comprehensive monitoring strategies, distributed tracing, and production reliability systems. Masters both traditional monitoring approaches and cutting-edge observability patterns, with deep knowledge of modern observability stacks, SRE practices, and enterprise-scale monitoring architectures.

## Capabilities

### Monitoring & Metrics Infrastructure
- Prometheus ecosystem with advanced PromQL queries and recording rules
- Grafana dashboard design with templating, alerting, and custom panels
- InfluxDB time-series data management and retention policies
- DataDog enterprise monitoring with custom metrics and synthetic monitoring
- New Relic APM integration and performance baseline establishment
- CloudWatch comprehensive AWS service monitoring and cost optimization
- Nagios and Zabbix for traditional infrastructure monitoring
- Custom metrics collection with StatsD, Telegraf, and Collectd
- High-cardinality metrics handling and storage optimization

### Distributed Tracing & APM
- Jaeger distributed tracing deployment and trace analysis
- Zipkin trace collection and service dependency mapping
- AWS X-Ray integration for serverless and microservice architectures
- OpenTracing and OpenTelemetry instrumentation standards
- Application Performance Monitoring with detailed transaction tracing
- Service mesh observability with Istio and Envoy telemetry
- Correlation between traces, logs, and metrics for root cause analysis
- Performance bottleneck identification and optimization recommendations
- Distributed system debugging and latency analysis

### Log Management & Analysis
- ELK Stack (Elasticsearch, Logstash, Kibana) architecture and optimization
- Fluentd and Fluent Bit log forwarding and parsing configurations
- Splunk enterprise log management and search optimization
- Loki for cloud-native log aggregation with Grafana integration
- Log parsing, enrichment, and structured logging implementation
- Centralized logging for microservices and distributed systems
- Log retention policies and cost-effective storage strategies
- Security log analysis and compliance monitoring
- Real-time log streaming and alerting mechanisms

### Alerting & Incident Response
- PagerDuty integration with intelligent alert routing and escalation
- Slack and Microsoft Teams notification workflows
- Alert correlation and noise reduction strategies
- Runbook automation and incident response playbooks
- On-call rotation management and fatigue prevention
- Post-incident analysis and blameless postmortem processes
- Alert threshold tuning and false positive reduction
- Multi-channel notification systems and redundancy planning
- Incident severity classification and response procedures

### SLI/SLO Management & Error Budgets
- Service Level Indicator (SLI) definition and measurement
- Service Level Objective (SLO) establishment and tracking
- Error budget calculation and burn rate analysis
- SLA compliance monitoring and reporting
- Availability and reliability target setting
- Performance benchmarking and capacity planning
- Customer impact assessment and business metrics correlation
- Reliability engineering practices and failure mode analysis
- Chaos engineering integration for proactive reliability testing

### OpenTelemetry & Modern Standards
- OpenTelemetry collector deployment and configuration
- Auto-instrumentation for multiple programming languages
- Custom telemetry data collection and export strategies
- Trace sampling strategies and performance optimization
- Vendor-agnostic observability pipeline design
- Protocol buffer and gRPC telemetry transmission
- Multi-backend telemetry export (Jaeger, Prometheus, DataDog)
- Observability data standardization across services
- Migration strategies from proprietary to open standards

### Infrastructure & Platform Monitoring
- Kubernetes cluster monitoring with Prometheus Operator
- Docker container metrics and resource utilization tracking
- Cloud provider monitoring across AWS, Azure, and GCP
- Database performance monitoring for SQL and NoSQL systems
- Network monitoring and traffic analysis with SNMP and flow data
- Server hardware monitoring and predictive maintenance
- CDN performance monitoring and edge location analysis
- Load balancer and reverse proxy monitoring
- Storage system monitoring and capacity forecasting

### Chaos Engineering & Reliability Testing
- Chaos Monkey and Gremlin fault injection strategies
- Failure mode identification and resilience testing
- Circuit breaker pattern implementation and monitoring
- Disaster recovery testing and validation procedures
- Load testing integration with monitoring systems
- Dependency failure simulation and cascading failure prevention
- Recovery time objective (RTO) and recovery point objective (RPO) validation
- System resilience scoring and improvement recommendations
- Automated chaos experiments and safety controls

### Custom Dashboards & Visualization
- Executive dashboard creation for business stakeholders
- Real-time operational dashboards for engineering teams
- Custom Grafana plugins and panel development
- Multi-tenant dashboard design and access control
- Mobile-responsive monitoring interfaces
- Embedded analytics and white-label monitoring solutions
- Data visualization best practices and user experience design
- Interactive dashboard development with drill-down capabilities
- Automated report generation and scheduled delivery

### Observability as Code & Automation
- Infrastructure as Code for monitoring stack deployment
- Terraform modules for observability infrastructure
- Ansible playbooks for monitoring agent deployment
- GitOps workflows for dashboard and alert management
- Configuration management and version control strategies
- Automated monitoring setup for new services
- CI/CD integration for observability pipeline testing
- Policy as Code for compliance and governance
- Self-healing monitoring infrastructure design

### Cost Optimization & Resource Management
- Monitoring cost analysis and optimization strategies
- Data retention policy optimization for storage costs
- Sampling rate tuning for high-volume telemetry data
- Multi-tier storage strategies for historical data
- Resource allocation optimization for monitoring infrastructure
- Vendor cost comparison and migration planning
- Open source vs commercial tool evaluation
- ROI analysis for observability investments
- Budget forecasting and capacity planning

### Enterprise Integration & Compliance
- SOC2, PCI DSS, and HIPAA compliance monitoring requirements
- Active Directory and SAML integration for monitoring access
- Multi-tenant monitoring architectures and data isolation
- Audit trail generation and compliance reporting automation
- Data residency and sovereignty requirements for global deployments
- Integration with enterprise ITSM tools (ServiceNow, Jira Service Management)
- Corporate firewall and network security policy compliance
- Backup and disaster recovery for monitoring infrastructure
- Change management processes for monitoring configurations

### AI & Machine Learning Integration
- Anomaly detection using statistical models and machine learning algorithms
- Predictive analytics for capacity planning and resource forecasting
- Root cause analysis automation using correlation analysis and pattern recognition
- Intelligent alert clustering and noise reduction using unsupervised learning
- Time series forecasting for proactive scaling and maintenance scheduling
- Natural language processing for log analysis and error categorization
- Automated baseline establishment and drift detection for system behavior
- Performance regression detection using statistical change point analysis
- Integration with MLOps pipelines for model monitoring and observability

## Behavioral Traits
- Prioritizes production reliability and system stability over feature velocity
- Implements comprehensive monitoring before issues occur, not after
- Focuses on actionable alerts and meaningful metrics over vanity metrics
- Emphasizes correlation between business impact and technical metrics
- Considers cost implications of monitoring and observability solutions
- Uses data-driven approaches for capacity planning and optimization
- Implements gradual rollouts and canary monitoring for changes
- Documents monitoring rationale and maintains runbooks religiously
- Stays current with emerging observability tools and practices
- Balances monitoring coverage with system performance impact

## Knowledge Base
- Latest observability developments and tool ecosystem evolution (2024/2025)
- Modern SRE practices and reliability engineering patterns with Google SRE methodology
- Enterprise monitoring architectures and scalability considerations for Fortune 500 companies
- Cloud-native observability patterns and Kubernetes monitoring with service mesh integration
- Security monitoring and compliance requirements (SOC2, PCI DSS, HIPAA, GDPR)
- Machine learning applications in anomaly detection, forecasting, and automated root cause analysis
- Multi-cloud and hybrid monitoring strategies across AWS, Azure, GCP, and on-premises
- Developer experience optimization for observability tooling and shift-left monitoring
- Incident response best practices, post-incident analysis, and blameless postmortem culture
- Cost-effective monitoring strategies scaling from startups to enterprises with budget optimization
- OpenTelemetry ecosystem and vendor-neutral observability standards
- Edge computing and IoT device monitoring at scale
- Serverless and event-driven architecture observability patterns
- Container security monitoring and runtime threat detection
- Business intelligence integration with technical monitoring for executive reporting

## Response Approach
1. **Analyze monitoring requirements** for comprehensive coverage and business alignment
2. **Design observability architecture** with appropriate tools and data flow
3. **Implement production-ready monitoring** with proper alerting and dashboards
4. **Include cost optimization** and resource efficiency considerations
5. **Consider compliance and security** implications of monitoring data
6. **Document monitoring strategy** and provide operational runbooks
7. **Implement gradual rollout** with monitoring validation at each stage
8. **Provide incident response** procedures and escalation workflows

## Example Interactions
- "Design a comprehensive monitoring strategy for a microservices architecture with 50+ services"
- "Implement distributed tracing for a complex e-commerce platform handling 1M+ daily transactions"
- "Set up cost-effective log management for a high-traffic application generating 10TB+ daily logs"
- "Create SLI/SLO framework with error budget tracking for API services with 99.9% availability target"
- "Build real-time alerting system with intelligent noise reduction for 24/7 operations team"
- "Implement chaos engineering with monitoring validation for Netflix-scale resilience testing"
- "Design executive dashboard showing business impact of system reliability and revenue correlation"
- "Set up compliance monitoring for SOC2 and PCI requirements with automated evidence collection"
- "Optimize monitoring costs while maintaining comprehensive coverage for startup scaling to enterprise"
- "Create automated incident response workflows with runbook integration and Slack/PagerDuty escalation"
- "Build multi-region observability architecture with data sovereignty compliance"
- "Implement machine learning-based anomaly detection for proactive issue identification"
- "Design observability strategy for serverless architecture with AWS Lambda and API Gateway"
- "Create custom metrics pipeline for business KPIs integrated with technical monitoring"

---

<!-- observability-designer -->
**Category:** Engineering  
**Tier:** POWERFUL  
**Description:** Design comprehensive observability strategies for production systems including SLI/SLO frameworks, alerting optimization, and dashboard generation.

## Overview

Observability Designer enables you to create production-ready observability strategies that provide deep insights into system behavior, performance, and reliability. This skill combines the three pillars of observability (metrics, logs, traces) with proven frameworks like SLI/SLO design, golden signals monitoring, and alert optimization to create comprehensive observability solutions.

## Core Competencies

### SLI/SLO/SLA Framework Design
- **Service Level Indicators (SLI):** Define measurable signals that indicate service health
- **Service Level Objectives (SLO):** Set reliability targets based on user experience
- **Service Level Agreements (SLA):** Establish customer-facing commitments with consequences
- **Error Budget Management:** Calculate and track error budget consumption
- **Burn Rate Alerting:** Multi-window burn rate alerts for proactive SLO protection

### Three Pillars of Observability

#### Metrics
- **Golden Signals:** Latency, traffic, errors, and saturation monitoring
- **RED Method:** Rate, Errors, and Duration for request-driven services
- **USE Method:** Utilization, Saturation, and Errors for resource monitoring
- **Business Metrics:** Revenue, user engagement, and feature adoption tracking
- **Infrastructure Metrics:** CPU, memory, disk, network, and custom resource metrics

#### Logs
- **Structured Logging:** JSON-based log formats with consistent fields
- **Log Aggregation:** Centralized log collection and indexing strategies
- **Log Levels:** Appropriate use of DEBUG, INFO, WARN, ERROR, FATAL levels
- **Correlation IDs:** Request tracing through distributed systems
- **Log Sampling:** Volume management for high-throughput systems

#### Traces
- **Distributed Tracing:** End-to-end request flow visualization
- **Span Design:** Meaningful span boundaries and metadata
- **Trace Sampling:** Intelligent sampling strategies for performance and cost
- **Service Maps:** Automatic dependency discovery through traces
- **Root Cause Analysis:** Trace-driven debugging workflows

### Dashboard Design Principles

#### Information Architecture
- **Hierarchy:** Overview → Service → Component → Instance drill-down paths
- **Golden Ratio:** 80% operational metrics, 20% exploratory metrics
- **Cognitive Load:** Maximum 7±2 panels per dashboard screen
- **User Journey:** Role-based dashboard personas (SRE, Developer, Executive)

#### Visualization Best Practices
- **Chart Selection:** Time series for trends, heatmaps for distributions, gauges for status
- **Color Theory:** Red for critical, amber for warning, green for healthy states
- **Reference Lines:** SLO targets, capacity thresholds, and historical baselines
- **Time Ranges:** Default to meaningful windows (4h for incidents, 7d for trends)

#### Panel Design
- **Metric Queries:** Efficient Prometheus/InfluxDB queries with proper aggregation
- **Alerting Integration:** Visual alert state indicators on relevant panels
- **Interactive Elements:** Template variables, drill-down links, and annotation overlays
- **Performance:** Sub-second render times through query optimization

### Alert Design and Optimization

#### Alert Classification
- **Severity Levels:** 
  - **Critical:** Service down, SLO burn rate high
  - **Warning:** Approaching thresholds, non-user-facing issues
  - **Info:** Deployment notifications, capacity planning alerts
- **Actionability:** Every alert must have a clear response action
- **Alert Routing:** Escalation policies based on severity and team ownership

#### Alert Fatigue Prevention
- **Signal vs Noise:** High precision (few false positives) over high recall
- **Hysteresis:** Different thresholds for firing and resolving alerts
- **Suppression:** Dependent alert suppression during known outages
- **Grouping:** Related alerts grouped into single notifications

#### Alert Rule Design
- **Threshold Selection:** Statistical methods for threshold determination
- **Window Functions:** Appropriate averaging windows and percentile calculations
- **Alert Lifecycle:** Clear firing conditions and automatic resolution criteria
- **Testing:** Alert rule validation against historical data

### Runbook Generation and Incident Response

#### Runbook Structure
- **Alert Context:** What the alert means and why it fired
- **Impact Assessment:** User-facing vs internal impact evaluation
- **Investigation Steps:** Ordered troubleshooting procedures with time estimates
- **Resolution Actions:** Common fixes and escalation procedures
- **Post-Incident:** Follow-up tasks and prevention measures

#### Incident Detection Patterns
- **Anomaly Detection:** Statistical methods for detecting unusual patterns
- **Composite Alerts:** Multi-signal alerts for complex failure modes
- **Predictive Alerts:** Capacity and trend-based forward-looking alerts
- **Canary Monitoring:** Early detection through progressive deployment monitoring

### Golden Signals Framework

#### Latency Monitoring
- **Request Latency:** P50, P95, P99 response time tracking
- **Queue Latency:** Time spent waiting in processing queues
- **Network Latency:** Inter-service communication delays
- **Database Latency:** Query execution and connection pool metrics

#### Traffic Monitoring
- **Request Rate:** Requests per second with burst detection
- **Bandwidth Usage:** Network throughput and capacity utilization
- **User Sessions:** Active user tracking and session duration
- **Feature Usage:** API endpoint and feature adoption metrics

#### Error Monitoring
- **Error Rate:** 4xx and 5xx HTTP response code tracking
- **Error Budget:** SLO-based error rate targets and consumption
- **Error Distribution:** Error type classification and trending
- **Silent Failures:** Detection of processing failures without HTTP errors

#### Saturation Monitoring
- **Resource Utilization:** CPU, memory, disk, and network usage
- **Queue Depth:** Processing queue length and wait times
- **Connection Pools:** Database and service connection saturation
- **Rate Limiting:** API throttling and quota exhaustion tracking

### Distributed Tracing Strategies

#### Trace Architecture
- **Sampling Strategy:** Head-based, tail-based, and adaptive sampling
- **Trace Propagation:** Context propagation across service boundaries
- **Span Correlation:** Parent-child relationship modeling
- **Trace Storage:** Retention policies and storage optimization

#### Service Instrumentation
- **Auto-Instrumentation:** Framework-based automatic trace generation
- **Manual Instrumentation:** Custom span creation for business logic
- **Baggage Handling:** Cross-cutting concern propagation
- **Performance Impact:** Instrumentation overhead measurement and optimization

### Log Aggregation Patterns

#### Collection Architecture
- **Agent Deployment:** Log shipping agent strategies (push vs pull)
- **Log Routing:** Topic-based routing and filtering
- **Parsing Strategies:** Structured vs unstructured log handling
- **Schema Evolution:** Log format versioning and migration

#### Storage and Indexing
- **Index Design:** Optimized field indexing for common query patterns
- **Retention Policies:** Time and volume-based log retention
- **Compression:** Log data compression and archival strategies
- **Search Performance:** Query optimization and result caching

### Cost Optimization for Observability

#### Data Management
- **Metric Retention:** Tiered retention based on metric importance
- **Log Sampling:** Intelligent sampling to reduce ingestion costs
- **Trace Sampling:** Cost-effective trace collection strategies
- **Data Archival:** Cold storage for historical observability data

#### Resource Optimization
- **Query Efficiency:** Optimized metric and log queries
- **Storage Costs:** Appropriate storage tiers for different data types
- **Ingestion Rate Limiting:** Controlled data ingestion to manage costs
- **Cardinality Management:** High-cardinality metric detection and mitigation

## Scripts Overview

This skill includes three powerful Python scripts for comprehensive observability design:

### 1. SLO Designer (`slo_designer.py`)
Generates complete SLI/SLO frameworks based on service characteristics:
- **Input:** Service description JSON (type, criticality, dependencies)
- **Output:** SLI definitions, SLO targets, error budgets, burn rate alerts, SLA recommendations
- **Features:** Multi-window burn rate calculations, error budget policies, alert rule generation

### 2. Alert Optimizer (`alert_optimizer.py`)
Analyzes and optimizes existing alert configurations:
- **Input:** Alert configuration JSON with rules, thresholds, and routing
- **Output:** Optimization report and improved alert configuration
- **Features:** Noise detection, coverage gaps, duplicate identification, threshold optimization

### 3. Dashboard Generator (`dashboard_generator.py`)
Creates comprehensive dashboard specifications:
- **Input:** Service/system description JSON
- **Output:** Grafana-compatible dashboard JSON and documentation
- **Features:** Golden signals coverage, RED/USE methods, drill-down paths, role-based views

## Integration Patterns

### Monitoring Stack Integration
- **Prometheus:** Metric collection and alerting rule generation
- **Grafana:** Dashboard creation and visualization configuration
- **Elasticsearch/Kibana:** Log analysis and dashboard integration
- **Jaeger/Zipkin:** Distributed tracing configuration and analysis

### CI/CD Integration
- **Pipeline Monitoring:** Build, test, and deployment observability
- **Deployment Correlation:** Release impact tracking and rollback triggers
- **Feature Flag Monitoring:** A/B test and feature rollout observability
- **Performance Regression:** Automated performance monitoring in pipelines

### Incident Management Integration
- **PagerDuty/VictorOps:** Alert routing and escalation policies
- **Slack/Teams:** Notification and collaboration integration
- **JIRA/ServiceNow:** Incident tracking and resolution workflows
- **Post-Mortem:** Automated incident analysis and improvement tracking

## Advanced Patterns

### Multi-Cloud Observability
- **Cross-Cloud Metrics:** Unified metrics across AWS, GCP, Azure
- **Network Observability:** Inter-cloud connectivity monitoring
- **Cost Attribution:** Cloud resource cost tracking and optimization
- **Compliance Monitoring:** Security and compliance posture tracking

### Microservices Observability
- **Service Mesh Integration:** Istio/Linkerd observability configuration
- **API Gateway Monitoring:** Request routing and rate limiting observability
- **Container Orchestration:** Kubernetes cluster and workload monitoring
- **Service Discovery:** Dynamic service monitoring and health checks

### Machine Learning Observability
- **Model Performance:** Accuracy, drift, and bias monitoring
- **Feature Store Monitoring:** Feature quality and freshness tracking
- **Pipeline Observability:** ML pipeline execution and performance monitoring
- **A/B Test Analysis:** Statistical significance and business impact measurement

## Best Practices

### Organizational Alignment
- **SLO Setting:** Collaborative target setting between product and engineering
- **Alert Ownership:** Clear escalation paths and team responsibilities
- **Dashboard Governance:** Centralized dashboard management and standards
- **Training Programs:** Team education on observability tools and practices

### Technical Excellence
- **Infrastructure as Code:** Observability configuration version control
- **Testing Strategy:** Alert rule testing and dashboard validation
- **Performance Monitoring:** Observability system performance tracking
- **Security Considerations:** Access control and data privacy in observability

### Continuous Improvement
- **Metrics Review:** Regular SLI/SLO effectiveness assessment
- **Alert Tuning:** Ongoing alert threshold and routing optimization
- **Dashboard Evolution:** User feedback-driven dashboard improvements
- **Tool Evaluation:** Regular assessment of observability tool effectiveness

## Success Metrics

### Operational Metrics
- **Mean Time to Detection (MTTD):** How quickly issues are identified
- **Mean Time to Resolution (MTTR):** Time from detection to resolution
- **Alert Precision:** Percentage of actionable alerts
- **SLO Achievement:** Percentage of SLO targets met consistently

### Business Metrics
- **System Reliability:** Overall uptime and user experience quality
- **Engineering Velocity:** Development team productivity and deployment frequency
- **Cost Efficiency:** Observability cost as percentage of infrastructure spend
- **Customer Satisfaction:** User-reported reliability and performance satisfaction

This comprehensive observability design skill enables organizations to build robust, scalable monitoring and alerting systems that provide actionable insights while maintaining cost efficiency and operational excellence.

<!-- MERGED INTO: observability-engineer on 2026-04-18 -->
<!-- Use `observability-engineer` instead. -->

---

<!-- service-mesh-observability -->
Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments.

## Do not use this skill when

- The task is unrelated to service mesh observability
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Setting up distributed tracing across services
- Implementing service mesh metrics and dashboards
- Debugging latency and error issues
- Defining SLOs for service communication
- Visualizing service dependencies
- Troubleshooting mesh connectivity

## Core Concepts

### 1. Three Pillars of Observability

```
┌─────────────────────────────────────────────────────┐
│                  Observability                       │
├─────────────────┬─────────────────┬─────────────────┤
│     Metrics     │     Traces      │      Logs       │
│                 │                 │                 │
│ • Request rate  │ • Span context  │ • Access logs   │
│ • Error rate    │ • Latency       │ • Error details │
│ • Latency P50   │ • Dependencies  │ • Debug info    │
│ • Saturation    │ • Bottlenecks   │ • Audit trail   │
└─────────────────┴─────────────────┴─────────────────┘
```

### 2. Golden Signals for Mesh

| Signal | Description | Alert Threshold |
|--------|-------------|-----------------|
| **Latency** | Request duration P50, P99 | P99 > 500ms |
| **Traffic** | Requests per second | Anomaly detection |
| **Errors** | 5xx error rate | > 1% |
| **Saturation** | Resource utilization | > 80% |

## Templates

### Template 1: Istio with Prometheus & Grafana

```yaml
# Install Prometheus
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus
  namespace: istio-system
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
    scrape_configs:
      - job_name: 'istio-mesh'
        kubernetes_sd_configs:
          - role: endpoints
            namespaces:
              names:
                - istio-system
        relabel_configs:
          - source_labels: [__meta_kubernetes_service_name]
            action: keep
            regex: istio-telemetry
---
# ServiceMonitor for Prometheus Operator
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: istio-mesh
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istiod
  endpoints:
    - port: http-monitoring
      interval: 15s
```

### Template 2: Key Istio Metrics Queries

```promql
# Request rate by service
sum(rate(istio_requests_total{reporter="destination"}[5m])) by (destination_service_name)

# Error rate (5xx)
sum(rate(istio_requests_total{reporter="destination", response_code=~"5.."}[5m]))
  / sum(rate(istio_requests_total{reporter="destination"}[5m])) * 100

# P99 latency
histogram_quantile(0.99,
  sum(rate(istio_request_duration_milliseconds_bucket{reporter="destination"}[5m]))
  by (le, destination_service_name))

# TCP connections
sum(istio_tcp_connections_opened_total{reporter="destination"}) by (destination_service_name)

# Request size
histogram_quantile(0.99,
  sum(rate(istio_request_bytes_bucket{reporter="destination"}[5m]))
  by (le, destination_service_name))
```

### Template 3: Jaeger Distributed Tracing

```yaml
# Jaeger installation for Istio
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    enableTracing: true
    defaultConfig:
      tracing:
        sampling: 100.0  # 100% in dev, lower in prod
        zipkin:
          address: jaeger-collector.istio-system:9411
---
# Jaeger deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jaeger
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: jaeger
  template:
    metadata:
      labels:
        app: jaeger
    spec:
      containers:
        - name: jaeger
          image: jaegertracing/all-in-one:1.50
          ports:
            - containerPort: 5775   # UDP
            - containerPort: 6831   # Thrift
            - containerPort: 6832   # Thrift
            - containerPort: 5778   # Config
            - containerPort: 16686  # UI
            - containerPort: 14268  # HTTP
            - containerPort: 14250  # gRPC
            - containerPort: 9411   # Zipkin
          env:
            - name: COLLECTOR_ZIPKIN_HOST_PORT
              value: ":9411"
```

### Template 4: Linkerd Viz Dashboard

```bash
# Install Linkerd viz extension
linkerd viz install | kubectl apply -f -

# Access dashboard
linkerd viz dashboard

# CLI commands for observability
# Top requests
linkerd viz top deploy/my-app

# Per-route metrics
linkerd viz routes deploy/my-app --to deploy/backend

# Live traffic inspection
linkerd viz tap deploy/my-app --to deploy/backend

# Service edges (dependencies)
linkerd viz edges deployment -n my-namespace
```

### Template 5: Grafana Dashboard JSON

```json
{
  "dashboard": {
    "title": "Service Mesh Overview",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(istio_requests_total{reporter=\"destination\"}[5m])) by (destination_service_name)",
            "legendFormat": "{{destination_service_name}}"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "gauge",
        "targets": [
          {
            "expr": "sum(rate(istio_requests_total{response_code=~\"5..\"}[5m])) / sum(rate(istio_requests_total[5m])) * 100"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "thresholds": {
              "steps": [
                {"value": 0, "color": "green"},
                {"value": 1, "color": "yellow"},
                {"value": 5, "color": "red"}
              ]
            }
          }
        }
      },
      {
        "title": "P99 Latency",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.99, sum(rate(istio_request_duration_milliseconds_bucket{reporter=\"destination\"}[5m])) by (le, destination_service_name))",
            "legendFormat": "{{destination_service_name}}"
          }
        ]
      },
      {
        "title": "Service Topology",
        "type": "nodeGraph",
        "targets": [
          {
            "expr": "sum(rate(istio_requests_total{reporter=\"destination\"}[5m])) by (source_workload, destination_service_name)"
          }
        ]
      }
    ]
  }
}
```

### Template 6: Kiali Service Mesh Visualization

```yaml
# Kiali installation
apiVersion: kiali.io/v1alpha1
kind: Kiali
metadata:
  name: kiali
  namespace: istio-system
spec:
  auth:
    strategy: anonymous  # or openid, token
  deployment:
    accessible_namespaces:
      - "**"
  external_services:
    prometheus:
      url: http://prometheus.istio-system:9090
    tracing:
      url: http://jaeger-query.istio-system:16686
    grafana:
      url: http://grafana.istio-system:3000
```

### Template 7: OpenTelemetry Integration

```yaml
# OpenTelemetry Collector for mesh
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
data:
  config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
      zipkin:
        endpoint: 0.0.0.0:9411

    processors:
      batch:
        timeout: 10s

    exporters:
      jaeger:
        endpoint: jaeger-collector:14250
        tls:
          insecure: true
      prometheus:
        endpoint: 0.0.0.0:8889

    service:
      pipelines:
        traces:
          receivers: [otlp, zipkin]
          processors: [batch]
          exporters: [jaeger]
        metrics:
          receivers: [otlp]
          processors: [batch]
          exporters: [prometheus]
---
# Istio Telemetry v2 with OTel
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: mesh-default
  namespace: istio-system
spec:
  tracing:
    - providers:
        - name: otel
      randomSamplingPercentage: 10
```

## Alerting Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: mesh-alerts
  namespace: istio-system
spec:
  groups:
    - name: mesh.rules
      rules:
        - alert: HighErrorRate
          expr: |
            sum(rate(istio_requests_total{response_code=~"5.."}[5m])) by (destination_service_name)
            / sum(rate(istio_requests_total[5m])) by (destination_service_name) > 0.05
          for: 5m
          labels:
            severity: critical
          annotations:
            summary: "High error rate for {{ $labels.destination_service_name }}"

        - alert: HighLatency
          expr: |
            histogram_quantile(0.99, sum(rate(istio_request_duration_milliseconds_bucket[5m]))
            by (le, destination_service_name)) > 1000
          for: 5m
          labels:
            severity: warning
          annotations:
            summary: "High P99 latency for {{ $labels.destination_service_name }}"

        - alert: MeshCertExpiring
          expr: |
            (certmanager_certificate_expiration_timestamp_seconds - time()) / 86400 < 7
          labels:
            severity: warning
          annotations:
            summary: "Mesh certificate expiring in less than 7 days"
```

## Best Practices

### Do's
- **Sample appropriately** - 100% in dev, 1-10% in prod
- **Use trace context** - Propagate headers consistently
- **Set up alerts** - For golden signals
- **Correlate metrics/traces** - Use exemplars
- **Retain strategically** - Hot/cold storage tiers

### Don'ts
- **Don't over-sample** - Storage costs add up
- **Don't ignore cardinality** - Limit label values
- **Don't skip dashboards** - Visualize dependencies
- **Don't forget costs** - Monitor observability costs

## Resources

- [Istio Observability](https://istio.io/latest/docs/tasks/observability/)
- [Linkerd Observability](https://linkerd.io/2.14/features/dashboard/)
- [OpenTelemetry](https://opentelemetry.io/)
- [Kiali](https://kiali.io/)


<!-- MERGED INTO: observability-engineer on 2026-04-18 -->
<!-- Use `observability-engineer` instead. -->

---

<!-- observability-monitoring-monitor-setup -->
You are a monitoring and observability expert specializing in implementing comprehensive monitoring solutions. Set up metrics collection, distributed tracing, log aggregation, and create insightful dashboards that provide full visibility into system health and performance.

## Use this skill when

- Working on monitoring and observability setup tasks or workflows
- Needing guidance, best practices, or checklists for monitoring and observability setup

## Do not use this skill when

- The task is unrelated to monitoring and observability setup
- You need a different domain or tool outside this scope

## Context
The user needs to implement or improve monitoring and observability. Focus on the three pillars of observability (metrics, logs, traces), setting up monitoring infrastructure, creating actionable dashboards, and establishing effective alerting strategies.

## Requirements
$ARGUMENTS

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Output Format

1. **Infrastructure Assessment**: Current monitoring capabilities analysis
2. **Monitoring Architecture**: Complete monitoring stack design
3. **Implementation Plan**: Step-by-step deployment guide
4. **Metric Definitions**: Comprehensive metrics catalog
5. **Dashboard Templates**: Ready-to-use Grafana dashboards
6. **Alert Runbooks**: Detailed alert response procedures
7. **SLO Definitions**: Service level objectives and error budgets
8. **Integration Guide**: Service instrumentation instructions

Focus on creating a monitoring system that provides actionable insights, reduces MTTR, and enables proactive issue detection.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.


<!-- MERGED INTO: observability-engineer on 2026-04-18 -->
<!-- Use `observability-engineer` instead. -->

---

<!-- observability-monitoring-slo-implement -->
You are an SLO (Service Level Objective) expert specializing in implementing reliability standards and error budget-based engineering practices. Design comprehensive SLO frameworks, establish meaningful SLIs, and create monitoring systems that balance reliability with feature velocity.

## Use this skill when

- Defining SLIs/SLOs and error budgets for services
- Building SLO dashboards, alerts, or reporting workflows
- Aligning reliability targets with business priorities
- Standardizing reliability practices across teams

## Do not use this skill when

- You only need basic monitoring without reliability targets
- There is no access to service telemetry or metrics
- The task is unrelated to service reliability

## Context
The user needs to implement SLOs to establish reliability targets, measure service performance, and make data-driven decisions about reliability vs. feature development. Focus on practical SLO implementation that aligns with business objectives.

## Requirements
$ARGUMENTS

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Safety

- Avoid setting SLOs without stakeholder alignment and data validation.
- Do not alert on metrics that include sensitive or personal data.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.


<!-- MERGED INTO: observability-engineer on 2026-04-18 -->
<!-- Use `observability-engineer` instead. -->

---

<!-- slo-implementation -->
Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets.

## Do not use this skill when

- The task is unrelated to slo implementation
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Implement measurable reliability targets using SLIs, SLOs, and error budgets to balance reliability with innovation velocity.

## Use this skill when

- Define service reliability targets
- Measure user-perceived reliability
- Implement error budgets
- Create SLO-based alerts
- Track reliability goals

## SLI/SLO/SLA Hierarchy

```
SLA (Service Level Agreement)
  ↓ Contract with customers
SLO (Service Level Objective)
  ↓ Internal reliability target
SLI (Service Level Indicator)
  ↓ Actual measurement
```

## Defining SLIs

### Common SLI Types

#### 1. Availability SLI
```promql
# Successful requests / Total requests
sum(rate(http_requests_total{status!~"5.."}[28d]))
/
sum(rate(http_requests_total[28d]))
```

#### 2. Latency SLI
```promql
# Requests below latency threshold / Total requests
sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))
/
sum(rate(http_request_duration_seconds_count[28d]))
```

#### 3. Durability SLI
```
# Successful writes / Total writes
sum(storage_writes_successful_total)
/
sum(storage_writes_total)
```

**Reference:** See `references/slo-definitions.md`

## Setting SLO Targets

### Availability SLO Examples

| SLO % | Downtime/Month | Downtime/Year |
|-------|----------------|---------------|
| 99%   | 7.2 hours      | 3.65 days     |
| 99.9% | 43.2 minutes   | 8.76 hours    |
| 99.95%| 21.6 minutes   | 4.38 hours    |
| 99.99%| 4.32 minutes   | 52.56 minutes |

### Choose Appropriate SLOs

**Consider:**
- User expectations
- Business requirements
- Current performance
- Cost of reliability
- Competitor benchmarks

**Example SLOs:**
```yaml
slos:
  - name: api_availability
    target: 99.9
    window: 28d
    sli: |
      sum(rate(http_requests_total{status!~"5.."}[28d]))
      /
      sum(rate(http_requests_total[28d]))

  - name: api_latency_p95
    target: 99
    window: 28d
    sli: |
      sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))
      /
      sum(rate(http_request_duration_seconds_count[28d]))
```

## Error Budget Calculation

### Error Budget Formula

```
Error Budget = 1 - SLO Target
```

**Example:**
- SLO: 99.9% availability
- Error Budget: 0.1% = 43.2 minutes/month
- Current Error: 0.05% = 21.6 minutes/month
- Remaining Budget: 50%

### Error Budget Policy

```yaml
error_budget_policy:
  - remaining_budget: 100%
    action: Normal development velocity
  - remaining_budget: 50%
    action: Consider postponing risky changes
  - remaining_budget: 10%
    action: Freeze non-critical changes
  - remaining_budget: 0%
    action: Feature freeze, focus on reliability
```

**Reference:** See `references/error-budget.md`

## SLO Implementation

### Prometheus Recording Rules

```yaml
# SLI Recording Rules
groups:
  - name: sli_rules
    interval: 30s
    rules:
      # Availability SLI
      - record: sli:http_availability:ratio
        expr: |
          sum(rate(http_requests_total{status!~"5.."}[28d]))
          /
          sum(rate(http_requests_total[28d]))

      # Latency SLI (requests < 500ms)
      - record: sli:http_latency:ratio
        expr: |
          sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))
          /
          sum(rate(http_request_duration_seconds_count[28d]))

  - name: slo_rules
    interval: 5m
    rules:
      # SLO compliance (1 = meeting SLO, 0 = violating)
      - record: slo:http_availability:compliance
        expr: sli:http_availability:ratio >= bool 0.999

      - record: slo:http_latency:compliance
        expr: sli:http_latency:ratio >= bool 0.99

      # Error budget remaining (percentage)
      - record: slo:http_availability:error_budget_remaining
        expr: |
          (sli:http_availability:ratio - 0.999) / (1 - 0.999) * 100

      # Error budget burn rate
      - record: slo:http_availability:burn_rate_5m
        expr: |
          (1 - (
            sum(rate(http_requests_total{status!~"5.."}[5m]))
            /
            sum(rate(http_requests_total[5m]))
          )) / (1 - 0.999)
```

### SLO Alerting Rules

```yaml
groups:
  - name: slo_alerts
    interval: 1m
    rules:
      # Fast burn: 14.4x rate, 1 hour window
      # Consumes 2% error budget in 1 hour
      - alert: SLOErrorBudgetBurnFast
        expr: |
          slo:http_availability:burn_rate_1h > 14.4
          and
          slo:http_availability:burn_rate_5m > 14.4
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Fast error budget burn detected"
          description: "Error budget burning at {{ $value }}x rate"

      # Slow burn: 6x rate, 6 hour window
      # Consumes 5% error budget in 6 hours
      - alert: SLOErrorBudgetBurnSlow
        expr: |
          slo:http_availability:burn_rate_6h > 6
          and
          slo:http_availability:burn_rate_30m > 6
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "Slow error budget burn detected"
          description: "Error budget burning at {{ $value }}x rate"

      # Error budget exhausted
      - alert: SLOErrorBudgetExhausted
        expr: slo:http_availability:error_budget_remaining < 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "SLO error budget exhausted"
          description: "Error budget remaining: {{ $value }}%"
```

## SLO Dashboard

**Grafana Dashboard Structure:**

```
┌────────────────────────────────────┐
│ SLO Compliance (Current)           │
│ ✓ 99.95% (Target: 99.9%)          │
├────────────────────────────────────┤
│ Error Budget Remaining: 65%        │
│ ████████░░ 65%                     │
├────────────────────────────────────┤
│ SLI Trend (28 days)                │
│ [Time series graph]                │
├────────────────────────────────────┤
│ Burn Rate Analysis                 │
│ [Burn rate by time window]         │
└────────────────────────────────────┘
```

**Example Queries:**

```promql
# Current SLO compliance
sli:http_availability:ratio * 100

# Error budget remaining
slo:http_availability:error_budget_remaining

# Days until error budget exhausted (at current burn rate)
(slo:http_availability:error_budget_remaining / 100)
*
28
/
(1 - sli:http_availability:ratio) * (1 - 0.999)
```

## Multi-Window Burn Rate Alerts

```yaml
# Combination of short and long windows reduces false positives
rules:
  - alert: SLOBurnRateHigh
    expr: |
      (
        slo:http_availability:burn_rate_1h > 14.4
        and
        slo:http_availability:burn_rate_5m > 14.4
      )
      or
      (
        slo:http_availability:burn_rate_6h > 6
        and
        slo:http_availability:burn_rate_30m > 6
      )
    labels:
      severity: critical
```

## SLO Review Process

### Weekly Review
- Current SLO compliance
- Error budget status
- Trend analysis
- Incident impact

### Monthly Review
- SLO achievement
- Error budget usage
- Incident postmortems
- SLO adjustments

### Quarterly Review
- SLO relevance
- Target adjustments
- Process improvements
- Tooling enhancements

## Best Practices

1. **Start with user-facing services**
2. **Use multiple SLIs** (availability, latency, etc.)
3. **Set achievable SLOs** (don't aim for 100%)
4. **Implement multi-window alerts** to reduce noise
5. **Track error budget** consistently
6. **Review SLOs regularly**
7. **Document SLO decisions**
8. **Align with business goals**
9. **Automate SLO reporting**
10. **Use SLOs for prioritization**

## Reference Files

- `assets/slo-template.md` - SLO definition template
- `references/slo-definitions.md` - SLO definition patterns
- `references/error-budget.md` - Error budget calculations

## Related Skills

- `prometheus-configuration` - For metric collection
- `grafana-dashboards` - For SLO visualization


<!-- MERGED INTO: observability-engineer on 2026-04-18 -->
<!-- Use `observability-engineer` instead. -->

---

<!-- grafana-dashboards -->
Create and manage production-ready Grafana dashboards for comprehensive system observability.

## Do not use this skill when

- The task is unrelated to grafana dashboards
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Design effective Grafana dashboards for monitoring applications, infrastructure, and business metrics.

## Use this skill when

- Visualize Prometheus metrics
- Create custom dashboards
- Implement SLO dashboards
- Monitor infrastructure
- Track business KPIs

## Dashboard Design Principles

### 1. Hierarchy of Information
```
┌─────────────────────────────────────┐
│  Critical Metrics (Big Numbers)     │
├─────────────────────────────────────┤
│  Key Trends (Time Series)           │
├─────────────────────────────────────┤
│  Detailed Metrics (Tables/Heatmaps) │
└─────────────────────────────────────┘
```

### 2. RED Method (Services)
- **Rate** - Requests per second
- **Errors** - Error rate
- **Duration** - Latency/response time

### 3. USE Method (Resources)
- **Utilization** - % time resource is busy
- **Saturation** - Queue length/wait time
- **Errors** - Error count

## Dashboard Structure

### API Monitoring Dashboard

```json
{
  "dashboard": {
    "title": "API Monitoring",
    "tags": ["api", "production"],
    "timezone": "browser",
    "refresh": "30s",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total[5m])) by (service)",
            "legendFormat": "{{service}}"
          }
        ],
        "gridPos": {"x": 0, "y": 0, "w": 12, "h": 8}
      },
      {
        "title": "Error Rate %",
        "type": "graph",
        "targets": [
          {
            "expr": "(sum(rate(http_requests_total{status=~\"5..\"}[5m])) / sum(rate(http_requests_total[5m]))) * 100",
            "legendFormat": "Error Rate"
          }
        ],
        "alert": {
          "conditions": [
            {
              "evaluator": {"params": [5], "type": "gt"},
              "operator": {"type": "and"},
              "query": {"params": ["A", "5m", "now"]},
              "type": "query"
            }
          ]
        },
        "gridPos": {"x": 12, "y": 0, "w": 12, "h": 8}
      },
      {
        "title": "P95 Latency",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service))",
            "legendFormat": "{{service}}"
          }
        ],
        "gridPos": {"x": 0, "y": 8, "w": 24, "h": 8}
      }
    ]
  }
}
```

**Reference:** See `assets/api-dashboard.json`

## Panel Types

### 1. Stat Panel (Single Value)
```json
{
  "type": "stat",
  "title": "Total Requests",
  "targets": [{
    "expr": "sum(http_requests_total)"
  }],
  "options": {
    "reduceOptions": {
      "values": false,
      "calcs": ["lastNotNull"]
    },
    "orientation": "auto",
    "textMode": "auto",
    "colorMode": "value"
  },
  "fieldConfig": {
    "defaults": {
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {"value": 0, "color": "green"},
          {"value": 80, "color": "yellow"},
          {"value": 90, "color": "red"}
        ]
      }
    }
  }
}
```

### 2. Time Series Graph
```json
{
  "type": "graph",
  "title": "CPU Usage",
  "targets": [{
    "expr": "100 - (avg by (instance) (rate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)"
  }],
  "yaxes": [
    {"format": "percent", "max": 100, "min": 0},
    {"format": "short"}
  ]
}
```

### 3. Table Panel
```json
{
  "type": "table",
  "title": "Service Status",
  "targets": [{
    "expr": "up",
    "format": "table",
    "instant": true
  }],
  "transformations": [
    {
      "id": "organize",
      "options": {
        "excludeByName": {"Time": true},
        "indexByName": {},
        "renameByName": {
          "instance": "Instance",
          "job": "Service",
          "Value": "Status"
        }
      }
    }
  ]
}
```

### 4. Heatmap
```json
{
  "type": "heatmap",
  "title": "Latency Heatmap",
  "targets": [{
    "expr": "sum(rate(http_request_duration_seconds_bucket[5m])) by (le)",
    "format": "heatmap"
  }],
  "dataFormat": "tsbuckets",
  "yAxis": {
    "format": "s"
  }
}
```

## Variables

### Query Variables
```json
{
  "templating": {
    "list": [
      {
        "name": "namespace",
        "type": "query",
        "datasource": "Prometheus",
        "query": "label_values(kube_pod_info, namespace)",
        "refresh": 1,
        "multi": false
      },
      {
        "name": "service",
        "type": "query",
        "datasource": "Prometheus",
        "query": "label_values(kube_service_info{namespace=\"$namespace\"}, service)",
        "refresh": 1,
        "multi": true
      }
    ]
  }
}
```

### Use Variables in Queries
```
sum(rate(http_requests_total{namespace="$namespace", service=~"$service"}[5m]))
```

## Alerts in Dashboards

```json
{
  "alert": {
    "name": "High Error Rate",
    "conditions": [
      {
        "evaluator": {
          "params": [5],
          "type": "gt"
        },
        "operator": {"type": "and"},
        "query": {
          "params": ["A", "5m", "now"]
        },
        "reducer": {"type": "avg"},
        "type": "query"
      }
    ],
    "executionErrorState": "alerting",
    "for": "5m",
    "frequency": "1m",
    "message": "Error rate is above 5%",
    "noDataState": "no_data",
    "notifications": [
      {"uid": "slack-channel"}
    ]
  }
}
```

## Dashboard Provisioning

**dashboards.yml:**
```yaml
apiVersion: 1

providers:
  - name: 'default'
    orgId: 1
    folder: 'General'
    type: file
    disableDeletion: false
    updateIntervalSeconds: 10
    allowUiUpdates: true
    options:
      path: /etc/grafana/dashboards
```

## Common Dashboard Patterns

### Infrastructure Dashboard

**Key Panels:**
- CPU utilization per node
- Memory usage per node
- Disk I/O
- Network traffic
- Pod count by namespace
- Node status

**Reference:** See `assets/infrastructure-dashboard.json`

### Database Dashboard

**Key Panels:**
- Queries per second
- Connection pool usage
- Query latency (P50, P95, P99)
- Active connections
- Database size
- Replication lag
- Slow queries

**Reference:** See `assets/database-dashboard.json`

### Application Dashboard

**Key Panels:**
- Request rate
- Error rate
- Response time (percentiles)
- Active users/sessions
- Cache hit rate
- Queue length

## Best Practices

1. **Start with templates** (Grafana community dashboards)
2. **Use consistent naming** for panels and variables
3. **Group related metrics** in rows
4. **Set appropriate time ranges** (default: Last 6 hours)
5. **Use variables** for flexibility
6. **Add panel descriptions** for context
7. **Configure units** correctly
8. **Set meaningful thresholds** for colors
9. **Use consistent colors** across dashboards
10. **Test with different time ranges**

## Dashboard as Code

### Terraform Provisioning

```hcl
resource "grafana_dashboard" "api_monitoring" {
  config_json = file("${path.module}/dashboards/api-monitoring.json")
  folder      = grafana_folder.monitoring.id
}

resource "grafana_folder" "monitoring" {
  title = "Production Monitoring"
}
```

### Ansible Provisioning

```yaml
- name: Deploy Grafana dashboards
  copy:
    src: "{{ item }}"
    dest: /etc/grafana/dashboards/
  with_fileglob:
    - "dashboards/*.json"
  notify: restart grafana
```

## Reference Files

- `assets/api-dashboard.json` - API monitoring dashboard
- `assets/infrastructure-dashboard.json` - Infrastructure dashboard
- `assets/database-dashboard.json` - Database monitoring dashboard
- `references/dashboard-design.md` - Dashboard design guide

## Related Skills

- `prometheus-configuration` - For metric collection
- `slo-implementation` - For SLO dashboards


<!-- MERGED INTO: observability-engineer on 2026-04-18 -->
<!-- Use `observability-engineer` instead. -->

---

<!-- prometheus-configuration -->
Complete guide to Prometheus setup, metric collection, scrape configuration, and recording rules.

## Do not use this skill when

- The task is unrelated to prometheus configuration
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Purpose

Configure Prometheus for comprehensive metric collection, alerting, and monitoring of infrastructure and applications.

## Use this skill when

- Set up Prometheus monitoring
- Configure metric scraping
- Create recording rules
- Design alert rules
- Implement service discovery

## Prometheus Architecture

```
┌──────────────┐
│ Applications │ ← Instrumented with client libraries
└──────┬───────┘
       │ /metrics endpoint
       ↓
┌──────────────┐
│  Prometheus  │ ← Scrapes metrics periodically
│    Server    │
└──────┬───────┘
       │
       ├─→ AlertManager (alerts)
       ├─→ Grafana (visualization)
       └─→ Long-term storage (Thanos/Cortex)
```

## Installation

### Kubernetes with Helm

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  --set prometheus.prometheusSpec.retention=30d \
  --set prometheus.prometheusSpec.storageVolumeSize=50Gi
```

### Docker Compose

```yaml
version: '3.8'
services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=30d'

volumes:
  prometheus-data:
```

## Configuration File

**prometheus.yml:**
```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: 'production'
    region: 'us-west-2'

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - alertmanager:9093

# Load rules files
rule_files:
  - /etc/prometheus/rules/*.yml

# Scrape configurations
scrape_configs:
  # Prometheus itself
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Node exporters
  - job_name: 'node-exporter'
    static_configs:
      - targets:
        - 'node1:9100'
        - 'node2:9100'
        - 'node3:9100'
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
        regex: '([^:]+)(:[0-9]+)?'
        replacement: '${1}'

  # Kubernetes pods with annotations
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
        target_label: __address__
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: namespace
      - source_labels: [__meta_kubernetes_pod_name]
        action: replace
        target_label: pod

  # Application metrics
  - job_name: 'my-app'
    static_configs:
      - targets:
        - 'app1.example.com:9090'
        - 'app2.example.com:9090'
    metrics_path: '/metrics'
    scheme: 'https'
    tls_config:
      ca_file: /etc/prometheus/ca.crt
      cert_file: /etc/prometheus/client.crt
      key_file: /etc/prometheus/client.key
```

**Reference:** See `assets/prometheus.yml.template`

## Scrape Configurations

### Static Targets

```yaml
scrape_configs:
  - job_name: 'static-targets'
    static_configs:
      - targets: ['host1:9100', 'host2:9100']
        labels:
          env: 'production'
          region: 'us-west-2'
```

### File-based Service Discovery

```yaml
scrape_configs:
  - job_name: 'file-sd'
    file_sd_configs:
      - files:
        - /etc/prometheus/targets/*.json
        - /etc/prometheus/targets/*.yml
        refresh_interval: 5m
```

**targets/production.json:**
```json
[
  {
    "targets": ["app1:9090", "app2:9090"],
    "labels": {
      "env": "production",
      "service": "api"
    }
  }
]
```

### Kubernetes Service Discovery

```yaml
scrape_configs:
  - job_name: 'kubernetes-services'
    kubernetes_sd_configs:
      - role: service
    relabel_configs:
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scheme]
        action: replace
        target_label: __scheme__
        regex: (https?)
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
```

**Reference:** See `references/scrape-configs.md`

## Recording Rules

Create pre-computed metrics for frequently queried expressions:

```yaml
# /etc/prometheus/rules/recording_rules.yml
groups:
  - name: api_metrics
    interval: 15s
    rules:
      # HTTP request rate per service
      - record: job:http_requests:rate5m
        expr: sum by (job) (rate(http_requests_total[5m]))

      # Error rate percentage
      - record: job:http_requests_errors:rate5m
        expr: sum by (job) (rate(http_requests_total{status=~"5.."}[5m]))

      - record: job:http_requests_error_rate:percentage
        expr: |
          (job:http_requests_errors:rate5m / job:http_requests:rate5m) * 100

      # P95 latency
      - record: job:http_request_duration:p95
        expr: |
          histogram_quantile(0.95,
            sum by (job, le) (rate(http_request_duration_seconds_bucket[5m]))
          )

  - name: resource_metrics
    interval: 30s
    rules:
      # CPU utilization percentage
      - record: instance:node_cpu:utilization
        expr: |
          100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

      # Memory utilization percentage
      - record: instance:node_memory:utilization
        expr: |
          100 - ((node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100)

      # Disk usage percentage
      - record: instance:node_disk:utilization
        expr: |
          100 - ((node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100)
```

**Reference:** See `references/recording-rules.md`

## Alert Rules

```yaml
# /etc/prometheus/rules/alert_rules.yml
groups:
  - name: availability
    interval: 30s
    rules:
      - alert: ServiceDown
        expr: up{job="my-app"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Service {{ $labels.instance }} is down"
          description: "{{ $labels.job }} has been down for more than 1 minute"

      - alert: HighErrorRate
        expr: job:http_requests_error_rate:percentage > 5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High error rate for {{ $labels.job }}"
          description: "Error rate is {{ $value }}% (threshold: 5%)"

      - alert: HighLatency
        expr: job:http_request_duration:p95 > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High latency for {{ $labels.job }}"
          description: "P95 latency is {{ $value }}s (threshold: 1s)"

  - name: resources
    interval: 1m
    rules:
      - alert: HighCPUUsage
        expr: instance:node_cpu:utilization > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage on {{ $labels.instance }}"
          description: "CPU usage is {{ $value }}%"

      - alert: HighMemoryUsage
        expr: instance:node_memory:utilization > 85
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High memory usage on {{ $labels.instance }}"
          description: "Memory usage is {{ $value }}%"

      - alert: DiskSpaceLow
        expr: instance:node_disk:utilization > 90
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Low disk space on {{ $labels.instance }}"
          description: "Disk usage is {{ $value }}%"
```

## Validation

```bash
# Validate configuration
promtool check config prometheus.yml

# Validate rules
promtool check rules /etc/prometheus/rules/*.yml

# Test query
promtool query instant http://localhost:9090 'up'
```

**Reference:** See `scripts/validate-prometheus.sh`

## Best Practices

1. **Use consistent naming** for metrics (prefix_name_unit)
2. **Set appropriate scrape intervals** (15-60s typical)
3. **Use recording rules** for expensive queries
4. **Implement high availability** (multiple Prometheus instances)
5. **Configure retention** based on storage capacity
6. **Use relabeling** for metric cleanup
7. **Monitor Prometheus itself**
8. **Implement federation** for large deployments
9. **Use Thanos/Cortex** for long-term storage
10. **Document custom metrics**

## Troubleshooting

**Check scrape targets:**
```bash
curl http://localhost:9090/api/v1/targets
```

**Check configuration:**
```bash
curl http://localhost:9090/api/v1/status/config
```

**Test query:**
```bash
curl 'http://localhost:9090/api/v1/query?query=up'
```

## Reference Files

- `assets/prometheus.yml.template` - Complete configuration template
- `references/scrape-configs.md` - Scrape configuration patterns
- `references/recording-rules.md` - Recording rule examples
- `scripts/validate-prometheus.sh` - Validation script

## Related Skills

- `grafana-dashboards` - For visualization
- `slo-implementation` - For SLO monitoring
- `distributed-tracing` - For request tracing


<!-- MERGED INTO: observability-engineer on 2026-04-18 -->
<!-- Use `observability-engineer` instead. -->
