Users and groups are created as _roles_. Users, groups, and roles reside at the DB instance level.

Users, groups, and roles are held at the instance level, not inside the database, because of the specific things that users and groups can access.

Although users exist at the public level, they do not automatically get permissions at the global level.

Users and groups in PostgreSQL are based on the concept of database roles.

A role can be configured as a user by assigning a login privilege. When you create a `LOGIN` role, you are creating a user.

A group is a role that allows other roles to inherit privileges.

Privileges are assigned to a role. A role can be a group or a user. If additional users are assigned to another user role, those users will inherit the main user privileges.

Users can inherit privileges from other users and groups, depending on what role is assigned.

Roles determine what a user can do in various situations. They set limits on a user for access to data. Roles also determine the ability of users or groups to perform specific functions, such as administrative tasks and creating and deleting databases.
## ALTER ROLE
Database administrators (DBAs) can change roles. DBAs can also change elements of a role such as a password or name. DBAs make changes to a role using the ALTER ROLE command.
## DROP ROLE
DBAs can also drop a role. DBAs remove roles using the DROP ROLE command. All objects owned by the role must be dropped or reassigned before the role can be dropped.
## CREATE USER
New users are created in SQL using the CREATE USER command.

CREATE USER is also an alias for CREATE ROLE. The only difference is that with the CREATE USER command, LOGIN is assumed by default. NOLOGIN is assumed when the command is written as CREATE ROLE.

To create a new user using this command, you must have a PostgreSQL superuser account.
## Groups
Groups are another type of role. Groups, unlike users, can own database objects.

Groups can be granted permissions like users. Groups are a way of logically assembling users to make it easier to manage privileges. Privileges can be granted to, or revoked from, a group
## Privileges
Roles can own database objects and assign privileges on those objects to other roles.

It is possible to grant membership in a role to another role, thus allowing the member role to use privileges assigned to another role.

The GRANT command assigns specific privileges to an object, one or more users, or a group of users.

The REVOKE command removes a previously granted privilege from a user or group.

A user has the sum of privileges granted directly to them, privileges granted to any group they belong to, and privileges granted to PUBLIC (the implicitly defined group of all users).