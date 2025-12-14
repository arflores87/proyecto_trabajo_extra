# Arquitectura del Sistema

## Visión General
El proyecto implementa una infraestructura DevSecOps completamente local orientada a simular un entorno de producción.

## Componentes
- Aplicación Flask (contenedor)
- Docker Compose como orquestador local
- ELK Stack para logs
- Prometheus y Grafana para métricas
- GitHub Actions como CI/CD

## Flujo
Usuario → Aplicación → Logs → ELK  
Aplicación → Métricas → Prometheus → Grafana  
Código → CI/CD → Build → Scan → Deploy