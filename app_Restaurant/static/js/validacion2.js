function validacionesFormulario(){
    
    let nombres, apellidos, usuario,email, telefono, contraseña1,contraseña2
    nombres = document.getElementById("first_name").value;
    apellidos = document.getElementById("last_name").value;
    usuario = document.getElementById("username").value;
    email = document.getElementById("email").value;
    telefono = document.getElementById("phone").value;
    contraseña1= document.getElementById("password1").value;
    contraseña2 = document.getElementById("password2").value;
    let espacios = false;
    let cont = 0;
   
  
  
  
    if(nombres == "" || apellidos == ""|| usuario == ""|| email == "" || telefono =="" ||contraseña1 == "" || contraseña2 == "" ){
  
      swal("Advertencia", "...todos los campos son obligatorios", "warning");
    
      return false;
    } 
  
    while (!espacios && (cont < contraseña1.length)) {
      if (contraseña1.charAt(cont) == " ")
        espacios = true;
      cont++;
    }
     
    if (espacios) {
        	        				
		swal("Advertencia", "...La contraseña no puede contener espacios en blanco", "warning");
        
      return false;
    }
  
    if (contraseña1 != contraseña2) {
        			        				
		swal("Advertencia", "...Las Contraseñas deben de coincidir", "warning");
        
        return false;
      } else {
        swal("Excelente", "Registro exitoso");	
        return true; 
    }
  
}