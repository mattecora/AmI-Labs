$(document).ready(function () {
    /* Task list population */
    $("#tasklist").append("<ul class=\"list-group\"></ul>");
    updateList();

    /* Add task handler */
    $("#addForm").on("submit", standardHandler);
});

function updateList() {
    /* Clear previous list */
    $("#tasklist").empty();
    $("#tasklist").append("<ul class=\"list-group\"></ul>");

    /* Get updated list */
    $.getJSON("http://127.0.0.1:5000/tasks", function(data) {
        for (var i = 0; i< data.length ; i++) {
            var t = data[i];
            if (t.urgent) {
                $("#tasklist ul").append("<li class=\"list-group-item text-danger\" data-urgent=\"true\"> " +
                                        "<span class=\"task-todo\">" + t.todo + "</span> " +
                                        "<button class=\"btn btn-primary btn-upd-task\" data-task=\"" + t.id + "\">Update</button> " +
                                        "<button class=\"btn btn-danger btn-del-task\" data-task=\"" + t.id + "\">Delete</button> " +
                                        "</li>");
            } else {
                $("#tasklist ul").append("<li class=\"list-group-item\" data-urgent=\"false\"> " +
                                        "<span class=\"task-todo\">" + t.todo + "</span> " +
                                        "<button class=\"btn btn-primary btn-upd-task\" data-task=\"" + t.id + "\">Update</button> " +
                                        "<button class=\"btn btn-danger btn-del-task\" data-task=\"" + t.id + "\">Delete</button> " +
                                        "</li>");
            }
        }

        /* Initialize update and delete handlers */
        $(".btn-del-task").click(function() {
            var taskID = $(this).data("task");
            delTask(taskID);
        });

        $(".btn-upd-task").click(function() {
            var taskID = $(this).data("task");
            var taskDescription = $(this).parent().find(".task-todo").html();
            var urgent = $(this).parent().hasClass("text-danger");

            /* Change form data */
            $("#taskDescription").val(taskDescription);
            $("#taskUrgent").prop("checked", urgent);

            /* Change form behaviour */
            $("#addForm").off("submit");
            $("#addForm").on("submit", function() {
                var description = $("#taskDescription").val();
                var urgent = $("#taskUrgent").prop("checked");
                var task = {
                    "id": taskID,
                    "todo": description,
                    "urgent": urgent
                };
                updTask(taskID, task);
                return false;
            });
            $("#addTask").html("Update");
            $("#addForm").prop("method", "PUT");
        });
    });
}

function addTask(task) {
    $.post({
        "url": "http://127.0.0.1:5000/tasks",
        "data": JSON.stringify(task),
        "contentType": "application/json",
        "success": function() {
            updateList();
        }
    });
}

function delTask(taskID) {
    $.ajax({
        "url": "http://127.0.0.1:5000/tasks/" + taskID,
        "method": "DELETE",
        "success": function() {
            updateList();
        }
    });
}

function updTask(taskID, task) {
    $.ajax({
        "url": "http://127.0.0.1:5000/tasks/" + taskID,
        "method": "PUT",
        "data": JSON.stringify(task),
        "contentType": "application/json",
        "success": function() {
            updateList();
        }
    });

    /* Restore form */
    $("#taskDescription").val("");
    $("#taskUrgent").prop("checked", false);
    $("#addForm").off("submit");
    $("#addForm").on("submit", standardHandler);
    $("#addTask").html("Add");
    $("#addForm").prop("method", "POST");
}

function standardHandler() {
    var description = $("#taskDescription").val();
    var urgent = $("#taskUrgent").prop("checked");
    var task = {
        "todo": description,
        "urgent": urgent
    };
    addTask(task);
    return false;
}