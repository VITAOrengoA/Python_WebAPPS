function validatePasswords() {
    var password1 = document.getElementById("pass").value;
    var password2 = document.getElementById("confirm_pass").value;
    var alertElement = document.getElementById("wrong_pass_alert");

    if (password1 !== password2) {
        alertElement.textContent = "Passwords do not match!\n\n";
        return false;
    }
    else 
    {
        alertElement.textContent = "";
        return true;
    }
}
 
function validateUsername() {
    var usernameInput = document.getElementById("name_input");
    var nameInputAlert = document.getElementById("name_input_alert");
    var username = usernameInput.value;
    var isValid = true;

    if (username.length !== 7) {
        nameInputAlert.textContent = "Username must be 7 characters long!";
        isValid = false;
    } else if (isNaN(parseInt(username))) {
        nameInputAlert.textContent = "Username must be all digits!";
        isValid = false;
    } else {
        nameInputAlert.textContent = "";
    }

    return isValid;
}