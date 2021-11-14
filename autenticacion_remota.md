# MECANISMOS DE AUTENTIFICACIÓN REMOTA.
La autenticación es el proceso de confirmar que algo (o alguien) es quien dice ser. A la parte que se identifica se le llama probador. A la parte que verifica la identidad se la llama verificador. Es habitual que el probador sea un usuario que quiere acceder a ciertos recursos y el verificador sea un sistema que protege el acceso a dichos recursos y tiene que verificar que el que accede sea un usuario que tiene permisos para acceder a esos recursos. 
Para que nosotros podamos realizar una conexión a un equipo remoto debemos de conocer tres cosas:
* La dirección IP del equipo al que queremos acceder.
* El nombre de usuario con el que nos autenticaremos.
* La contraseña del usuario.
Si conocemos toda esta información podemos autenticarnos remotamente.

Fuente: Autenticación con servidores remotos. (2017). CódigoFacilito. Recuperado 7 de noviembre de 2021, de https://www.codigofacilito.com/articulos/autenticacion_servidores_remotos

![autenticacion](https://user-images.githubusercontent.com/50895566/140667572-10ea1f99-2a7e-4104-b6b3-2ea199c99338.jpg)

Con la autenticación remota, los usuarios de ACM Client pueden usar su nombre de usuario y contraseña de dominio local para acceder al sistema ACM. La autenticación remota utiliza un servidor de dominio externo para autenticar usuarios que tienen acceso al sistema o proteger un tipo de colaboración de extracción de LDAP de identidades. No se necesita una contraseña independiente configurada en el dispositivo ACM. Sin embargo, los permisos de acceso de los usuarios se basan aún en las funciones que tienen asignadas en el sistema ACM.

Antes de que se pueda configurar la autenticación remota en el dispositivo ACM, un administrador del sistema con privilegios en todos los servidores necesarios para admitir la autenticación remota debe:

Agregar uno o más dominios externos
Agregar uno o más servidores AD o LDAP a cada dominio del sistema
Emitir certificados raíz para cada dominio
Activar cada host remoto para presentar su certificado SSL al conectarse al software del servidor ACM
La configuración de los servidores de dominio externo y la creación de sus certificados raíz está fuera del alcance de este documento.

Para permitir la autenticación remota, debe:

Conectarse a los servidores de dominio externo que alojan los servidores AD o LDAP que desea usar para la autenticación y validar los certificados SSL que presentan. Lista Ajustes del sistema - Dominios externos.
Especificar el dominio predeterminado y el servidor que aloja la base de datos AD que se vaya a utilizar para la autenticación de los usuarios del software ACM y hacer cumplir la autenticación de certificados. Para obtener más información, consulte Página Ajustes del sistema: autenticación remota.
Los certificados SSL (capa de sockets seguros) se utilizan para comprobar hosts remotos y cifrar todo el tráfico de inicio de sesión entre hosts conectados. Solo los operadores de sistema ACM con privilegios administrativos y las siguientes delegaciones asignadas a su función pueden validar certificados SSL:

Certificados de validación de dominios externos: delegación requerida para validar un certificado SSL desde un host AD de Windows

Certificados de validación de colaboración: delegación requerida para validar un certificado SSL desde un host de la base de datos LDAP en una colaboración utilizando el tipo de colaboración servidor de extracción de LDAP de identidades

Puede configurar identidades diferentes para que se autentiquen por dominios diferentes. Cada identidad debe configurarse para utilizar uno de estos dominios para durante la autenticación. Esto se hace en la sección Información de la cuenta: en el panel Identidad:agregar o Identidad:editar de la Identidad dada. Para obtener más información, consulte

# Principales mecanismos de autenticación para aumentar la seguridad

Los mecanismos de autenticación para verificar la identidad digital de los usuarios se diferencian unos de otros según posean un mayor o menor número de factores de autenticación, interpretados cada uno de ellos como capas de seguridad que protegen la confidencialidad de los datos de autenticación. Son tres los factores mediante los cuales un usuario puede verificar su identidad:

* Por medio de algo que el usuario sabe: autenticación basada en información que solo él conoce. Por ejemplo, una contraseña o PIN.
* Por medio de algo que el usuario tiene: autenticación basada en la posesión de algo, ya sea físico o no. Por ejemplo, un token o un código recibido por SMS.
* Por medio de algo inherente al usuario: autenticación basada en una característica biométrica. Por ejemplo, su huella dactilar o el reconocimiento facial.

A estos factores se pueden sumar otros dos, de menor uso:

* Por medio de donde el usuario se encuentra: autenticación basada en su ubicación en el momento de realizar la acción.
* Por medio de lo que el usuario hace: autenticación basada en algún comportamiento específico sobre un dispositivo, como la forma en la que mueve el mouse o pulsa una tecla/pantalla.
