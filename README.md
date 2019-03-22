# usuarios-cluster

Interfaz web para generar usuarios en el clúster.

# Especificación funcional

Esta aplicación debería ejecutarse en el nodo principal del clúster institucional.

## Autenticación

La autenticación se realiza con los usuarios del sistema operativo.

La aplicación debe verificar que el usuario existe
y que es parte del grupo de "investigadores líderes"
para permitir el acceso.

Adicionalmente, para realizar administración de usuarios,
se verifica que pertenece además al grupo de investigación que quiere administrar
y los usuarios que está modificando también.

## Generar nuevos usuarios

Si estas condiciones se cumplen,
la aplicación generará un usuario de acuerdo al procedimiento 20
del [Manual de Procedimientos del Instituto Nacional de Medicina Genómica](http://www.inmegen.gob.mx/media/filer_public/e0/21/e021bb2a-0863-49ae-a75a-43cb524c4085/manual_procedimientos_inmegen_2018_18oct18_ni.pdf )
aprobado en Octubre del 2018.

Para generar los usuarios se solicitarán los siguientes datos:

- Nombre completo
- Nombre de usuario preferido (si está disponible se le dará)
- Correo electrónico
- Extensión telefónica
- Fecha de expiración (¿cuándo terminan proyecto/doctorado/etc?)

La fecha de expiración puede ser indefinida únicamente si el usuario es trabajador del instituto.
En este caso, la dirección de correo electrónico debe pertenecer al dominio `inmegen.gob.mx`.

### Confirmación de usuario

Al generar el usuario, se le enviará un correo al usuario
con una liga para confirmar su correo electrónico y establecer su contraseña.

## Cambiar fecha de expiración de usuarios

Un investigador líder puede cambiar la fecha de expiración de usuarios.
Esta vista muestra un menú de los usuarios dentro de su grupo de investigación
y la fecha en que expiran.

La fecha no puede ser más allá de dos años en el futuro.
