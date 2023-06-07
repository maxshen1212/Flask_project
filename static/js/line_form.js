$("#member_num").on("change", function () {
  console.log($("#member_num").val());
  var menber_num = $("#member_num").val();
  var member_list = document.getElementById("member_list");
  var template = ``;
  for (var i = 0; i < menber_num; i++) {
    template += `
        <div class="col-12">
            <label for="member${i+1}" class="form-label">成員${i+1}</label>
            <input
            type="text"
            class="form-control"
            id="member${i+1}"
            name="member${i+1}"
            placeholder="成員"
            />
            <div class="invalid-feedback">請填寫成員！！</div>
        </div>
        <div class="col-12">
            <label for="mail${i+1}" class="form-label">成員${i+1}的mail</label>
            <input
            type="text"
            class="form-control"
            id="mail${i+1}"
            name="mail${i+1}"
            placeholder="e-mail"
            />
            <div class="invalid-feedback">請填寫mail！！</div>
        </div>
    `;
  }
  member_list.innerHTML = template;
});
