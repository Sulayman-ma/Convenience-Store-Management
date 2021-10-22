function search() {
    var input, query, rows;

    input = document.querySelector('#searchBtn')

    // search query
    query = input.value.toLowerCase().trim()
    
    // NodeList of item rows
    rows = (document.querySelectorAll('.item-row'))

    for(let row of rows) {
        let itemName = row.className.slice(9).toLowerCase()
        if (itemName.includes(query)) {
            row.removeAttribute('style')
        } else {
            row.setAttribute('style', 'display: none;')
        }
    }
}


function modifyItems() {
    var removeForm, modForm

    removeForm = document.querySelector('.remove-items')
    modForm = document.querySelector('.modify-items')

    if(event.target.classList.contains('modify-btn')) {
        removeForm.setAttribute('style', 'display: none;')
        modForm.setAttribute('style', 'display: block;')
    } else {
        removeForm.setAttribute('style', 'display: block;')
        modForm.setAttribute('style', 'display: none;')
    }
}


function modifyCart() {
    var mainCart, modCart
    mainCart = document.querySelector('.main-cart')
    modCart = document.querySelector('.mod-cart')

    if(event.target.classList.contains('mod-switch')) {
        modCart.setAttribute('style', 'display: block;')
        mainCart.setAttribute('style', 'display: none;')
    } else {
        modCart.setAttribute('style', 'display: none;')
        mainCart.setAttribute('style', 'display: block;')
    }
}