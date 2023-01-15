type="text/javascript"

// window.alert("It works !");

var btn = document.querySelector("#AddFour");
btn.onclick = function() {AlertOnClick()};

var four = document.querySelector("#Four1_container");
var allFour = document.querySelector("#allFours");


var counter = 1;

function AlertOnClick () {
    //allFour.appendChild(four.cloneNode(true))

    //Duplicate Form and change ids
    allFour.appendChild(duplicateNode(four, ["id", "name"]))

    //Change Four number
    var fourNum = document.querySelector('#fourNum_' + counter)
    fourNum.textContent = "Four " + counter 
};

function duplicateNode(/*DOMNode*/sourceNode, /*Array*/attributesToBump) {
    counter++;
    var out = sourceNode.cloneNode(true);
    if (out.hasAttribute("id")) { out["id"] = bump(out["id"]); }
    var nodes = out.getElementsByTagName("*");
    
    for (var i = 0, len1 = nodes.length; i < len1; i++) {
        var node = nodes[i];
        for (var j = 0, len2 = attributesToBump.length; j < len2; j++) {
            var attribute = attributesToBump[j];
            if (node.hasAttribute(attribute)) {
                node[attribute] = bump(node[attribute]);
            }
        }
    }
    
    function bump(/*String*/str) {
        return str + "_" + counter;
    }
    return out;
}

function handlerDateChange(e) {
    date = document.querySelector('#dateInput')
    datestr = 
    document.querySelector('#navbar').text = "Gestionnaire de fiche prod' " + date.value  
}