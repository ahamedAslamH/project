var times = {},
        re = /^\d+(?=:)/;

      for (var i = 13, n = 1; i < 24; i++, n++) {
        times[i] = n < 10 ? "0" + n : n;
      }

      document.getElementById("frtime").onchange = function () {
        var time = this,
          value = time.value,
          match = value.match(re)[0];
        this.value =
          (match && match >= 13 ? value.replace(re, times[match]) : value) +
          (time.valueAsDate.getTime() < 43200000 ? " AM" : " PM");
      };
      document.getElementById("extime").onchange = function () {
        var time = this,
          value = time.value,
          match = value.match(re)[0];
        this.nextElementSibling.innerHTML =
          (match && match >= 13 ? value.replace(re, times[match]) : value) +
          (time.valueAsDate.getTime() < 43200000 ? " AM" : " PM");
      };