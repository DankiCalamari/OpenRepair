<div align="center">

# OpenRepair

**Gestor de taller de reparaciones — open-source y autohospedable.**

Clientes · reparaciones con seguimiento de estado · presupuestos · historial · búsqueda · export CSV · resguardo PDF.

`Flask` + `MariaDB` · se levanta con **un solo comando**.

</div>

---

## Empieza en 30 segundos

> **Único requisito:** [Docker](https://www.docker.com/products/docker-desktop/) instalado.

```bash
git clone https://github.com/robertocarrascoso/OpenRepair.git
cd OpenRepair
docker compose up -d
```

Abre **http://localhost:8000** e inicia sesión:

| Email                  | Contraseña |
|------------------------|------------|
| `admin@openrepair.com` | `admin123` |

Eso es todo. Sin editar archivos, sin pasos extra. La base de datos arranca **vacía**
(sin datos de relleno) y el usuario admin se crea solo la primera vez.

> [!WARNING]
> `admin123` es la contraseña por defecto y es **pública**. Cámbiala desde el panel
> en cuanto entres, o define la tuya en `.env` **antes del primer arranque**:
> ```env
> ADMIN_EMAIL=tu@correo.com
> ADMIN_PASSWORD=una-contraseña-fuerte
> ```
> Imprescindible antes de exponer la app a internet.

---

## Características

- **Roles** admin / técnico (sesiones, contraseñas con hash)
- **Código automático** `REP-AÑO-NNNNN` por reparación
- **Flujo de estados:** Recibido → Diagnosticado → Presupuesto → Reparando → Listo → Entregado
- **Ficha de cliente** con historial completo y gasto total
- **Dashboard** con métricas (pendientes, ingresos del mes, tiempo medio)
- **Búsqueda** con filtros avanzados y paginación
- **Exportar** a CSV y resguardo en PDF
- **Idiomas** español e inglés: español si el navegador lo acepta; inglés en caso contrario.
  Cambia con el botón de bandera en el acceso o la barra de navegación; la bandera muestra el idioma actual (🇺🇸 / 🇪🇸).
  La selección también se aplica a los resguardos PDF y a los CSV.

---

## Comandos útiles

```bash
docker compose logs -f web    # ver logs de la app
docker compose down           # parar (los datos persisten)
docker compose down -v        # parar y BORRAR la base de datos
```

### Datos de demo (opcional)

Para rellenar con clientes y reparaciones de ejemplo y probar la app:

```bash
docker compose exec web python base-de-datos/seed.py
```

> [!CAUTION]
> El seed **borra y recrea** todos los datos cada vez. No lo uses con datos reales.

---

## Configuración

Todo se controla por variables de entorno en `.env` (copia `.env.example`). Todas tienen
valores por defecto, así que `.env` es **opcional** para probar en local.

| Variable | Para qué sirve |
|---|---|
| `PORT` | Puerto público de la web (def. `8000`) |
| `DB_NAME` | Nombre de la base de datos |
| `DB_USER` / `DB_PASSWORD` | Credenciales de la app a la DB |
| `DB_ROOT_PASSWORD` | Contraseña root de MariaDB |
| `SECRET_KEY` | Clave de sesiones Flask (¡aleatoria!) |
| `ADMIN_EMAIL` / `ADMIN_PASSWORD` | Admin creado en el 1er arranque |

Genera una `SECRET_KEY` segura:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## Cómo funciona el stack

- **web** — app Flask servida con `gunicorn` (3 workers).
- **db** — MariaDB 11. El esquema `base-de-datos/schema.sql` se ejecuta solo la primera vez.
- Los datos viven en un volumen Docker (`db_data`) y persisten entre reinicios.

---

## Desplegar sin máquina propia (PaaS)

El `Dockerfile` funciona tal cual en **Render**, **Railway** o **Fly.io**: conecta este repo,
añade una base de datos MySQL/MariaDB gestionada y define las variables de entorno
(`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `SECRET_KEY`, `ADMIN_PASSWORD`).

---

## Desarrollo local (sin Docker)

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # apunta DB_HOST a tu MySQL/MariaDB local
python app.py                 # dev server en http://localhost:5000
```

---

## Licencia

MIT
