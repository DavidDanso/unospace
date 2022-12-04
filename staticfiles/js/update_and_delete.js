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

// loading animation ==========================================================-->
var waitTime = 3 * 60 * 1000; // = 3min.

$(function () {
  $("button").on("click", function () {
    var btn = $(this);
    var progress = btn.find(".progress");
    progress.show();
    btn.addClass("loading-start");
    btn.attr("disabled", true);

    setTimeout(function () {
      btn.removeClass("loading-start").removeAttr("disabled");
      progress.hide();
    }, waitTime);
  });
});

// remove notes ==========================================================-->
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
