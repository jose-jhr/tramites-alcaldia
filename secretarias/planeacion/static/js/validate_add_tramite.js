$(document).ready(function(){

    $("#form_tramit").submit(function(e){
    //nombre_tramite,nombre_solic,num_ide_solic,contacto_solic,correo_solic,fecha_solic,state_solicitud,observacion,formFile
    //read views from form
    let error = false;
    let select_tip_tramit = $("#select_tip_tramit").val();
    let nombre_tramite_sec = $("#nombre_tramite_sec").val();
    let nombre_solic = $("#nombre_solic").val();
    let num_ide_solic = $("#num_ide_solic").val();
    let contacto_solic = $("#contacto_solic").val();
    let correo_solic = $("#correo_solic").val();
    let fecha_solic = $("#fecha_solic").val();
    let state_solicitud = $("#state_solicitud").val();
    let observaciones = $("#observacion").val();
    let formFile = $("#formFile").val();

    //test function vaalue form
    if(testValues(select_tip_tramit,nombre_tramite_sec,nombre_solic,num_ide_solic,contacto_solic,
        correo_solic,fecha_solic,state_solicitud,observaciones,formFile)){
        let id_tramite_tipo = $("#select_tip_tramit").val();
        let tip_tramites_tip = $("#select_tip_tramit option:selected").text();
        let nombre_tramite = $("#nombre_tramite_sec").val();
        let nombre_solicitante = $("#nombre_solic").val();
        let num_ide_solicitante = $("#num_ide_solic").val();
        let contacto_solicitante = $("#contacto_solic").val();
        let correo_solicitante = $("#correo_solic").val();
        let fecha_solicitud = $("#fecha_solic").val();
        let state_solicitud = $("#state_solicitud").val();
        let observaciones = $("#observacion").val();
        //add elements send form
        let formData = new FormData();
        formData.append('id_tramite_tipo',id_tramite_tipo);
        formData.append('tip_tramites_tip',tip_tramites_tip);
        formData.append('nombre_tramite',nombre_tramite);
        formData.append('nombre_solicitante',nombre_solicitante);
        formData.append('num_ide_solicitante',num_ide_solicitante);
        formData.append('contacto_solicitante',contacto_solicitante);
        formData.append('correo_solicitante',correo_solicitante);
        formData.append('fecha_solicitud',fecha_solicitud);
        formData.append('state_solicitud',state_solicitud);
        formData.append('observaciones',observaciones);
        formData.append('formFile',$('#formFile')[0].files[0]);
        //send form

        // Realiza la solicitud POST a la vista mi_vista en tu aplicación de Django
        fetch('/register_tramite', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            // Procesa la respuesta de la vista
            if (response.ok) {
                // La solicitud se realizó correctamente
                console.log('La solicitud POST se realizó correctamente.');
            } else {
                // Ocurrió un error al realizar la solicitud
                console.log('Ocurrió un error al realizar la solicitud POST.');
            }
        })
        .catch(error => {
            // Procesa cualquier error que ocurra durante la solicitud
            console.error(error);
        });

        /*
        alert('Enviando datos');
        $.ajax({
            url: '/register_tramite',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data){
                alert(data)
                if(data == 'ok'){
                    alert('Tramite agregado correctamente');
                }else{
                    alert('Error al agregar tramite');
                }
            }
        });

        */
    }else{
        e.preventDefault();
    }

    });



    function testValues(select_tip_tramit,nombre_tramite_sec,nombre_solic,num_ide_solic,contacto_solic,
        correo_solic,fecha_solic,state_solicitud,observaciones,formFile){
        //view select with select_tip_tramit is value!= 0
        if(select_tip_tramit == 0){
            alert("Seleccione un tipo de tramite por favor");
            //message error in select with id select_tip_tramit
            $("#select_tip_tramit").focus();
            return false;
        }
        if(nombre_tramite_sec == ""){
            alert("Ingrese el nombre del tramite por favor");
            //focus error color red in input with id nombre_tramite_sec
            focusElement("nombre_tramite_sec");
            return false;
        }
        if(nombre_solic == ""){
            alert("Ingrese el nombre del solicitante por favor");
            //focus error color red in input with id nombre_solic
            focusElement("nombre_solic");
            return false;
        }
        if(num_ide_solic == ""){
            alert("Ingrese el numero de identificacion del solicitante por favor");
            //focus error color red in input with id num_ide_solic
            focusElement("num_ide_solic");
            return false;
        }
        if(contacto_solic == ""){
            alert("Ingrese el numero de contacto del solicitante por favor");
            //focus error color red in input with id contacto_solic
            focusElement("contacto_solic");
            return false;
        }
        if(correo_solic == ""){
            alert("Ingrese el correo del solicitante por favor");
            //focus error color red in input with id correo_solic
            focusElement("correo_solic");
            return false;
        }
        if(fecha_solic == "" && "dd/mm/aaaa"){
            alert("Ingrese la fecha de solicitud por favor");
            //focus error color red in input with id fecha_solic
            focusElement("fecha_solic");
            return false;
        }
        if(state_solicitud == "0"){
            alert("Ingrese el estado de la solicitud por favor");
            //focus error color red in input with id state_solicitud
            focusElement("state_solicitud");
            return false;
        }
        return true;
    }

    function focusElement(element){
        //focus red
        $("#"+element).css("border","1px solid red");
        //no focus click in input with id nombre_tramite_sec
        $("#"+element).click(function(){
            $("#"+element).css("border","1px solid #ced4da");
        });
    }

});