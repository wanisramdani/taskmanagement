var fieldEl = document.getElementById("filter-field");
var typeEl = document.getElementById("filter-type");
var valueEl = document.getElementById("filter-value");

var groupbyClient = document.getElementById("groupby-client");
var groupbyTask = document.getElementById("groupby-task");
var groupbyProject = document.getElementById("groupby-project");


//Custom filter example
function customFilter(data){
    return data.car && data.rating < 3;
}

//Trigger setFilter function with correct parameters
function updateFilter(){
    var filterVal = fieldEl.options[fieldEl.selectedIndex].value;
    var typeVal = typeEl.options[typeEl.selectedIndex].value;

    if(filterVal){
        clientTable.setFilter(filterVal, typeVal, valueEl.value);
       
    }
}

fieldEl.addEventListener("change", updateFilter);
typeEl.addEventListener("change", updateFilter);
valueEl.addEventListener("keyup", updateFilter);

var filterClear = document.getElementById("filter-clear");

filterClear.addEventListener("click", function(){
    valueEl.value = "";
    clientTable.setGroupBy(false)
    clientTable.clearFilter();
});

groupbyClient.addEventListener("click", function(){
    clientTable.setGroupBy("name")
});
groupbyTask.addEventListener("click", function(){
    clientTable.setGroupBy("task.title")
});
groupbyProject.addEventListener("click", function(){
    clientTable.setGroupBy("project.title")
});

var clientTable = new Tabulator("#client-data-tables", {
    height: 450,
    pagination:"local",
    paginationSize:6,
    paginationSizeSelector: [2, 6, 10, 100],
    movableRows:true,
    movableColumns:true,
    ajaxURL: "http://127.0.0.1:8080/dashboard/allClientData/",
    layout: 'fitColumns',
    columns: [
        {title:"Name", field:"name", width: 150},
        {title:"Email", field:"email"},
        {title:"Project", field:"project.title"},
        {title:"Task", field:"task.title"},
    ],
    
})
