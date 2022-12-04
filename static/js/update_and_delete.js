// button.style
document
  .querySelectorAll(".button")
  .forEach(
    (button) =>
      (button.innerHTML =
        "<div><span>" +
        button.textContent.trim().split("").join("</span><span>") +
        "</span></div>")
  );

// remove API notes ==========================================================-->
let notes = document.getElementsByClassName("delete-note");
for (let i = 0; notes.length > i; i++) {
  notes[i].addEventListener("click", (e) => {
    let noteId = e.target.dataset.note;
    let taskId = e.target.dataset.task;

    fetch("http://127.0.0.1:8000/api/delete-note/", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ task: taskId, note: noteId }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        e.target.remove();
      });
  });
}
