var tubGroupBY = [];

var fieldEl = document.getElementById("filter-field");
var typeEl = document.getElementById("filter-type");
var valueEl = document.getElementById("filter-value");

var groupby = Array.from(document.getElementsByClassName("groupby"))

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
    tubGroupBY = [];
    clientTable.setGroupBy(false);
    clientTable.clearFilter();
});

// Group by
groupby.forEach(g => {
    g.addEventListener('click', e=> {
        if (g.id == "groupby-client" && tubGroupBY.indexOf('name') === -1) {
            tubGroupBY.push('name')
        };
        if (g.id == "groupby-task" && tubGroupBY.indexOf('task.title') === -1){
            tubGroupBY.push('task.title')
        };
        if (g.id == "groupby-project" && tubGroupBY.indexOf('project.title') === -1){
            tubGroupBY.push('project.title')
        };
        clientTable.setGroupBy(tubGroupBY);
    });
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
