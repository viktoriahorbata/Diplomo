const iconOpen = document.getElementById('iconOpen')
const iconClose = document.getElementById('iconClose')
const mainMenu = document.getElementById('mainMenu')
const menuIcons = document.getElementById('menuIcons')
const subList = document.getElementById('subList')

menuIcons.addEventListener('click', ()=> {
    console.log('AAAAAAAAAAA')
	iconOpen.classList.toggle('d-none')
	iconClose.classList.toggle('d-none')
	mainMenu.classList.toggle('hide')
})

subList.addEventListener('click', ()=> {
    document.getElementById('subListIcon').classList.toggle('rotate-180')

})