var form = document.getElementById("form");


;['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  form.addEventListener(eventName, preventDefaults, false)
})

function preventDefaults (e) {
  e.preventDefault()
  e.stopPropagation()
}



form.addEventListener("dragenter", () => {
	form.classList.add('highlight')
}, false)

form.addEventListener("dragleave", () => {
	form.classList.remove('highlight')
}, false)

// form.addEventListener("dragover", () => {
// 	console.log("dragover");
// }, false)

form.addEventListener("drop", (e) => {
	console.log("Dropped file")
	form.classList.remove('highlight')
	let dt = e.dataTransfer
	let files = dt.files
}, false)