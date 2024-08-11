// function init() {
//     import('./header.js')
//         .then(module => {
//             // You can use the imported module here
//             console.log('Module loaded successfully:', module);
//         })
//         .catch(error => {
//             console.error('Error loading module:', error);
//         });
// }

// document.addEventListener("DOMContentLoaded", init);




function init() {
    import('./header.js');
}
// init()
const totalPartials = document.querySelectorAll('[hx-trigger="load"], [data-hx-trigger="load"]').length;
let loadedPartialsCount = 0;

document.body.addEventListener('htmx:afterOnLoad', () => {
    loadedPartialsCount++;
    if (loadedPartialsCount === totalPartials) init();
});