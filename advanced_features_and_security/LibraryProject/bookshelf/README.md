# LibraryProject 📚

A secure Django application for managing a digital library system with role-based access control, custom user profiles, and best security practices.

---

## 🔧 Project Features

- ✅ **Custom User Model** (with `profile_photo`, `date_of_birth`, etc.)
- ✅ **Role-Based Access Control** (Admin, Librarian, Member)
- ✅ **Permission Decorators** to control access to views
- ✅ **Secure Settings Configuration**
- ✅ **CSRF Protection in Forms**
- ✅ **SQL Injection Mitigation** via Django ORM
- ✅ **Content Security Policy (CSP)**

---

"""
Permissions Setup:
- Custom permissions are defined in the Book model (can_view, can_create, can_edit, can_delete).
- These permissions are assigned to Django groups via the admin interface:
    - Viewers: can_view
    - Editors: can_view, can_create, can_edit
    - Admins: all permissions
- Views use @permission_required to restrict access based on user permissions.
"""

## 🛡 Security Measures Implemented

### Django Settings:
- `DEBUG = False` for production readiness
- `SECURE_BROWSER_XSS_FILTER = True` – Protects against XSS
- `SECURE_CONTENT_TYPE_NOSNIFF = True` – Prevents MIME-type sniffing
- `X_FRAME_OPTIONS = 'DENY'` – Prevents clickjacking
- `CSRF_COOKIE_SECURE = True`, `SESSION_COOKIE_SECURE = True` – Ensures cookies are sent over HTTPS only

### CSRF Protection:
All forms include `{% csrf_token %}` for protection against Cross-Site Request Forgery.

### Views:
- Access controlled using `@permission_required(...)`
- Use of Django's ORM to safely query the database and prevent SQL injection
- Validations handled using Django Forms

---
