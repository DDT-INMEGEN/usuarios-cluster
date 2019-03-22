# Visión y alcance

Automatizar la gestión de usuarios del clúster institucional.

# Definición de producto

Permite a los investigadores líderes que trabajan en el INMEGEN
registrar inmediatamente a sus estudiantes y asociados
para usar los recursos del clúster institucional
y eliminar la administración manual.

# Requerimientos de negocio

- Liberar tiempo de la Subdirección de Bionformática para el desarrollo de sistemas bioinformáticos.
- Reportar en la meta de automatizar procesos de gestión.
- Automatizar el reporte de usuarios requerido en el procedimiento 20 del [Manual de Procedimientos del Instituto Nacional de Medicina Genómica][manual].
- Mejorar el tiempo de respuesta para los investigadores líderes.

# Especificación funcional

Los investigadores líderes entran desde su navegador a <http://castillo.cluster.inmegen.gob.mx>,
acceden con su usuario y contraseña en el clúster institucional
u opcionalmente con el usuario y contraseña de su cuenta de correo institucional.

A los usuarios comunes los dirige a una página de documentación del clúster institucional
y les permite cambiar su contraseña o reestablecerla si no tienen acceso.

A los investigadores líderes les muestra un menú en el que pueden generar usuarios,
extender el periodo de uso de sus estudiantes
o terminar el periodo de acceso de los usuarios a su cargo.

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
