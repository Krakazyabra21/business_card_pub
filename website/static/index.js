const form = document.querySelector(".form");
const name = form.querySelector("#name");
const phone = form.querySelector("#phone");
const email = form.querySelector("#email");
const button = form.querySelector(".form-group__button");

const validation = (item) => {
  item.addEventListener("input", () => {
    const items = [item, form, email, button, phone];

    if (item.validity.valid) {
      items.forEach((formItem) => formItem.classList.remove("not-validated"));
    } else {
      form.classList.add("not-validated");
      item.classList.add("not-validated");
    }
  });
};

validation(name);
validation(phone);
validation(email);
