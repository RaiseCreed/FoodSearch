// document.addEventListener('DOMContentLoaded', function () {
//     hljs.highlightAll();
//   });
  
  console.log("dsada");
  let alertWrapper = document.querySelector('.alert')
  let alertClose = document.querySelector('.alert__close')
  
  if (alertWrapper){
    console.log('Alert Wrapper clicked')
    alertClose.addEventListener('click', () => alertWrapper.style.display = 'None')
  }