El proyecto usa django con sqlite
porque el número de usuarios es de menos de 1000 personas
y no hay personal para mantener una base de datos.

La base de datos puede regenerarse a partir de `/etc/fstab`
y `/etc/fstab` se pueden generar los usuarios a partir de la base de datos.

## Base de datos

grupos (ID:key, nombre: varchar)
usuarios (ID: key, group: foreign key-grupos, nombre: varchar, apellidos: varchar, correo: VARCHAR(320), expire: date)
