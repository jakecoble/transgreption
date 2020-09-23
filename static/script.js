console.log('JavaScript loaded')

var intersectsWithViewport = function (el) {
    var { top, bottom } = el.getBoundingClientRect()

    return (top < window.scrollX + window.innerHeight &&
            bottom > window.scrollX)
}

window.addEventListener('load', () => {
    docs = document.querySelectorAll('.site-container')

    var focused = docs[0]

    window.addEventListener('scroll', () => {
        docs.forEach(doc => {
            var { top } = doc.getBoundingClientRect()
            var { top: currTop } = focused.getBoundingClientRect()

            if (intersectsWithViewport(doc) &&
                (top < currTop || !intersectsWithViewport(focused))) {
                focused = doc
                docId = doc.querySelector('h2').id

                document.querySelectorAll('.focused-link')
                        .forEach(focused => focused.classList.remove('focused-link'))

                document.querySelector(`#${docId}-link`)
                        .classList.add('focused-link')
            }
        })
    })
})
