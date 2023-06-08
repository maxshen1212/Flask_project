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
            <div class="d-inline rounded mx-1 display-3 my-1" disabled>
                ${time_regular[i]}
            </div>
            <p class="d-inline"><b>歌曲：</b>${
              avalible_time[time_regular[i]].song
            }</p> | 
            <p class="d-inline"><b>團員：</b>${
              avalible_time[time_regular[i]].member
            }</p>
            <button type="button" class="btn btn-sm btn-outline-danger ms-3 cancel_btn" id="${
              time_regular[i]
            }">刪除</button>
            </div>
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
            <div class="d-inline rounded mx-1 display-3 my-1" disabled>
                ${time_regular[i]}
            </div>
            <p class="d-inline"><b>歌曲：</b>${
              avalible_time[time_regular[i]].song
            }</p> | 
            <p class="d-inline"><b>團員：</b>${
              avalible_time[time_regular[i]].member
            }</p>
            <button type="button" class="btn btn-sm btn-outline-danger ms-3" onclick="delete_line(${date},${
          time_regular[i]
        })">刪除</button>
        </div>
        `;
      }
    }
    time_list.innerHTML = template;
  });
  $(".cancel_btn").on("click", function () {
    time = $(".cancel_btn").attr("id");
    delete_line(date, time);
    console.log(time);
    console.log(date);
  });
}

function date_line_info(date) {
  // $.ajax({
  //   url: "/cancel_line", //存取Json的網址
  //   type: "POST",
  //   data: date,
  //   dataType: "json",
  //   success: function (data) {
  //     return data;
  //   },
  // });
}

function delete_line(date, time) {
  var today = new Date().toLocaleDateString();
  var day;
  if (DateDiff(today, date) == 0) {
    day = "day0";
  } else if (DateDiff(today, date) == 1) {
    day = "day1";
  }
  console.log(day);
  var form_data = new FormData();
  form_data.append("day", day);
  form_data.append("time", time);

  $.ajax({
    url: "/cancel_line", //存取Json的網址
    type: "POST",
    data: form_data,
    contentType: false,
    processData: false,
    dataType: "json",
    success: function (aa) {
      console.log(aa);
    },
  });
}
