(function() {
  function showContactForm() {
    contactForm.classList.remove('display-none');
    contactInfo.classList.add('display-none');
  }

  function hideContactForm() {
    contactForm.classList.add('display-none');
    contactInfo.classList.remove('display-none');
  }

  function addShowFormHandler() {
    var editButton = document.getElementById('edit-contact-info-btn');
    editButton.addEventListener('click', showContactForm);
  }

  function getFormState(form) {
    //  Serialize form values into a comma delimited string
    var serializedForm = new Array();
    for (var i = 0; i < form.elements.length; i++) {
      var field = form.elements[i];
      serializedForm.push(field.value);
    }
    return serializedForm.join(',');
  }

  function setButtonDisabled() {
    // Save Button only enabled if form has been modified
    var currentState = getFormState(contactForm);
    if (initialState === currentState) {
      saveButton.setAttribute('disabled', true);
    } else {
      saveButton.removeAttribute('disabled');
    }
  }

  var contactInfo = document.getElementById('contact-info');
  var contactForm = document.getElementById('contact-edit-form');
  var saveButton = contactForm.getElementsByTagName('button')[0];
  var cancelButton = contactForm.getElementsByClassName('button--cancel')[0];

  var initialState = getFormState(contactForm);
  contactForm.addEventListener('input', setButtonDisabled);
  cancelButton.addEventListener('click', hideContactForm);

  addShowFormHandler();
})();
