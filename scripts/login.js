function validateForm() {
    var name = form.getElementById('username_login');
    var password = form.getElementById('password_login');
    if (name === "" || password === "") {
        alert("Name must be filled out");
        return false;
    }
}