function getPasswordStrength(password) {
  let strength = 0;
  if (password.match(/[a-z]+/)) {
    strength += 1;
  }
  if (password.match(/[A-Z]+/)) {
    strength += 1;
  }
  if (password.match(/[0-9]+/)) {
    strength += 1;
  }
  if (password.match(/[$@#&!]+/)) {
    strength += 1;
  }
  return strength;
}

function getPasswordStrengthText(strength) {
  switch (strength) {
    case 0:
      return '';
    case 1:
      return 'Fortaleza de la contraseña: Baja';
    case 2:
      return 'Fortaleza de la contraseña: Media';
    case 3:
    case 4:
      return 'Fortaleza de la contraseña: Alta';
  }
}

const passwordInput = document.getElementById('id_password1');
const passwordStrengthContainer = document.getElementById('password-strength-container');
const passwordValidationMessage = document.getElementById('password-validation-message');

passwordInput.addEventListener('input', function() {
  const password = passwordInput.value;
  const passwordStrength = getPasswordStrength(password);
  const passwordStrengthText = getPasswordStrengthText(passwordStrength);
  passwordStrengthContainer.innerText = passwordStrengthText;
  const passwordIsValid = validatePassword(password);
  if (passwordIsValid) {
    passwordValidationMessage.innerText = '';
    passwordValidationMessage.setAttribute('data-strength', 'strong');
    passwordInput.classList.remove('is-invalid');
  } else {
    passwordValidationMessage.innerText = 'La contraseña debe ser al menos 6 caracteres, 2 letras mayúsculas, 1 numero';
    passwordValidationMessage.setAttribute('data-strength', '');
    passwordInput.classList.add('is-invalid');
  }
});

function validatePassword(password) {
  return password.length >= 6 && (password.match(/[A-Z]/g) || []).length >= 2;
}
