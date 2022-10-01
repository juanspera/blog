# Este es mi primer blog.
**Alumno: Juan Pablo Spera
Versión: entrega final**

La web es un blog personal sólo para usuarios registrados. Es decir, el autor es el único en poder subir, modificar o eliminar posts al blog (por ello es personal) y, para tener acceso al contenido del blog, hay que estar registrado.

Por ello, al iniciar somos dirigidos a la página de login. Si no contamos con un usuario, podemos registrarlo con el botón de arriba a la derecha, para a continuación realizar el correspondiente login. Hasta que no se realiza correctamente el login todos los demás botones están bloqueados (salvo los links de abajo a facebook, twitter e instagram).

Una vez loggeado, accedemos a la página de principal del blog, que tiene arriba a la izquierda el nombre del usuario loggeado (clickando en el mismo se puede editar el usuario), seguido del avatar del usuario (clickando en el punto se puede subir por primera vez un avatar o modificarlo).

La botonera verde arriba a la derecha cuenta con links a la página principal, la página acerca del autor, la página para que nos da acceso a subir, modificar o eliminar posts (sólo se puede acceder estando loggeado como superusuario, es decir para que acceda sólo el autor del blog personal), los datos de contacto y el botón de logout.

En la página principal debajo de las fotos que van rotando, con el título Mi Blog, se van listando (de más nuevo a más antiguo) todos los posts subidos por el autor/administrador.

En la página principal del blog se pueden visualizar las imágenes de los posts haciendo click en las mismas, así como acceder a los links de los posts (por ejemplo el link al github del autor). Además, en la página principal también se pueden filtrar los posts por palabras que contengan los títulos con el botón azul "Filtrar" a la derecha de Mi blog.

Cada post/blog cuenta con un título,, un subtítulo (opcional), un comentario (el comentario se puede crear con emoticons, estilos, colores, ya que cuenta con CKEditor), y puede contar con una imagen y/o un link (y también se enseñará la fecha de creación automáticamente). Los posts se pueden crear, editar o eliminar desde el panel del administrador o desde la web entrando en el botón admin (restringido) sólo como superusuario, ya que de lo contrario nos pedirá un login con más atributos. 

Para subir, editar o eliminar un post hay que loguearse como admin y se puede hacer desde la página panel accediendo con el botón "admin (restringido)" o en http://127.0.0.1:8000/admin/

Nombre de superusuario: juanspera

Contraseña: bocajrs1


Al finalizar la sesión se recomienda realizar correctamente el log out con el último botón de arriba a la derecha, ya que sino puede quedar el usuario conectado para futuras sesiones.

**Versión de Python:**

runtime.txt

**Libraries:**

requirements.txt

**Unit Tests:**

UnitTests.md