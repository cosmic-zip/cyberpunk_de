const { invoke } = window.__TAURI__.tauri;

function exec_terminal() {
  invoke("greet", { name: "World" }).then((response) => {
    console.log(response);
  });
}
