#!/usr/bin/env bash
# Збірка для Render: залежності, статика, міграції, bootstrap адміна з DJANGO_USERNAME / DJANGO_PASSWORD.
set -eo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput

if [ -n "${DJANGO_USERNAME:-}" ] && [ -n "${DJANGO_PASSWORD:-}" ]; then
  python3 manage.py shell <<'PY'
import os
from django.contrib.auth import get_user_model

username = (os.environ.get("DJANGO_USERNAME") or "").strip()
password = os.environ.get("DJANGO_PASSWORD") or ""
if not username or not password:
    raise SystemExit(0)

User = get_user_model()
email = (os.environ.get("DJANGO_ADMIN_EMAIL") or "").strip() or f"{username}@localhost"

try:
    user = User.objects.get(username=username)
except User.DoesNotExist:
    User.objects.create_superuser(username, email, password)
else:
    if email:
        user.email = email
    user.is_staff = True
    user.is_superuser = True
    user.set_password(password)
    user.save()
PY
fi
