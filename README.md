# Este es mi primer blog.
**Alumno: Juan Pablo Spera
Versión: entrega final**

La web es un blog personal sólo para usuarios registrados. Es decir, el autor es el único en poder subir posts al blog (por ello es personal) y, para tener acceso al contenido del blog, hay que estar registrado.

Por ello, al iniciar somos dirigidos a la página de login. Si no contamos con un usuario podemos registrarlo con el botón de arriba a la derecha, para a continuación realizar el correspondiente login. Hasta que no se realiza correctamente el login todos los demás botones están bloqueados (salvo los links de abajo a facebook, twitter e instagram).

Una vez loggeado, accedemos a la página de principal del blog, que tiene arriba a la izquierda el nombre del usuario loggeado (clickando en el mismo se puede editar el usuario), seguido del avatar del usuario (clickando en el punto se puede subir o modificar la foto).

La botonera verde ariba a la derecha cuenta con links a la página principal, la página acerca del autor, la página para subir, modificar o eliminar posts (sólo se puede acceder estando loggeado como superusuario, es decir para que acceda sólo el autor del blog personal), los datos de contacto y el botón de logout.

En la página principal, debajo de las fotos que van rotando, con el título Mi Blog, se van listando (de más nuevo a más antiguo) todos los posts subidos por el autor/administrador.

Cada post/blog cuenta con un título,, un subtítulo (opcional), un comentario (el comentario se puede crear con emoticons, estilos, colores, ya que cuenta con CKEditor), y puede contar con una imagen y/o un link (y en la página principal se enseñará también la fecha de creación). Los posts se pueden crear, editar o eliminar desde el panel del administrador o desde la web entrando en el botón admin (restringido) sólo como superusuario, ya que de lo contrario nos pedirá un login con más atributos. 

Para subir, editar o eliminar un post hay que loguearse como admin en http://127.0.0.1:8000/admin/

Nombre de usuario: juanspera

Contraseña: bocajrs1

Una vez subidos los posts en la página principal del blog se pueden visualizar las imágenes haciendo click en las mismas, así como acceder a los links de los posts (por ejemplo el link al github del autor).

Al finalizar la sesión se recomienda realizar correctamente el log out con el último botón de arriba a la derecha, ya que sino puede quedar el usuario conectado para futuras sesiones.

**Versión de Python:**

runtime.txt

**Libraries:**

requirements.txt

**Unit Tests:**

UnitTests.md