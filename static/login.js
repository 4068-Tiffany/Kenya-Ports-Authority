function login() {
    // 1. Get the values from the input boxes
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // 2. Simple check: Make sure they aren't empty
    if (email === "" || password === "") {
        document.getElementById('error').innerText = "Please enter both email and password.";
        return;
    }

    // 3. Move to the next page
    // Change "/generate_routes" to whatever your main page route is in app.py
    window.location.href = "/dashboard";
}