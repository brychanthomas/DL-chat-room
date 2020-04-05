function update() {
  $.ajax({
    method: "GET",
    url: "/get-messages",
    cache: false,
    success: function (data, status, xhr) {
      if (xhr.status == 200) {
        console.log('Successful update');
        document.getElementById("messages-div").innerHTML = data;
      }
      setTimeout(update(), 2000);
    }
  });
}

update();
