# Visión y alcance

Automatizar la gestión de usuarios del clúster institucional.

# Definición de producto

Permite a los investigadores líderes que trabajan en el INMEGEN
generar cuentas de usuario para que sus estudiantes y asociados
usen los recursos del clúster institucional,
eliminando la necesidad de administrar manualmente las cuentas de usuario.

# Glosario

Instituto: El Instituto Nacional de Medicina Genómica.

Clúster Institucional: El grupo de cómputo dedicado a cómputo científico en el Instituto.

Investigador Líder: La persona responsable de un Grupo de Investigación en el Instituto

Grupo de Investigación: El identificador de grupo de sistema operativo utiliza para administrar los permisos de las Cuentas de Usuario.

Usuario: La persona que utilizará el Clúster Institucional.

Cuenta de Usuario: El identificador que la persona usa para acceder al Clúster Institucional o al Correo Institucional.

Contraseña: el secreto que permite a los Usuarios acceder a los recursos del Clúster Institucional.

Periodo de Acceso: el periodo durante el que un usuario puede acceder a los recursos del Clúster Institucional con su Cuenta de Usuario.

Correo Institucional: cuenta de correo electrónico de los dominios `inmegen.gob.mx` o `inmegen.edu.mx`.

# Requerimientos de negocio

- Liberar tiempo de la Subdirección de Bionformática para el desarrollo de sistemas bioinformáticos.
- Reportar en la meta de automatizar procesos de gestión.
- Automatizar el reporte de usuarios requerido en el procedimiento 20 del [Manual de Procedimientos del Instituto Nacional de Medicina Genómica][manual].
- Mejorar el tiempo de respuesta para los Investigadores Líderes.

# Actores y sus intereses

- Usuario: Usar el clúster.
- Investigador Líder: Que sus estudiantes trabajen en su artículo.
- Subdirección de Bioinformática: No gastar 40 minutos cada que alguien quiere una Cuenta de Usuario.

# Especificación funcional

El Usuario entra desde su navegador a <http://castillo.cluster.inmegen.gob.mx>,
acceden con su Cuenta de Usuario y Contraseña en el Clúster Institucional
o con la Cuenta de Usuario y Contraseña de su Correo Institucional.
Estas dos formas de acceso son equivalentes.

Cualquier Usuario puede ver documentación del Clúster Institucional
y establecer, cambiar o restablecer su Contraseña.

El Investigador Líder observa un menú en el que puede
- Generar o eliminar Cuentas de Usuario que únicamente pertenezcan a su Grupo de Investigación,
- Extender o terminar el Periodo de Acceso de las cuentas de usuario a su cargo.
- Agregar o eliminar el acceso de Cuentas de Usuario a su Grupo de Investigación.

El administrador del Clúster Institucional puede
- generar, eliminar o actualizar un Grupo de Investigación,
- asignar la Cuenta de Usuario del responsable como Invesigador Líder,
- y generar un [reporte del número de usuarios][manual] en el Clúster Institucional.

Cuando se genera una Cuenta de Usuario se notifica al Usuario para establecer su Contraseña.

Cada Cuenta de Usuario debe permitir el acceso al Clúster Institucional durante el Periodo de Acceso.

# Requerimientos de calidad

- Cada página debe cargar en menos de 800ms dentro del Instituto.

# Documentación suplementaria

[Manual de Procedimientos del Instituto Nacional de Medicina Genómica][manual]

[manual]: http://www.inmegen.gob.mx/media/filer_public/e0/21/e021bb2a-0863-49ae-a75a-43cb524c4085/manual_procedimientos_inmegen_2018_18oct18_ni.pdf

[Documentación de usuario del clúster institucional](# "Esta documentación aún no existe")

[Sistema de gestión del clúster institucional](https://github.com/xihh87/cluster/)
