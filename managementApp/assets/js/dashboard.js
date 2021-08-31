/* 
function processData(dataset) {
    var result = []
    dataset = JSON.parse(dataset);
    dataset.forEach(item => result.push(item.fields));
    return result;
}

$.ajax({
    url: $("#client-data-tables").attr("data-url"),
    dataType: 'json',
    success: function(data) {
        new Flexmonster({
            container: "#client-data-tables",
            componentFolder: "https://cdn.flexmonster.com/",
            width: "100%",
            height: 430,
            toolbar: true,
            report: {
                dataSource: {
                    type: "json",
                    data: processData(data)
                },
                slice: {}
            }
        });
        new Flexmonster({
            container: "#client-data-tables",
            componentFolder: "https://cdn.flexmonster.com/",
            width: "100%",
            height: 430,
            //toolbar: true,
            report: {
                dataSource: {
                    type: "json",
                    data: processData(data)
                },
                slice: {},
                "options": {
                    "viewType": "charts",
                    "chart": {
                        "type": "pie"
                    }
                }
            }
        });
    }
});
*/

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

var clientLowDataTable = new Tabulator("#clientLowData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsLowData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})

var clientMidDataTable = new Tabulator("#clientMidData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsMidData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})

var clientHighDataTable = new Tabulator("#clientHighData",{
    height: 150,
    ajaxURL: "http://127.0.0.1:8080/dashboard/clientsHighData/",
    layout: 'fitColumns',
    columns: [
        {title: "name", field:"name"},
        {title: "total_delayed", field:"total_delayed"},
        {title: "total_wip", field:"total_wip"},
        {title: "total_completed", field:"total_completed"},
    ],
})

//trigger download of data.csv file
document.getElementById("download-csv").addEventListener("click", function(){
    table.download("csv", "data.csv");
});