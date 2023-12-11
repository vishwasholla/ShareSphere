const searchInput = document.getElementById("search-input");
const tableRows = document.querySelectorAll(".list tr");

searchInput.addEventListener("input", function () {
    console.log('event listner')
    const searchTerm = searchInput.value.toLowerCase();

    tableRows.forEach(function (row) {
        const usernameCell = row.querySelector(".name");
        const username = usernameCell.textContent.toLowerCase();

        if (username.includes(searchTerm)) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
});
