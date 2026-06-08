# DriveDrop

**Sube archivos a Google Drive desde el clic derecho de Windows.**

DriveDrop es una utilidad para Windows que permite enviar archivos y carpetas a Google Drive de forma rápida, local y sencilla, directamente desde el menú contextual del Explorador de archivos.

En lugar de abrir el navegador, entrar a Google Drive, buscar el archivo y subirlo manualmente, DriveDrop reduce todo ese proceso a una sola acción:

```text
Clic derecho → Subir con DriveDrop → listo
```

---

## ¿Por qué existe DriveDrop?

Subir documentos a Google Drive debería ser una tarea simple. Sin embargo, el flujo tradicional suele ser repetitivo:

1. Abrir el navegador.
2. Entrar a Google Drive.
3. Iniciar sesión si hace falta.
4. Hacer clic en “Nuevo”.
5. Elegir “Subir archivo” o “Subir carpeta”.
6. Buscar el archivo en el explorador.
7. Confirmar la subida.

Para estudiantes, oficinas, administrativos, creadores de contenido o cualquier persona que guarda archivos en la nube constantemente, esos pasos se vuelven una pérdida de tiempo.

**DriveDrop nace para eliminar esa fricción.**

---

## Propuesta

DriveDrop agrega una opción al menú contextual de Windows:

```text
Subir con DriveDrop
```

Cuando el usuario selecciona un archivo o carpeta y usa esta opción, DriveDrop copia ese elemento a la carpeta local sincronizada de Google Drive. Luego, Google Drive para escritorio se encarga de subirlo automáticamente a la nube.

Esto permite tener una experiencia simple, rápida y sin configuraciones complejas.

---

## Características principales

- Subir archivos desde el clic derecho de Windows.
- Subir carpetas completas.
- Copiar archivos sin eliminar el original.
- Detección automática de carpetas locales de Google Drive.
- Creación automática de una carpeta `DriveDrop` dentro de Google Drive.
- Prevención de sobrescritura de archivos existentes.
- Icono personalizado en el menú contextual.
- Funcionamiento local sin servidores externos.
- No requiere Google Cloud.
- No requiere OAuth.
- No requiere configurar APIs.
- Ejecutable descargable desde GitHub Releases.

---

## Cómo funciona

```text
Archivo o carpeta seleccionada
        ↓
Clic derecho en Windows
        ↓
Subir con DriveDrop
        ↓
Copia local a Google Drive Desktop
        ↓
Sincronización automática en Google Drive
```

DriveDrop no reemplaza Google Drive. Lo complementa.

Su objetivo es hacer más cómodo el proceso de enviar archivos a la nube usando la sincronización local que ya ofrece Google Drive para escritorio.

---

## Ventajas

### Menos pasos

El usuario no necesita abrir el navegador ni navegar por Google Drive manualmente.

### Más productividad

Ideal para personas que respaldan documentos, tareas, reportes, imágenes, PDFs o carpetas de trabajo de forma frecuente.

### Sin costos extra

La versión MVP no usa servicios pagos, Google Cloud ni servidores propios.

### Simple de instalar

El usuario puede descargar el ejecutable desde Releases y configurar el menú contextual.

### Local y privado

DriveDrop trabaja en la computadora del usuario. No envía archivos a servidores externos propios.

---

## Público objetivo

DriveDrop está pensado para:

- Estudiantes que suben tareas y documentos.
- Oficinas administrativas.
- Personas que respaldan archivos frecuentemente.
- Usuarios que trabajan con PDFs, imágenes, documentos y hojas de cálculo.
- Equipos que necesitan simplificar flujos repetitivos.
- Cualquier usuario de Windows que use Google Drive para escritorio.

---

## Requisitos

Para usar DriveDrop se necesita:

- Windows 10 o Windows 11.
- Google Drive para escritorio instalado.
- Una cuenta de Google configurada en Google Drive Desktop.

No se necesita:

- Cuenta de Google Cloud.
- Tarjeta de crédito.
- Configuración de OAuth.
- Activar APIs manualmente.
- Servidores externos.

---

## Instalación

### Opción recomendada: descargar desde Releases

Puedes descargar la última versión de DriveDrop desde GitHub Releases:

