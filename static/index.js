


    // Get add button
    const addButton = document.getElementById("add-btn");

    addButton.addEventListener('click', function(e) {

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
                        <button class="btn btn-warning edit-btn" data-id="${data["id"]}">Edit</button>
                    </div>
                </div>
            </div>
            `
            let main_row = document.getElementById("row");
            main_row.innerHTML += new_item;
   
            // reset the btn trigger for deletes
            deleteTrigger();
            showNotificationSuccess("item added succesfully");
        })
        .catch(error => console.error('Error:', error));
    })


    // Get all delete buttons
    function deleteTrigger() {
        const deleteButtons = document.querySelectorAll('.delete-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            console.log("Delete triggered!");
            const deviceId = this.getAttribute('data-id');
            
            // Send DELETE request
            fetch(`/delete/${deviceId}`, {
                method: 'DELETE',
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    let element = document.getElementById(`card-${deviceId}`);
                    element.remove();
                    showNotificationSuccess("item deleted succesfully");
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while trying to delete the device.');
            });
        });
    });
    }

    deleteTrigger();

    function showNotificationSuccess(msg) {
        const notification = document.getElementById('notification_success');
        notification.innerHTML = msg;
        notification.style.display = 'block'; // Show the notification
    
        setTimeout(() => {
            notification.style.display = 'none'; // Hide after 3 seconds
        }, 3000);
    }
    
