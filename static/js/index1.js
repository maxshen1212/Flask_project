function init_datetime() {
  // 初始化時間選擇器
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
