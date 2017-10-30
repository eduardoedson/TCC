function refreshMask () {
  $('.dateinput').mask('00/00/0000', {placeholder:"__/__/____"});
}

function refreshDatePicker() {
    $.datepicker.setDefaults($.datepicker.regional['pt-BR']);
    $('.dateinput').datepicker();
}

$(document).ready(function (){
  refreshMask();
  refreshDatePicker();
});

/* Máscaras ER */
function mascara(o,f){
    v_obj = o
    v_fun = f
    setTimeout("execmascara()", 1);
}

function execmascara(){
    v_obj.value = v_fun(v_obj.value)
}

function mascara_tel(v){
    v = v.replace(/\D/g, "");                  //Remove tudo o que não é dígito
    v = v.replace(/^(\d{2})(\d)/g, "($1) $2"); //Coloca parênteses em volta dos dois primeiros dígitos
    v = v.replace(/(\d)(\d{4})$/, "$1-$2");    //Coloca hífen entre o quarto e o quinto dígitos
    return v;
}

function mascara_cpf(v){
  v = v.replace(/\D/g,"")
  v = v.replace(/(\d{3})(\d)/,"$1.$2")
  v = v.replace(/(\d{3})(\d)/,"$1.$2")
  v = v.replace(/(\d{3})(\d{1,2})$/,"$1-$2")
  return v
}

function mascara_rg(v){
  v = v.replace(/\D/g,"")
  v = v.replace(/(\d{1})(\d)/,"$1.$2")
  v = v.replace(/(\d{3})(\d)/,"$1.$2")
  return v
}

function mascara_cep(v){
  v = v.replace(/\D/g,"")
  v = v.replace(/^(\d{2})(\d)/,"$1.$2")
  v = v.replace(/\.(\d{3})(\d)/,".$1-$2")
  return v
}

function id(el){
  return document.getElementById(el);
}

id('id_telefone').onkeyup = function(){
  mascara(this, mascara_tel);
}
id('id_referencia_telefone').onkeyup = function(){
  mascara(this, mascara_tel);
}
id('id_celular').onkeyup = function(){
  mascara(this, mascara_tel);
}
id('id_cpf').onkeyup = function(){
  mascara(this, mascara_cpf);
}
id('id_cep').onkeyup = function(){
  mascara(this, mascara_cep);
}
id('id_rg').onkeyup = function(){
  mascara(this, mascara_rg);
}
