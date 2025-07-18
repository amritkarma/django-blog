# 📝 Django Blog Platform – Aera

Aera is a feature-rich blog platform built with Django 5.2.4 and TailwindCSS. It supports user authentication, post management, comments, SEO metadata, category filters, custom user profiles, and more. This project is ideal for developers looking to learn or extend a full-featured blog in Django.

---

## 🚀 Features

- 🔐 Custom user authentication (email-based login)
- ✍️ Create, edit, delete blog posts with **draft/publish** status
- 📚 Category-wise filtering and navigation
- 💬 Comment system on blog posts
- 📸 Image uploads for posts and profiles
- 🧭 Sitemap, RSS Feed, robots.txt, ads.txt
- 📄 SEO fields (title, description)
- 🧵 TailwindCSS integration via CLI
- 📬 Contact form and newsletter subscription
- ⚙️ Admin panel and site config
- 🌐 Error views (404, 500, 403, 400)

---

## 🛠 Tech Stack

- **Backend:** Django 5.2.4
- **Frontend:** TailwindCSS 4.1
- **Python:** 3.13.5
- **Database:** SQLite3 (default), PostgreSQL (production)
- **Other Libraries:**
  - Pillow
  - python-dotenv
  - psycopg
  - Whitenoise
  - Gunicorn

---

## 📦 Requirements

Install using:

```bash
pip install -r requirements.txt
```

## ⚙️ Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/amritkarma/django-blog.git
cd django-blog
```

### 2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt

```

### 4. 4. Install TailwindCSS dependencies

Navigate to the `django-blog` directory:

```bash

cd django-blog
Then install dependencies and run the Tailwind CLI using one of the following tools:
```
Using npm:

```bash
npm install
npm run dev
```
Using bun:

```bash
bun install
bun run dev
```
Using yarn:

```bash
yarn install
yarn dev
```
Using pnpm:

```bash
pnpm install
pnpm dev
```
💡 Make sure to have one of the above tools installed globally before running the commands.

### 5. Apply migrations and create a superuser

```bash
python manage.py migrate
python manage.py createsuperuser

```

### 6. Run the development servers

```bash
python manage.py runserver

```

Visit http://127.0.0.1:8000/

#

```bash
# .env

# Django settings
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,localhost,127.0.0.1

# PostgreSQL Database configuration
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# Email configuration
EMAIL_HOST=smtp.yourprovider.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
```


## 📡 Deployment Notes

- ✅ Use **Whitenoise** for static file serving.
- 🐍 Use **Gunicorn** in production:

```bash
gunicorn main.wsgi
```

* 🎯 Tailwind builds must be **precompiled in production**:

```bash
npm run dev  # or: bun run dev / yarn dev / pnpm dev
```

* ⚠️ Make sure to set:

```python
DEBUG = False
```

* 📦 Configure **PostgreSQL** properly in `main/settings.py` under `DATABASES` when deploying to production.

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
GitHub: [@amritkarma](https://github.com/amritkarma)

---

# 🌍 Routes

| URL                     | Description                   |
| ----------------------- | ----------------------------- |
| `/`                     | Blog homepage with pagination |
| `/auth/login/`          | Login page                    |
| `/auth/signup/`         | Signup page                   |
| `/auth/profile/<slug>/` | User profile                  |
| `/category/<slug>/`     | Category-wise post view       |
| `/contact/`             | Contact form                  |
| `/rss/`                 | RSS feed                      |
| `/sitemap.xml`          | Sitemap                       |
| `/robots.txt`           | Robots file                   |
| `/ads.txt`              | Ads file                      |
