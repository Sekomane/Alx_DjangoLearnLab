\# Advanced Features and Security



\## Custom User Model

This project uses a custom user model (`CustomUser`) defined in the `bookshelf` app.

The model extends Django’s `AbstractUser` and adds the following fields:

\- date\_of\_birth

\- profile\_photo



The custom user model is set using:

AUTH\_USER\_MODEL = 'bookshelf.CustomUser'



\## Custom Permissions

Custom permissions are defined on the Book model in `bookshelf/models.py`:

\- can\_view

\- can\_create

\- can\_edit

\- can\_delete



\## Groups

The following groups are used to manage access:

\- Viewers: can\_view

\- Editors: can\_view, can\_create, can\_edit

\- Admins: can\_view, can\_create, can\_edit, can\_delete



\## Permission Enforcement

Permissions are enforced in views using Django’s `@permission\_required` decorator

with `raise\_exception=True` to prevent unauthorized access.



\## Usage

Assign users to the appropriate groups using the Django admin panel to control

access to different parts of the application.



