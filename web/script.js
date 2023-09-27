function call_Back(apiKeyValue) {
  console.log('aaaaaaaaaaaaaaaaaaaaaa nb aaaaaaaaaaaaaaaaaaa')

  var validationResult = document.getElementById("validationResult");

  if (apiKeyValue) {
    console.log('aaaaaaaaaaaaaaa   aaaaaaaaaaaaaaaaaaaaaaaaaa')

    validationResult.textContent = "Valide";
    validationResult.classList.add("valid");

    // Afficher le deuxième formulaireformulaire
    var secondForm = document.getElementById("secondForm");
    secondForm.style.display = "block";

    // Masquer le premier formulaire
    var firstForm = document.getElementById("first-of-type");
    firstForm.style.display = "none";
  } else {
    console.log('aaaaaaaaaaaaaaaaaaaa nd aaaaaaaaaaaaaaaaaaaaa')
 
    validationResult.textContent = "Invalide";
    validationResult.classList.add("invalid");
  }
}

function validateAPIKey() {
  var apiKeyInput = document.getElementById("apiKey");
  var apiKeyValue = apiKeyInput.value.trim();
  var validationResult = document.getElementById("validationResult");

  // Supprimer les anciens résultats de validation s'ils existent
  if (validationResult) {
    validationResult.remove();
  }

  // Créer un nouvel élément pour afficher le résultat de validation
  validationResult = document.createElement("div");
  validationResult.id = "validationResult";
  validationResult.classList.add("validation-result");
  console.log('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa vvvv vvv  saaaaaaa')

  eel.verify_api_key(apiKeyValue)(call_Back);  // Appel de la fonction Python et passage de la fonction JavaScript "call_Back" en tant que callback
  console.log('aaaaaaaaaaaaaaaaaaaaaaaaaa    vvvv vv   aaaaaaaaaaaaaaa')

  // if (apiKeyValue == "qwerty") {
  //   validationResult.textContent = "Valide";
  //   validationResult.classList.add("valid");

  //   // Afficher le deuxième formulaire
  //   var secondForm = document.getElementById("secondForm");
  //   secondForm.style.display = "block";

  //   // Masquer le premier formulaire
  //   var firstForm = document.querySelector("form:first-of-type");
  //   firstForm.style.display = "none";
  // } else {
  //   validationResult.textContent = "Invalide";
  //   validationResult.classList.add("invalid");
  // }

  // Ajouter le résultat de validation en bas du conteneur
  var container = document.querySelector(".container");
  container.appendChild(validationResult);

  // Supprimer le résultat de validation après 2 secondes
  // setTimeout(function() {
  //   validationResult.remove();
  // }, 2000);
}

function generate() {
  var moduleName = document.getElementById("name").value;
  var searchQuery = document.getElementById("description").value;

  // Utilisez les valeurs récupérées comme nécessaire
  eel.create_module(moduleName, searchQuery)(call_generate)
  console.log("Nom du module :", moduleName);
  console.log("Recherche :", searchQuery);
}

function call_generate(value) {
  var validationResultodoo = document.getElementById("validationResultodoo");
console.log('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
  if (value) {
    console.log('aaaaaaaaaaaaaaaaaa  aaaaaaaaaaaaaaaaaaaaaaa')

    validationResultodoo.textContent = "Valide";
    validationResultodoo.classList.add("valid");

    // Afficher le conteneur de recherche
    var searchContainer = document.querySelector(".search-container");
    searchContainer.style.display = "block";
  } else {
    console.log('aaaaaaaaaaaaaaaa   aaaaaaaaaaaaaaaaaaaaaaaaa')

    validationResultodoo.textContent = "Invalide";
    validationResultodoo.classList.add("invalid");
  }
}


