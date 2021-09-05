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
        if (g.id == "groupby-client") {
            let pos = tubGroupBY.indexOf('name')
            if (pos !== -1) {
                if (pos === 0) tubGroupBY.splice(pos, pos + 1)
                else tubGroupBY.splice(pos, pos)
            }else {
                tubGroupBY.push('name')
            }
        };
        if (g.id == "groupby-task"){
            let pos = tubGroupBY.indexOf('task.title')
            if (pos !== -1) {
                if (pos === 0) tubGroupBY.splice(pos, pos + 1)
                else tubGroupBY.splice(pos, pos)
                
            }else {
                tubGroupBY.push('task.title')
            }
        };
        if (g.id == "groupby-project"){
            let pos = tubGroupBY.indexOf('project.title')
            if (pos !== -1) {
                if (pos === 0) tubGroupBY.splice(pos, pos + 1)
                else tubGroupBY.splice(pos, pos)
            }else {
                tubGroupBY.push('project.title')
            } 
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
    columns: [
        {title:"Name", field:"name", width: 150},
        {title:"Email", field:"email"},
        {title:"Project", columns: [
         {title:"Title" ,field:"project.title"}, 
         {title:"Priority" ,field:"project.priority"},
         {title:"Deadline" ,field:"project.deadline", sorter:"date"},
         {title:"Days Left" ,field:"project.daysLeft"},  
        ]},
        {title:"Task", columns: [
            {title:"Title" ,field:"task.title"}, 
            {title:"Priority" ,field:"task.priority"},
            {title:"Deadline" ,field:"task.deadline", sorter:"date"},
            {title:"Days Left" ,field:"task.daysLeft"},  
        ]},
        {title:"Subtask", columns: [
            {title:"Title" ,field:"subtask.title"}, 
            {title:"Priority" ,field:"subtask.priority"},
            {title:"Deadline" ,field:"subtask.deadline", sorter:"date"},
            {title:"Days Left" ,field:"subtask.daysLeft"},  
        ]},
    ],
    
})
