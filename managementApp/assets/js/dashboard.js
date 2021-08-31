const dataset = [];
const data = fetch('http://127.0.0.1:8080/api/clients/?format=json')
    .then(response => response.json())
    .then(data =>  Object.entries(data).map(obj  => dataset.push(obj[1]) ));



var clientTable = new Tabulator("#client-data-tables", {
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/api/clients/?format=json",
    layout: 'fitColumns',
    columns: [
        {title:"Name", field:"name", width: 150},
        {title:"phoneNumber", field:"phoneNumber", hozAlign:"left",},
        {title:"email", field:"email"},
        {title:"address", field:"address", sorter:"date", hozAlign:"center"},
    ],
    rowClick:function(e, row){
        alert("TODO: " + row.getData().id + " redicrect to client profile or charts");
    }
})

var subtaskTable = new Tabulator("#subtask-data-tables", {
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/api/subTasks/?format=json",
    layout: 'fitColumns',
    columns: [
        {title:"Title", field:"title", width: 150},
        {title:"Priority", field:"priority",},
        {title:"Deadline", field:"deadline"},
        {title:"DaysLeft", field:"daysLeft",},
        {title:"status", field:"status"},
    ],

})

var taskTable = new Tabulator("#task-data-tables", {
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/api/tasks/?format=json",
    layout: 'fitColumns',
    columns: [
        {title:"Title", field:"title", width: 150},
        {title:"Priority", field:"priority",},
        {title:"Deadline", field:"deadline"},
        {title:"DaysLeft", field:"daysLeft",},
        {title:"status", field:"status"},
    ],

})

var projectTable = new Tabulator("#project-data-tables", {
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/api/project/?format=json",
    layout: 'fitColumns',
    columns: [
        {title:"Title", field:"title", width: 150},
        {title:"Priority", field:"priority",},
        {title:"Deadline", field:"deadline"},
        {title:"DaysLeft", field:"daysLeft",},
        {title:"status", field:"status"},
    ],
})

/* */

var clientProjectLowDataTable = new Tabulator("#clientLowData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsProjectLowData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})

document.getElementById("download-project-low-csv").addEventListener("click", function(){
    clientProjectLowDataTable.download("csv", "low-project.csv");
});

var clientProjectMidDataTable = new Tabulator("#clientMidData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsProjectMidData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})

document.getElementById("download-project-mid-csv").addEventListener("click", function(){
    clientProjectLowDataTable.download("csv", "mid-project.csv");
});


var clientProjectHighDataTable = new Tabulator("#clientHighData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsProjectHighData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})

document.getElementById("download-project-high-csv").addEventListener("click", function(){
    clientProjectLowDataTable.download("csv", "high-project.csv");
});


/* TASK */

var clientProjectHighDataTable = new Tabulator("#clientsTaskLowData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsTaskLowData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})

document.getElementById("download-task-low-csv").addEventListener("click", function(){
    clientProjectLowDataTable.download("csv", "low-task.csv");
});


var clientProjectHighDataTable = new Tabulator("#clientsTaskMidData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsTaskMidData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})

document.getElementById("download-task-mid-csv").addEventListener("click", function(){
    clientProjectLowDataTable.download("csv", "mid-task.csv");
});

var clientProjectHighDataTable = new Tabulator("#clientsTaskHighData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsTaskHighData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})

document.getElementById("download-task-high-csv").addEventListener("click", function(){
    clientProjectLowDataTable.download("csv", "high-task.csv");
});

/* */

var clientProjectHighDataTable = new Tabulator("#clientsSubtaskLowData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsSubtaskLowData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})
document.getElementById("download-subtask-low-csv").addEventListener("click", function(){
    clientProjectLowDataTable.download("csv", "low-subtask.csv");
});

var clientProjectHighDataTable = new Tabulator("#clientsSubtaskMidData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsSubtaskMidData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})

document.getElementById("download-subtask-mid-csv").addEventListener("click", function(){
    clientProjectLowDataTable.download("csv", "mid-subtask.csv");
});

var clientProjectHighDataTable = new Tabulator("#clientsSubtaskHighData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsSubtaskHighData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})

document.getElementById("download-subtask-high-csv").addEventListener("click", function(){
    clientProjectLowDataTable.download("csv", "high-subtask.csv");
});