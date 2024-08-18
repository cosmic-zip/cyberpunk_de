$(document).ready(function () {
  var myString = "This is the content to be injected into the iframe.";
  var iframe = $("#browserIframe"); // Replace 'myIframe' with your iframe's ID

  // Access the iframe's document
  var iframeDoc = iframe[0].contentWindow.document;

  // Set the iframe's content to the string
  iframeDoc.body.innerHTML = myString;
});
