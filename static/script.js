console.log('JavaScript loaded')

window.addEventListener('load', () => {
    titles = document.querySelectorAll('.site-title')

    window.addEventListener('scroll', () => {
        titles.forEach(title => {
            var { top } = title.getBoundingBoxRect()
        })
    })
})
