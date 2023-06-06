// 初始化時間選擇器
function init_datetime() {
  $("#datepicker")
    .datepicker({
      format: "yyyy/mm/dd",
      startDate: "-0d",
      endDate: "+7d",
    })
    .datepicker("update", new Date());
  //監聽時間選擇器
  $("#datepicker").on("changeDate", function () {
    console.log($("#datepicker").datepicker("getFormattedDate"));
  });
}
function search_time() {
  var avalible_time = {
    "11:00": "愛在夏天",
    "11:30": "摯友",
    "12:00": null,
  };
  const time_regular = ["11:00", "11:30", "12:00"];
  var search_btn = document.getElementById("search_btn");
  var time_list = document.getElementById("time_list");
  console.log(avalible_time["11:00"]);
  search_btn.addEventListener("click", function () {
    $("#time_list_bg").show();
    var template=``;
    for (var i = 0; i < time_regular.length; i++) {
      if (avalible_time[time_regular[i]] != null) {
        template += `
        <div class="col">
            <button class="btn btn-outline-danger my-1" disabled>
                ${time_regular[i]}
            </button>
            <p class="d-inline">歌曲：${avalible_time[time_regular[i]]}</p>
        </div>
        `;
      } else {
        template += `
        <div class="col">
            <a class="btn btn-outline-danger my-1" id="${time_regular[i]}" href="/index5" >${time_regular[i]}</a>
            <p class="d-inline">可預約!!!</p>
        </div>
        `;
      }
    }
    time_list.innerHTML = template;
  });
}
function reservation_form() {
  
}

function test() {
  $.ajax({
    url: "" + ip + "/api/Historical_Temp", //存取Json的網址
    type: "GET",
    data: { x: temptext },
    dataType: "json",
    //contentType: "application/json",
    success: function (data) {
      rectemp = data;
      temp = temptext;
      button(value);
    },
  });
}
