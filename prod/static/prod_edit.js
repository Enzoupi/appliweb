// prod_edit.js

// Initialize sums for each element type
const sums = {
    T80: 0,
    BuchNat: 0,
    PetEp: 0,
    RizSar: 0,
    BuchNoix: 0,
    PetEp: 0,
    BuchMG: 0,
    Brioche: 0,
    Cookies: 0,
    // Add similar entries for other types
};

// Function to update sums
function updateSums() {
    console.log("Updating sums");

    // Loop over element types and calculate sums
    for (const type in sums) {
        const inputs = document.querySelectorAll(`.${type}-input`);
        sums[type] = Array.from(inputs).reduce((sum, input) => sum + parseFloat(input.value || 0), 0);
        document.getElementById(`sum-${type}`).textContent = `${type}: ${sums[type].toFixed(2)}`;
    }
}

// Attach the updateSums function to input change events
document.addEventListener('change', function(event) {
    if (event.target.classList.contains('form-control')) {
        updateSums();
    }
});

function compareProds() {
    // Get the selected Prod for comparison from the dropdown menu
    const selectProd = document.getElementById('selectProd');
    const selectedProdId = selectProd.value;

    if (selectedProdId) {
        console.log('True');
        // Construct the URL dynamically
        const url = `/prod/prodlist/${prodData.pk}/${selectedProdId}/compare/`;
        window.location.href = url;
    } else {
        console.log('False');
        alert('Please select a Prod for comparison.');
    }
}

// Initial update
updateSums();

// Initialize compare_id with the ID of the first available Prod
const defaultCompareId = "{{ availableProds.0.pk }}";
document.getElementById('selectProd').value = defaultCompareId;
