
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Proyecto para la materia de Base de Datos. Desarrollado en el framework Django.

Disponible en http://placemee.herokuapp.com.

## Caracteristicas

- Usuarios pueden crear cuentas y dejar reviews en cualquier ubicacion.
- Usuarios pueden ser ascendidos a "clientes" en el panel de admin para poder crear ubicaciones. Solo los clientes pueden añadir ubicaciones a la app.
- Los clientes pertenecen a una compañia/empresa, las ubicaciones se registran con el ID de dicha compañia.
- Se pueden generar reportes en CSV para las ubicaciones y reviews de las compañias. Solo los miembros de la compañia lo pueden descargar. Miembros de compañias no pueden ver los datos de compañias ajenas.
- Los admins pueden generar reportes con todas las ubicaciones y reviews en la app.
- Usuarios no pueden descargar los reportes.


## Cambios desde el jueves

- Usuarios ya no pueden crear ubicaciones, solo los "clientes".
- Los usuarios solo pueden ser ascendidos a clientes desde el panel de administracion.
- Los admins deben aprobar las ubicaciones antes de que aparezcan en las listas. Si no es aprobada, solo se puede acceder via URL.
- Se cambiaron las primary keys de numeros por UUIDs base64 para las URLs.
- Se generan y descargan reportes de ubicaciones y reviews en CSV de acuerdo a la compañia a la que pertenece el usuario que la descarga. Usuarios normales no pueden descargar, usuarios de una compañia no pueden ver datos de otras compañias.
- Se corrigio el problema en el que si ya existia un review, los demas usuarios solo lo podian editar, no se podia agregar con el boton.