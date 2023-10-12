function taskRemoveAnimation(task_id) {
    const task_card = document.getElementById(`task${task_id}`);
    taskStatusUpdate(task_id);
    task_card.classList.add('fade-out');
    task_card.addEventListener('animationend', function () {
        task_card.classList.remove('fade-out');
        task_card.style.display = 'none';
        location.reload();
    });
}

function getCookie(name) {
    const value = "; " + document.cookie;
    const parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}

function taskStatusUpdate(task_id) {
    const request = new XMLHttpRequest();
    request.open("POST", `http://127.0.0.1:8000/todo/tasks/task_status_update/${task_id}/`, true);
    request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    request.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            console.log("Success!");
        }
    };
    request.send();
}
