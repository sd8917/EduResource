var token = null
var loading = null;

window.onload = function(){
    loading = document.getElementById('loading');

}
function validate(event){
    console.log('Form Submission ')

        var error = document.getElementById('message');
        var message = null;
        var form = event.target;

        var message = validateForm(form);
        
        var values = form.elements;

        var name = values.name.value;
        var email = values.email.value;
        token = values.csrfmiddlewaretoken.value;

        if(message){
            error.innerHTML = message
            error.hidden = false;
        }
        else{
            error.innerHTML = "";
            error.hidden = true;

            //email ... 
            sendEmail(email,name,token);   
        }
 
    event.stopPropagation();
    console.log(token);

    return false;
}

function validateForm(form){

        var message   = null;
        var values    = form.elements;

        var name      = values.name.value;
        var email     = values.email.value;
        var password  = values.password.value;
        var phone     = values.phone.value;
        var repassword= values.repassword.value;
        token         = values.csrfmiddlewaretoken.value;

        if(!name.trim()){
            message      = "Name is Required"
        }else if(!email.trim()){
            message      = "Email is Required"
        }
        else if(!password.trim()){
            message      = "Password is Required.";
        }
        else if(!repassword.trim()){
            message      = "Enter Password Again.";
        }
        else if(password.trim() != repassword.trim()){
                message  = "Password Not Matched.";
        }

        return message;
}

function sendEmail(email,name,token){
    // console.log('Send Email OTP on ' + email) 
    //alert();
    loading.hidden= false;
    $.ajax({
        method : "POST",
        url : "/send-otp",
        data : {name :name,email:email,'csrfmiddlewaretoken':token}
    }).done(function(msg){
        //alert("data saved : " + msg);
        loading.hidden= true;
        showOtpInput();
    }).fail(function(err){
        loading.hidden= true;
        alert('Cant send Email');
    });

}

function showOtpInput(){
    var otpInput = document.getElementById('VerificationInput');
    var submitButton =document.getElementById('submitButton');
    var verifyButton = document.getElementById('verifyButton');

    otpInput.hidden =false;
    submitButton.hidden = true;
    verifyButton.hidden = false;

}


function verifyCode(){
    var codeInput = document.getElementById('code');
    var code = codeInput.value;

    loading.hidden= false;
    $.ajax({
        method : "POST",
        url : "/verify",
        data : {'code' :code,'csrfmiddlewaretoken':token}
    }).done(function(msg){
        loading.hidden= true;
        submitForm();
    }).fail(function(err){
        loading.hidden= true;
        alert('Code is invalid');
    });
}

function submitForm(){
    try{
        var form = document.getElementById('form');
        var message = validateForm(form);
        
        if(message){

        }
        else{
            form.submit();
        }
    }
   catch{
       console.log(err);
   }
    
}

