const scrollUp = document.querySelector('#scroll-up')
const checkbox = document.querySelector('#checkbox')
const hamburger = document.querySelector('#hamburger')
const navMenu = document.querySelector('ul')
const navLink = document.querySelectorAll('#nav-link')

scrollUp.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    left: 0,
    behavior: 'smooth'
  })
})

checkbox.addEventListener('change', () => {
  document.body.classList.toggle('dark')
})

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('active')
  navMenu.classList.toggle('active')
})

navLink.forEach(n => {
  n.addEventListener('click', () => {
    hamburger.classList.remove('active')
    navMenu.classList.remove('active')
  })
})