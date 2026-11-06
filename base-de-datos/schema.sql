CREATE DATABASE IF NOT EXISTS openrepair
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci;

USE openrepair;

-- Users table (login)
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(256) NOT NULL,
    rol ENUM('admin', 'tecnico') NOT NULL DEFAULT 'tecnico',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Customers table
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Repairs table
CREATE TABLE reparaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(20) NOT NULL UNIQUE,
    cliente_id INT NOT NULL,
    tipo_dispositivo VARCHAR(50) NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    averia TEXT NOT NULL,
    observaciones TEXT,
    estado VARCHAR(30) DEFAULT 'Recibido',
    presupuesto DECIMAL(8,2),
    precio_final DECIMAL(8,2),
    presupuesto_aceptado BOOLEAN DEFAULT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Repair counter by year (never decreases)
CREATE TABLE contadores (
    year INT PRIMARY KEY,
    ultimo_num INT NOT NULL DEFAULT 0
);

-- Status history table
CREATE TABLE historial_estados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reparacion_id INT NOT NULL,
    estado VARCHAR(50) NOT NULL,
    tecnico VARCHAR(100),
    nota TEXT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (reparacion_id) REFERENCES reparaciones(id)
);

ALTER TABLE usuarios MODIFY rol ENUM('admin', 'manager', 'tecnico', 'readonly') NOT NULL DEFAULT 'tecnico';
ALTER TABLE clientes ADD COLUMN numero_cliente VARCHAR(20) UNIQUE AFTER id, ADD COLUMN apellido VARCHAR(100) AFTER nombre, ADD COLUMN empresa VARCHAR(160), ADD COLUMN telefono_alternativo VARCHAR(30), ADD COLUMN direccion VARCHAR(200), ADD COLUMN suburbio VARCHAR(100), ADD COLUMN estado VARCHAR(40) DEFAULT 'Victoria', ADD COLUMN codigo_postal VARCHAR(10), ADD COLUMN tipo_cliente ENUM('individual','empresa','organizacion') DEFAULT 'individual', ADD COLUMN notas_internas TEXT, ADD COLUMN contacto_preferido ENUM('email','telefono','sms') DEFAULT 'telefono', ADD COLUMN consentimiento_marketing BOOLEAN DEFAULT FALSE;
ALTER TABLE reparaciones ADD COLUMN categoria_dispositivo VARCHAR(60), ADD COLUMN numero_serie VARCHAR(120), ADD COLUMN imei VARCHAR(40), ADD COLUMN color VARCHAR(50), ADD COLUMN condicion TEXT, ADD COLUMN accesorios TEXT, ADD COLUMN danos_fisicos TEXT, ADD COLUMN bloqueo_dispositivo TEXT, ADD COLUMN fecha_ingreso DATETIME DEFAULT CURRENT_TIMESTAMP, ADD COLUMN fecha_prevista DATE, ADD COLUMN prioridad ENUM('baja','normal','alta','urgente') DEFAULT 'normal', ADD COLUMN tecnico_id INT NULL, ADD COLUMN notas_internas TEXT, ADD COLUMN notas_cliente TEXT, ADD COLUMN portal_token_hash CHAR(64) UNIQUE, ADD COLUMN portal_token_expira DATETIME, ADD COLUMN portal_token_revocado BOOLEAN DEFAULT FALSE, ADD COLUMN moneda CHAR(3) DEFAULT 'AUD';

CREATE TABLE reparacion_fotos (id INT AUTO_INCREMENT PRIMARY KEY, reparacion_id INT NOT NULL, ruta VARCHAR(255) NOT NULL, etiqueta VARCHAR(60), mime_type VARCHAR(100), creado_por INT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (reparacion_id) REFERENCES reparaciones(id) ON DELETE CASCADE);
CREATE TABLE bitacora_trabajo (id INT AUTO_INCREMENT PRIMARY KEY, reparacion_id INT NOT NULL, usuario_id INT, tipo VARCHAR(40) DEFAULT 'nota', contenido TEXT NOT NULL, minutos INT DEFAULT 0, creado_at DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (reparacion_id) REFERENCES reparaciones(id) ON DELETE CASCADE);
CREATE TABLE auditoria (id BIGINT AUTO_INCREMENT PRIMARY KEY, usuario_id INT, accion VARCHAR(80) NOT NULL, entidad VARCHAR(80), entidad_id INT, detalles JSON, creado_at DATETIME DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE cotizaciones (id INT AUTO_INCREMENT PRIMARY KEY, reparacion_id INT NOT NULL, version INT NOT NULL DEFAULT 1, estado ENUM('borrador','enviada','aprobada','rechazada','expirada') DEFAULT 'borrador', subtotal DECIMAL(10,2) DEFAULT 0, descuento DECIMAL(10,2) DEFAULT 0, total DECIMAL(10,2) DEFAULT 0, vence_el DATE, comentarios_cliente TEXT, portal_token_hash CHAR(64) UNIQUE, aprobado_en DATETIME, creado_por INT, creado_at DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (reparacion_id) REFERENCES reparaciones(id) ON DELETE CASCADE);
CREATE TABLE piezas (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(160) NOT NULL, sku VARCHAR(80) UNIQUE, fabricante VARCHAR(100), proveedor VARCHAR(160), coste DECIMAL(10,2) DEFAULT 0, precio DECIMAL(10,2) DEFAULT 0, cantidad INT DEFAULT 0, minimo INT DEFAULT 0, ubicacion VARCHAR(80), dolibarr_id VARCHAR(80));
CREATE TABLE reparacion_piezas (id INT AUTO_INCREMENT PRIMARY KEY, reparacion_id INT NOT NULL, pieza_id INT NOT NULL, cantidad INT NOT NULL, estado ENUM('reservada','consumida','devuelta') DEFAULT 'reservada', UNIQUE KEY uq_repair_part (reparacion_id,pieza_id), FOREIGN KEY (reparacion_id) REFERENCES reparaciones(id) ON DELETE CASCADE, FOREIGN KEY (pieza_id) REFERENCES piezas(id));
CREATE TABLE integraciones (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(40) UNIQUE NOT NULL, habilitada BOOLEAN DEFAULT FALSE, configuracion_cifrada TEXT, ultimo_sync DATETIME, ultimo_error TEXT);
CREATE TABLE mensajes (id INT AUTO_INCREMENT PRIMARY KEY, cliente_id INT NOT NULL, reparacion_id INT, canal ENUM('email','sms') NOT NULL, destinatario VARCHAR(200), asunto VARCHAR(200), contenido TEXT NOT NULL, estado ENUM('pendiente','enviado','fallido') DEFAULT 'pendiente', enviado_at DATETIME, error TEXT, creado_at DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (cliente_id) REFERENCES clientes(id), FOREIGN KEY (reparacion_id) REFERENCES reparaciones(id) ON DELETE SET NULL);
CREATE TABLE garantias (id INT AUTO_INCREMENT PRIMARY KEY, reparacion_id INT NOT NULL, reparacion_original_id INT, inicio DATE NOT NULL, fin DATE NOT NULL, cobertura TEXT, exclusiones TEXT, estado ENUM('activa','reclamada','resuelta','anulada') DEFAULT 'activa', FOREIGN KEY (reparacion_id) REFERENCES reparaciones(id), FOREIGN KEY (reparacion_original_id) REFERENCES reparaciones(id));
