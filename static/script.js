var frames = document.querySelectorAll('iframe')
for (let i = 0; i < frames.length; i++) {
    frames[i].addEventListener('load', e => {
        e.currentTarget.parentElement.classList.add('loaded')
    })
}
