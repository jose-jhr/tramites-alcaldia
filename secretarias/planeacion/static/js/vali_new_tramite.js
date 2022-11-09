//detect button submit
$(document).ready(function(){
    //verifi form submit
    $("#form_new_tramite").submit(function(e){
        let error = false;
        //get data for validate
        var nombre = $("#nombre_tramite").val();
        if(nombre == ""){
            errorFocus("nombre_tramite");
            error = true;
        }

        var responsable = $("#responsable_tramite").val();
        if(responsable == ""){
            errorFocus("responsable_tramite");
            error = true;
        }

        var descripcion_tramite = $("#descripcion_tramite").val();
        if(descripcion_tramite == ""){
            errorFocus("descripcion_tramite");
            error = true;
        }

        if(error){
            e.preventDefault();
        }
        

    });
});

function errorFocus(id){
       //message error in #descripcion_tramite
       $("#"+id).after("<span class='error'>Este campo es obligatorio</span>");
       //message error in #descripcion_tramite
         $("#"+id).css("border","1px solid red");
         //desaparecer message error in #descripcion_tramite
            $("#"+id).keyup(function(){
                $(".error").fadeOut();
                $("#"+id).css("border","1px solid #ced4da");
                //delete <span>
                $(".error").remove();
            });
        
}