# 🚀 Marketing AI

> Plataforma Multiagente de Marketing Inteligente construida con **LangGraph**, **LangChain**, **Tavily**, **Streamlit** y **SQLite**.

<div align="center">

![Status](https://img.shields.io/badge/Status-MVP%20Funcional-brightgreen?style=flat)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=flat&logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C6C?style=flat&logo=langchain&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C6C?style=flat&logo=langchain&logoColor=white)
![Tavily](https://img.shields.io/badge/Tavily-1E3A5F?style=flat&logo=tavily&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=flat&logo=googlegemini&logoColor=white)

</div>

Marketing AI es una aplicación diseñada para asistir a emprendedores, negocios y profesionales del marketing mediante un sistema de agentes especializados que colaboran para generar estrategias, contenido, campañas publicitarias y recomendaciones de crecimiento digital.

---

# 📋 Características

## ✅ Sistema Multiagente

La plataforma utiliza una arquitectura basada en agentes especializados coordinados por un Supervisor.

### 🧠 Supervisor Agent

Responsable de:

- Analizar la solicitud del usuario.
- Determinar qué agente debe intervenir.
- Coordinar el flujo de trabajo.
- Consolidar respuestas.

### ✍️ Content Agent

Especializado en:

- Generación de contenido.
- Calendarios editoriales.
- Ideas de publicaciones.
- Copywriting.
- Storytelling.

### 📱 Social Media Agent

Especializado en:

- Estrategias para redes sociales.
- Crecimiento orgánico.
- Contenido para TikTok.
- Instagram.
- Facebook.
- Community Management.

### 🔍 SEO Agent

Especializado en:

- Investigación de palabras clave.
- Optimización SEO.
- Estrategias de posicionamiento.
- Contenido optimizado.

### 📢 Ads Agent

Especializado en:

- Campañas publicitarias.
- Meta Ads.
- Google Ads.
- Segmentación.
- Presupuestos.
- CTAs.

---

# 🏗 Arquitectura

```text
Usuario
   │
   ▼
Supervisor
   │
   ├── Content Agent
   ├── Social Agent
   ├── SEO Agent
   └── Ads Agent
   │
   ▼
Respuesta Final
```

## ⚙️ Tecnologías Utilizadas

| Categoría | Tecnologías |
|-----------|------------|
| **Backend** | Python 3.13+, LangGraph, LangChain, Google Gemini, Pydantic |
| **Frontend** | Streamlit |
| **Persistencia** | SQLite |
| **Seguridad** | Hash de contraseñas, Gestión de sesiones |

## 📁 Estructura del Proyecto
```text
marketing_ai/
│
├── agents/
│   ├── ads_agent.py
│   ├── agent_factory.py
│   ├── content_agent.py
│   ├── seo_agent.py
│   ├── social_agent.py
│   └── supervisor.py
│
├── config/
│   ├── llm.py
│   └── settings.py
│
├── graph/
│   └── marketing_graph.py
│
├── logs/
│
├── memory/
│   ├── conversation_memory.py
│   ├── init_db.py
│   ├── sqlite_memory.py
│   └── user_memory.py
│
├── schemas/
│   ├── agent_models.py
│   ├── responses.py
│   └── state.py
│
├── services/
│   ├── auth_service.py
│   ├── chat_service.py
│   ├── graph_service.py
│   ├── message_service.py
│   ├── session_service.py
│   ├── streaming_service.py
│   └── thread_service.py
│
├── tests/
│
├── tools/
│   ├── formatter_tools.py
│   ├── hashtag_tools.py
│   ├── seo_tools.py
│   ├── tavily_tools.py
│   └── tiktok_tools.py
│
├── ui/
│   ├── app.py
│   └── login.py
│
├── marketing.db
│
└── README.md
```

---
## 🔐 Sistema de Usuarios

La aplicación incorpora:

### Registro
Permite crear nuevas cuentas.

**Información almacenada:**
- Usuario
- Contraseña hasheada

### Inicio de Sesión
Permite autenticación segura.

### Cierre de Sesión
Elimina:
- Usuario actual
- Conversación activa
- Historial temporal
- Estado de sesión

---

## 💾 Persistencia

### Tabla `users`
Almacena:

| Columna | Tipo |
|---------|------|
| id | INTEGER |
| username | TEXT |
| password_hash | TEXT |
| created_at | TIMESTAMP |

### Tabla `conversations`
Almacena:

| Columna | Tipo |
|---------|------|
| thread_id | TEXT |
| user_id | INTEGER |
| title | TEXT |
| created_at | TIMESTAMP |

### Tablas LangGraph
Generadas automáticamente:

| Tabla | Descripción |
|-------|-------------|
| checkpoints | Puntos de control del grafo |
| writes | Escrituras del sistema |

**Permiten:**
- Memoria persistente
- Recuperación de contexto
- Historial de conversaciones

## 💬 Conversaciones

Cada usuario posee conversaciones independientes.

**Características:**

- Creación automática
- Historial persistente
- Eliminación de conversaciones
- Títulos automáticos
- Recuperación al reiniciar la aplicación

---

## 🔄 Streaming

La aplicación muestra el progreso de los agentes en tiempo real.

**Ejemplo:**   
🧠 Supervisor trabajando...  
📱 Social Agent trabajando...  
✅ Proceso completado  

## 🚀 Instalación

### 1. Clonar repositorio

```bash
https://github.com/solanomillo/marketing_ai.git
```

### 2. Crear entorno virtual
Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crear archivo:
```text
.env
```

Ejemplo:
```text
GOOGLE_API_KEY=tu_api_key
TAVILY_API_KEY=tu_api_key
```

### 5. Ejecutar aplicación
```bash
streamlit run ui/app.py
```

---

## 🧪 Estado Actual

| Item | Valor |
|------|-------|
| **Versión** | `v1.0.0` |
| **Estado** | `MVP Funcional` |

### Incluye:

✅ Multiagentes  
✅ Supervisor  
✅ Login  
✅ Registro  
✅ Conversaciones por usuario  
✅ Persistencia SQLite  
✅ Streaming  
✅ Historial

---

## 🔮 Roadmap V2

| Módulo | Características |
|--------|----------------|
| **🧠 Memoria Inteligente** | Nombre de empresa, Rubro, Público objetivo, Ubicación, Redes sociales, Tono de marca |
| **📚 Sistema RAG** | Carga de PDFs, Manuales de marca, Estrategias, Documentación |
| **🌐 Redes Sociales** | Facebook, Instagram, TikTok, LinkedIn |
| **📢 Publicidad** | Meta Ads, Google Ads |
| **📊 Analítica** | Google Analytics, Search Console |
| **📊 Dashboard** | Métricas, Costos, Rendimiento, Historial de actividad |
| **💳 Monetización SaaS** | Plan Gratuito, Plan Pro, Créditos mensuales, Facturación |

---
## 🛠 Mejoras Técnicas

### Base de Datos
- **Actual:** SQLite
- **Futuro:** PostgreSQL

### Caché
- **Implementar:** Redis

### Observabilidad
- **Implementar:** LangSmith
- **Para:**
  - Trazas
  - Debug
  - Costos
  - Monitoreo

### Contenedores
- **Agregar:** Docker y Docker Compose

## 🤝 Contribuciones

Las contribuciones son bienvenidas.

**Proceso recomendado:**

1. Crear rama
2. Realizar cambios
3. Ejecutar pruebas
4. Crear Pull Request

---

## 📄 Licencia

MIT License

---

## 👨‍💻 Autor

**Julio Solano**

- 🔗 GitHub: [https://github.com/solanomillo](https://github.com/solanomillo)
- 🔗 LinkedIn: [https://www.linkedin.com/in/julio-cesar-solano](https://www.linkedin.com/in/julio-cesar-solano)
- 📧 Email: solanomillo144@gmail.com

