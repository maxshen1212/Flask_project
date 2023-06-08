function init_datetime() {
  $("#datepicker")
    .datepicker({
      format: "yyyy/mm/dd",
      startDate: "0d",
      endDate: "+2d",
    })
    .datepicker("update", new Date());
  //監聽時間選擇器
  $("#datepicker").on("changeDate", function () {
    console.log($("#datepicker").datepicker("getFormattedDate"));
  });
}

function search_time() {
  var date = $("#datepicker").datepicker("getFormattedDate");
  var avalible_time = date_line_info(date);
  // 預設回傳值
  var avalible_time = {
    "11:00": { song: "愛在夏天", member: ["治翰", "維剛", "柏雄"] },
    "11:30": { song: "摯友", member: ["max", "max", "max"] },
    "12:00": null,
    "12:30": null,
    "13:00": null,
  };
  const time_regular = ["11:00", "11:30", "12:00", "12:30", "13:00"];
  var time_list = document.getElementById("time_list");
  console.log(avalible_time["11:00"]);
  var template = ``;
  for (var i = 0; i < time_regular.length; i++) {
    if (avalible_time[time_regular[i]] != null) {
      template += `
        <div class="col">
            <button class="btn btn-outline-danger my-1" disabled>
                ${time_regular[i]}
            </button>
            <p class="d-inline"><b>歌曲：</b>${
              avalible_time[time_regular[i]].song
            }</p> | 
            <p class="d-inline"><b>團員：</b>${
              avalible_time[time_regular[i]].member
            }</p>
        </div>
        `;
    }
  }
  time_list.innerHTML = template;
  $("#datepicker").on("change", function () {
    console.log("asd");
    var template = ``;
    for (var i = 0; i < time_regular.length; i++) {
      if (avalible_time[time_regular[i]] != null) {
        template += `
        <div class="col">
            <button class="btn btn-outline-danger my-1" disabled>
                ${time_regular[i]}
            </button>
            <p class="d-inline"><b>歌曲：</b>${
              avalible_time[time_regular[i]].song
            }</p> | 
            <p class="d-inline"><b>團員：</b>${
              avalible_time[time_regular[i]].member
            }</p>
            <button class="btn btn-outline-danger my-1" onclick="delete_line(${date},${avalible_time[time_regular[i]].song})>刪除</button>
        </div>
        `;
      }
    }
    time_list.innerHTML = template;
  });
}

function date_line_info(date) {
  // $.ajax({
  //   url: "/date_line_info", //存取Json的網址
  //   type: "GET",
  //   data: date,
  //   dataType: "json",
  //   success: function (data) {
  //     return data;
  //   },
  // });
}

function delete_line(date,song) {

}
