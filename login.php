<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script
      src="https://kit.fontawesome.com/64d58efce2.js"
      crossorigin="anonymous"
    ></script>
    <link rel="stylesheet" href="style.css" />
    <title>Registro / Inicio de sesion</title>
  </head>
  <script src="https://code.jquery.com/jquery-3.5.0.js"></script>
  <body>
    <div class="container">
      <div class="forms-container">
        <div class="signin-signup">
          <form action="#" class="sign-in-form">
            <h2 class="title">Iniciar sesion</h2>
            <div class="input-field">
              <i class="fas fa-user"></i>
              <input type="text" placeholder="Usuario" id="usuario" />
            </div>
            <div class="input-field">
              <i class="fas fa-lock"></i>
              <input type="password" placeholder="Contraseña" id="password" />
            </div>
            <button value="Login" class="btn solid">Iniciar</button>
            <p class="social-text">O usa una de estas opciones</p>
            <div class="social-media">
              <a href="#" class="social-icon">
                <i class="fab fa-facebook-f"></i>
              </a>
              <a href="#" class="social-icon">
                <i class="fab fa-twitter"></i>
              </a>
              <a href="#" class="social-icon">
                <i class="fab fa-google"></i>
              </a>
              <a href="#" class="social-icon">
                <i class="fab fa-linkedin-in"></i>
              </a>
            </div>
          </form>
        </div>
      </div>
    </div>
    <script>
      function irAInicio(){
        console.log(document.getElementById("usuario").value);
        if(document.getElementById("usuario").value!="" && document.getElementById("password").value!=""){
          location.href="index.php";
        }
      }
      $(".btn").click(irAInicio)
    </script>
    <!-- <script src="app.js"></script> -->
  </body>
</html>