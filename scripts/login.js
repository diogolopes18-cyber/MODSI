function validateForm() {
    var name = form.getElementById('username_login');
    var password = form.getElementById('password_login');
    var password_confirm = form.getElementById('password_login_confirm')

    if (name === "" || password === "") {
        alert("Name must be filled out");
        return false;
    }

    if (password != password_confirm) {
        alert("Passwords must match");
        return false;
    }

}