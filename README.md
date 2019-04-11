# Visión y alcance

Automatizar la gestión de usuarios del clúster institucional.

# Definición de producto

Permite a los investigadores líderes que trabajan en el INMEGEN
generar cuentas de usuario para que sus estudiantes y asociados
usen los recursos del clúster institucional,
eliminando la necesidad de administrar manualmente las cuentas de usuario.

# Glosario

Instituto: El Instituto Nacional de Medicina Genómica.

Clúster institucional: El grupo de cómputo dedicado a cómputo científico en el Instituto.

Investigador líder: La persona que dirige un grupo de investigación en el Instituto y cuya cuenta de usuario le permite administrar los usuarios de su grupo de investigación.

Grupo de investigación: El identificador de grupo de sistema operativo utiliza para administrar los permisos de las cuentas de usuario.

Usuario: La persona que utilizará el clúster institucional.

Cuenta de usuario: El identificador que la persona usa para trabajar en el clúster institucional.

Contraseña: el secreto que permite a los usuarios acceder a los recursos del clúster institucional.

Periodo de acceso: el periodo durante el que un usuario puede acceder a los recursos del clúster institucional con su cuenta de usuario.

# Requerimientos de negocio

- Liberar tiempo de la Subdirección de Bionformática para el desarrollo de sistemas bioinformáticos.
- Reportar en la meta de automatizar procesos de gestión.
- Automatizar el reporte de usuarios requerido en el procedimiento 20 del [Manual de Procedimientos del Instituto Nacional de Medicina Genómica][manual].
- Mejorar el tiempo de respuesta para los investigadores líderes.

# Actores y sus intereses

Estudiantes: Usar el clúster.
Investigador líder: Que sus estudiantes trabajen en su artículo.
Subdirección de Bioinformática: No gastar 40 minutos cada que alguien quiere una cuenta de usuario.

# Especificación funcional

Los usuarios entran desde su navegador a <http://castillo.cluster.inmegen.gob.mx>,
acceden con su cuenta de usuario y contraseña en el clúster institucional
o con la cuenta de usuario y contraseña de su cuenta de correo institucional.

A los usuarios comunes se les muestra documentación del clúster institucional
y les permite cambiar su contraseña o reestablecerla si no tienen acceso.

A los investigadores líderes les muestra un menú en el que pueden generar cuentas de usuario,
extender el periodo de uso de sus estudiantes
o terminar el periodo de acceso de las cuentas de usuario a su cargo.

# Requerimientos de calidad

- Cada página debe cargar en menos de 800ms

# Especificación técnica

Esta aplicación genera usuarios en el nodo principal del clúster institucional,
porque desde allí se gestiona el acceso a los servidores del clúster.

## Autenticación

La autenticación se realiza con los usuarios del sistema operativo
y en un futuro se podría implementar el acceso con correo institucional.

La aplicación debe verificar que el usuario existe
y que es parte del grupo de "investigadores líderes"
para permitir el acceso.

Adicionalmente, para realizar administración de usuarios,
se verifica que pertenece además al grupo de investigación que quiere administrar
y los usuarios que está modificando también.

## Generar nuevos usuarios

Si estas condiciones se cumplen,
la aplicación generará un usuario de acuerdo al procedimiento 20
del [Manual de Procedimientos del Instituto Nacional de Medicina Genómica][manual]
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

Al generar un usuario, se le enviará un correo electrónico
con una liga para confirmar su correo electrónico y establecer su contraseña.

## Cambiar fecha de expiración de usuarios

Un investigador líder puede cambiar la fecha de expiración de los usuarios que pertenecen a su grupo de investigación.
Esta vista muestra un menú de los usuarios dentro de su grupo de investigación
y la fecha en que expiran.

Para estudiantes, la fecha no puede ser más allá de dos años en el futuro (tiempo para proyectos de maestría).

La expiración de usuarios con cuenta de correo institucional se debe realizar cuando se da de baja una persona.

[manual]: http://www.inmegen.gob.mx/media/filer_public/e0/21/e021bb2a-0863-49ae-a75a-43cb524c4085/manual_procedimientos_inmegen_2018_18oct18_ni.pdf
