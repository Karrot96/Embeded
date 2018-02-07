function landingClearFog(){
    x=document.getElementsByClassName('glass')
    x[0].style.background = 'rgba(217,214,209,0)'
    y=document.getElementsByClassName('FogOverlay')
    y[0].style.opacity = '0'
    z=document.getElementsByClassName('menu')
    z[0].style.display = 'block'
}
