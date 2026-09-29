"""English interface strings; database values remain in Spanish."""

import re


def browser_language(languages):
    return 'es' if any(
        lang.lower().split('-')[0] == 'es' and quality > 0
        for lang, quality in languages
    ) else 'en'


ENGLISH = {'* Al menos un dato de contacto (teléfono o email)': '* At least one contact detail (phone or '
                                                      'email)',
 '1. El plazo de recogida es de 30 días desde la notificación de finalización.': '1. Collect your '
                                                                                 'device within 30 '
                                                                                 'days of the '
                                                                                 'completion '
                                                                                 'notice.',
 '2. El presupuesto no incluye IVA salvo que se indique expresamente.': '2. The estimate excludes '
                                                                        'VAT unless expressly '
                                                                        'stated.',
 '3. OpenRepair no se hace responsable de datos almacenados en el dispositivo.': '3. OpenRepair is '
                                                                                 'not responsible '
                                                                                 'for data stored '
                                                                                 'on the device.',
 '4. Este resguardo es necesario para la recogida del dispositivo.': '4. This receipt is required '
                                                                     'to collect the device.',
 'AVERÍA / MOTIVO DE ENTRADA': 'ISSUE / REASON FOR INTAKE',
 'Acceso al panel de gestión': 'Sign in to your workshop',
 'Acceso restringido a administradores.': 'Administrator access only.',
 'Administrador': 'Administrator',
 'Alta': 'Added',
 'Alta:': 'Added:',
 'Anterior': 'Previous',
 'Avería': 'Issue',
 'Avería *': 'Issue *',
 'Avería:': 'Issue:',
 'Buscar': 'Search',
 'Buscar por código, nombre o teléfono...': 'Search by code, name, or phone...',
 'CONDICIONES DE SERVICIO:': 'SERVICE TERMS:',
 'Cambiar estado': 'Change status',
 'Cambio de estado no válido.': 'Invalid status change.',
 'Cancelar': 'Cancel',
 'Cerrar': 'Close',
 'Cliente': 'Customer',
 'Cliente actualizado correctamente.': 'Customer updated successfully.',
 'Cliente no encontrado.': 'Customer not found.',
 'Cliente:': 'Customer:',
 'Clientes': 'Customers',
 'Consola': 'Console',
 'Contraseña': 'Password',
 'Creado correctamente.': 'Created successfully.',
 'Crear nuevo usuario': 'Create user',
 'Crear usuario': 'Create user',
 'Código': 'Code',
 'DATOS DEL CLIENTE': 'CUSTOMER DETAILS',
 'DATOS DEL DISPOSITIVO': 'DEVICE DETAILS',
 'Dar entrada y generar resguardo': 'Create repair and generate receipt',
 'Datos del cliente': 'Customer details',
 'Datos del dispositivo': 'Device details',
 'Descargar': 'Download',
 'Describir el problema del dispositivo...': 'Describe the device problem...',
 'Descripción de la avería *': 'Issue description *',
 'Desde': 'From',
 'Desde entrada hasta entrega al cliente': 'From intake to customer delivery',
 'Diagnosticado': 'Diagnosed',
 'Dispositivo': 'Device',
 'Dispositivo:': 'Device:',
 'Editar': 'Edit',
 'Editar cliente': 'Edit customer',
 'Editar datos': 'Edit details',
 'El nombre es obligatorio.': 'Name is required.',
 'Eliminar': 'Delete',
 'Email o contraseña incorrectos.': 'Incorrect email or password.',
 'En curso': 'In progress',
 'Entrada:': 'Intake:',
 'Entradas registradas en el periodo actual': 'Repairs created this period',
 'Entrar': 'Sign in',
 'Entregado': 'Delivered',
 'Enviar presupuesto': 'Send estimate',
 'Esperando pieza': 'Waiting for part',
 'Estado': 'Status',
 'Estado operativo, distribución de cargas y actividad reciente del periodo en curso.': 'Workshop '
                                                                                        'status, '
                                                                                        'workload '
                                                                                        'distribution, '
                                                                                        'and '
                                                                                        'recent '
                                                                                        'activity '
                                                                                        'for the '
                                                                                        'current '
                                                                                        'period.',
 'Este mes': 'This month',
 'Exportar CSV': 'Export CSV',
 'Facturado en reparaciones entregadas': 'Revenue from delivered repairs',
 'Fecha': 'Date',
 'Fecha entrada': 'Intake date',
 'Fecha:': 'Date:',
 'Filtrar': 'Filter',
 'Firma del cliente:': 'Customer signature:',
 'Gasto total:': 'Total spent:',
 'Golpes, arañazos, accesorios entregados...': 'Dents, scratches, accessories included...',
 'Guardar cambios': 'Save changes',
 'Guardar precio': 'Save price',
 'Hasta': 'To',
 'Historial': 'History',
 'Historial de reparaciones': 'Repair history',
 'Importe presupuesto (€)': 'Estimate amount (€)',
 'Imprimir resguardo': 'Print receipt',
 'Indica al menos un dato de contacto (teléfono o email).': 'Enter at least one contact detail '
                                                            '(phone or email).',
 'Indicadores clave': 'Key metrics',
 'Ingresos / mes': 'Revenue / month',
 'Inicia sesión para continuar.': 'Sign in to continue.',
 'Iniciar sesión': 'Sign in',
 'Limpiar': 'Clear',
 'Listo': 'Ready',
 'Marca': 'Brand',
 'Marca:': 'Brand:',
 'Modelo': 'Model',
 'Modelo:': 'Model:',
 'Móvil': 'Mobile phone',
 'No hay reparaciones': 'No repairs found',
 'No hay usuarios registrados.': 'No users registered.',
 'No puedes eliminar tu propio usuario.': 'You cannot delete your own user.',
 'Nombre': 'Name',
 'Nombre *': 'Name *',
 'Nombre del cliente': 'Customer name',
 'Nombre del técnico': 'Technician name',
 'Nombre, avería y tipo de dispositivo son obligatorios.': 'Name, issue, and device type are '
                                                           'required.',
 'Nombre:': 'Name:',
 'Nueva entrada': 'New repair',
 'OBSERVACIONES': 'NOTES',
 'Obs:': 'Notes:',
 'Observaciones': 'Notes',
 'Observaciones / Estado estético': 'Notes / Cosmetic condition',
 'Ordenador': 'Desktop computer',
 'Otro': 'Other',
 'Panel de administración': 'Administration',
 'Panel de control': 'Dashboard',
 'Portátil': 'Laptop',
 'Precio final': 'Final price',
 'Precio final (€)': 'Final price (€)',
 'Precio final:': 'Final price:',
 'Presupuesto': 'Estimate',
 'Presupuesto / Precio': 'Estimate / Price',
 'Presupuesto aceptado': 'Estimate accepted',
 'Presupuesto enviado': 'Estimate sent',
 'Presupuesto:': 'Estimate:',
 'Página': 'Page',
 'Recibido': 'Received',
 'Reimprimir PDF': 'Reprint PDF',
 'Reparaciones': 'Repairs',
 'Reparaciones activas pendientes de entrega': 'Active repairs awaiting delivery',
 'Reparaciones por estado': 'Repairs by status',
 'Reparación actualizada.': 'Repair updated.',
 'Reparación no encontrada.': 'Repair not found.',
 'Reparando': 'Repairing',
 'Resumen del': 'Workshop',
 'Rol': 'Role',
 'Salir': 'Sign out',
 'Seleccionar estado...': 'Select status...',
 'Seleccionar...': 'Select...',
 'Servicio técnico de reparaciones — Tel: 600 000 000': 'Repair service — Phone: 600 000 000',
 'Sesión cerrada.': 'Signed out.',
 'Siguiente': 'Next',
 'Sin actividad reciente.': 'No recent activity.',
 'Sobremesa': 'Desktop computer',
 'Sí, eliminar': 'Yes, delete',
 'Tel:': 'Phone:',
 'Teléfono': 'Phone',
 'Teléfono:': 'Phone:',
 'Tiempo medio': 'Average time',
 'Tipo de dispositivo *': 'Device type *',
 'Tipo dispositivo': 'Device type',
 'Tipo:': 'Type:',
 'Tipos de dispositivo': 'Device types',
 'Todas →': 'All →',
 'Todos': 'All',
 'Todos los campos son obligatorios.': 'All fields are required.',
 'Total reparaciones:': 'Total repairs:',
 'Técnico': 'Technician',
 'Tú': 'You',
 'Usuario no encontrado.': 'User not found.',
 'Usuarios registrados': 'Registered users',
 'Ver todas →': 'View all →',
 'Ya existe un usuario con ese email.': 'A user with that email already exists.',
 'cliente@email.com': 'customer@email.com',
 'de': 'of',
 'días': 'days',
 'taller': 'overview',
 '¿Seguro que quieres eliminar esta reparación? Esta acción no se puede deshacer.': 'Are you sure '
                                                                                    'you want to '
                                                                                    'delete this '
                                                                                    'repair? This '
                                                                                    'action cannot '
                                                                                    'be undone.',
 'Últimas entradas': 'Latest repairs',
 '— Actividad': '— Activity',
 '— Carga de trabajo': '— Workload',
 '— Distribución': '— Distribution',
 '— Flujo operativo': '— Workflow',
 '✂ Cortar por aquí — Etiqueta para el dispositivo': '✂ Cut here — Device label'}


def translate(text):
    if not isinstance(text, str):
        return text
    if text in ENGLISH:
        return ENGLISH[text]

    patterns = (
        (r'^Estado cambiado a "(.+)"\.$', lambda m: f'Status changed to "{translate(m[1])}".'),
        (r'^Presupuesto de (.+)€ enviado\.$', lambda m: f'Estimate of €{m[1]} sent.'),
        (r'^Precio final: (.+)€\.$', lambda m: f'Final price: €{m[1]}.'),
        (r'^Reparación (.+) eliminada\.$', lambda m: f'Repair {m[1]} deleted.'),
        (r'^Usuario "(.+)" creado correctamente\.$', lambda m: f'User "{m[1]}" created successfully.'),
        (r'^Usuario "(.+)" eliminado\.$', lambda m: f'User "{m[1]}" deleted.'),
    )
    for pattern, format_message in patterns:
        match = re.fullmatch(pattern, text)
        if match:
            return format_message(match)
    return text
