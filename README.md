# Proyecto DevSecOps Local

## Descripción
Infraestructura local con CI/CD, observabilidad, monitoreo y seguridad integrada.

## Componentes
- Aplicación Flask
- Docker Compose
- Prometheus + Grafana
- ELK Stack
- GitHub Actions (CI/CD)
- Trivy (Security Scan)

## Despliegue
```bash
docker compose up -d
```

## Accesos
- App: http://localhost:5000
- Grafana: http://localhost:3000
- Kibana: http://localhost:5601
- Prometheus: http://localhost:9090