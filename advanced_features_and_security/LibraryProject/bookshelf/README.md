"""
Permissions Setup:
- Custom permissions are defined in the Book model (can_view, can_create, can_edit, can_delete).
- These permissions are assigned to Django groups via the admin interface:
    - Viewers: can_view
    - Editors: can_view, can_create, can_edit
    - Admins: all permissions
- Views use @permission_required to restrict access based on user permissions.
"""
