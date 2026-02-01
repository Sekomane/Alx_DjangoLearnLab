# Advanced Features and Security

## Custom User Model
This project uses a custom user model (`CustomUser`) defined in the `bookshelf` app.
The model extends Django’s `AbstractUser` and adds the following fields:
- date_of_birth
- profile_photo

The custom user model is set using:
AUTH_USER_MODEL = 'bookshelf.CustomUser'

## Custom Permissions
Custom permissions are defined on the Book model in `bookshelf/models.py`:
- can_view
- can_create
- can_edit
- can_delete

## Groups
The following groups are used to manage access:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Permission Enforcement
Permissions are enforced in views using Django’s `@permission_required` decorator
with `raise_exception=True` to prevent unauthorized access.

## Usage
Assign users to the appropriate groups using the Django admin panel to control
access to different parts of the application.
