$(document).ready(function () {
	$("#task-modal").on ("show.bs.modal", function (event) {
		const button = $(event.relatedTarget);
		const taskID = button.data ("source");
		const content = button.data ("content");

		const modal = $(this);
		if (taskID === "New Task") {
			modal.find (".modal-title").text (taskID);
			$("#task-form-display").removeAttr ("taskID");
		}

		else {
			modal.find (".modal-title").text ("Edit Task " + taskID);
			$("#task-form-display").attr ("taskID", taskID);
		}

		if (content) {
			modal.find (".form-control").val (content);
		}

		else {
			modal.find (".form-control").val ("");
		}
	});

	$("#submit-task").click (function () {
		const item_id = $("#task-form-display").attr ("taskID");
		console.log ($("#task-form-display").attr ("taskID"));
		// console.log ($("#task-modal").find (".form-control").val ());
		$.ajax ({
			type: item_id ? "PUT" : "POST",
			url: item_id ? `/api/todo/items/${item_id}/update` : "/api/todo/items/create",
			contentType: "application/json;charset=UTF-8",
			data: JSON.stringify ({
				"description": $("#task-modal").find (".form-control").val ()
			}),
			success: function (res) {
				console.log (res.response);
				location.reload ();
			},
			error: function () {
				console.log ("Error");
			}
		});
	});

	$(".remove").click (function () {
		const remove = $(this);
		const item_id = remove.data ("source");
		console.log (item_id);
		$.ajax ({
			type: "DELETE",
			url: `/api/todo/items/${item_id}/remove`,
			success: function (res) {
				console.log (res.response);
				location.reload ();
			},
			error: function () {
				console.log ("Error");
			}
		});
	});

	$(".state").click (function () {
		console.log ("State clicked!");
		const state = $(this);
		const item_id = state.data ("source");
		console.log (item_id);
		let new_state = 0;
		if (state.text () === "In Progress") {
			new_state = 3;
		}

		else if (state.text () === "Completed") {
			new_state = 1;
		}

		else if (state.text () === "Todo") {
			new_state = 2;
		}

		$.ajax ({
			type: "PUT",
			url: `/api/todo/items/${item_id}/status`,
			contentType: "application/json;charset=UTF-8",
			data: JSON.stringify ({
				"status": new_state
			}),
			success: function (res) {
				console.log (res);
				location.reload ();
			},
			error: function () {
				console.log ("Error");
			}
		});
	});

});
