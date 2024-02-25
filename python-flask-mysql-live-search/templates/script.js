$(document).ready(function () {
  $("#livebox").on("input", function (e) {
    $("#datalist").empty();
    $.ajax({
      method: "post",
      url: "/livesearch",
      data: { text: $("#livebox").val() },
      success: function (res) {
        var data = "<ul>";
        $.each(res, function (index, value) {
          data += "<li>" + value.title + "</li>";
        });
        data += "</ul>";
        $("#datalist").html(data);
      },
    });
  });
});
