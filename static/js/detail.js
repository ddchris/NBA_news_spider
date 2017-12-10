// 建立 XMLHttpRequest 物件
var xhr = new XMLHttpRequest()

// 當伺服器回應時執行
// 想開啟跨來源 HTTP 請求的話，Server 必須在 Response 的 Header 裡面加上 Access-Control-Allow-Origin
xhr.onload = function () {

	//if (status === 200){
		response_object = JSON.parse(xhr.responseText);
		var headline = response_object.headline;
		var img_dir = response_object.img_dir;
		var publish_time = response_object.publish_time;
		var repoter = response_object.repoter;
		var content = response_object.content;

		html =  ('<h1>'+ headline +'</h1>');
		html += '<div class="shareBar__info--author"><span>';
		html += ( publish_time + '&nbsp&nbsp&nbsp' + '</span>' + repoter + '</div>');
		html += ('<img src="' + img_dir + '">');
		html += ( '<p>'+ content + '</p>');

		var el_story_body = document.getElementById('story_body_content');
		el_story_body.innerHTML = html;

	//}
}

var el_id = document.getElementById('news_id');
id = el_id.textContent;

xhr.open('GET','http://127.0.0.1:8080/api/myapp/'+ id + '/', true);
xhr.send();
