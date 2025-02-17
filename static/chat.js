
// Javascript code for adding functionality

// Add a keyup event listener to the input field

// Get the elements from the document
const messagePage = document.querySelector(".message-page");
const messageInput = document.querySelector(".message-bottom input");
const messageButton = document.querySelector(".message-bottom button");



messageInput.addEventListener("keyup", function (event) {
    // Check if the enter key was pressed
    if (event.which == 13) {
        // Prevent the default behavior of the enter key
        event.preventDefault();
        // Trigger the click event on the button
        messageButton.click();
    }
});


// Add an event listener for the button click
messageButton.addEventListener("click", function () {
    // Get the value of the input field

    //IMPORTANT: FEED THIS "messageText" into the model 
    const messageText = messageInput.value;
    // Check if the input is not empty
    if (messageText) {
        // Create a new message container element
        const messageContainer = document.createElement("div");
        // Add the outgoing class to the message container
        messageContainer.classList.add("message-container", "outgoing");
        // Create a new image element for the user avatar
        const messageImage = document.createElement("img");
        // Set the source and alt attributes of the image
        messageImage.src = "user-avatar.png";
        messageImage.src = "https://cdn.pixabay.com/photo/2017/05/13/09/04/question-mark-2309040_640.jpg"
        messageImage.alt = "User Avatar";
        // Create a new paragraph element for the message text
        const messageParagraph = document.createElement("p");
        // Set the text content of the paragraph
        messageParagraph.textContent = messageText;
        // Create a new time element for the message time
        const messageTime = document.createElement("time");
        // Get the current date and time
        const currentTime = new Date();
        // Format the time as hh:mm
        const formattedTime = currentTime.getHours() + ":" + currentTime.getMinutes();
        // Set the text content of the time
        messageTime.textContent = formattedTime;
        // Append the image, paragraph, and time elements to the message container
        messageContainer.appendChild(messageImage);
        messageContainer.appendChild(messageParagraph);
        messageContainer.appendChild(messageTime);
        // Append the message container to the message page
        messagePage.appendChild(messageContainer);
        // Clear the input field
        messageInput.value = "";
        // Scroll to the bottom of the message page
        messagePage.scrollTop = messagePage.scrollHeight;

        // Make an asynchronous request to the server ("/get") with the user's message "messageText"
        $.get("/get", { msg: messageText }).done(function (data) {
            // var botHtml = '<p class="botText"><span>' + data + '</span></p>'; // Create an HTML element for the bot's response


            // $("#chatbox").append(botHtml); // Append the bot's response to the chatbox


            //EXPERIMENTAL START
            const messageContainer = document.createElement("div");
            // Add the outgoing class to the message container
            messageContainer.classList.add("message-container", "incoming");
            // Create a new image element for the user avatar
            const messageImage = document.createElement("img");
            // Set the source and alt attributes of the image
            // messageImage.src = "OIP.png";
            messageImage.src = "https://wallpapers.com/images/hd/anime-meme-pfp-spy-x-family-anya-forger-hdoysk4qije5kscv.jpg"
            messageImage.alt = "BOT Avatar";
            // Create a new paragraph element for the message text
            const messageParagraph = document.createElement("p");
            // Set the text content of the paragraph
            messageParagraph.textContent = data;
            // Create a new time element for the message time
            const messageTime = document.createElement("time");
            // Get the current date and time
            const currentTime = new Date();
            // Format the time as hh:mm
            const formattedTime = currentTime.getHours() + ":" + currentTime.getMinutes();
            // Set the text content of the time
            messageTime.textContent = formattedTime;
            // Append the image, paragraph, and time elements to the message container
            messageContainer.appendChild(messageImage);
            messageContainer.appendChild(messageParagraph);
            messageContainer.appendChild(messageTime);
            // Append the message container to the message page
            messagePage.appendChild(messageContainer);
            // Scroll to the bottom of the message page
            messagePage.scrollTop = messagePage.scrollHeight;
            // EXPERIMENTAL END
            document.getElementById('message-page').scrollIntoView({ block: 'start', behavior: 'smooth' });
        });
    }
});