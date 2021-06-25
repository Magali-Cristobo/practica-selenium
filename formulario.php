<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="../main.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<script src="https://code.jquery.com/jquery-3.5.0.js"></script>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" id="inicio" href="index.php">Inicio</a>
        </li>
        <li class="nav-item active">
          <a class="nav-link" id="formulario" href="formulario.php">Formulario<span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" id="iniciarSesion" href="login.php">Iniciar Sesion</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#">Contacto</a>
        </li>
      </ul>
    </div>
  </nav>
  <div class="container wrapper">
    <form onsubmit="return chequearForm(event)">
      <label class="pageTitle title">Formulario </label>
      <label class="secondaryTitle title">Complete el formulario de aca abajo.</label>
      <div class="form-group">
        <label>Ingrese el nombre</label>
        <input type="text" class="nombre form-control" id="nombre" placeholder="Name" />
      </div>
      <div class="form-group">
        <label>Ingrese el email</label>
        <input type="text" class="email form-control" id="email" placeholder="Email"/>
      </div>
      <div class="form-group">
        <label>Ingrese el mensaje</label>
        <textarea class="mensaje form-control" id="mensaje" placeholder="Mensaje"></textarea>
      </div>
      <input type="checkbox" class="termsConditions" value="Term">
      <label style="color: grey" for="terms"> Acepto los <span style="color: #0e3721">Terminos de uso</span> & <span style="color: #0e3721"></span>.</label><br>
        <p id="resultado" style="display: none"></p>
      <button class="btn enviar">Enviar</button>
    </form>
  </div>
  <script>
      function chequearForm(e){
          e.preventDefault();
          console.log(document.getElementById("nombre").value);
          console.log(document.getElementById("email").value);
          console.log(document.getElementById("mensaje").value);
          if(document.getElementById("nombre").value!="" && document.getElementById("email").value!="" && document.getElementById("mensaje").value!=""){
              console.log("entre");
              document.getElementById('resultado').innerHTML = 'Formulario enviado correctamente!';
              // $(".resultado").html("Formulario enviado correctamente!");
              $("#resultado").css("display","block");
              $("#resultado").css("color","green");
          }
          else{
              document.getElementById('resultado').innerHTML = 'Complete todos los campos';
              $("#resultado").css("display","block");
              $("#resultado").css("color","red");
          }

      }
      $(".btn").click(chequearForm);
  </script>
  <script src="app.js"></script>
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>

</html>
