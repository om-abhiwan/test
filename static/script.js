function sendResponse() {
    console.log("function is call")
    const csrfToken = document.head.querySelector('meta[name="csrf-token"]').content;
    userQuerry = document.getElementById("querry").value
    console.log(userQuerry)
    if (userQuerry == "") {
        return "Nothing"

    }
    userChatHistory = document.getElementById("Chatbot").innerHTML
    document.getElementById("Chatbot").innerHTML = userChatHistory + '<div style="margin-top: 10px; margin-left: auto;width:fit-content" class="alert alert-primary" role="alert"> <strong>'
        + userQuerry +
        '</strong></div>'
    fetch('/api/chatbotResponse', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ "querry": userQuerry })
    })
        .then(response => response.json())
        .then(response => {
            console.log(JSON.stringify(response))
            if (response['message'] == '0') {
                return null
            }
            if (response['message']) {
                chatbotHistory = document.getElementById("Chatbot").innerHTML

                document.getElementById("Chatbot").innerHTML =
                    chatbotHistory + '<div style="margin-top:1%;width:fit-content" class="alert alert-success"  role="alert">' + response['message'] + '</div>'
            }
            if (Array.isArray(response['button']) == true) {
                chatbotHistory = document.getElementById("Chatbot").innerHTML
                for (let i = 0; i < response['button'].length; i++) {
                    console.log(response['button'])
                    if (response['button'][i] == '0') {
                        break
                    }
                    chatbotHistory = document.getElementById("Chatbot").innerHTML
                    document.getElementById("Chatbot").innerHTML =
                        chatbotHistory + ` <button style="margin-top:1%;width:fit-content" type="button" class="btn btn-success"
                         onclick='productDetails("${response['button'][i]}")'>
                ${response['button'][i]} </button>`
                }
            }
            if (isLink(response['message'])) {
                chatbotHistory = document.getElementById("Chatbot").innerHTML
                document.getElementById("Chatbot").innerHTML =
                    chatbotHistory + `<div style="margin-top:1%;width:fit-content" class="alert alert-success"  role="alert">Yeh we Have<br><img style="width:50%;" src="${response['message']}"> </div>`
            }
        }
        )
    document.getElementById('querry').value = "";
    setTimeout(scrollWin, 100);

}
function productDetails(productName) {
    document.getElementById('querry').value = productName;
    document.getElementById('button').click();
}
function isLink(str) {
    // Regular expression pattern to match URLs
    var urlPattern = /^(http(s)?:\/\/)?([\w-]+\.)*[\w-]+[\.][a-zA-Z]{2,}([/?#].*)?$/;

    // Test if the string matches the URL pattern
    return urlPattern.test(str);
}

function scrollWin() {
    var element = document.getElementById("ScrollBottom")

    element.scrollTo(0, 10000);
}

function addNewChat() {
    location.reload();
}