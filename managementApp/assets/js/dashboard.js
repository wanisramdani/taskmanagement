const dataset = [];
const data = fetch('http://127.0.0.1:8080/api/clients/?format=json')
    .then(response => response.json())
    .then(data =>  Object.entries(data).map(obj  => dataset.push(obj[1]) ));


var dict = {
    "#clientLowData": "http://127.0.0.1:8080/dashboard/clientsProjectLowData/",
    "#clientMidData": "http://127.0.0.1:8080/dashboard/clientsProjectMidData/",
    "#clientHighData": "http://127.0.0.1:8080/dashboard/clientsProjectHighData/",
   
    "#clientsTaskLowData": "http://127.0.0.1:8080/dashboard/clientsProjectLowData/",
    "#clientsTaskMidData": "http://127.0.0.1:8080/dashboard/clientsTaskMidData/",
    "#clientsTaskHighData": "http://127.0.0.1:8080/dashboard/clientsTaskHighData/",

    "#clientsSubtaskLowData": "http://127.0.0.1:8080/dashboard/clientsSubtaskLowData/",
    "#clientsSubtaskMidData": "http://127.0.0.1:8080/dashboard/clientsSubtaskMidData/",
    "#clientsSubtaskHighData": "http://127.0.0.1:8080/dashboard/clientsSubtaskHighData/",
}

for (var key in dict) {
    console.log("for loop")
    var value = dict[key]
    var table = new Tabulator(key,{
        height: 150,
        ajaxURL: dict[key],
        layout: 'fitColumns',
        groupBy: 'priority',
        columns: [
            {title: "priority", field: "priority"},
            {title: "name", field:"name"},
            {title: "total_delayed", field:"total_delayed"},
            {title: "total_wip", field:"total_wip"},
            {title: "total_completed", field:"total_completed"},
        ],
    })
    /*document.getElementById("download-subtask-high-csv").addEventListener("click", function(){
        clientProjectLowDataTable.download("csv", "high-subtask.csv");
    }); */
    
}


/*

var dictModel = {
    "#subtask-data-tables": "http://127.0.0.1:8080/api/subTasks/?format=json",
    "#task-data-tables": "http://127.0.0.1:8080/api/tasks/?format=json",
    "#project-data-tables": "http://127.0.0.1:8080/api/project/?format=json",
}

for (var key in dictModel) {
    var value = dictModel[key]
    var table = new Tabulator(key, {
        height: 150,
        ajaxURL: value,
        layout: 'fitColumns',
        columns: [
            {title:"Title", field:"title", width: 150},
            {title:"Priority", field:"priority",},
            {title:"Deadline", field:"deadline"},
            {title:"DaysLeft", field:"daysLeft",},
            {title:"status", field:"status"},
        ],
        rowClick:function(e, row){
            alert("TODO: " + row.getData().id + " redicrect to client profile or charts");
        }
    })
    document.getElementById("download-subtask-high-csv").addEventListener("click", function(){
        clientProjectLowDataTable.download("csv", "high-subtask.csv");
    }); 
    
}
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

*/