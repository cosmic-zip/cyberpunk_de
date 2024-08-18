// access the pre-bundled global API functions
const { invoke } = window.__TAURI__.tauri;

// now we can call our Command!
// You will see "Welcome from Tauri" replaced
// by "Hello, World!"!
invoke("greet", { name: "World" })
  // `invoke` returns a Promise
  .then((response) => {
    console.log(response);
  });
