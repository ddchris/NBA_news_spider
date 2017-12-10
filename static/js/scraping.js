
var data = ''
var get_data = function() {
	// 建立 XMLHttpRequest 物件
	var xhr = new XMLHttpRequest();

	// 當伺服器回應時執行
	// 想開啟跨來源 HTTP 請求的話，Server 必須在 Response 的 Header 裡面加上 Access-Control-Allow-Origin
	xhr.onload = function () {
		//if (status === 200){
			response_object = JSON.parse(xhr.responseText);
			console.log(response_object);

			if (data =='' || response_object !== data) {
			// 若資料有更新則動作
				var news_el = document.querySelector('#hot_news');

				html =  '';
				for (var i = response_object.length; i >= response_object.length-4; i--) {
					if (response_object[i]) {  // 檢查是否有空值
						var new_id = response_object[i].id;
						var headline = response_object[i].headline;
						var img_dir = response_object[i].img_dir;
						// var news_url = response_object[i].news_url;
						var publish_time = response_object[i].publish_time;
						var repoter = response_object[i].repoter;

						html += ('<dt class="news"> <a href="/' + new_id + '/">');
						html += '<span class="img-boxs">';
						html += ('<img src="' + img_dir + '"></span><b>');
						html += (repoter + '&nbsp&nbsp&nbsp' +publish_time +'</b><h3>' + headline);
						html += '</h3></a></dt>';
					}
				}
				news_el.innerHTML = html;
				console.log('新聞已更新')
				data = response_object   // 記錄此次取得資料
			}
		//}
	}
	xhr.open('GET','https://scrapnbanews.herokuapp.com/api/myapp/', true);
	xhr.send();
}

var renew_database = function() {

	var xhr = new XMLHttpRequest();
	xhr.onload = function () {
		console.log('scraping finish!');
	};

	xhr.open('GET','https://scrapnbanews.herokuapp.com/', true);
	xhr.send();
}

var running = function () {
	renew_database()
	get_data()
}

get_data()
setInterval(running,1800000);
// 設定每 10 分鐘跟 api 要一次資料