[Descargar DriveDrop](https://github.com/sshioo/DriveDrop/releases)

En la sección **Assets**, descarga el archivo:

```text
DriveDrop.exe
```

> Nota: Windows puede mostrar una advertencia de seguridad porque el ejecutable no está firmado digitalmente. Esto es normal en proyectos personales o de código abierto.

### Instalar Google Drive para escritorio

Si todavía no tienes Google Drive para escritorio, descárgalo desde:

```text
https://www.google.com/drive/download/
```

Inicia sesión con tu cuenta de Google y asegúrate de que tu unidad local de Drive esté disponible.

Ejemplos de rutas comunes:

```text
G:\My Drive
G:\Mi unidad
C:\Users\usuario\Google Drive
```

### Guardar el ejecutable

Guarda `DriveDrop.exe` en una carpeta fija de tu equipo, por ejemplo:

```text
C:\Users\TU_USUARIO\AppData\Local\DriveDrop\DriveDrop.exe
```

Esto ayuda a que el menú contextual siempre apunte al mismo lugar.

### Configurar el menú contextual

Configura el menú contextual para que apunte a la ruta donde guardaste `DriveDrop.exe`.

Después de configurarlo, aparecerá la opción:

```text
Subir con DriveDrop
```

En Windows 11, puede aparecer dentro de:

```text
Mostrar más opciones
```

Actualmente, DriveDrop v0.1.0 incluye el ejecutable como descarga directa. En próximas versiones se publicará un paquete `.zip` con instalador, desinstalador e iconos listos para usar.

---

## Uso

1. Selecciona un archivo o carpeta.
2. Haz clic derecho.
3. Elige:

```text
Subir con DriveDrop
```

4. DriveDrop copiará el elemento a Google Drive.
5. Google Drive Desktop lo sincronizará automáticamente.

---

## Estructura del proyecto

```text
DriveDrop/
├─ app/
│  ├─ main.py
│  ├─ config.py
│  ├─ copier.py
│  ├─ notifications.py
│  └─ drivedrop.bat
├─ assets/
│  └─ drivedrop.ico
├─ installer/
│  ├─ install_context_menu.reg
│  └─ uninstall_context_menu.reg
├─ requirements.txt
├─ README.md
├─ LICENSE
└─ .gitignore
```

---

## Desarrollo

Clonar el repositorio:

```powershell
git clone https://github.com/sshioo/DriveDrop.git
cd DriveDrop
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
```

Probar desde terminal:

```powershell
python -m app.main "C:\ruta\archivo.pdf"
```

Crear ejecutable:

```powershell
python -m PyInstaller --onefile --noconsole --clean --icon "assets\drivedrop.ico" --name DriveDrop "app\main.py"
```

El ejecutable se generará en:

```text
dist\DriveDrop.exe
```

Probar el ejecutable:

```powershell
.\dist\DriveDrop.exe "C:\ruta\archivo.pdf"
```

---

## Publicación en Releases

Para distribuir DriveDrop, el ejecutable se publica en GitHub Releases en lugar de subirse directamente al repositorio.

Release actual:

```text
v0.1.0
```

Asset principal:

```text
DriveDrop.exe
```

Esto permite que los usuarios descarguen la aplicación sin clonar el repositorio.

Para crear una nueva versión:

```powershell
git tag v0.1.0
git push origin v0.1.0
```

Luego se crea un nuevo release en GitHub y se adjunta:

```text
dist\DriveDrop.exe
```

En futuras versiones se recomienda publicar un paquete `.zip` con:

```text
DriveDrop.exe
install_context_menu.bat
uninstall_context_menu.bat
assets/drivedrop.ico
README.txt
```

---

## Estado del proyecto

DriveDrop se encuentra en una primera versión MVP.

La prioridad de esta versión es validar el flujo principal:

```text
Enviar archivos a Google Drive desde el clic derecho de Windows.
```

---

## Hoja de ruta

Próximas mejoras planeadas:

- Instalador completo para Windows.
- Interfaz gráfica de configuración.
- Selección personalizada de carpeta destino.
- Modo copiar o mover.
- Soporte mejorado para múltiples archivos.
- Notificaciones con progreso.
- Historial de archivos enviados.
- Integración opcional con Google Drive API.
- Soporte para otros servicios en la nube.

---

## Filosofía del proyecto

DriveDrop busca resolver una tarea cotidiana con una experiencia simple.

No intenta ser una plataforma compleja ni reemplazar herramientas existentes. Su propósito es reducir pasos, ahorrar tiempo y hacer que una acción repetitiva se sienta natural dentro del flujo de trabajo de Windows.

La mejor herramienta no siempre es la más grande. A veces es la que aparece justo donde la necesitas.

---

## Licencia

Este proyecto está publicado bajo la licencia MIT.

```text
Copyright (c) 2026 Shioo
```

Puedes usar, modificar y distribuir este software respetando los términos de la licencia.

Consulta el archivo `LICENSE` para más detalles.
