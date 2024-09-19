// get edit button
const editButton = document.getElementById("edit-btn");

editButton.addEventListener('click', function(e) {

    let name = document.getElementById('edit_name');
    let price = document.getElementById("edit_price");
    let description = document.getElementById('edit_description');
    let mac_address = document.getElementById('edit_mac_address');
    let serial_number = document.getElementById('edit_serial_number');
    let manufacturer = document.getElementById('edit_manufacturer');

    // get the data-id from the latest edit model triggered
    let itemId = document.getElementById("edit_modal").getAttribute("data-id");

    fetch(`/edit/${itemId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name.value,
            price: price.value,
            description: description.value,
            mac_address: mac_address.value,
            serial_number: serial_number.value,
            manufacturer: manufacturer.value
        })
    }) 
    .then(response => response.json())
    .then(data => {
        // get item card to update
        let itemCardObject = document.getElementById(`card-${itemId}`);
        let updatedObject = `
        <div class="card mb-4">
                    <div class="card-body">
                        <h5 class="card-title">${name.value}</h5>
                        <p class="card-text">
                            <strong>Price:</strong> ${price.value} <br>
                            <strong>Description:</strong> ${description.value} <br>
                            <strong>MAC Address:</strong> ${mac_address.value} <br>
                            <strong>Serial Number:</strong> ${serial_number.value} <br>
                            <strong>Manufacturer:</strong> ${manufacturer.value} <br>
                        </p>

                        <button class="btn btn-danger delete-btn" data-id="${itemId}">Delete</button>
                        <button data-toggle="modal" data-target="#edit_modal" class="btn btn-warning edit-btn" data-id="${data["id"]}">Edit</button>
                    </div>
                </div>
        `;
        itemCardObject.innerHTML = updatedObject;

        // reset delete trigger
        deleteTrigger()

        showNotificationSuccess("Data updated succesfully");
    });

});


// Get add button
const addButton = document.getElementById("add-btn");

addButton.addEventListener('click', function (e) {

    let name = document.getElementById('name');
    let price = document.getElementById("price");
    let description = document.getElementById('description');
    let mac_address = document.getElementById('mac_address');
    let serial_number = document.getElementById('serial_number');
    let manufacturer = document.getElementById('manufacturer');

    fetch('/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name.value,
            price: price.value,
            description: description.value,
            mac_address: mac_address.value,
            serial_number: serial_number.value,
            manufacturer: manufacturer.value
        })
    })
        .then(response => response.json())
        .then(data => {
            let new_item = `
            <div class="col-md-4", id="card-${data["id"]}">
                <div class="card mb-4">
                    <div class="card-body">
                        <h5 class="card-title">${data["name"]}</h5>
                        <p class="card-text">
                            <strong>Price:</strong> ${data["price"]} <br>
                            <strong>Description:</strong> ${data["description"]} <br>
                            <strong>MAC Address:</strong> ${data["mac_address"]} <br>
                            <strong>Serial Number:</strong> ${data["serial_number"]} <br>
                            <strong>Manufacturer:</strong> ${data["manufacturer"]} <br>
                        </p>

                        <button class="btn btn-danger delete-btn" data-id="${data["id"]}">Delete</button>
                        <button data-toggle="modal" data-target="#edit_modal" class="btn btn-warning edit-btn" data-id="${data["id"]}">Edit</button>
                    </div>
                </div>
            </div>
            `
            let main_row = document.getElementById("row");
            main_row.innerHTML += new_item;

            // reset fields for add modal
            document.getElementById('name').value = "";
            document.getElementById("price").value = 0;
            document.getElementById('description').value = "";
            document.getElementById('mac_address').value = "";
            document.getElementById('serial_number').value = "";
            document.getElementById('manufacturer').value = "";

            // reset the btn trigger for deletes
            deleteTrigger();
            editTrigger();
            showNotificationSuccess("item added succesfully");
        })
        .catch(error => console.error('Error:', error));
});


// Get all delete buttons
function deleteTrigger() {
    const deleteButtons = document.querySelectorAll('.delete-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            console.log("Delete triggered!");
            const itemId = this.getAttribute('data-id');

            // Send DELETE request
            fetch(`/delete/${itemId}`, {
                method: 'DELETE',
            })
                .then(response => response.json())
                .then(data => {
                    if (data.message) {
                        let element = document.getElementById(`card-${itemId}`);
                        if (element) {
                            element.remove();
                            showNotificationSuccess("item deleted succesfully");
                        }
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });
}

deleteTrigger();


function editTrigger() {
    const editButtons = document.querySelectorAll('.edit-btn');

    editButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            const itemId = this.getAttribute('data-id');
            // pass the data-id to the current edit modal
            let modal = document.getElementById("edit_modal").setAttribute("data-id", itemId);

            fetch(`/${itemId}`, {
                method: 'GET',
            })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('edit_name').value = data.name;
                    document.getElementById("edit_price").value = data.price;
                    document.getElementById('edit_description').value = data.description;
                    document.getElementById('edit_mac_address').value = data.mac_address;
                    document.getElementById('edit_serial_number').value = data.serial_number;
                    document.getElementById('edit_manufacturer').value = data.manufacturer;
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });
}

editTrigger();

function showNotificationSuccess(msg) {
    const notification = document.getElementById('notification_success');
    notification.innerHTML = msg;
    notification.style.display = 'block'; // Show the notification

    setTimeout(() => {
        notification.style.display = 'none'; // Hide after 3 seconds
    }, 3000);
}

