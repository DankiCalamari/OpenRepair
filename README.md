<div align="center">

# OpenRepair

**Open-source, self-hosted repair shop manager.**

Customers · repair status tracking · estimates · history · search · CSV export · PDF receipts.

`Flask` + `MariaDB` · start with **one command**.

</div>

---

## Get started in 30 seconds

> **Only requirement:** [Docker](https://www.docker.com/products/docker-desktop/).

```bash
git clone https://github.com/robertocarrascoso/OpenRepair.git
cd OpenRepair
docker compose up -d
```

Open **http://localhost:8000** and sign in:

| Email                  | Password   |
|------------------------|------------|
| `admin@openrepair.com` | `admin123` |

That's it. No files to edit or extra steps. The database starts **empty**
(without sample data), and the admin account is created on first startup.

> [!WARNING]
> `admin123` is the **public default password**. Change it in the admin panel
> as soon as you sign in, or set your own in `.env` **before the first startup**:
> ```env
> ADMIN_EMAIL=you@example.com
> ADMIN_PASSWORD=use-a-strong-password
> ```
> Do this before exposing the app to the internet.

---

## Features

- **Roles:** admin and technician, with sessions and hashed passwords
- **Automatic repair codes:** `REP-YEAR-NNNNN`
- **Status flow:** Received → Diagnosed → Estimate sent → Estimate accepted → Repairing → Ready → Delivered
- **Customer records:** full repair history and total spending
- **Dashboard:** pending repairs, monthly revenue, and average turnaround time
- **Search:** advanced filters and pagination
- **Exports:** CSV and PDF receipts
- **Languages:** Spanish when the browser accepts it; English otherwise.
  Switch languages with the flag button on the sign-in page or navigation bar.
  The flag shows the current language (🇺🇸 / 🇪🇸). The selection also applies to
  PDF receipts and CSV exports.

---

## Useful commands

```bash
docker compose logs -f web    # view app logs
docker compose down           # stop; data persists
docker compose down -v        # stop and DELETE the database
```

### Sample data (optional)

To populate the app with example customers and repairs:

```bash
docker compose exec web python base-de-datos/seed.py
```

> [!CAUTION]
> The seed script **deletes and recreates** all data each time. Do not run it
> against real data.

---

## Configuration

Configure the app with environment variables in `.env` (copy `.env.example`).
All variables have defaults, so `.env` is **optional** for a local trial.

| Variable | Purpose |
|---|---|
| `PORT` | Public web port (default: `8000`) |
| `DB_NAME` | Database name |
| `DB_USER` / `DB_PASSWORD` | App database credentials |
| `DB_ROOT_PASSWORD` | MariaDB root password |
| `SECRET_KEY` | Flask session key (use a random value) |
| `ADMIN_EMAIL` / `ADMIN_PASSWORD` | Admin account created on first startup |

Generate a secure `SECRET_KEY`:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## How it works

- **web:** Flask app served by `gunicorn` with three workers.
- **db:** MariaDB 11. `base-de-datos/schema.sql` runs only when the database volume is first created.
- Data lives in the `db_data` Docker volume and persists across restarts.

---

## Deploy without your own server (PaaS)

The `Dockerfile` can be used with **Render**, **Railway**, or **Fly.io**. Connect
this repo, add a managed MySQL/MariaDB database, import
`base-de-datos/schema.sql` once, and set `DB_HOST`, `DB_NAME`, `DB_USER`,
`DB_PASSWORD`, `SECRET_KEY`, and `ADMIN_PASSWORD`.

---

## Local development (without Docker)

Create a local MySQL/MariaDB database, import `base-de-datos/schema.sql`, and
set its credentials in `.env` before starting the app.

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # then set your local database credentials
python app.py                 # dev server at http://localhost:5000
```

---

## License

MIT
