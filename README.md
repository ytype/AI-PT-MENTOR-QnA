# AI-PT-MENTOR-QnA

## Q. 프론트엔드(html)이랑 백엔드(python) 연결하는 방법

html에서 동적인 데이터를 보내고, 받기 위해서는 자바스크립트가 필요합니다.

여담으로 프론트엔드에서 돌아가는 언어는 자바스크립트, 웹 어셈블리(C/C++, Rust) => Blazor(C#) 입니다.

보편적으로 사용되는 건 자바스크립트이며, Angular, React, Vue, Svelte 등의 프레임워크를 많이 사용합니다.

현 시점에서는 react를 가장 인기가 좋습니다.

자바스크립트에서 서버로 통신하는 방법은 다음이 있습니다. (상황에 따라서 사용하면 되고, 다른 라이브러리를 사용해도 좋습니다.)

1. 순수 자바스크립트 fetch

2. jquery에서 ajax

3. promise기반 axios

react, vue에서는 axios를 가장 많이 사용합니다.

예시로 flask 서버에서 get 요청을 받으면 Hello!를 리턴하게 만들고

``` python
@app.route('/')
def hello():
   return "Hello!"
```

vue에서 axios를 사용한다면 코드는 다음과 같습니다.

``` javascript
axios.get('localhost:5000')
    .then((response) => {
        console.log(response)
    })
```

`then` 은 자바스크립트의 비동기 문법으로 데이터를 가져오고 할 일 역할을 합니다.

추가로 파이썬을 자바스크립트로 변환시키는 Brython도 있습니다.

하지만 Brython 구글 검색 결과가 335,000개로 적은 편이고, 결국 자바스크립트이기 때문에, 자바스크립트를 하시는 편이 좋을 것 같습니다.

## Q. 웹 상에서 파이썬을 실행시켜서 결과를 불러올 수 있는지

위에서 기술한 것 처럼 파이썬 서버에서 프론트엔드의 요청을 받아서 결과를 리턴하는 것이 일반적입니다.

파이썬에서 실행하려면 Brython가 있지만, 위에 있는 이유로 추천하지 않습니다.

1. 프론트엔드에서는 요청을 보내고, 받기만 하고, 파이썬 실행은 서버에서 한다.

2. 외부 모듈을 돌리는 역할(ex_ tensorflow.js) 이라면 자바스크립트로 제작된 모듈을 찾는다.

## Q. 웹 앱을 만들 수 있는지

용어를 좀 더 나누어본다면

`웹 앱` : 구글로 예를 든다면, 웹 브라우저에서 www.google.com을 입력하는 것을 앱에서 웹 뷰를 사용하여 www.google.com 을 띄워주는 것 입니다.

[나동빈 - 안드로이드 스튜디오에서 웹 뷰(Web View)로 웹 앱 만들기](https://blog.naver.com/PostView.nhn?blogId=ndb796&logNo=221402597656&redirect=Dlog&widgetTypeCall=true&directAccess=false)

`하이브리드 앱` : 웹 기술 스택으로 앱을 제작하는 것으로, `html,css,js`를 앱으로 변환하는 cordova나 vue,react를 앱으로 만드는 vue native, react native가 있습니다. (vue,react와는 문법이 조금 다릅니다.)

`네이티브 앱` : 안드로이드 -자바, 코틀린, ios- swift, object C 등으로 제작한 앱 입니다.

프론트엔드를 다 만들어서 서버에 올리고, 앱에서는 웹 뷰를 띄워서 `https://aiptmentor.nicepage.io/question.html?version=b101b4b7-67a3-4d63-8afd-30e99114f1e2` 페이지를 보여주는 방법으로 가능합니다.

안드로이드 알림을 띄우거나, 내장 센서를 사용하는 등의 기능을 위헤서는 하이브리드나 네이티브로 제작해야합니다.

## Q. 안드로이드로 하는게 나을지

안드로이드 내장 센서나 기능을 이용하는게 아니라면 개인 취향대로 하면 됩니다.

추후 자바나 코틀린을 하고 싶다면 안드로이드 네이티브를 선택하면 됩니다.

웹쪽에 전문성을 가지고 싶으시다면 하이브리드를 추천드립니다.

추가로 안드로이드 뿐만 아니라 ios도 한번에 제작하려면 크로스플랫폼으로 cordova, vue, react native, google flutter, ms xamarin 등이 있습니다.

## +

cordova debugging : https://smallbutdeep.tistory.com/511