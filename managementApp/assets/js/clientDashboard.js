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
        clientTable.setFilter(filterVal, typeVal, valueEl.value);
       
    }
}

fieldEl.addEventListener("change", updateFilter);
typeEl.addEventListener("change", updateFilter);
valueEl.addEventListener("keyup", updateFilter);

var filterClear = document.getElementById("filter-clear");

filterClear.addEventListener("click", function(){
    valueEl.value = "";

    clientTable.clearFilter();
});

var clientTable = new Tabulator("#client-data-tables", {
    height: 450,
    pagination:"local",
    paginationSize:6,
    paginationSizeSelector: [2, 6, 10, 100],
    movableRows:true,
    movableColumns:true,
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
