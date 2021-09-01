/* TODO: rename ids */
var dict = {
    /* id: url */
    "clientLowData": "http://127.0.0.1:8080/dashboard/clientsProjectLowData/",
    "clientsTaskLowData": "http://127.0.0.1:8080/dashboard/clientsProjectLowData/",
    "clientsSubtaskLowData": "http://127.0.0.1:8080/dashboard/clientsSubtaskLowData/",
}

var fieldEl = document.getElementById("filter-field");
var typeEl = document.getElementById("filter-type");
var valueEl = document.getElementById("filter-value");

//Custom filter example
function customFilter(data){
    return data.car && data.rating < 3;
}

//Trigger setFilter function with correct parameters
function updateFilter(){
    var filterVal = fieldEl.options[fieldEl.selectedIndex].value;
    var typeVal = typeEl.options[typeEl.selectedIndex].value;

    if(filterVal){
        table.setFilter(filterVal, typeVal, valueEl.value);
        clientProjectsTable.setFilter(filterVal, typeVal, valueEl.value);
        clientTasksTable.setFilter(filterVal, typeVal, valueEl.value);
        clientSubtaskTable.setFilter(filterVal, typeVal, valueEl.value);
    }
}

//Update filters on value change
fieldEl.addEventListener("change", updateFilter);
typeEl.addEventListener("change", updateFilter);
valueEl.addEventListener("keyup", updateFilter);

var filterClear = document.getElementById("filter-clear");
//Clear filters on "Clear Filters" button click

filterClear.addEventListener("click", function(){
    valueEl.value = "";

    clientProjectsTable.clearFilter();
    clientTasksTable.clearFilter();
    clientSubtaskTable.clearFilter();
});

for (var id in dict) {
    var url = dict[id]
    var table = new Tabulator("#".concat(id), {
        height: 150,
        autoColumns: true,
        ajaxURL: url,
        layout: 'fitColumns',
        groupBy: 'priority',
        columns: [
            {title: "name", field:"name"},
            {title: "priority", field: "priority", formatter:"color", width:50},
            {title: "total_delayed", field:"total_delayed"},
            {title: "total_wip", field:"total_wip"},
            {title: "total_completed", field:"total_completed"},
        ],
    })
    document.getElementById("download-".concat(id)).addEventListener("click", function(){
        table.download("csv", id.concat(".csv"));
    }); 
    if (id == "clientLowData") {
        var clientProjectsTable = table
    } else if (id == "clientsTaskLowData") {
        var clientTasksTable = table
    } else if (id == "clientsSubtaskLowData") {
        var clientSubtaskTable = table
    }
    
}

/* Models tables */
var dictModel = {
    "subtask-data-tables": "http://127.0.0.1:8080/api/subTasks/?format=json",
    "task-data-tables": "http://127.0.0.1:8080/api/tasks/?format=json",
    "project-data-tables": "http://127.0.0.1:8080/api/project/?format=json",
}

for (var id in dictModel) {
    var url = dictModel[id]
    var tableModel = new Tabulator("#".concat(id), {
        height: 150,
        ajaxURL: url,
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
