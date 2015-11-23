
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Proyecto para la materia de Base de Datos. Desarrollado en el framework Django.

Disponible en http://placemee.herokuapp.com.

## Características

- Usuarios pueden crear cuentas y dejar reviews en cualquier ubicación.
- Usuarios pueden ser ascendidos a "clientes" en el panel de admin para poder crear ubicaciones. Solo los clientes pueden añadir ubicaciones a la app.
- Los clientes pertenecen a una compañía/empresa, las ubicaciones se registran con el ID de dicha compañía.
- Se pueden generar reportes en CSV y PDF para las ubicaciones y reviews de las compañías. Solo los miembros de la compañía lo pueden descargar. Miembros de compañías no pueden ver los datos de compañías ajenas.
- Los admins pueden generar reportes con todas las ubicaciones y reviews en la app.
- Usuarios no pueden descargar los reportes.


## Cambios desde el jueves

- Usuarios ya no pueden crear ubicaciones, solo los "clientes".
- Los usuarios solo pueden ser ascendidos a clientes desde el panel de administración.
- Los admins deben aprobar las ubicaciones antes de que aparezcan en las listas. Si no es aprobada, solo se puede acceder via URL.
- Se cambiaron las primary keys de números por UUIDs base64 para las URLs.
- Se creó el dashboard de clientes donde se muestran gráficos lineares sobre las ubicaciones de la empresa del cliente (/app/dashboard/).
- Se creó el dashboard de admins donde se muestran gráficos lineares sobre todas las ubicaciones en la app (/app/dashboard/admin/).
- Se generan y descargan reportes de ubicaciones y reviews en CSV y PDF desde el dashboard de clientes de acuerdo a la compañía a la que pertenece el usuario que la descarga. Usuarios normales no pueden descargar, usuarios de una compañía no pueden ver datos de otras compañías.
- Se creó el listado de ubicaciones que pertenecen a cada compañía. Accesible desde el dashboard de clientes.
- Los admins pueden descargar reportes en CSV y PDF de todas las ubicaciones y reviews desde el dashboard de admins.
- Se corrigió el problema en el que si ya existía un review, los demás usuarios solo lo podían editar, no se podía agregar uno nuevo con el botón (Nuevo bug: un usuario puede crear miles de reviews en el mismo lugar).
- Ahora se guarda el average rating de cada ubicación en la base de datos y se cambiaron los corazones por estrellas para permitir medias estrellas en los ratings.
