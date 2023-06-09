function DateDiff(date1, date2) {
  // date1 和 date2 是 yyyy/mm/dd 格式
  let strDate, oDate1, oDate2, result;
  strDate = date1.split("/");
  oDate1 = new Date(strDate[1] + "/" + strDate[2] + "/" + strDate[0]);
  strDate = date2.split("/");
  oDate2 = new Date(strDate[1] + "/" + strDate[2] + "/" + strDate[0]);
  result = parseInt(Math.abs(oDate1 - oDate2) / 1000 / 60 / 60 / 24); // 把相差的毫秒數轉換為天數
  return result;
}

const time_regular = [
  "19:30",
  "20:00",
  "20:30",
  "21:00",
  "21:30",
  "22:00",
  "22:30",
  "23:00",
  "23:30",
  "24:00",
];

// 初始化時間選擇器
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
  var search_btn = document.getElementById("search_btn");
  search_btn.addEventListener("click", function () {
    $("#time_list_bg").show();
    select_date = $("#datepicker").datepicker("getFormattedDate");
    get_line(select_date);
  });
}

function get_line(select_date) {
  var today = new Date().toLocaleDateString();
  var day;
  if (DateDiff(today, select_date) == 0) {
    day = "day0";
  } else if (DateDiff(today, select_date) == 1) {
    day = "day1";
  }
  var line = {
    "19:30": null,
    "20:00": null,
    "20:30": null,
    "21:00": null,
    "21:30": null,
    "22:00": null,
    "22:30": null,
    "23:00": null,
    "23:30": null,
    "24:00": null,
  };
  $.ajax({
    url: "/get_line/" + day, //存取Json的網址
    type: "GET",
    processData: false,
    dataType: "json",
    success: function (response) {
      for (var i = 0; i < response.data.length; i++) {
        // console.log(response.data[i])
        line[response.data[i][2]] = response.data[i][3];
      }
      var time_list = document.getElementById("time_list");
      var template = ``;
      for (var i = 0; i < time_regular.length; i++) {
        if (line[time_regular[i]] != null) {
          template += `
        <div class="col">
            <button class="btn btn-outline-danger my-1" disabled>
                ${time_regular[i]}
            </button>
            <p class="d-inline">歌曲：${line[time_regular[i]]}</p>
        </div>
        `;
        } else {
          template += `
        <div class="col">
            <a class="btn btn-outline-danger my-1" id="${time_regular[i]}" href="/line_form/${day}/${time_regular[i]}" >${time_regular[i]}</a>
            <p class="d-inline">可預約!!!</p>
        </div>
        `;
        }
      }
      time_list.innerHTML = template;
    },
  });
  // console.log(line);
}
