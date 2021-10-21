function modifyCart() {
    if(event.target.className == 'mod-switch') {
        modCart.setAttribute('style', 'display: block;')
        mainCart.setAttribute('style', 'display: none;')
    } else {
        modCart.setAttribute('style', 'display: none;')
        mainCart.setAttribute('style', 'display: block;')
    }
}


var modSwitch = document.querySelector('.mod-switch')
var resSwitch = document.querySelector('.res-switch')

var mainCart = document.querySelector('.main-cart')
var modCart = document.querySelector('.mod-cart')

modSwitch.addEventListener('click', modifyCart)
resSwitch.addEventListener('click', modifyCart)